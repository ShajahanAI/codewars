// https://www.codewars.com/kata/54d472e98776e4eb5b000215/train/javascript

// Passed

function pitchClass(note) {
  let noteToPitchClass = {
    C: 0,
    D: 2,
    E: 4,
    F: 5,
    G: 7,
    A: 9,
    B: 11,
  };
  let functionToApply = (val) => val;
  if (note.includes("#")) {
    functionToApply = (val) => (val + 1 > 11 ? 0 : val + 1);
  } else if (note.includes("b")) {
    functionToApply = (val) => (val - 1 < 0 ? 11 : val - 1);
  }

  note = note.replace("#", "").replace("b", "");
  let result =
    noteToPitchClass[note] !== undefined
      ? functionToApply(noteToPitchClass[note])
      : null;
  return result;
}

const output = pitchClass("D#");
console.log(output);