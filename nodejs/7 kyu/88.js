// https://www.codewars.com/kata/541da001259d9ca85d000688/train/javascript

// Passed

function seqlist(first, c, l) {
  let sequence = [first];
  for (let termNumber = 1; termNumber < l; termNumber++) {
    let term = first + termNumber * c;
    sequence.push(term);
  }

  return sequence;
}

const output = seqlist(0, -5, 8);
console.log(output);