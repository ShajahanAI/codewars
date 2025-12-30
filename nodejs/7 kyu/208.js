// https://www.codewars.com/kata/56b8903933dbe5831e000c76/train/javascript

// Passed

function spoonerize(words) {
  let [firstWord, secondWord] = words.split(" ");
  let [modifiedFirstWord, modifiedSecondWord] = [
    secondWord[0] + firstWord.slice(1),
    firstWord[0] + secondWord.slice(1),
  ];
  let result = `${modifiedFirstWord} ${modifiedSecondWord}`;
  return result;
}

const output = spoonerize("nit picking");
console.log(output);