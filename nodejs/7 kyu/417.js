// https://www.codewars.com/kata/55b42574ff091733d900002f/train/javascript

// Passed

function friend(friends) {
  let result = friends.filter((possibleFriend) => possibleFriend.length === 4);
  return result;
}

const output = friend([
  "Jimm",
  "Cari",
  "aret",
  "truehdnviegkwgvke",
  "sixtyiscooooool",
]);
console.log(output);