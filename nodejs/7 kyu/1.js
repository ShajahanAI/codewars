// https://www.codewars.com/kata/57b4dd38d2a31c75f7000299/train/javascript

// Failed

function smallWordHelper(sentence){
    let words = sentence.split(' ');
    let newWords = words.map(word => {
        if (word.length <= 3) {
            return word.toUpperCase();
        }
        else if (word.length >= 4) {
            let vowels = ['a', 'e', 'i', 'o', 'u'];
            for (const vowel of vowels){
                word = word.replace(vowel, '');
                word = word.replace(vowel.toUpperCase(), ''); 
            } 
        }
        return word
    });
    let newSentence = newWords.join(' ');
    return newSentence;
}

let output = smallWordHelper("nvear");
console.log(output);
