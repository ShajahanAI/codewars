// https://www.codewars.com/kata/5925acf31a9825d616000e74/train/javascript

// Passed

function killcount(counselors, jason) {
  const victims = counselors
    .map((conselor_intelligence) =>
      conselor_intelligence[1] < jason ? conselor_intelligence[0] : null
    )
    .filter((victim) => victim !== null);
  return victims;
}

const output = killcount([["Chad", 2], ["Tommy", 9]], 7);
console.log(output)