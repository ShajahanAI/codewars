// https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/train/javascript

// Passed

function evaporator(content, evapPerDay, threshold) {
  let currentPercent = 100;
  let day = 1;
  while (((100 - evapPerDay) / 100) * currentPercent > threshold) {
    day++;
    currentPercent = ((100 - evapPerDay) / 100) * currentPercent;
  }

  return day;
}

const output = evaporator(100, 5, 5);
console.log(output);