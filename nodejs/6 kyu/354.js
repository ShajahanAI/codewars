// https://www.codewars.com/kata/52dffa05467ee54b93000712/train/javascript

// Passed

function sort(sentence) {
  let removePunctuation = (word) => {
    let characters = word.split("");
    let modifiedWord = characters
      .filter((char) => RegExp("[A-Za-z]").test(char))
      .join("");
    return modifiedWord;
  };
  let wordsWithoutPunctuation = sentence
    .split(" ")
    .map((word) => removePunctuation(word));
  let [
    wordsBeginningWithLowercasedCharacter,
    wordsBeginningWithUppercasedCharacter,
  ] = [[], []];
  for (const word of wordsWithoutPunctuation) {
    if (word[0].toLowerCase() === word[0]) {
      wordsBeginningWithLowercasedCharacter.push(word);
    } else {
      wordsBeginningWithUppercasedCharacter.push(word);
    }
  }

  let getSortedSentenceFromWords = (words, sortDescending) => {
    let sortedWords = sortDescending ? words.sort().reverse() : words.sort();
    let sortedSentence = sortedWords.join(" ");
    return sortedSentence;
  };

  let result = (
    getSortedSentenceFromWords(wordsBeginningWithLowercasedCharacter, false) +
    " " +
    getSortedSentenceFromWords(wordsBeginningWithUppercasedCharacter, true)
  ).trim();
  return result;
}

const output = sort(
  "I, habitan of the Alleghanies, treating of him as he is in himself in his own rights",
);
console.log(output);