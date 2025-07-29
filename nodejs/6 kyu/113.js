// https://www.codewars.com/kata/5897cdc26551af891c000124/train/javascript

// Passed

function hofstadterQ(n, memo = {}) {
  if (n === 1 || n === 2) return 1;

  if (n in memo) {
    return memo[n];
  }

  // caching to memo
  let result =
    hofstadterQ(n - hofstadterQ(n - 1, (memo = memo)), (memo = memo)) +
    hofstadterQ(n - hofstadterQ(n - 2, (memo = memo)), (memo = memo));
  memo[n] = result;

  return result;
}

const output = hofstadterQ(1000);
console.log(output);