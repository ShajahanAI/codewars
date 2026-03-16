// https://www.codewars.com/kata/69b58aaee8f1deef7ece7d0e/train/javascript

// Passed

function breachAttempts(hackers, securityLevel, increase) {
  let successfulBreaches = 0;
  for (const hackLevel of hackers) {
    if (securityLevel < hackLevel) {
      successfulBreaches++;
    } else {
      securityLevel += increase;
    }
  }

  return successfulBreaches;
}

const output = breachAttempts([7, 6, 8, 9], 6, 2, 1);
console.log(output);