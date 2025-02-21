// https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c/train/javascript

// Passed

function switcher(x){
    const alphabets = 'abcdefghijklmnopqrstuvwxyz'.split('').reverse();
    const charactersMap = {
        27: '!',
        28: '?',
        29: ' ',
    };
    alphabets.forEach((letter, index) => {
        charactersMap[index + 1] = letter;
    })
    
    // We have the complete characterMap and can form the word / sentence.

    return x.map(value => charactersMap[Number(value)]).join('');
}

const output = switcher(['24', '12', '23', '22', '4', '26', '9', '8']);
console.log(output);