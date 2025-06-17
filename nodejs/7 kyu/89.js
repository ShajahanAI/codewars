// https://www.codewars.com/kata/56541980fa08ab47a0000040/train/javascript

// Passed

function printerError(s) {
  const validCharacters = "abcdefghijklm";
  const errors = s.split("").filter((char) => !validCharacters.includes(char));
  const result = String(errors.length) + "/" + String(s.length);
  return result;
}

const output = printerError("aaaxbbbbyyhwawiwjjjwwm");
console.log(output);