// https://www.codewars.com/kata/5a24254fe1ce0ec2eb000078/train/javascript

// Passed

function solve(str, idx) {
  let result = -1;
  if (str[idx] !== "(") {
    return result;
  }

  let depthCounter = 0;
  for (let currentIdx = idx + 1; currentIdx < str.length; currentIdx++) {
    let char = str[currentIdx];
    if (char === ")") {
      if (depthCounter === 0) {
        result = currentIdx;
        break;
      }

      depthCounter--;
    } else if (char === "(") {
      depthCounter++;
    }
  }

  return result;
}

const output = solve("((1)23(45))(aB)", 0);
console.log(output);