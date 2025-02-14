// https://www.codewars.com/kata/56b0f5f84de0afafce00004e/train/javascript

// Failed

function relativelyPrime(n, arr) {
  let relativePrimes = [];
  let nFactors = [];

  for (let i = 2; i <= n - 1; i++) {
    if (n % i === 0) {
      nFactors.push(i);
    }
  }

  for (const num of arr) {
    let isRelativePrime = true;
    for (const nFactor of nFactors) {
      if (isRelativePrime && num % nFactor !== 0) {
        isRelativePrime = true;
      } else {
        isRelativePrime = false;
      }
    }

    if (isRelativePrime) {
      relativePrimes.push(num);
    }
  }

  return relativePrimes;
}

const output = relativelyPrime(15, [72, 27, 32, 61, 77, 11, 40]);
console.log(output);
