// https://www.codewars.com/kata/59b2963132779166d2001018/train/javascript

// Passed

function arrMultiply(arr){
    return arr.reduce((accumulator, currentValue) => accumulator * Number(currentValue), 1);
}

let output = arrMultiply(['2', '4', '3']);
console.log(output);