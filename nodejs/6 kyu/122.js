// https://www.codewars.com/kata/5832514f64a4cecd1c000013/train/javascript

// Passed

function piecesValue(arr, s) {
  const hash = Object.freeze({
    queen: 9,
    rook: 5,
    bishop: 3,
    knight: 3,
    pawn: 1,
    king: 0,
  });

  let pieceColour = s[0];
  let result = arr
    .map((row) =>
      row
        .map((square) =>
          square.startsWith(pieceColour) ? hash[square.split("-")[1]] : 0
        )
        .reduce((prev, curr) => prev + curr, 0)
    )
    .reduce((prev, curr) => prev + curr, 0);
  return result;
}

const output = piecesValue(
  [
    ["b-bishop", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "b-queen", " ", " ", " ", " ", "w-queen"],
    [" ", "b-king", " ", "b-pawn", "w-rook", " ", " ", " "],
    [" ", " ", " ", " ", "w-pawn", " ", " ", " "],
    [" ", " ", " ", " ", " ", "w-bishop", " ", " "],
    ["w-king", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "b-pawn", "b-pawn", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
  ],
  "white"
);
console.log(output);