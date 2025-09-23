// https://www.codewars.com/kata/5bd00c99dbc73908bb00057a/train/javascript

// Passed

function alphaSeq(str) {
  const alphabets = "abcdefghijklmnopqrstuvwxyz";

  str = str.toLowerCase();
  let sequence = str
    .split("")
    .sort()
    .map(
      (alphabet) =>
        alphabet.toUpperCase() + alphabet.repeat(alphabets.indexOf(alphabet))
    )
    .join(",");
  return sequence;
}

const output = alphaSeq("ZpglnRxqenU");
console.log(output);