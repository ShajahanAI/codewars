// https://www.codewars.com/kata/59f11118a5e129e591000134/train/javascript

// Passed

function repeats(arr) {
  let numCountDict = new Object();
  for (const num of arr) {
    if (!(num in numCountDict)) {
      numCountDict[num] = 0;
    }

    numCountDict[num]++;
  }

  let result = 0;
  for (num of Object.keys(numCountDict)) {
    if (numCountDict[num] === 1) {
      // num only appears once (is unique)
      result += Number(num);
    }
  }

  return result;
}

const output = repeats([9, 10, 19, 13, 19, 13]);
console.log(output);