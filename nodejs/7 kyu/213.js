// https://www.codewars.com/kata/5894017082b9fb62c50000df/train/javascript

// Passed

function areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) {
  let yourStrongestArm = Math.max(yourLeft, yourRight);
  let friendsStrongestArm = Math.max(friendsLeft, friendsRight);
  let isEquallyStrong =
    yourStrongestArm === friendsStrongestArm &&
    yourLeft + yourRight === friendsLeft + friendsRight;
  return isEquallyStrong;
}

const output = areEquallyStrong(10, 5, 11, 4);
console.log(output);