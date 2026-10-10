// https://www.codewars.com/kata/559e5b717dd758a3eb00005a/train/javascript

// Passed

function dropCap(n) {
  let titleCase = (word) => word[0].toUpperCase() + word.slice(1).toLowerCase();
  let words = n.split(" ");
  let modifiedWords = words.map((word) =>
    word.length > 2 ? titleCase(word) : word,
  );
  let result = modifiedWords.join(" ");
  return result;
}

const output = dropCap("more  than    one space between words");
console.log(output);