// https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/javascript

// Passed

function correct(string) {
  let mistakeToCorrectionMap = {
    5: "S",
    0: "O",
    1: "I",
  };

  let result = string;
  for (const mistake of Object.keys(mistakeToCorrectionMap)) {
    let correction = mistakeToCorrectionMap[mistake];
    result = result.replaceAll(String(mistake), correction);
  }

  return result;
}

const output = correct("L0ND0N");
console.log(output);