// https://www.codewars.com/kata/55c6126177c9441a570000cc/train/javascript

// Passed

function orderWeight(strng) {
  const weightSumMap = new Object();
  strng.split(" ").forEach((weight) => {
    const weightDigits = weight.split("").map(Number);
    const sumWeightDigits = weightDigits.reduce((prev, curr) => prev + curr, 0);

    if (!(sumWeightDigits in weightSumMap))
      weightSumMap[sumWeightDigits] = new Array();

    weightSumMap[sumWeightDigits].push(weight);
  });

  const orderedWeights = new Array();
  Object.keys(weightSumMap)
    .sort((a, b) => a - b)
    .forEach((weightSum) => {
      const weigthsArray = weightSumMap[weightSum].sort(); // Sorting alphabetically
      orderedWeights.push(...weigthsArray);
    });

  return orderedWeights.join(" ");
}

const output = orderWeight("103 123 4444 99 2000");
console.log(output);
