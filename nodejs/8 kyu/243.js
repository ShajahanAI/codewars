// https://www.codewars.com/kata/57ab2d6072292dbf7c000039/train/javascript

// Passed

function correctPolishLetters(string) {
  let polishToEnglishMap = {
    ą: "a",
    ć: "c",
    ę: "e",
    ł: "l",
    ń: "n",
    ó: "o",
    ś: "s",
    ź: "z",
    ż: "z",
  };

  let result = "";
  for (const letter of string) {
    if (letter in polishToEnglishMap) {
      result += polishToEnglishMap[letter];
    } else {
      result += letter;
    }
  }

  return result;
}

const output = correctPolishLetters("Jędrzej Błądziński");
console.log(output);