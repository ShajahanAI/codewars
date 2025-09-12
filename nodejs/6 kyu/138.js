// https://www.codewars.com/kata/59c3e819d751df54e9000098/train/javascript

// Passed

function getConsectiveItems(items, key) {
  items = String(items);
  key = String(key);
  let consecutiveCounts = [];
  let currentCount = 0;
  for (const char of items) {
    if (char === key) {
      currentCount++;
    } else {
      consecutiveCounts.push(currentCount);
      currentCount = 0;
    }
  }

  let maxConsecutiveCount = Math.max(...consecutiveCounts, currentCount);
  return maxConsecutiveCount;
}

const output = getConsectiveItems(
  "ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii",
  "i"
);
console.log(output);