// https://www.codewars.com/kata/5680781b6b7c2be860000036/train/javascript

// Passed

function vowelIndices(word) {
  let vowelPositions = [];
  let vowels = ["a", "e", "i", "o", "u", "y"];
  let currIdx = 0;
  for (const letter of word) {
    if (vowels.includes(letter.toLowerCase())) {
      vowelPositions.push(currIdx + 1);
    }

    currIdx++;
  }

  return vowelPositions;
}

const output = vowelIndices("apple");
console.log(output);