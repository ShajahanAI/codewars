// https://www.codewars.com/kata/5aa736a455f906981800360d/train/javascript

// Passed

function feast(beast, dish) {
  let [startLetter, endLetter] = [beast[0], beast[beast.length - 1]];
  let result = dish.startsWith(startLetter) && dish.endsWith(endLetter);
  return result;
}

const output = feast("great blue heron", "garlic naan");
console.log(output);