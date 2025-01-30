// https://www.codewars.com/kata/56143efa9d32b3aa65000016/train/javascript

// Passed

function sumCircles(...diameters) {
    // Squaring diameters
    diameters.forEach((diameter, index, arr) => arr[index] = Math.pow(diameter, 2));
    let area = (Math.PI/4) * diameters.reduce((prev, curr) => prev + curr, 0);

    return `We have this much circle: ${Math.round(area)}`;
}

let output = sumCircles(1, 2, 3, 4, 5, 6, 7, 8, 9, 10); // expecting 385
console.log(output);