// https://www.codewars.com/kata/58f8b35fda19c0c79400020f/train/javascript

// Passed

function allNonConsecutive(arr) {
  let nonConsecutives = [];
  for (let idx = 0; idx < arr.length; idx++) {
    if (idx == arr.length - 1) continue;

    if (arr[idx + 1] - arr[idx] !== 1) {
      // found a non consecutive at idx + 1
      let nonConsecutive = arr[idx + 1];
      nonConsecutives.push({
        i: idx + 1,
        n: nonConsecutive,
      });
    }
  }

  return nonConsecutives;
}

const output = allNonConsecutive([1, 2, 3, 4, 6, 7, 8, 10]);
console.log(output);