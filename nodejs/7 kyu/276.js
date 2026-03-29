// https://www.codewars.com/kata/62a933d6d6deb7001093de16/train/javascript

// Passed

function getTheVowels(word) {
  let vowels = ["a", "e", "i", "o", "u"];
  let currentIdx = 0;
  let consecutiveVowelCount = 0;
  for (const letter of word) {
    if (letter === vowels[currentIdx]) {
      consecutiveVowelCount++;
      currentIdx++;

      if (currentIdx >= vowels.length) {
        currentIdx = 0;
      }
    }
  }

  return consecutiveVowelCount;
}

const output = getTheVowels("akfheujfkgiaaaofmmfkdfuaiiie");
console.log(output);