// https://www.codewars.com/kata/58c2158ec7df54a39d00015c/train/javascript

// Passed

function momentOfTimeInSpace(moment) {
  let timeCharacters = new Set([..."123456789"]);
  let [time, space] = [0, 0];
  for (const char of moment) {
    if (timeCharacters.has(char)) {
      time += Number(char);
    } else {
      space++;
    }
  }

  let [past, present, future] = [false, false, false];
  if (time > space) {
    future = true;
  } else if (time < space) {
    past = true;
  } else {
    present = true;
  }

  let result = [past, present, future];
  return result;
}

const output = momentOfTimeInSpace("12:02 pm");
console.log(output);