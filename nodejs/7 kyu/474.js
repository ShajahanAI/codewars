// https://www.codewars.com/kata/56bf3287b5106eb10f000899/train/javascript

// Passed

function moveVowel(input) {
  let vowels = new Set("aeiou");
  let [firstPart, secondPart] = ["", ""];

  for (const char of input) {
    if (vowels.has(char.toLowerCase())) {
      secondPart += char;
    } else {
      firstPart += char;
    }
  }

  let result = firstPart + secondPart;
  return result;
}

const output = moveVowel("apple");
console.log(output);