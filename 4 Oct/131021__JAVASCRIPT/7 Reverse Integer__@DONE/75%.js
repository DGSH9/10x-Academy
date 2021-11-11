let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
// var a = prompt("Enter a value");
num = parseInt(readLine());
var last; 
sum = 0;
while(num > 0)
{
  last = num % 10;
  sum = sum * 10 + last;
  num = parseInt(num / 10);
}
console.log(sum);