// https://www.codewars.com/kata/6507e3170b7009117e0c7865/train/javascript

// Passed

function freedPrisoners(prison) {
  let canFree = (doorState, stateChangeCount) =>
    stateChangeCount % 2 === 0 ? doorState : !doorState;
  let result = 0;
  if (prison.length && prison[0]) {
    for (const doorState of prison) {
      if (canFree(doorState, result)) {
        result++;
      }
    }
  }

  return result;
}

const output = freedPrisoners([true, true, false, false, false, true, false]);
console.log(output);