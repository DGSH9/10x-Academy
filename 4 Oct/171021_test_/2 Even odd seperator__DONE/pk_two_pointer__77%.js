let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------

var arr=data[0].split(" ").map(Number);
var n = arr.length
var i=0
var j=n-1
while(i<j){
	while(arr[i]%2!==0 && i<j){
		i+=1
	}
	while(arr[j]%2===0 && i<j){
		j-=1
	}
	var tmp=arr[i]
	arr[i]=arr[j]
	arr[j]=tmp
}
console.log(arr.join(" "))