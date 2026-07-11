// https://www.codewars.com/kata/586566b773bd9cbe2b000013/train/javascript

// Passed

function noRepeat(str) {
  let charToCountMap = new Object();
  for (const char of str) {
    if (!(char in charToCountMap)) {
      charToCountMap[char] = 0;
    }

    charToCountMap[char]++;
  }

  let result;
  for (const char of str) {
    if (charToCountMap[char] === 1) {
      result = char;
      break;
    }
  }

  return result;
}

const output = noRepeat("aabbccdde");
console.log(output);