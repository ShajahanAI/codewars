// https://www.codewars.com/kata/5906a218dfeb0dbb52000005/train/javascript

// Passed

function hiddenWord(num) {
  const charMap = {
    6: "a",
    1: "b",
    7: "d",
    4: "e",
    3: "i",
    2: "l",
    9: "m",
    8: "n",
    0: "o",
    5: "t",
  };

  const word = String(num)
    .split("")
    .map((num) => charMap[Number(num)])
    .join("");
  return word;
}


const output = hiddenWord(637);
console.log(output);