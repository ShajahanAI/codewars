// https://www.codewars.com/kata/57eae20f5500ad98e50002c5/

// Passed

function noSpace(x){
    return x.replaceAll(" ", String());
  }

let output = noSpace("a sentence       with too           many whitespaces");
console.log(output);