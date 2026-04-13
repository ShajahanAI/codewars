// https://www.codewars.com/kata/56576f82ab83ee8268000059/train/javascript

// Passed

function spacey(array) {
  let result = array.map((elem, idx) => array.slice(0, idx + 1).join(""));
  return result;
}

const output = spacey(["this", "cheese", "has", "no", "holes"]);
console.log(output);