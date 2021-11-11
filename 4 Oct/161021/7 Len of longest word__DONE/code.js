// https://6793fdf6.widgets.sphere-engine.com/lp?hash=Td6nHnnDOv

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
var st = readLine();
var arr1 = st.split(" ");
var arr2 = [];
for(var i = 0;i<arr1.length;i++){
  x = arr1[i].length;
  arr2.push(x);
}
mx = 0
for(var i=0;i<arr2.length;i++){
  if(arr2[i]>mx){
    mx = arr2[i]
  }
}
console.log(mx)