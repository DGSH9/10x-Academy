// https://6793fdf6.widgets.sphere-engine.com/lp?hash=k2WnaCB90v

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
arr1 = [];
for(var i=1;i<=n;i++){
    arr1.push(i);
}
var max1 = parseInt(readLine());
var m = parseInt(readLine());

var arr2 = []
for(var j=0;j<m;j++){
    var x = parseInt(readLine());
    arr2.push(x);
}

// 1 2 2 3 =>
for(var i=0;i<arr1.length;i++){
    count1 = 0;
    for(var z=0;z<arr2.length;z++){
        if(arr1[i]==arr2[z]){
            count1+=1;
        }
    }
    if(count1==max1){
        console.log(arr1[i]);
        break;
    }
}
