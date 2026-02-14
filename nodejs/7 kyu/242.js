// https://www.codewars.com/kata/5a2b7edcb6486a856e00005b/train/javascript

// Passed

function checkVowel(string, position) {
  if (position < 0 || position >= string.length) {
    return false;
  }

  let letter = string[position].toLowerCase();
  let isVowel = "aeiou".includes(letter);
  return isVowel;
}

const output = checkVowel("cat", 1);
console.log(output);