// https://www.codewars.com/kata/64fc03a318692c1333ebc04c/train/javascript

// Passed

function bestFriend(txt, a, b) {
  txt = txt.toLowerCase();
  a = a.toLowerCase();
  b = b.toLowerCase();
  let result = true;
  for (let idx = 0; idx < txt.length; idx++) {
    if (txt[idx] === a) {
      if (idx === txt.length - 1 || txt[idx + 1] !== b) {
        result = false;
        break;
      }
    }
  }

  return result;
}

const output = bestFriend("he headed to the store", "h", "e");
console.log(output);