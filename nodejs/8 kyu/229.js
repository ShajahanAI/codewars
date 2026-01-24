// https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/javascript

// Passed

function check(a, x) {
  let result = a.includes(x);
  return result;
}

const output = check([66, 101], 66);
console.log(output);