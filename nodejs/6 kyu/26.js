// https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/javascript

// Passed

function toWeirdCase(string) {
  const wordToWeirdCase = (word) => {
    return word
      .split("")
      .map((char, index) =>
        index % 2 !== 0 ? char.toLowerCase() : char.toUpperCase()
      )
      .join("");
  };

  return string
    .split(" ")
    .map((word) => wordToWeirdCase(word))
    .join(" ");
}

const output = toWeirdCase("hello world");
console.log(output);
