// https://www.codewars.com/kata/5710a50d336aed828100055a/train/javascript

// Passed

function sc(screws) {
  let totalTime = 0;
  let currentScrew = "";
  for (const screw of screws) {
    if (currentScrew && currentScrew !== screw) {
      totalTime += 5; // Time to switch screwdriver
    }

    totalTime += 2; // To remove and move to next screw
    currentScrew = screw;
  }

  totalTime -= 1; // Because we had reached the end but still considered moving to the next screw
  return totalTime;
}

const output = sc("-+-+-+");
console.log(output);
