// https://www.codewars.com/kata/58941fec8afa3618c9000184/train/javascript

// Passed

function growingPlant(upSpeed, downSpeed, desiredHeight) {
  let plantHeight = 0;
  let days = 0;
  while (plantHeight < desiredHeight) {
    days += 0.5;
    if ((days / 0.5) % 2 === 1) {
      plantHeight += upSpeed;
    } else {
      plantHeight -= downSpeed;
    }
  }

  days = Math.ceil(days);
  return days;
}

const output = growingPlant(100, 10, 910);
console.log(output);