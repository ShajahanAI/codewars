// https://www.codewars.com/kata/5a58d889880385c2f40000aa/train/javascript

// Passed

function automorphic(n) {
  let squaredNumber = n ** 2;
  if (String(squaredNumber).endsWith(String(n))) {
    return "Automorphic";
  }

  return "Not!!";
}

const output = automorphic(25);
console.log(output);