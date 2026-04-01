// https://www.codewars.com/kata/559a28007caad2ac4e000083/train/javascript

// Passed

function perimeter(n) {
  let memo = {};
  let calculateFibo = (i) => {
    if (i === 0 || i === 1) {
      return 1;
    }

    if (i in memo) {
      return memo[i];
    }

    let result = calculateFibo(i - 1) + calculateFibo(i - 2);
    memo[i] = result;
    return result;
  };

  let perimeter = 0;
  for (let squareCount = 0; squareCount <= n; squareCount++) {
    let fiboNum = calculateFibo(squareCount);
    perimeter += fiboNum * 4;
  }

  return perimeter;
}

const output = perimeter(30);
console.log(output);