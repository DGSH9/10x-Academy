// https://6793fdf6.widgets.sphere-engine.com/lp?hash=qfwGFUaXIX


let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

var n = parseInt(readLine());
var arr1 = [];
for(var i=0;i<n;i++){
  var x = parseInt(readLine());
  arr1.push(x);
}

count_odd = 0
count_even= 0
for(var i=0;i<n;i++){
  if(arr1[i]%2 == 0){
    count_even+=1;
  }
  else{
    count_odd+=1
  }
}
console.log(count_odd);
console.log(count_even);
