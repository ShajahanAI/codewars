// https://www.codewars.com/kata/5a19226646d843de9000007d/train/javascript

// Passed

function countConsonants(str) {
  let vowels = new Set("aeiou");
  let uniqueLowercasedCharacters = Array.from(
    new Set(str.toLowerCase().split("")),
  );
  let consonants = uniqueLowercasedCharacters.filter(
    (char) =>
      97 <= char.charCodeAt() && char.charCodeAt() <= 122 && !vowels.has(char),
  );
  let result = consonants.length;
  return result;
}

const output = countConsonants("Count my unique consonants!!");
console.log(output);