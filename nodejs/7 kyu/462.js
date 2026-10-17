// https://www.codewars.com/kata/57cc847e58a06b1492000264/train/javascript

// Passed

function sortTransform(a) {
  let arrToWord = (arr) => {
    let charCodes = arr.slice(0, 2).concat(arr.slice(arr.length - 2));
    let characters = charCodes.map((charCode) =>
      String.fromCharCode(charCode).trim(),
    );
    let word = characters.join("");
    return word;
  };

  let ascendingArr = [...a].sort((a, b) => a - b);
  let descendingArr = [...ascendingArr].reverse();

  let lastWordCharacters = a
    .map((charCode) => String.fromCharCode(charCode).trim())
    .sort();
  let lastWord = lastWordCharacters
    .slice(0, 2)
    .concat(lastWordCharacters.slice(lastWordCharacters.length - 2))
    .join("");
  let words = [a, ascendingArr, descendingArr].map(arrToWord).concat(lastWord);

  let result = words.join("-");
  return result;
}

const output = sortTransform([111, 112, 113, 114, 115, 113, 114, 110]);
console.log(output);