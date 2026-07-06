// https://www.codewars.com/kata/57547f9182655569ab0008c4/train/javascript

// Passed

function replicate(times, number) {
  number = String(number);
  let result =
    times > 0
      ? number
          .repeat(times)
          .split(number)
          .filter((emptyStr, idx) => idx !== 0)
          .map((emptyStr) => Number(number))
      : [];
  return result;
}

const output = replicate(3, 5);
console.log(output);