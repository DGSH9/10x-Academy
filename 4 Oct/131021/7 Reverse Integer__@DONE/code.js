// https://6793fdf6.widgets.sphere-engine.com/lp?hash=kXFfDMo9Bc

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
reqNum = num
if(num > 0)
{
  num = num
}
else
{
  num = num *(-1)
}
var last; 
sum = 0;
while(num > 0)
{
  last = num % 10;
  sum = sum * 10 + last;
  num = parseInt(num / 10);
}
if(reqNum > 0)
{
console.log(sum);
}
else if(reqNum == 0)
{
 console.log('0');
}
else
{
  console.log(sum*(-1));
}