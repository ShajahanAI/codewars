// https://www.codewars.com/kata/52840d2b27e9c932ff0016ae/train/javascript

// Passed

function locate(arr, value) {
  for (const elem of arr) {
    if (Array.isArray(elem)) {
      let valueFound = locate(elem, value);
      if (valueFound) {
        return true;
      }
    } else {
      if (elem === value) {
        return true;
      }
    }
  }

  return false;
}

const output = locate(["a", "b", ["c", "d", ["e"]]], "d");
console.log(output);