// Loads each .sb3 in the real Scratch VM, clicks the green flag, answers questions and prints what the sprite says
const fs = require('fs'), path = require('path');
const VM = require('scratch-vm');
const respostas = {
  aula03_nivel2: ['Ana', 'Química'], aula03_nivel3: ['Ana', 'Química', 'Salvador'],
  aula06_nivel1: ['Ana'], aula06_nivel2: ['100', '15'], aula06_nivel3: ['1200', '1350', '0.85'],
  aula08_nivel2: ['17', 's'], aula08_nivel3: ['2024'],
  aula09_nivel1: ['7'], aula09_nivel2: ['6', '9'], aula09_nivel3: ['50.15'],
  aula10_nivel1: ['7'], aula10_nivel2: ['8.5'], aula10_nivel3: ['75', '60'],
  aula13_nivel3: ['7'], aula16_nivel2: ['1000', '1'], aula16_nivel3: ['8', '12', '6', '-1'],
  aula18_nivel1: ['5'], aula18_nivel2: Array.from({length: 100}, (_, i) => String(i + 1)),
  aula18_nivel3: ['50', '25', '12', '6', '3', '2', '1'],
  aula26_nivel2: ['Ana', 'Bia', 'Caio', 'Davi', 'Eva'], aula26_nivel3: ['3']};
(async () => {
  const dir = process.argv[2];
  for (const f of fs.readdirSync(dir).sort()) {
    const nome = f.replace('.sb3', ''), fila = [...(respostas[nome] || [])], falas = [];
    const vm = new VM(); const {ScratchStorage} = require('scratch-storage'); vm.attachStorage(new ScratchStorage());
    vm.setTurboMode(true);
    vm.runtime.on('QUESTION', q => { if (q !== null) vm.runtime.emit('ANSWER', fila.shift() ?? ''); });
    vm.runtime.on('SAY', (alvo, tipo, texto) => { if (texto && falas[falas.length - 1] !== texto) falas.push(texto); });
    try {
      await vm.loadProject(fs.readFileSync(path.join(dir, f)));
      const blocos = vm.runtime.targets[1].blocks._blocks;
      vm.start(); vm.greenFlag(); setTimeout(() => vm.runtime.startHats('event_whenkeypressed', {KEY_OPTION: 'space'}), 9000);
      const inicio = Date.now();
      while (vm.runtime.threads.length && Date.now() - inicio < 60000) await new Promise(r => setTimeout(r, 50));
      vm.stopAll();
      console.log(`${nome}: ${Object.keys(blocos).length} blocos | ` + falas.join(' / ').slice(0, 150));
    } catch (e) { console.log(`${nome}: ERRO ${e}`); }
  }
  process.exit(0);
})();
