// https://www.codewars.com/kata/581f4ac139dc423f04000b99/train/javascript

// Passed

function transposeTwoStrings (array) {
    max_length = array.reduce((prev, curr) => prev.length > curr.length ? prev : curr ).length;
    array[0] = array[0].padEnd(max_length, " ");
    array[1] = array[1].padEnd(max_length, " ");

    let out = "";
    for (let idx = 0; idx < array[0].length; idx++) {
        out += idx !== array[0].length - 1 ? `${array[0][idx]} ${array[1][idx]}\n` : `${array[0][idx]} ${array[1][idx]}`;
    }

    return out;
}

const output = transposeTwoStrings(["Hello", "World"]);
console.log(output);