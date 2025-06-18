// https://www.codewars.com/kata/5ace2d9f307eb29430000092/train/javascript

// Passed

function modifyMultiply(str, loc, num) {
  const words = str.split(" ");
  const wordToMultiply = words[loc];
  let resultArray = [];
  for (let i = 0; i < num; i++) {
    resultArray.push(wordToMultiply);
  }
  const result = resultArray.join("-");
  return result;
}

const output = modifyMultiply(
  "Creativity is the process of having original ideas that have value. It is a process; it's not random.",
  8,
  10
);
console.log(output);