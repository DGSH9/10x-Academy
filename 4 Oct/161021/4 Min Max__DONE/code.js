// https://6793fdf6.widgets.sphere-engine.com/lp?hash=ZjlUV3BE1G
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
  var x = parseInt(readLine());
  arr1.push(x);
}

min1 = 99999999999999
max1 = -99999999999
for(var i = 0;i<n;i++){
  if(arr1[i] < min1){
    min1 = arr1[i];
  }
  if(arr1[i] > max1){
    max1 = arr1[i]
  }
}
console.log(max1);
console.log(min1);