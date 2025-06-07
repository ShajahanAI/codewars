// https://www.codewars.com/kata/6584b7cac29ca91dd9124009/train/javascript

// Passed

function convertLojban(lojban) {
  const lojbanToNumber = {
    pa: 1,
    re: 2,
    ci: 3,
    vo: 4,
    mu: 5,
    xa: 6,
    ze: 7,
    bi: 8,
    so: 9,
    no: 0,
  };

  let lojbanDigit = "";
  let lojbanNumber = "";
  for (let idx = 0; idx < lojban.length; idx++) {
    lojbanDigit += lojban[idx];
    if (lojbanDigit in lojbanToNumber) {
      lojbanNumber += String(lojbanToNumber[lojbanDigit]);
      lojbanDigit = "";
    }
  }
  lojbanNumber = Number(lojbanNumber);
  return lojbanNumber;
}

const output = convertLojban("renonore");
console.log(output);