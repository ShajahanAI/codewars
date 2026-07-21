// https://www.codewars.com/kata/6912508732aab96c59c09c7d/train/javascript

// Passed

function reloadSheeps(arr) {
  let sheepSet = new Set("sheep");

  let result = [];
  for (const possibleSheep of arr) {
    let possibleSheepMap = new Object();
    for (const char of possibleSheep) {
      if (!sheepSet.has(char)) {
        continue;
      }

      if (!(char in possibleSheepMap)) {
        possibleSheepMap[char] = 0;
      }
      possibleSheepMap[char]++;
    }

    let isProperSheep = true;
    for (const char of sheepSet) {
      let charCountToCompare = char === "e" ? 2 : 1;
      if (possibleSheepMap[char] !== charCountToCompare) {
        isProperSheep = false;
        break;
      }
    }
    if (isProperSheep) {
      result.push("sheep");
    }
  }

  return result;
}

const output = reloadSheeps(["pe", "hehe", "heeps", "eee", "ti", "peehs"]);
console.log(output);