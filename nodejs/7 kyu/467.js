// https://www.codewars.com/kata/573c91c5eaffa3bd350000b0/train/javascript

// Passed

function gematria(str) {
  let characterToValueMap = new Object();
  let charactersToValueString =
    "a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, k=10, l=20, m=30, n=40, o=50, p=60, q=70, r=80, s=90, t=100, u=200, x=300, y=400, z=500, j=600, v=700, w=900";
  for (const characterToValueString of charactersToValueString.split(",")) {
    let [char, val] = characterToValueString.split("=");
    val = Number(val);
    characterToValueMap[char.trim()] = val;
  }

  let result = str
    .toLowerCase()
    .split("")
    .map((char) =>
      char in characterToValueMap ? characterToValueMap[char] : 0,
    )
    .reduce((prev, curr) => prev + curr, 0);
  return result;
}

const output = gematria("Coding is fun");
console.log(output);