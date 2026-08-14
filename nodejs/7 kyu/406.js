// https://www.codewars.com/kata/57d4e99bec16701a67000033/train/javascript

// Passed

function heavyMetalUmlauts(boringText) {
  let letterToReplacementMap = {
    A: "Ä",
    E: "Ë",
    I: "Ï",
    O: "Ö",
    U: "Ü",
    Y: "Ÿ",
    a: "ä",
    e: "ë",
    i: "ï",
    o: "ö",
    u: "ü",
    y: "ÿ",
  };

  let result = "";
  for (const char of boringText) {
    let replacement = letterToReplacementMap[char]
      ? letterToReplacementMap[char]
      : char;
    result += replacement;
  }

  return result;
}

const output = heavyMetalUmlauts("Announcing the Macbook Air Guitar");
console.log(output);