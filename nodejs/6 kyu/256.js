// https://www.codewars.com/kata/5a6225e5d8e145b540000127/train/javascript

// Passed

function common(a, b, c) {
  let totalSum = 0;
  let compileItemCountMap = (arr) => {
    let itemCountMap = {};
    for (const item of arr) {
      if (!(item in itemCountMap)) {
        itemCountMap[item] = 0;
      }

      itemCountMap[item]++;
    }

    return itemCountMap;
  };

  let bItemCountMap = compileItemCountMap(b);
  let cItemCountMap = compileItemCountMap(c);

  for (const item of a) {
    if (bItemCountMap[item] && cItemCountMap[item]) {
      bItemCountMap[item]--;
      cItemCountMap[item]--;
      totalSum += item;
    }
  }

  return totalSum;
}

const output = common([1, 2, 3], [5, 3, 2], [7, 3, 2]);
console.log(output);