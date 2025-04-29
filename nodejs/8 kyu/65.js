// https://www.codewars.com/kata/5803956ddb07c5c74200144e/train/javascript

// Passed

function datingRange(age) {
  let minAge, maxAge;
  if (age <= 14) {
    minAge = age - 0.1 * age;
    maxAge = age + 0.1 * age;
  } else {
    minAge = age / 2 + 7;
    maxAge = 2 * (age - 7);
  }

  minAge = Math.floor(minAge);
  maxAge = Math.floor(maxAge);
  const ageRange = `${minAge}-${maxAge}`;

  return ageRange;
}

const output = datingRange(24);
console.log(output);