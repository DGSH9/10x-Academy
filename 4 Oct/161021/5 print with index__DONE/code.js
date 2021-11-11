// https://6793fdf6.widgets.sphere-engine.com/lp?hash=aaNNX541UO

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------

var n = parseInt(readLine());
var arr1 = [];
for(var i=0;i<n;i++){
  var x = readLine();
  arr1.push(x);
}

for(var i= 0;i<n;i++){
  console.log(i,arr1[i]);
}