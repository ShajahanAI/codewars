// https://www.codewars.com/kata/59727ff285281a44e3000011/train/javascript

// Passed

function bandNameGenerator(str) {
  let bandName;
  if (str[0] === str[str.length - 1]) {
    bandName = str[0].toUpperCase() + str.slice(1) + str.slice(1);
  } else {
    bandName = "The " + str[0].toUpperCase() + str.slice(1);
  }

  return bandName;
}

const output = bandNameGenerator("sandles");
console.log(output);