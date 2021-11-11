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
arr1 = [];
for(var i=0;i<n;i++){
  var x = parseInt(readLine());
  arr1.push(x);
}

var arr2 = [];
for(var i=0;i<n;i++){
  let inarr = arr1;
  arr2[i] =inarr.pop(i);
}
console.log(arr2);