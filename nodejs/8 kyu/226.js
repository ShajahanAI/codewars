// https://www.codewars.com/kata/5302d846be2a9189af0001e4/train/javascript

// Passed

function sayHello(name, city, state) {
  let fullName = name.join(" ");
  let result = `Hello, ${fullName}! Welcome to ${city}, ${state}!`;
  return result;
}

const output = sayHello(["John", "Smith"], "Phoenix", "Arizona");
console.log(output);