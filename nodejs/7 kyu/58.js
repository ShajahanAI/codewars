// https://www.codewars.com/kata/5747a9bbe2fab9a0c400012f/train/javascript

// Passed

function gcContent(dna) {
  if (!dna) {
    return 0;
  }

  const GC = dna
    .split("")
    .filter((char) => (char === "G") | (char === "C")).length;
  const GC_CONTENT = (GC / dna.length) * 100;
  return GC_CONTENT;
}

const output = gcContent("AAACCCGGGTTT");
console.log(output);