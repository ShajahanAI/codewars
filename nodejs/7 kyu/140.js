// https://www.codewars.com/kata/61123a6f2446320021db987d/train/javascript

// Passed

const prevMultOfThree = (n) => {
  let strNumber = String(n);
  for (let idx = 0; idx < strNumber.length; idx++) {
    let currentNumber = Number(strNumber.slice(0, strNumber.length - idx));
    if (currentNumber % 3 === 0) {
      return currentNumber;
    }
  }

  return null;
};

const output = prevMultOfThree(1244);
console.log(output);
