// https://www.codewars.com/kata/5b190aa7803388ec97000054/train/javascript

// Passed

function tram(stops, descending, onboarding) {
  let totalPassengersAtAnyPoint = [0];
  for (let idx = 0; idx < stops; idx++) {
    let currentTotalPassengers =
      totalPassengersAtAnyPoint[totalPassengersAtAnyPoint.length - 1];
    currentTotalPassengers -= descending[idx];
    currentTotalPassengers += onboarding[idx];
    totalPassengersAtAnyPoint.push(currentTotalPassengers);
  }

  let minimumRequiredCapacity = Math.max(...totalPassengersAtAnyPoint);
  return minimumRequiredCapacity;
}

const output = tram(4, [0, 2, 4, 4], [3, 5, 2, 0]);
console.log(output);