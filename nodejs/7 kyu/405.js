// https://www.codewars.com/kata/5829994cd04efd4373000468/train/javascript

// Passed

function nameFile(fmt, nbr, start) {
  let result = [];
  let isWhole = (numToCheck) => Math.ceil(numToCheck) === numToCheck;
  if (nbr > 0 && isWhole(nbr) && isWhole(start)) {
    for (let indexNum = start; indexNum < start + nbr; indexNum++) {
      let fileName = fmt.replaceAll("<index_no>", String(indexNum));
      result.push(fileName);
    }
  }

  return result;
}

const output = nameFile("IMG <index_no>", 4, 1);
console.log(output);