// https://www.codewars.com/kata/584dc1b7766c2bb158000226/train/javascript

// Passed

function choreAssignment(chores) {
  // sorting the chores
  chores.sort((a, b) => a - b);

  // The maximal workload would be max(chores) + min(chores)
  let workloads = [];
  for (let index = 0; index < chores.length / 2; index++) {
    const workload = chores[index] + chores[chores.length - index - 1];
    workloads.push(workload);
  }

  // sorting workloads
  workloads.sort((a, b) => a - b);

  return workloads;
}

const output = choreAssignment([1, 5, 2, 8, 4, 9, 6, 4, 2, 2, 2, 9]);
console.log(output);
