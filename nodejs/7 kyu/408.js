// https://www.codewars.com/kata/59de469cfc3c492da80000c5/train/javascript

// Passed

function compress(sentence) {
  let wordToValueMap = new Object();
  let words = sentence.toLowerCase().split(" ");
  let currentVal = 0;
  let result = "";
  for (const word of words) {
    if (!(word in wordToValueMap)) {
      wordToValueMap[word] = currentVal;
      currentVal++;
    }

    let wordVal = wordToValueMap[word];
    result += String(wordVal);
  }

  return result;
}

const output = compress("SILLY LITTLE BOYS silly little boys");
console.log(output);