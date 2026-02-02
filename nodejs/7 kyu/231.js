// https://www.codewars.com/kata/57212c55b6fa235edc0002a2/train/javascript

// Passed

function commonGround(s1, s2) {
  let s2Words = s2.split(" ");
  let commonWords = [];
  for (const s2Word of s2Words) {
    if (s1.includes(s2Word)) {
      commonWords.push(s2Word);
    }
  }

  let result = commonWords.length ? commonWords.join(" ") : "death";
  return result;
}

const output = commonGround("eat a burger and drink a coke", "drink a coke");
console.log(output);