// https://www.codewars.com/kata/54e9554c92ad5650fe00022b/train/javascript

// Passed

function toCurrency(price) {
  price = String(price);
  let counter = 0;
  let currency = "";
  for (let idx = price.length - 1; idx >= 0; idx--) {
    counter++;
    if (counter === 4) {
      currency = "," + currency;
      counter = 1;
    }

    currency = price[idx] + currency;
  }

  return currency;
}

const output = toCurrency(123456789012);
console.log(output);