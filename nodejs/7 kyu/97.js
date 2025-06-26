// https://www.codewars.com/kata/552ab0a4db0236ff1a00017a/train/javascript

// Passed

function sillycase(silly) {
  const midpoint = Math.ceil(silly.length / 2);
  let firstHalf = silly.slice(0, midpoint).toLowerCase();
  let secondHalf = silly.slice(midpoint).toUpperCase();
  const result = firstHalf + secondHalf;
  return result;
}

const output = sillycase("codewars");
console.log(output);