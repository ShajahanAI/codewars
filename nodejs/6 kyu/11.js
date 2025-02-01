// https://www.codewars.com/kata/5966847f4025872c7d00015b/train/javascript

// Passed

function averageString(str) {
    console.log(str);
    const DIGIT_MAP = {zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, 
                       six: 6, seven: 7, eight: 8, nine: 9};
    
    const INVERT_DIGIT_MAP = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
        6: "six", 7: "seven", 8: "eight", 9: "nine"};
    
    let sum = 0;
    for (const digit_in_words of str.split(' ')) {
        if (digit_in_words in DIGIT_MAP) {
            sum += DIGIT_MAP[digit_in_words];
        }
        else {
            return "n/a"
        }
    }

    let avg = Math.floor(sum / str.split(' ').length);
    return INVERT_DIGIT_MAP[avg] ;
  }

let output = averageString("one two three");
console.log(output);