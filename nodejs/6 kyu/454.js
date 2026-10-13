// https://www.codewars.com/kata/583d704a70407fcb43000443/train/javascript

// Passed

function pathFinding(path) {
  let laundromat1 = [3, 2];
  let laundromat2 = [-4, 3];

  let [x, y] = [0, 0];
  for (const direction of path) {
    if (direction === "n") {
      y++;
    } else if (direction === "s") {
      y--;
    } else if (direction === "e") {
      x++;
    } else if (direction === "w") {
      x--;
    }
  }

  let robotCoords = [x, y];
  let result =
    robotCoords.toString() === laundromat1.toString() ||
    robotCoords.toString() === laundromat2.toString();
  return result;
}

const output = pathFinding(["s", "e", "e", "n", "n", "e", "n"]);
console.log(output);