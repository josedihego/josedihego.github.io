"""Crops figures of Cormen et al., Introduction to Algorithms, 3rd ed. (local PDF) for the slides.
A caption is a block in the caption font (word height < 9pt) that starts with 'Figure X.Y'; the drawing is the band between
the body text (or running head) above it and the caption. The caption itself is left out: the slide has its own, in Portuguese.
Uso: python3 cormen_fig.py <pdf> <pasta de saída> 2.2 6.1 ...   (gera <pasta>/fig_2_2.png)"""
import sys, os, re, subprocess, tempfile
from PIL import Image, ImageChops

BLOCO = re.compile(r'<block xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</block>', re.S)
PALAVRA = re.compile(r'<word xMin="[\d.]+" yMin="([\d.]+)" xMax="[\d.]+" yMax="([\d.]+)">([^<]*)</word>')
_indice = {}


def blocos(pdf, pagina):
    with tempfile.NamedTemporaryFile(suffix='.html') as f:
        subprocess.run(['pdftotext', '-f', str(pagina), '-l', str(pagina), '-bbox-layout', pdf, f.name], check=True)
        html = open(f.name).read()
    res = []
    for b in BLOCO.finditer(html):
        ws = PALAVRA.findall(b.group(5))
        if not ws:
            continue
        altura = sum(float(y2) - float(y1) for y1, y2, _ in ws) / len(ws)
        res.append({'y0': float(b.group(2)), 'y1': float(b.group(4)), 'n': len(ws), 'h': altura, 'txt': [w[2] for w in ws]})
    return res


def paginas_com_legenda(pdf, fig):
    """Pages whose text has a line starting with 'Figure <fig>' (candidates; the bbox check confirms the caption)."""
    if pdf not in _indice:
        texto = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout.split('\f')
        idx = {}
        for i, pg in enumerate(texto, 1):
            for m in re.finditer(r'^\s*Figure (\d+\.\d+)\s', pg, re.M):
                idx.setdefault(m.group(1), []).append(i)
        _indice[pdf] = idx
    return sorted(set(_indice[pdf].get(fig, [])))


def recortar(pdf, fig, saida, dpi=300):
    for pagina in paginas_com_legenda(pdf, fig):
        bs = blocos(pdf, pagina)
        leg = [b for b in bs if b['h'] < 9 and b['n'] > 6 and b['txt'][:2] == ['Figure', fig]]
        if not leg:
            continue
        leg = leg[0]
        # limite de cima: cabeçalho, texto corrido (fonte de 10pt) ou a legenda de outra figura da mesma página
        acima = [b['y1'] for b in bs if b['y1'] <= leg['y0'] and b is not leg and
                 (b['y0'] < 55 or (b['h'] >= 9.3 and b['n'] >= 5) or (b['h'] < 9 and b['txt'][0] == 'Figure'))]
        topo = max(acima, default=40) + 3
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(['pdftoppm', '-f', str(pagina), '-l', str(pagina), '-r', str(dpi), '-png', pdf, f'{tmp}/p'], check=True)
            img = Image.open([os.path.join(tmp, x) for x in os.listdir(tmp)][0]).convert('RGB')
        k = dpi / 72
        faixa = img.crop((0, int(topo * k), img.width, int((leg['y0'] - 2) * k)))
        fundo = Image.new('RGB', faixa.size, (255, 255, 255))
        caixa = ImageChops.difference(faixa, fundo).convert('L').point(lambda v: 255 if v > 20 else 0).getbbox()
        if not caixa:
            continue
        m = int(6 * k)
        faixa.crop((max(0, caixa[0] - m), max(0, caixa[1] - m), min(faixa.width, caixa[2] + m), min(faixa.height, caixa[3] + m))).save(saida)
        return pagina
    raise ValueError(f'Figura {fig} não encontrada')


if __name__ == '__main__':
    pdf, pasta = sys.argv[1], sys.argv[2]
    os.makedirs(pasta, exist_ok=True)
    for fig in sys.argv[3:]:
        print(fig, 'página', recortar(pdf, fig, os.path.join(pasta, f"fig_{fig.replace('.', '_')}.png")))
