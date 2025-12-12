// https://www.codewars.com/kata/571c1e847beb0a8f8900153d/train/javascript

// Passed

function rakeGarden(garden) {
  let modifiedGardenItems = garden
    .split(" ")
    .map((word) => (["rock", "gravel"].includes(word) ? word : "gravel"));
  let modifiedGarden = modifiedGardenItems.join(" ");
  return modifiedGarden;
}

const output = rakeGarden(
  "slug spider rock gravel gravel gravel gravel gravel gravel gravel"
);
console.log(output);