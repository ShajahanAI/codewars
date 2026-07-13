// https://www.codewars.com/kata/6a520b948dc07d11d0342a58/train/javascript

// Passed

function zfcDefinition(n, memo = {}) {
  if (n === 0) {
    return "{}";
  }

  let definitions = [];
  for (let num = 0; num < n; num++) {
    let definition;
    if (num in memo) {
      definition = memo[num];
    } else {
      definition = zfcDefinition(num, (memo = memo));
      memo[num] = definition;
    }

    definitions.push(definition);
  }
  let result = `{${definitions.join(",")}}`;
  return result;
}

const output = zfcDefinition(3);
console.log(output);