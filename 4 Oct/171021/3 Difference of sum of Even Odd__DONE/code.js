// https://6793fdf6.widgets.sphere-engine.com/lp?hash=lm7yCQJqqW

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let arr1 = data[0].split(" ").map(Number);
sumEven = 0
sumOdd = 0

for(var i=0;i<arr1.length;i++){
    if(i%2==0){
        sumEven=sumEven + arr1[i];
    }
    else{
        sumOdd =sumOdd + arr1[i];
    }
}
console.log(sumEven-sumOdd);