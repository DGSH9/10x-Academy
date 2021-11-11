// https://6793fdf6.widgets.sphere-engine.com/lp?hash=DlFv0CyFZj

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------

let n = parseInt(readLine());
var arr1 = [];
for(let i=0;i<n;i++){
  arr1.push(parseInt(readLine()));
}
console.log(arr1);