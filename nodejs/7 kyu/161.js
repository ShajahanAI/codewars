// https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/javascript

// Passed

function openOrSenior(data) {
  let memberPositions = data.map((memberData) =>
    memberData[0] >= 55 && memberData[1] > 7 ? "Senior" : "Open"
  );
  return memberPositions;
}

const output = openOrSenior([
  [45, 12],
  [55, 21],
  [19, -2],
  [104, 20],
]);
console.log(output);