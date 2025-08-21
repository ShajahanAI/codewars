// https://www.codewars.com/kata/5898b4b71d298e51b600014b/train/javascript

// Passed

function sortTheInnerContent(words) {
  let modifiedWords = words.split(" ").map((word) =>
    word.length <= 2
      ? word
      : word[0] +
        word
          .slice(1, word.length - 1)
          .split("")
          .sort()
          .reverse()
          .join("") +
        word[word.length - 1]
  );
  let modifiedSentence = modifiedWords.join(" ");
  return modifiedSentence;
}

const output = sortTheInnerContent(
  "sort the inner content in descending order"
);
console.log(output);