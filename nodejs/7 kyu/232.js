// https://www.codewars.com/kata/563f037412e5ada593000114/train/javascript

// Passed

function calculateYears(principal, interest, tax, desired) {
  let yearsNeeded = 0;
  let currentAmt = principal;
  while (currentAmt < desired) {
    let interestAmt = currentAmt * interest;
    let taxAccured = interestAmt * tax;
    currentAmt = currentAmt + (interestAmt - taxAccured);
    yearsNeeded++;
  }
  return yearsNeeded;
}

const output = calculateYears(1000, 0.05, 0.18, 1100);
console.log(output);