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
for(var i=0;i<n;i++)
{
    var x = parseInt(readLine());
    arr1.push(x);
}
var y = parseInt(readLine());

sum = 0;
for(var j=1;j<n;j+=y)
{
  sum+=arr1[j];
}
console.log(sum);
