// https://www.codewars.com/kata/5a430359e1ce0e35540000b1/train/javascript

// Passed

function averageLength(array) {
  const avgLength =
    array.reduce((totalLength, currWord) => totalLength + currWord.length, 0) /
    array.length;
  return array.map((word) => word[0].repeat(Math.round(avgLength)));
}

const output = averageLength(["aa", "bbbbb", "c"]);
console.log(output);
