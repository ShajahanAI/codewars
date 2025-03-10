// https://www.codewars.com/kata/55d410c492e6ed767000004f/train/javascript

// Passed

function vowel2index(str) {
  const vowels = ["a", "e", "i", "o", "u"];
  return str
    .split("")
    .map((char, idx) =>
      vowels.includes(char.toLowerCase()) ? String(idx + 1) : char
    )
    .join("");
}

const output = vowel2index("hello");
console.log(output);
