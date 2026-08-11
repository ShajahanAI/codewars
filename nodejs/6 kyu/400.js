// https://www.codewars.com/kata/53046ceefe87e4905e00072a/train/javascript

// Passed

function palindrome(string) {
  let filteredCharacters = Array.from(string)
    .map((char) => char.toLowerCase())
    .filter((char) => {
      let charCode = char.charCodeAt();
      return (
        (charCode >= 97 && charCode <= 122) ||
        (charCode >= 49 && charCode <= 57)
      );
    });

  let result = filteredCharacters.length
    ? [...filteredCharacters].join("") === filteredCharacters.reverse().join("")
    : true;
  return result;
}

const output = palindrome("A man, a plan, a canal - Panama");
console.log(output);