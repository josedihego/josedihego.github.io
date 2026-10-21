"""Creates vscode/data/user-data/languagepacks.json so VS Code opens in Portuguese on the very first start.
VS Code only writes this file after its first start; the paths in it are absolute, so abrir-vscode.sh
rewrites them to wherever the kit was extracted. Uso: python3 gerar_languagepacks.py <pasta do kit>"""
import sys, os, json, glob, hashlib

kit = sys.argv[1]
ext_dir = os.path.join(kit, 'vscode', 'data', 'extensions')
pacote = glob.glob(os.path.join(ext_dir, 'ms-ceintl.vscode-language-pack-pt-br-*'))[0]
manifesto = json.load(open(os.path.join(pacote, 'package.json')))
instaladas = json.load(open(os.path.join(ext_dir, 'extensions.json')))
uuid = next(e['identifier'].get('uuid') for e in instaladas if e['identifier']['id'].lower() == 'ms-ceintl.vscode-language-pack-pt-br')
localizacao = manifesto['contributes']['localizations'][0]
base = '__KIT_DIR__/vscode/data/extensions/' + os.path.basename(pacote)
dados = {localizacao['languageId']: {
    'hash': hashlib.md5((manifesto['name'] + manifesto['version']).encode()).hexdigest(),
    'extensions': [{'extensionIdentifier': {'id': 'ms-ceintl.vscode-language-pack-pt-br', 'uuid': uuid}, 'version': manifesto['version']}],
    'translations': {t['id']: base + '/' + t['path'].lstrip('./') for t in localizacao['translations']},
    'label': localizacao.get('localizedLanguageName', 'português (Brasil)'),
}}
json.dump(dados, open(os.path.join(kit, 'vscode', 'data', 'user-data', 'languagepacks.json'), 'w'), ensure_ascii=False)
print('languagepacks.json:', len(dados['pt-br']['translations']), 'traduções')
