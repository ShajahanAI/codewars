// https://www.codewars.com/kata/55eca815d0d20962e1000106/

// Passed

function generateRange(min, max, step){
    const rangeArray = [];
    for (let num = min; num <= max; num+=step) {
        rangeArray.push(num);
    }
    return rangeArray
}

const output = generateRange(2, 10, 2);
console.log(output);