// https://www.codewars.com/kata/5a19701d80171fd71d000029/train/javascript

// Passed

function getCharacterCodes(str) {
  let characters = str.split("");
  let characterCodes = characters.map((char) => char.charCodeAt());
  return characterCodes;
}

function encode(str) {
  let characterCodes = getCharacterCodes(str);
  let newCharacters = characterCodes.map((code) =>
    String.fromCharCode(code * 6),
  );
  let result = newCharacters.join("");
  return result;
}

function decode(str) {
  let characterCodes = getCharacterCodes(str);
  let newCharacters = characterCodes.map((code) =>
    String.fromCharCode(code / 6),
  );
  let result = newCharacters.join("");
  return result;
}

const output1 = encode("Hello World!");
const output2 = decode("ưɞʈʈʚÀȊʚʬʈɘÆ");
console.log(output1, output2);