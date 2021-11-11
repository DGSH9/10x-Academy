// https://6793fdf6.widgets.sphere-engine.com/lp?hash=cg2cI17cQB

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}
function conseChars(s) {
    let max = 0
    let count = 1
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i-1])
            count++
        else {
            max = Math.max(max, count)
            count = 1
        }
    }
    max = Math.max(max, count)

    return max
};
x = readLine();
if(x.length > 0) {
    console.log(conseChars(x));
} else {
    console.log(0);
}