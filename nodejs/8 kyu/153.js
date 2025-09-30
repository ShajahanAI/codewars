// https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1/train/javascript

// Passed

function getAge(inputString) {
  let age = Number(inputString.split(" ")[0]);
  return age;
}

const output = getAge("4 years old");
console.log(output);