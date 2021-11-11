// https://6793fdf6.widgets.sphere-engine.com/lp?hash=kt4HTB6Hkq
let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
let tmp = parseInt(readLine())
while (42!==tmp) {
  console.log(tmp)
  tmp = parseInt(readLine())
}