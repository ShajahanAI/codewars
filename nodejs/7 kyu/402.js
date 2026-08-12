// https://www.codewars.com/kata/5a71939d373c2e634200008e/train/javascript

// Passed

function solve(str) {
  let wordLengths = str.split(" ").map((word) => word.length);
  let strWithoutSpace = str.replaceAll(" ", "");
  let newWords = [];
  let currentIdx = strWithoutSpace.length - 1;
  for (const wordLength of wordLengths) {
    let word = "";
    for (let count = 0; count < wordLength; count++) {
      word += strWithoutSpace[currentIdx];
      currentIdx--;
    }

    newWords.push(word);
  }
  let result = newWords.join(" ");
  return result;
}

const output = solve("your code rocks");
console.log(output);