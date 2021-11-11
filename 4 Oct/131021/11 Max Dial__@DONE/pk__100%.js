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
    arr1.push(0);
}
var max1 = parseInt(readLine());
var m = parseInt(readLine());
var flag=0
var ans;
for(var j=0;j<m;j++){
    var x = parseInt(readLine());
    arr1[x-1]+=1
    if(arr1[x-1]===max1){
    	flag=1
    	ans=x;
        break;
    }
}
if(flag===1){
	console.log(ans);
}else{
	console.log(0);
}