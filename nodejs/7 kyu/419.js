// https://www.codewars.com/kata/570f6436b29c708a32000826/train/javascript

// Passed

function firstNonRepeated(s) {
  let charToCountMap = new Object();
  for (const char of s) {
    if (!(char in charToCountMap)) {
      charToCountMap[char] = 0;
    }

    charToCountMap[char]++;
  }

  let result = null;
  for (const char of s) {
    let charCount = charToCountMap[char];
    if (charCount === 1) {
      result = char;
      break;
    }
  }

  return result;
}

const output = firstNonRepeated("test");
console.log(output);