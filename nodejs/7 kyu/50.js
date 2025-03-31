// https://www.codewars.com/kata/55b95c76e08bd5eef100001e/train/javascript

// Passed

function countArara(n) {
  let numberString = "";
  console.log(n);

  if (n % 2 === 0) {
    numberString += "adak ".repeat(Math.floor(n / 2)).trim();
  } else {
    numberString += "adak ".repeat(Math.floor((n - 1) / 2)).trim();
    numberString += " anane";
    numberString = numberString.trim();
  }

  return numberString;
}

const output = countArara(363);
console.log(output);