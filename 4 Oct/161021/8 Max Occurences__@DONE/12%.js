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

var arr2 = [];
for(var i =0;i<n;i++){
  count1 = 0;
  for(var j=0;j<n;j++){
    if(arr1[i]==arr1[j]){
      count1+=1;
    }
  }
  arr2.push(count1);
}
// console.log(arr2);
max1 = -9999999999999999999999
for(var i=0;i<n;i++){
  if(arr1[i]>max1){
    max1 = arr1[i];
    var ans = arr1[i]
  }
}
if(max1==1){
  console.log(-1);
}
else{
console.log(arr1[ans]);
}