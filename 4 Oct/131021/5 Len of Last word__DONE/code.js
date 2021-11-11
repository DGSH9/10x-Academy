// https://6793fdf6.widgets.sphere-engine.com/lp?hash=pxqXVhaYH7

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
var str = readLine();
var arr1 = str.split(' ');
console.log(arr1[arr1.length-1].length)