// https://www.codewars.com/kata/59de795c289ef9197f000c48/train/javascript

// Passed

function removeBMW(str) {
  if (typeof str !== "string") {
    return new Error("This program only works for text.");
  }
  let charactersToRemove = "bmwBMW";
  let filteredCharacters = str
    .split("")
    .filter((char) => !charactersToRemove.includes(char));
  let result = filteredCharacters.join("");
  return result;
}

const output = removeBMW("bmwvolvoBMW");
console.log(output);