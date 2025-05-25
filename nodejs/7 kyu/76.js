// https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/train/javascript

// Passed

function capitalize(s, arr) {
  const characters = s.split("");
  const capitalizedString = characters
    .map((char, idx) => (arr.includes(idx) ? char.toUpperCase() : char))
    .join("");
  return capitalizedString;
}

const output = capitalize("abcdef",[1,2,5]);
console.log(output);