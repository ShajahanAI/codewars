// https://www.codewars.com/kata/55147ff29cd40b43c600058b/train/javascript

// Passed

function charConcat(string) {
  let result = "";
  for (let index = 0; index < Math.floor(string.length / 2); index++) {
    result += `${string[index]}${string[string.length - (index + 1)]}${
      index + 1
    }`;
  }

  return result;
}

const output = charConcat("abcdef");
console.log(output);
