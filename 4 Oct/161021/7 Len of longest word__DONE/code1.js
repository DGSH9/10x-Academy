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
var mx = 0
for(var i=0;i<arr1.length;i++){
  if(arr1[i].length>mx){
    mx = arr1[i].length
  }
}
console.log(mx)