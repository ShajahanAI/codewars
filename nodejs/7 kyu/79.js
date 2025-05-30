// https://www.codewars.com/kata/567d71b93f8a50f461000019/train/javascript

// Passed

const crossover = (chromosome1, chromosome2, index) => {
  let crossover1 = chromosome1.slice(index);
  let crossover2 = chromosome2.slice(index);
  let crossoveredChromosomes = [
    chromosome1.slice(0, index) + crossover2,
    chromosome2.slice(0, index) + crossover1,
  ];
  return crossoveredChromosomes;
};

const output = crossover('111000','000110',3);
console.log(output);