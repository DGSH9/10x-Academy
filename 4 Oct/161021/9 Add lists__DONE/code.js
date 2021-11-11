// https://6793fdf6.widgets.sphere-engine.com/lp?hash=M84iAVPMF9


let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
function addlist(arr1,arr2)
{
    //if arr1.length > arr2.length
    if(arr2.length > arr1.length)
    {
      //swapping
      temp = arr1;
      arr1 = arr2
      arr2 = temp
    }

    let answer = [];
    carry = 0;
    for(let i=0;i<arr2.length;i++)
    {
      let x = arr1[i] + arr2[i] + carry ;
      answer.push(x%10);
      carry = parseInt(x/10);

    }

    for(let i = arr2.length;i<arr1.length;i++)
    {
      let x = arr1[i] + carry ;
      answer.push(x%10);
      carry = parseInt(x/10);
    }

    if(carry !==0)
    {
      answer.push(carry);
    }
    return answer;
}



let t = parseInt(readLine());
while(t)
{   
  let arr1 = readLine().split(" ");
  for(let i=0;i<arr1.length;i++) arr1[i] = parseInt(arr1[i]);

  let arr2 = readLine().split(" ");
  for(let i=0;i<arr2.length;i++) arr2[i] = parseInt(arr2[i]);

  let ans = addlist(arr1,arr2);
  console.log(ans.join(""));

  t -=1;
}