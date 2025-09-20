// https://www.codewars.com/kata/58bf9bd943fadb2a980000a7/train/javascript

// Passed

function whoIsPaying(name) {
  let result = [name];
  if (name.length > 2) {
    result.push(name.slice(0, 2));
  }

  return result;
}

const output = whoIsPaying("Melania");
console.log(output);