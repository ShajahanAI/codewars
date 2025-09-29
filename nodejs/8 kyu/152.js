// https://www.codewars.com/kata/570597e258b58f6edc00230d/train/javascript

// Passed

function array(string) {
  let commaSeparatedCharacters = string.split(",");
  if (
    commaSeparatedCharacters.length === 0 ||
    commaSeparatedCharacters.length === 1 ||
    commaSeparatedCharacters.length === 2
  )
    return null;

  let result = commaSeparatedCharacters
    .slice(1, commaSeparatedCharacters.length - 1)
    .join(" ");
  return result;
}

const output = array("1,2,3,4");
console.log(output);