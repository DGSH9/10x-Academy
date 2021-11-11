// https://6793fdf6.widgets.sphere-engine.com/lp?hash=CH386BzDYj
// https://6793fdf6.widgets.sphere-engine.com/lp?hash=eFP8e03TG4

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
// 12  =>2
// 
// -------- Do NOT edit anything above this line ----------
num1 = readLine();
prod = 1
sum = 0

sz = num1.length;
for(var i=0;i<sz;i++)
{
  last = num1%10;
  prod = prod*last;
  sum = sum + last;
  num1 = parseInt(num1/10);
}
console.log(prod-sum);