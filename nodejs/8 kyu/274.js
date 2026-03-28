// https://www.codewars.com/kata/55eea63119278d571d00006a/train/javascript

// Passed

function nextId(ids) {
  let idsSet = new Set(ids);
  let smallestUnusedId = 0;
  while (idsSet.has(smallestUnusedId)) {
    smallestUnusedId++;
  }

  return smallestUnusedId;
}

const output = nextId([1, 2, 0, 2, 3, 5]);
console.log(output);