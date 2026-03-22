// https://www.codewars.com/kata/56d6b7e43e8186c228000637/train/javascript

// Passed

function colourAssociation(array) {
  let colourToAttributeArr = array.map((item) => {
    let [colour, attribute] = item;
    let colourToAttributeObj = new Object();
    colourToAttributeObj[colour] = attribute;
    return colourToAttributeObj;
  });

  return colourToAttributeArr;
}

const output = colourAssociation([
  ["white", "goodness"],
  ["blue", "tranquility"],
]);
console.log(output);