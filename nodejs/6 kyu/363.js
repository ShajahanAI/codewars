// https://www.codewars.com/kata/55688b4e725f41d1e9000065/train/javascript

// Passed

function fibonacci(max) {
  let memo = new Object();
  let getFibo = (idx) => {
    if (idx === 0) {
      return 0;
    } else if (idx === 1) {
      return 1;
    }

    let result;
    if (idx in memo) {
      result = memo[idx];
    } else {
      result = getFibo(idx - 1) + getFibo(idx - 2);
      memo[idx] = result;
    }

    return result;
  };

  let getEvenFiboSequenceTillN = (n) => {
    let currentIdx = 0;
    let fiboVal = getFibo(currentIdx);
    let result = [];
    while (fiboVal < n) {
      if (fiboVal % 2 === 0) {
        result.push(fiboVal);
      }

      currentIdx++;
      fiboVal = getFibo(currentIdx);
    }

    return result;
  };

  let evenFiboSequenceTillN = getEvenFiboSequenceTillN(max);
  let result = evenFiboSequenceTillN.reduce((prev, curr) => prev + curr, 0);
  return result;
}

const output = fibonacci(2147483647);
console.log(output);