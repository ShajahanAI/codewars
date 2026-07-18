
// https://www.codewars.com/kata/57bec3bc5640aa5f3f00003e/train/javascript

// Passed

function generateCurrencyMatrix(currency) {
  let currenciesInDescendingStrength = [
    "EUR",
    "GBP",
    "AUD",
    "NZD",
    "USD",
    "CAD",
    "CHF",
    "JPY",
  ];

  let isStrongerCurrency = false;
  let result = [];
  for (currencyToCompare of currenciesInDescendingStrength) {
    if (currency === currencyToCompare) {
      isStrongerCurrency = true;
      continue;
    }

    let currencyPair = isStrongerCurrency
      ? `${currency}${currencyToCompare}`
      : `${currencyToCompare}${currency}`;
    result.push(currencyPair);
  }

  return result;
}

const output = generateCurrencyMatrix("GBP");
console.log(output);