// https://www.codewars.com/kata/5572392fee5b0180480001ae/train/javascript

// Passed

function computerToPhone(numbers) {
  computerPhoneMap = {
    1: "7",
    2: "8",
    3: "9",
    4: "4",
    5: "5",
    6: "6",
    7: "1",
    8: "2",
    9: "3",
    0: "0",
  };

  const phoneLayout = numbers
    .split("")
    .map((num) => computerPhoneMap[Number(num)])
    .join("");
  return phoneLayout;
}

const output = computerToPhone("0789456123");
console.log(output);