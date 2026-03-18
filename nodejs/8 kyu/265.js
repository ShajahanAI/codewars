// https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/javascript

// Passed

function hero(bullets, dragons) {
  let whetherHeroSurvives = bullets >= dragons * 2;
  return whetherHeroSurvives;
}

const output = hero(10, 5);
console.log(output);