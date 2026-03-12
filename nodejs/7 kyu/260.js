// https://www.codewars.com/kata/557a2c136b19113912000010/train/javascript

// Passed

function reverseIt(data) {
  let dataType = typeof data;
  let reverse = (strElem) => String(strElem).split("").reverse().join("");
  if (dataType === "number") {
    data = Number(reverse(data));
  } else if (dataType === "string") {
    data = reverse(data);
  }

  return data;
}

const output = reverseIt(314159);
console.log(output);