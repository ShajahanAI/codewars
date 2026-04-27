// https://www.codewars.com/kata/5668e3800636a6cd6a000018/train/javascript

// Passed

function ghostBusters(building) {
  let result = "You just wanted my autograph didn't you?";
  let terms = building.split(" ");
  if (terms.length > 1) {
    result = terms.join("");
  }

  return result;
}

const output = ghostBusters("Sky scra per");
console.log(output);