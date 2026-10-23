// https://www.codewars.com/kata/57efa1a2108d3f73f60000e9/train/javascript

// Passed

function trim(x) {
  for (let layerIdx = 0; layerIdx < x.length; layerIdx++) {
    let layer = x[layerIdx];
    let isLastLayer = layerIdx === x.length - 1;

    for (let hairIdx = 0; hairIdx < layer.length; hairIdx++) {
      layer[hairIdx] = isLastLayer
        ? "..."
        : layer[hairIdx] === "J"
          ? "|"
          : layer[hairIdx];
    }
  }

  return x;
}

const output = trim([
  ["J", "|", "J", "J"],
  ["J", "|", "|", "J"],
  ["...", "|", "J", "|"],
]);
console.log(output);