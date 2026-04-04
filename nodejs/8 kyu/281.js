// https://www.codewars.com/kata/53af2b8861023f1d88000832/train/javascript

// Passed

function areYouPlayingBanjo(name) {
  let result;
  if (name[0].toLowerCase() === "r") {
    result = name + " plays banjo";
  } else {
    result = name + " does not play banjo";
  }

  return result;
}

const output = areYouPlayingBanjo("Paul");
console.log(output);