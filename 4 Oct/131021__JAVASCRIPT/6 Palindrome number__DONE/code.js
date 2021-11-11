// https://6793fdf6.widgets.sphere-engine.com/lp?hash=ogfx0myH9J

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------

// program to check if the string is palindrome or not

function checkP(str) {
    const len = string.length;
    for (let i = 0; i < len / 2; i++) {
        if (string[i] !== string[len - 1 - i]) {
            return 'False';
        }
    }
    return 'True';
}
const string = readLine();
const ans = checkP(string);
console.log(ans);