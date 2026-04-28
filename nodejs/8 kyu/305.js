// https://www.codewars.com/kata/5704aea738428f4d30000914/train/javascript

// Passed

function tripleTrouble(one, two, three) {
  let arrToJoin = one
    .split("")
    .map((char, idx) => one[idx] + two[idx] + three[idx]);
  let result = arrToJoin.join("");
  return result;
}

const output = tripleTrouble("aaa", "bbb", "ccc");
console.log(output);