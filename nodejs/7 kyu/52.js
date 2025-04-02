// https://www.codewars.com/kata/5838a66eaed8c259df000003/train/javascript

// Passed

function convertPalindromes(numbers) {
  let isPalindrome = (text) => text === text.split("").reverse().join("");
  return numbers.map((num) => Number(isPalindrome(String(num))));
}
const output = convertPalindromes([202, 133]);
console.log(output);
