// https://www.codewars.com/kata/5808c8eff0ed4210de000008/train/javascript

// Passed

function part(x) {
  let alanTerms = [
    "partridge",
    "peartree",
    "chat",
    "dan",
    "toblerone",
    "lynn",
    "alphapapa",
    "nomad",
  ];
  let validTerms = x.filter((term) => alanTerms.includes(term.toLowerCase()));
  let result =
    validTerms.length === 0
      ? "Lynn, I've pierced my foot on a spike!!"
      : "Mine's a Pint" + "!".repeat(validTerms.length);
  return result;
}

const output = part([
  "Grouse",
  "Partridge",
  "Pheasant",
  "Goose",
  "Starling",
  "Robin",
  "Thrush",
  "Emu",
  "PearTree",
  "Chat",
  "Dan",
  "Square",
  "Toblerone",
  "Lynn",
  "AlphaPapa",
  "BMW",
  "Graham",
  "Tool",
  "Nomad",
  "Finger",
  "Hamster",
]);
console.log(output);