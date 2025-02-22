// https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/javascript

// Passed

function solution(str) {
  const pairArray = [];
  const charactersArray = str.split("");
  let pair;
  for (let index = 0; index < charactersArray.length; index += 2) {
    const char = charactersArray[index];
    if (charactersArray[index + 1] === undefined) {
      pair = char + "_";
    } else {
      pair = char + charactersArray[index + 1];
    }

    pairArray.push(pair);
  }

  return pairArray;
}

const output = solution("hello");
console.log(output);
