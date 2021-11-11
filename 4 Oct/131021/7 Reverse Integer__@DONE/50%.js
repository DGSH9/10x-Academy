let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
function rev(num)
{
	num = num + "";
	return num.split("").reverse().join("");
}
num = parseInt(readLine());
console.log(rev(num));