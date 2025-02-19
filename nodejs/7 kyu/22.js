// https://www.codewars.com/kata/577d5ce442a8d81e790002b2/train/javascript

// Passed

function validName(array) {
  if (array.length === 0) {
    return "You must test at least one name.";
  } else if (array.length === 1) {
    return "Congratulations, you can choose any name you like!";
  }

  return array.every((childName, index) => {
    return [0].includes(index)
      ? true
      : childName.toLowerCase()[0] ===
          array[index - 1].toLowerCase()[array[index - 1].length - 1];
  })
    ? "Congratulations, your baby names are compatible!"
    : "Back to the drawing board, your baby names are not compatible.";
}

const output = validName(["George", "Charlotte"]);
console.log(output);
