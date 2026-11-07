// https://www.codewars.com/kata/5e2c7639b5d728001489d910/train/javascript

// Passed

function getProductId(url) {
  let urlSplitByP = url.split("-p-");
  let productId = urlSplitByP[urlSplitByP.length - 1].split("-")[0];
  return productId;
}

const output = getProductId(
  "http://www.exampleshop.com/fancy-coffee-cup-p-90764-12052019.html",
);
console.log(output);