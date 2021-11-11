// https://6793fdf6.widgets.sphere-engine.com/lp?hash=ZcCuiUnKT8

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let n = parseInt(readLine());
if (n==0)
{
 console.log(-1);
}
else
{

  let arr1 = [];
  for(let i =0;i<n;i++)
  {
    arr1.push(parseInt(readLine()));
  }
  
  
  let count1 = 1;
  ans = 1;
  for(let j=1;j<n;j++)
  {
    if(arr1[j]===arr1[j-1])
    {
    count1++;
    }
    else
    {
      ans = Math.max(ans,count1);
      count1 = 1;
    }
  }
  ans  = Math.max(ans,count1);
  
  let final1 = [];
  count1 = 1;
  for(let j=1;j<n;j++){
    if(arr1[j]===arr1[j-1])
    {
      count1++;
    }
    else
    {
      if(count1===ans)
      {
        final1.push(arr1[j-1]);
      }
      count1 = 1;
    }
  }

  if(count1===ans)
  {
    final1.push(arr1[arr1.length-1]);
  }

  for(let i=0;i< final1.length;i++)
  {
    console.log(final1[i]);
  }
  
}
