// https://www.codewars.com/kata/56747fd5cb988479af000028/train/javascript

// Passed

function getMiddle(s) {
  let startIdx, endIdx;
  if (s.length % 2 === 0) {
    startIdx = s.length / 2 - 1;
    endIdx = startIdx + 2;
  } else {
    startIdx = Math.floor(s.length / 2);
    endIdx = startIdx + 1;
  }

  let middle = s.slice(startIdx, endIdx);
  return middle;
}

const output = getMiddle("middle");
console.log(output);