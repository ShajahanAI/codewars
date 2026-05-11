// https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/javascript

// Passed

function removeUrlAnchor(url) {
  let result = url.split("#")[0];
  return result;
}

const output = removeUrlAnchor("www.codewars.com/katas/?page=1#about");
console.log(output);