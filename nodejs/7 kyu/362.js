// https://www.codewars.com/kata/58b6c403a38abaaf6c00006b/train/javascript

// Passed

function sameEncryption(s1, s2) {
  let encryptString = (stringToEncrypt) => {
    let middleTerm = String(
      String(stringToEncrypt.slice(1, stringToEncrypt.length - 1).length),
    );
    while (middleTerm.length > 1) {
      middleTerm = middleTerm
        .split("")
        .map((digit) => Number(digit))
        .reduce((prev, curr) => prev + curr, 0);
      middleTerm = String(middleTerm);
    }
    let encryptedString =
      stringToEncrypt[0] +
      middleTerm +
      stringToEncrypt[stringToEncrypt.length - 1];
    return encryptedString;
  };

  let result = encryptString(s1) === encryptString(s2);
  return result;
}

const output = sameEncryption("fKhjuytrdfcdc", "flJc");
console.log(output);