// https://www.codewars.com/kata/5a084a098ba9146690000969/train/javascript

// Passed

function timeConvert(num) {
  if (num < 0) {
    num = 0;
  }

  let applyPadding = (num) =>
    String(num).length === 1 ? "0" + String(num) : String(num);
  let hours = applyPadding(Math.floor(num / 60));
  let minutes = applyPadding(num % 60);
  let convertedTime = [hours, minutes].join(":");
  return convertedTime;
}

const output = timeConvert(75);
console.log(output);