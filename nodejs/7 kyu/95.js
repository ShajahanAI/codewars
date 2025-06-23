// https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/javascript

// Passed

function dnaStrand(dna) {
  const dnaMap = {
    A: "T",
    C: "G",
    T: "A",
    G: "C",
  };

  let complementDna = dna
    .split("")
    .map((symbol) => dnaMap[symbol])
    .join("");
  return complementDna;
}

const output = dnaStrand("ATTGC");
console.log(output);