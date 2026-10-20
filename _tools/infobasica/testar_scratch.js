// Loads each .sb3 in the real Scratch VM, clicks the green flag, answers questions and prints what the sprite says
const fs = require('fs'), path = require('path');
const VM = require('scratch-vm');
const respostas = {aula03: ['Ana', 'Química'], aula06: ['100', '15'], aula08: ['17', 's'], aula09: ['6', '9'],
  aula10: ['8.5'], aula16: ['1000', '1'], aula18: Array.from({length: 100}, (_, i) => String(i + 1)),
  aula26: ['Ana', 'Bia', 'Caio', 'Davi', 'Eva']};
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
      vm.start(); vm.greenFlag();
      const inicio = Date.now();
      while (vm.runtime.threads.length && Date.now() - inicio < 60000) await new Promise(r => setTimeout(r, 50));
      vm.stopAll();
      console.log(`${nome}: ${Object.keys(blocos).length} blocos | ` + falas.join(' / ').slice(0, 150));
    } catch (e) { console.log(`${nome}: ERRO ${e}`); }
  }
  process.exit(0);
})();
