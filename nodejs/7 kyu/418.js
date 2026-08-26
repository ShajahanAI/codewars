// https://www.codewars.com/kata/57b2e428d24156b312000114/train/javascript

// Passed

function volume(r, h) {
  let cyllinderVolume = Math.PI * r ** 2 * h;
  let result = Math.floor((1 / 3) * cyllinderVolume);
  return result;
}

const output = volume(56, 30);
console.log(output);