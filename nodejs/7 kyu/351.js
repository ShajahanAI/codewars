// https://www.codewars.com/kata/56582133c932d8239900002e/train/javascript

// Passed

function mostFrequentItemCount(collection) {
  let itemToCountMap = new Object();
  let mostFrequentCount = 0;
  for (const item of collection) {
    if (!(item in itemToCountMap)) {
      itemToCountMap[item] = 0;
    }

    itemToCountMap[item]++;
    let currentItemCount = itemToCountMap[item];
    if (currentItemCount > mostFrequentCount) {
      mostFrequentCount = currentItemCount;
    }
  }

  return mostFrequentCount;
}

const output = mostFrequentItemCount([
  3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3,
]);
console.log(output);