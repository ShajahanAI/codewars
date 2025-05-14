// https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/javascript

// Passed

function wave(str) {
  const mexicanWave = str
    .split("")
    .map((char, idx) => {
      if (char === " ") return null;
      let mexicanWord =
        str.slice(0, idx) + str[idx].toUpperCase() + str.slice(idx + 1);
      return mexicanWord;
    })
    .filter((word) => word !== null);

  return mexicanWave;
}

const output = wave("hello");
console.log(output);