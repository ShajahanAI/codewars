// https://www.codewars.com/kata/619f200fd0ff91000eaf4a08/train/javascript

// Passed

function oddOrEven(n) {
  let isOdd = (num) => num % 2 === 1;
  if (isOdd(n)) {
    return "Either";
  } else {
    let numberPairs = n / 2;
    if (isOdd(numberPairs)) {
      return "Odd";
    } else {
      return "Even";
    }
  }
}

const output = oddOrEven(6);
console.log(output);