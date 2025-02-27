// https://www.codewars.com/kata/52b5247074ea613a09000164/train/javascript

// Passed

function cookingTime(eggs) {
    let eggBatches = eggs % 8 ? Math.floor(eggs/8) + 1 : eggs / 8;
    return 5  * eggBatches;
}

const output = cookingTime(17);
console.log(output);