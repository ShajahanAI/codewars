// https://www.codewars.com/kata/524f5125ad9c12894e00003f

// Passed

function remainder(n, m){
    // Divide the larger argument by the smaller argument and return the remainder
    const dividend = n > m ? n : m;
    const divisor = m > n ? n : m;
    console.log('Dividend:-', dividend, 'Divisor:-', divisor);

    if (divisor === 0)
        return NaN

    if (!(dividend && divisor)) {
        if (dividend === 0)
            return 0
    }
     
    return dividend % divisor
  }

const output = remainder(55, 7);
console.log(output);