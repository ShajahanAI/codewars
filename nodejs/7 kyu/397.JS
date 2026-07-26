// https://www.codewars.com/kata/592a6ad46d6c5a62b600003f/train/javascript

// Passed

const KEY = "GA-DE-RY-PO-LU-KI";
const SUBSTITUTE_MAP = new Object();

for (const group of KEY.split("-")) {
  let [key, val] = Array.from(group);
  SUBSTITUTE_MAP[key] = val;
  SUBSTITUTE_MAP[val] = key;
}

function transform(str) {
  let result = "";
  for (const char of str) {
    let val = char;
    if (char.toUpperCase() in SUBSTITUTE_MAP) {
      val = SUBSTITUTE_MAP[char.toUpperCase()];
    }
    if (char.toLowerCase() === char) {
      val = val.toLowerCase();
    }

    result += val;
  }

  return result;
}

function encode(str) {
  let result = transform(str);
  return result;
}

function decode(str) {
  let result = transform(str);
  return result;
}

const output1 = encode("Ala has a cat");
const output2 = decode("Gug hgs g cgt");
console.log(output1, output2);