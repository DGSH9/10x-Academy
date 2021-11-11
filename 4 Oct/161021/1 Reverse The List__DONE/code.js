// https://6793fdf6.widgets.sphere-engine.com/lp?hash=8oiH7nrTOm

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
for(var i=0;i<n;i++){
    var x = parseInt(readLine());
    arr1.push(x);
}
arr1.reverse();
for(var j=0;j<n;j++){
    console.log(arr1[j]);
}
// console.log(arr1);
