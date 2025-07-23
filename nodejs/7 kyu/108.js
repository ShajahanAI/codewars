// https://www.codewars.com/kata/59ad7d2e07157af687000070/train/javascript

// Passed

function sentencify(words) {
  words[0] = words[0][0].toUpperCase() + words[0].slice(1);
  let sentence = words.join(" ");
  sentence += ".";
  return sentence;
}

const output = sentencify(["let", "there", "be", "light"]);
console.log(output);