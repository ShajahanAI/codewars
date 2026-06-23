// https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/javascript

// Passed

function divisors(integer) {
  let divisorNums = [];
  for (
    let possibleDivisor = 2;
    possibleDivisor <= Math.ceil(integer / 2);
    possibleDivisor++
  ) {
    if (integer % possibleDivisor === 0) {
      divisorNums.push(possibleDivisor);
    }
  }

  let result = divisorNums.length === 0 ? `${integer} is prime` : divisorNums;
  return result;
}

const output = divisors(12);
console.log(output);