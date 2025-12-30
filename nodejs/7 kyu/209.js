// https://www.codewars.com/kata/56dbed3a13c2f61ae3000bcd/train/javascript

// Passed

function noonerize(numbers) {
  if (!numbers.every((num) => typeof num == "number")) return "invalid array";
  let numbersAsString = numbers.map((num) => String(num));
  let [firstNumString, secondNumString] = numbersAsString;
  let [modifiedFirstNum, modifiedSecondNum] = [
    secondNumString[0] + firstNumString.slice(1),
    firstNumString[0] + secondNumString.slice(1),
  ];
  let AbsoluteDifference = Math.abs(
    Number(modifiedFirstNum) - Number(modifiedSecondNum)
  );
  return AbsoluteDifference;
}

const output = noonerize([55, 63]);
console.log(output);