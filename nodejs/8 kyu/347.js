// https://www.codewars.com/kata/64fbfe2618692c2018ebbddb/train/javascript

// Passed

function flickSwitch(arr) {
  let currentVal = true;
  let result = [];
  for (const item of arr) {
    if (item === "flick") {
      currentVal = !currentVal;
    }

    result.push(currentVal);
  }

  return result;
}

const output = flickSwitch(["codewars", "flick", "code", "wars"]);
console.log(output);