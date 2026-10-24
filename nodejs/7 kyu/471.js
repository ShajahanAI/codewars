// https://www.codewars.com/kata/5af974846bf32304a2000e98/train/javascript

// Passed

function majority(arr) {
  let elementToCountMap = new Object();
  let maxCount = 0;
  for (const elem of arr) {
    if (!(elem in elementToCountMap)) {
      elementToCountMap[elem] = 0;
    }

    elementToCountMap[elem]++;
    if (maxCount < elementToCountMap[elem]) {
      maxCount = elementToCountMap[elem];
    }
  }

  let elementsWithMaxCount = [];
  for (const elem of Object.keys(elementToCountMap)) {
    let elemCount = elementToCountMap[elem];
    if (maxCount === elemCount) {
      elementsWithMaxCount.push(elem);
    }
  }

  let result =
    elementsWithMaxCount.length === 1 ? elementsWithMaxCount[0] : null;
  return result;
}

const output = majority(["A", "A", "A", "BBBBBBBB"]);
console.log(output);