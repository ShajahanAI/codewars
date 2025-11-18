// https://www.codewars.com/kata/58a369fa5b3daf464200006c/train/javascript

// Passed

function getPercentage(sent, limit) {
  limit = limit ? limit : 1000;

  if (sent === 0) {
    return "No e-mails sent";
  } else if (sent >= limit) {
    return "Daily limit is reached";
  } else {
    let percent = Math.floor((sent / limit) * 100);
    let result = `${percent}%`;
    return result;
  }
}

const output = getPercentage(256, 500);
console.log(output);