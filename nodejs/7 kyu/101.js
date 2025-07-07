// https://www.codewars.com/kata/57b6f850a6fdc76523001162/train/javascript

// Passed

function counterEffect(hitCount) {
  let result = [];
  for (let digit of hitCount) {
    digit = Number(digit);
    let preceedingDigits = [];
    for (let count = 0; count <= digit; count++) {
      preceedingDigits.push(count);
    }
    result.push(preceedingDigits);
  }

  return result;
}

const output = counterEffect("1250");
console.log(output);