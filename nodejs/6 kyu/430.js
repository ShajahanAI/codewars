// https://www.codewars.com/kata/54f9f4d7c41722304e000bbb/train/javascript

// Passed

function firstDup(string) {
  let charToFirstIdxMap = new Object();
  let charToCountMap = new Object();

  for (let idx = 0; idx < string.length; idx++) {
    let char = string[idx];
    if (!(char in charToFirstIdxMap)) {
      charToFirstIdxMap[char] = idx;
    }

    if (!(char in charToCountMap)) {
      charToCountMap[char] = 0;
    }

    charToCountMap[char]++;
  }

  let result;
  for (const char of Object.keys(charToCountMap)) {
    let charCount = charToCountMap[char];
    if (charCount === 1) {
      continue;
    }

    if (
      result === undefined ||
      charToFirstIdxMap[char] < charToFirstIdxMap[result]
    ) {
      result = char;
    }
  }

  return result;
}

const output = firstDup("tweet");
console.log(output);