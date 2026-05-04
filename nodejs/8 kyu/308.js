// https://www.codewars.com/kata/56d49587df52101de70011e4/train/javascript

// Passed

function leo(oscar) {
  let result;
  if (oscar == 88) {
    result = "Leo finally won the oscar! Leo is happy";
  } else if (oscar == 86) {
    result = "Not even for Wolf of wallstreet?!";
  } else if (oscar > 88) {
    result = "Leo got one already!";
  } else {
    result = "When will you give Leo an Oscar?";
  }
  return result;
}

const output = leo(88);
console.log(output);