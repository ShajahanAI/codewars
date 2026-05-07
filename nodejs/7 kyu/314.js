// https://www.codewars.com/kata/59e49b2afc3c494d5d00002a/train/javascript

// Passed

function sortVowels(s) {
  const VOWELS = new Set("aeiou");
  let rows = [];

  if (typeof s === "string") {
    let characters = s.split("");
    for (const char of characters) {
      let row = VOWELS.has(char.toLowerCase()) ? "|" + char : char + "|";
      rows.push(row);
    }
  }

  let result = rows.join("\n");
  return result;
}

const output = sortVowels("Rnd Te5T");
console.log(output);