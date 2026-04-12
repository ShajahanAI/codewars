// https://www.codewars.com/kata/57ed30dde7728215300005fa/train/javascript

// Passed

function bump(x) {
  let bumpsCount = 0;
  let result = "Woohoo!";
  for (const roadPart of x) {
    if (roadPart === "n") {
      bumpsCount++;
    }

    if (bumpsCount > 15) {
      result = "Car Dead";
      break;
    }
  }
  return result;
}

const output = bump("__nn_nnnn__n_n___n____nn__nnn");
console.log(output);