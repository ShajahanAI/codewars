// https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/javascript

// Passed

function capitalize(s) {
  let characters = s.split("");
  let result = ["", ""];
  for (let idx = 0; idx < characters.length; idx++) {
    let char = characters[idx];
    let isEvenIdx = idx % 2 === 0;
    result[0] += isEvenIdx ? char.toUpperCase() : char.toLowerCase();
    result[1] += isEvenIdx ? char.toLowerCase() : char.toUpperCase();
  }
  return result;
}

const output = capitalize("abracadabra");
console.log(output);