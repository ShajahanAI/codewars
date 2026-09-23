// https://www.codewars.com/kata/57d1f36705c186d018000813/train/javascript

// Passed

function gordon(a) {
  let vowels = new Set("AEIOU");
  let wordToGordonWord = (word) => {
    let gordonWord = "";
    for (const char of word.toUpperCase()) {
      gordonWord += char === "A" ? "@" : vowels.has(char) ? "*" : char;
    }

    gordonWord += "!!!!";
    return gordonWord;
  };
  let words = a.split(" ").map(wordToGordonWord);
  let result = words.join(" ");
  return result;
}

const output = gordon("i am a chef");
console.log(output);