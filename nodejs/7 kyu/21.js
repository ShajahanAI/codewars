// https://www.codewars.com/kata/5f0ed36164f2bc00283aed07/train/javascript

// Passed

function overTheRoad(address, n) {
  const maxHouses = 2 * n;
  const sumHouses = 1 + maxHouses;

  // sumHouses = oddHouse + evenHouse
  return sumHouses - address;
}


const output = overTheRoad(3, 5);
console.log(output);