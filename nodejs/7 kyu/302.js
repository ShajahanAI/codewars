// https://www.codewars.com/kata/585a033e3a36cdc50a00011c/train/javascript

// Passed

function freqSeq(str, sep) {
  let characterToFrequencyMap = new Object();
  for (const char of str) {
    if (!(char in characterToFrequencyMap)) {
      characterToFrequencyMap[char] = 0;
    }
    characterToFrequencyMap[char]++;
  }

  let sequenceArr = str
    .split("")
    .map((char) => String(characterToFrequencyMap[char]));
  let sequence = sequenceArr.join(sep);
  return sequence;
}

const output = freqSeq("hello world", "-");
console.log(output);