// https://www.codewars.com/kata/5b049d57de4c7f6a6c0001d7/train/javascript

// Passed

function apparently(string) {
  let words = string.split(" ");
  let apparentlyWords = [];

  for (let idx = 0; idx < words.length; idx++) {
    apparentlyWords.push(words[idx]);
    if (
      ["and", "but"].includes(words[idx].toLowerCase()) &&
      (idx === words.length - 1 ||
        words[idx + 1].toLowerCase() !== "apparently")
    ) {
      apparentlyWords.push("apparently");
    }
  }

  let apparentlySentence = apparentlyWords.join(" ");
  return apparentlySentence;
}

const output = apparently(
  "It was great and I have never been on live television before but sometimes I dont watch this.",
);
console.log(output);