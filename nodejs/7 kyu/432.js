// https://www.codewars.com/kata/57ee24e17b45eff6d6000164/train/javascript

// Passed

function catMouse(x) {
  let result = x.length - 2 > 3 ? "Escaped!" : "Caught!";
  return result;
}

const output = catMouse("C.....m");
console.log(output);