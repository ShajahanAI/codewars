// https://www.codewars.com/kata/57e3f79c9cb119374600046b/train/javascript

// Passed

function hello(name) {
  name = name ? name[0].toUpperCase() + name.slice(1).toLowerCase() : name;
  let result = name ? `Hello, ${name}!` : `Hello, World!`;
  return result;
}

const output = hello("johN");
console.log(output);