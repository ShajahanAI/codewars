// https://www.codewars.com/kata/588810c99fb63e49e1000606/train/javascript

// Passed

function houseOfCats(legs) {
  let possiblePersonCounts = [];
  for (
    let possibleCatCount = 0;
    possibleCatCount <= Math.floor(legs / 4);
    possibleCatCount++
  ) {
    const possiblePersonCount = Math.floor((legs - possibleCatCount * 4) / 2);
    possiblePersonCounts.push(possiblePersonCount);
  }

  return possiblePersonCounts.reverse();
}

const output = houseOfCats(10);
console.log(output);
