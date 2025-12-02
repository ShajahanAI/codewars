// https://www.codewars.com/kata/5eb27d81077a7400171c6820/train/javascript

// Passed

function gracefulTipping(bill) {
  let tip = 1.15 * bill;
  if (tip < 10) {
    tip = Math.ceil(tip);
  } else {
    let elegantDivisor = Number(
      "5" + "0".repeat(String(Math.floor(tip)).length - 2)
    );
    tip = elegantDivisor * Math.ceil(tip / elegantDivisor);
  }

  return tip;
}

const output = gracefulTipping(11.99);
console.log(output);