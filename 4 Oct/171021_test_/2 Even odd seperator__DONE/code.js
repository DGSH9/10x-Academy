// https://6793fdf6.widgets.sphere-engine.com/lp?hash=xg0EmP02Cw

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------

let arr = data[0].split(" ");
let odd = [];
let even = [];
for (let i=0;i<arr.length;i++){
	if (arr[i]%2===0){
		even.push(arr[i]);
	}
	else{
		odd.push(arr[i])
	}
}

var string = "";
odd.forEach(function(element){
	string += element+" ";
});
even.forEach(function(element){
	string += element+" ";
});
console.log(string);