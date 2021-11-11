// https://6793fdf6.widgets.sphere-engine.com/lp?hash=NgFu998tJT

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
length = parseInt(readLine());
breadth = parseInt(readLine());
let perimeter = 2*(length+breadth);

if (length<=0 || breadth<=0) 
{
    console.log('0');
} 
else 
{
    console.log(perimeter);
}