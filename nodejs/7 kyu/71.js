// https://www.codewars.com/kata/5a262cfb8f27f217f700000b/train/javascript

// Passed

function solve(a, b) {
  const uniqueA = a.split("").filter((letter) => !b.includes(letter));
  const uniqueB = b.split("").filter((letter) => !a.includes(letter));
  const uniqueCharacters = uniqueA.join("") + uniqueB.join("");
  return uniqueCharacters;
}

const output = solve("xyab", "xzca");
console.log(output);