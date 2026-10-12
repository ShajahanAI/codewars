// https://www.codewars.com/kata/55f2b110f61eb01779000053/train/javascript

// Passed

function getSum(a, b) {
  let result = 0;
  let [smallNum, bigNum] = [a, b].sort((num_1, num_2) => num_1 - num_2);
  for (let num = smallNum; num <= bigNum; num++) {
    result += num;
  }

  return result;
}

const output = getSum(0, 1);
console.log(output);