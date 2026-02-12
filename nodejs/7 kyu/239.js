// https://www.codewars.com/kata/597bb84522bc93b71e00007e/train/javascript

// Passed

function stringMerge(string1, string2, letter) {
  let subString1 = string1.slice(0, string1.indexOf(letter));
  let subString2 = string2.slice(string2.indexOf(letter) + 1);
  let result = subString1 + letter + subString2;
  return result;
}

const output = stringMerge("person", "here", "e");
console.log(output);