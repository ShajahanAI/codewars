// https://www.codewars.com/kata/585b1fafe08bae9988000314/train/javascript

// Passed

function explode(s) {
  let explodedString = s
    .split("")
    .map((digitString) => digitString.repeat(Number(digitString)))
    .join("");
  return explodedString;
}

const output = explode("312");
console.log(output);