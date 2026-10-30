// https://www.codewars.com/kata/670031c78cc02fa6c28ba28a/train/javascript

// Passed

function channellingPrimes(n) {
  let isPrime = (num) => {
    for (let n = 2; n <= num / 2; n++) {
      if (num % n === 0) {
        return false;
      }
    }
    return true;
  };

  let result = BigInt(0);
  for (let num = 1; num <= n; num++) {
    if (isPrime(num)) {
      result += 2n ** (BigInt(num) - 1n);
    }
  }
  result -= 1n;
  return result;
}

const output = channellingPrimes(21);
console.log(output);