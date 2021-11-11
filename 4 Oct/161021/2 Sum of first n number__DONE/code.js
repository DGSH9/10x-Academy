// https://6793fdf6.widgets.sphere-engine.com/lp?hash=fx0Tz5ocdA

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
// (n*(n+1))/2
var n = parseInt(readLine());
console.log(parseInt((n*(n+1))/2));