// https://www.codewars.com/kata/5a1c28f9c9fc0ef2e900013b/train/javascript

// Passed

function pyramid(n) {
  let layers = [];
  for (let layerNumber = 0; layerNumber < n; layerNumber++) {
    let layer = " ".repeat(n - layerNumber - 1);
    if (layerNumber !== n - 1) {
      layer += "/" + " ".repeat(layerNumber * 2) + "\\";
    } else {
      layer += "/" + "_".repeat(layerNumber * 2) + "\\";
    }
    layers.push(layer);
  }

  let asciiPyramid = layers.join("\n") + "\n";
  return asciiPyramid;
}

const output = pyramid(10);
console.log(output);