// https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/javascript

// Passed

function replace(s) {
  let vowels = "aeiou";
  for (const vowel of vowels) {
    s = s.replaceAll(vowel, "!");
    s = s.replaceAll(vowel.toUpperCase(), "!");
  }

  return s;
}

const output = replace("Hi");
console.log(output);
