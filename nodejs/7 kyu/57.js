// https://www.codewars.com/kata/5b16490986b6d336c900007d/train/javascript

// Passed

function myLanguages(results) {
  const reverseMap = {};
  Object.keys(results).forEach((lang) => {
    let score = results[lang];
    reverseMap[score] = lang;
  });

  const scores = Object.values(results)
    .sort((a, b) => b - a)
    .filter((score) => score >= 60);
  const languages = scores.map((score) => reverseMap[score]);
  return languages;
}

const output = myLanguages({ Java: 10, Ruby: 80, Python: 65 });
console.log(output);
