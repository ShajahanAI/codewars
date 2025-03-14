// https://www.codewars.com/kata/585af8f645376cda59000200/train/javascript

// Passed

function formatPoem(poem) {
  return poem
    .split(".")
    .map((sentence) => sentence.trim())
    .join(".\n")
    .trim();
}

const output = formatPoem(
  "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."
);
console.log(output);