// https://www.codewars.com/kata/59e9f404fc3c49ab24000112/train/javascript

// Passed

function nerdify(txt) {
  let charToReplaceCharMap = {
    A: "4",
    E: "3",
    a: "4",
    e: "3",
    l: "1",
  };

  let result = "";
  for (char of txt) {
    newCharacter = char;
    if (char in charToReplaceCharMap) {
      newCharacter = charToReplaceCharMap[char];
    }

    result += newCharacter;
  }

  return result;
}

const output = nerdify("Los Angeles");
console.log(output);