// https://www.codewars.com/kata/57efab9acba9daa4d1000b30/train/javascript

// Passed

function bald(x) {
  let totalHairs = x
    .split("")
    .map((char) => (char === "-" ? 0 : 1))
    .reduce((prev, curr) => prev + curr, 0);
  let result = ["-".repeat(x.length)];
  let description;
  if (totalHairs === 0) {
    description = "Clean!";
  } else if (totalHairs === 1) {
    description = "Unicorn!";
  } else if (totalHairs === 2) {
    description = "Homer!";
  } else if (totalHairs <= 5) {
    description = "Careless!";
  } else {
    description = "Hobo!";
  }

  result.push(description);
  return result;
}

const output = bald("/---------");
console.log(output);