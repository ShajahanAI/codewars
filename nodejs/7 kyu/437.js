// https://www.codewars.com/kata/59c0b9d4cb7fb4dd41000962/train/javascript

// Passed

function bulbMaze(maze) {
  let offStatusSymbol = "x";
  for (let idx = 0; idx < maze.length; idx++) {
    let currentRoomSymbol = maze[idx];
    if (currentRoomSymbol !== " ") {
      if (currentRoomSymbol !== offStatusSymbol) {
        return false;
      }
    }

    offStatusSymbol = offStatusSymbol === "x" ? "o" : "x";
  }

  return true;
}

const output = bulbMaze("xo oxox");
console.log(output);