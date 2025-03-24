// https://www.codewars.com/kata/5832db03d5bafb7d96000107/train/javascript

// Passed

function lottery(str) {
  const digitsOnly = str
    .split("")
    .map((char) => (char >= "0" && char <= "9" ? char : ""))
    .filter((char) => char.length);

  // Removing duplicates
  let uniqueDigits = [];
  digitsOnly.forEach((char) => {
    if (!uniqueDigits.includes(char)) {
      uniqueDigits.push(char);
    }
  });

  return uniqueDigits.length ? uniqueDigits.join("") : "One more run!";
}

const output = lottery("a43bfs54ds");
console.log(output);