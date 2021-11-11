let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
function conseChars(string) {
	var maxi = 0;
	for(var i = 0; i < string.length - 1; i++) {
		var c = 1;
		if(string[i] == string[i + 1]) {
			c += 1;
			continue;
		}
		if(c > maxi) {
			maxi = c;
		}
	}
	return maxi;
}
x = readLine();
if(x.length > 0) {
	console.log(conseChars(x));
} else {
	console.log(0);
}