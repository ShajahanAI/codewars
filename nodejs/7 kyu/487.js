// https://www.codewars.com/kata/5a21f943c5e284d4340000cb/train/javascript

// Passed

function debug(s) {
  let indexesToRemove = new Set();

  let tempStr = String();
  for (let idx = 0; idx < s.length; idx++) {
    tempStr += s[idx];
    if (tempStr.endsWith("bug")) {
      if (idx === s.length - 1 || s[idx + 1] !== "s") {
        indexesToRemove.add(idx - 2);
      }
    }
  }

  let idx = 0;
  let result = "";
  while (idx < s.length) {
    if (indexesToRemove.has(idx)) {
      idx += 3;
      continue;
    }

    result += s[idx];
    idx++;
  }

  return result;
}

const output = debug("obugobugobuoobugsoo");
console.log(output);