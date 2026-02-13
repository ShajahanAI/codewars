// https://www.codewars.com/kata/557dd2a061f099504a000088/train/javascript

// Passed

function listToArray(list) {
  let arr = [];
  let node = list;
  while (node !== null) {
    let val = node.value;
    arr.push(val);
    node = node.next;
  }

  return arr;
}

const output = listToArray({
  value: true,
  next: {
    value: false,
    next: { value: "true", next: { value: "false", next: null } },
  },
});
console.log(output);