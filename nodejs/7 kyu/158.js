// https://www.codewars.com/kata/57061b6fcb7293901a000ac7/train/javascript

// Passed

function headSmash(array) {
  if (typeof array === "number") {
    return "This isn't the gym!!";
  }

  let result =
    array.length !== 0
      ? array.map((string) => string.replaceAll("O", " "))
      : "Gym is empty";
  return result;
}

const output = headSmash([
  "*****************************************",
  "**  _O_   *   _O_   *   _O_   *   _O_  **",
  "** C(.)J  *  /(.)J  *  /(.)J  *  C(.)J **",
  "** _/ |_  *  _| |_  *  _( )_  *  _/ )_ *",
]);
console.log(output);