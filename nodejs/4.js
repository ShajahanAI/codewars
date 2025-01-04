// https://www.codewars.com/kata/58d248c7012397a81800005c/train/javascript

// Passed

function cubeChecker(volume, side){
    return volume <= 0 | side <= 0 ? false : volume === side * side * side;
  };