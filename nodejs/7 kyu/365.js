// https://www.codewars.com/kata/55955a48a4e9c1a77500005a/train/javascript

// Passed

function greet(name) {
  let result = name ? `hello ${name}!` : null;
  return result;
}

const output = greet("Niks");
console.log(output);