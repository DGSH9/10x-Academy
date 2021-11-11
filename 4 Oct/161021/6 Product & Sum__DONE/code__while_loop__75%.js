let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
n = readLine();
prod = 1;
sum1 = 0;
while(n>0)
{
    var last = n%10;
    prod = prod*last;
    sum1 = sum1 + last;
    n = parseInt(n/10);
}
console.log(prod - sum1);
// console.log(prod);
// console.log(sum1);

