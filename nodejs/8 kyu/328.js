// https://www.codewars.com/kata/5875b200d520904a04000003/train/javascript

// Passed

function enough(cap, on, wait) {
  let totalPeople = on + wait;
  let result;
  if (totalPeople <= cap) {
    result = 0;
  } else {
    result = totalPeople - cap;
  }
  return result;
}

const output = enough(100, 60, 50);
console.log(output);