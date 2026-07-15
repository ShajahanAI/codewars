
// https://www.codewars.com/kata/5acc79efc6fde7838a0000a0/train/javascript

// Passed

class Node {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

function search(n, root) {
  if (root === null) {
    return false;
  } else if (root.value === n) {
    return true;
  }

  return search(n, root.left) || search(n, root.right);
}

const output = search(555, new Node(666, new Node(555), new Node(444)));
console.log(output);