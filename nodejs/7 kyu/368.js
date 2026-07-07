// https://www.codewars.com/kata/588817db5fb13af14a000020/train/javascript

// Passed

function timedReading(maxLength, text) {
  let cleanseWord = (word) => {
    let letters = word
      .split("")
      .filter((char) => RegExp("[a-z]").test(char.toLowerCase()));
    let cleansedWord = letters.join("");
    return cleansedWord;
  };
  let words = text.split(" ").map((word) => cleanseWord(word));
  let wordsThatWereRead = words.filter(
    (word) => word.length !== 0 && word.length <= maxLength,
  );
  let result = wordsThatWereRead.length;
  return result;
}

const output = timedReading(4, "The Fox asked the stork, 'How is the soup?'");
console.log(output);