// https://www.codewars.com/kata/57e0206335e198f82b00001d/train/javascript

// Passed

function esrever(str) {
  if (str.length === 0) return "";

  const punctuation = str[str.length - 1];
  let stringToReverse = str.slice(0, str.length - 1);
  let result = stringToReverse.split("").reverse().join("") + punctuation;
  return result;
}

const output = esrever("b3tTer p4ss thIS 0ne.");
console.log(output);