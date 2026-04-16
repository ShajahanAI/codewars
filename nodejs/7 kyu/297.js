// https://www.codewars.com/kata/5a60d519400f93fc450032e5/train/javascript

// Passed

function hopAcross(lst) {
  let [leftToRightHops, rightToLeftHops] = [0, 0];

  // leftToRight
  let currentIdx = 0;
  while (currentIdx < lst.length) {
    leftToRightHops++;
    currentIdx += lst[currentIdx];
  }

  // rightToLeft
  currentIdx = lst.length - 1;
  while (currentIdx >= 0) {
    rightToLeftHops++;
    currentIdx -= lst[currentIdx];
  }

  let totalHops = leftToRightHops + rightToLeftHops;
  return totalHops;
}

const output = hopAcross([2, 2, 3, 1, 1, 2, 1]);
console.log(output);