// https://www.codewars.com/kata/5b5604e26dc79e6832000101/train/javascript

// Passed

function invertHash(hash) {
  const keys = Object.keys(hash);
  let invertedHash = new Object();
  keys.forEach((key) => {
    invertedHash[hash[key]] = key;
  });

  return invertedHash;
}

const output = invertHash({ a: "1", b: "2", c: "3" });
console.log(output);