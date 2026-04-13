// https://www.codewars.com/kata/5b662d286d0db722bd000013/train/javascript

// Passed

function redacted(doc1, doc2) {
  let isLineRedacted = (l1, l2) => {
    if (l1.length != l2.length) {
      return false;
    }

    for (let idx = 0; idx < l1.length; idx++) {
      if (l1[idx] === "X") {
        continue;
      }

      if (l1[idx] !== l2[idx]) {
        return false;
      }
    }

    return true;
  };

  let doc1Lines = doc1.split("\n");
  let doc2Lines = doc2.split("\n");

  if (doc1Lines.length !== doc2Lines.length) {
    return false;
  }

  let isRedactedProperly = true;
  for (let idx = 0; idx < doc1Lines.length; idx++) {
    let [l1, l2] = [doc1Lines[idx], doc2Lines[idx]];
    isRedactedProperly = isLineRedacted(l1, l2);

    if (!isRedactedProperly) {
      break;
    }
  }

  return isRedactedProperly;
}

const output = redacted(
  "The name of the mole is Professor XXXXX",
  "The name of the mole is Professor Dinglemouse",
);
console.log(output);