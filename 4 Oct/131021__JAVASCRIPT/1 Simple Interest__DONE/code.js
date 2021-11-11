// https://6793fdf6.widgets.sphere-engine.com/lp?hash=6uxx1txMdo

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
p = parseInt(readLine());
t = parseInt(readLine());
r = parseInt(readLine());

let si = (p * t * r)/100 ;
console.log(si);