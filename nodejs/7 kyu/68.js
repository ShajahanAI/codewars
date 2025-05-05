// https://www.codewars.com/kata/56d55dcdc87df58c81000605/train/javascript

// Passed

function validCard(card) {
  const cardSum = card
    .split(" ")
    .join("")
    .split("")
    .map((numString, idx) => {
      if (idx % 2 !== 0) {
        return Number(numString);
      }

      let num = Number(numString) * 2;
      if (String(num).length > 1) {
        // final number would have to single digit
        num = String(num)
          .split("")
          .map((digit) => Number(digit))
          .reduce((prev, curr) => prev + curr, 0);
      }
      return num;
    })
    .reduce((prev, curr) => prev + curr, 0);

  return cardSum % 10 === 0 ? true : false;
}

const output = validCard("5457 6238 9823 4311");
console.log(output);
