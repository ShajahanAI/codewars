// https://www.codewars.com/kata/580751a40b5a777a200000a1/train/javascript

// Passed

function vowelOne(s) {
  const vowels = ["a", "e", "i", "o", "u"];
  return s
    .split("")
    .map((char) => (vowels.includes(char.toLowerCase()) ? "1" : "0"))
    .join("");
}

const output = vowelOne('hello world');
console.log(output);