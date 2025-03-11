// https://www.codewars.com/kata/58356a94f8358058f30004b5/train/javascript

// Passed

function flyBy(lamps, drone) {
  if (drone.length >= lamps.length) return "o".repeat(lamps.length);
  const onLamps = "o".repeat(drone.length);
  const offLamps = "x".repeat(lamps.length - drone.length);
  return onLamps.concat(offLamps);
}

const output = flyBy("xxxxxx", "====T");
console.log(output);