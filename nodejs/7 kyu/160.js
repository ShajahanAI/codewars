// https://www.codewars.com/kata/58acfe4ae0201e1708000075/train/javascript

// Passed

function inviteMoreWomen(L) {
  let arraySum = L.reduce((prev, curr) => prev + curr, 0);
  if (arraySum > 0) {
    return true;
  }

  return false;
}

const output = inviteMoreWomen([1, -1, 1]);
console.log(output);