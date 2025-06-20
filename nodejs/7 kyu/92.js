// https://www.codewars.com/kata/55b1fd84a24ad00b32000075/train/javascript

// Passed

var AmIAfraid = function (day, num) {
  const dayNumberMap = {
    Monday: (num) => num === 12,
    Tuesday: (num) => num > 95,
    Wednesday: (num) => num === 34,
    Thursday: (num) => num === 0,
    Friday: (num) => num % 2 === 0,
    Saturday: (num) => num === 56,
    Sunday: (num) => num === 666 || num === -666,
  };

  const isAfraid = dayNumberMap[day](num);
  return isAfraid;
};

const output = AmIAfraid("Tuesday", 965);
console.log(output);