// https://www.codewars.com/kata/582b0d73c190130d550000c6/train/javascript

// Passed

function factors(n) {
  let [pastMaxSquare, pastMaxCube] = [false, false];
  let result = [[], []];
  for (let num = 2; num < n; num++) {
    if (pastMaxSquare && pastMaxCube) {
      break;
    }

    let numSquare = num ** 2;
    let numCube = numSquare * num;

    if (n % numSquare === 0) {
      result[0].push(num);
    }

    if (n % numCube === 0) {
      result[1].push(num);
    }

    if (numSquare > n) {
      pastMaxSquare = true;
    }

    if (numCube > 2) {
      pastMaxCube = true;
    }
  }

  return result;
}

const output = factors(81);
console.log(output);