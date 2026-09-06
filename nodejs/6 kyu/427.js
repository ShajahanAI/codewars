// https://www.codewars.com/kata/55b3425df71c1201a800009c/train/javascript

// Passed

function stat(strg) {
  let hhmmssToSeconds = (hhmmss) => {
    let [hh, mm, ss] = hhmmss.split("|").map((numStr) => Number(numStr));
    let result = hh * 3600 + mm * 60 + ss;
    return result;
  };

  let secondsToHhmmss = (seconds) => {
    let formatNumber = (num) =>
      String(num).length == 1 ? "0" + String(num) : String(num);
    let hh = Math.floor(seconds / 3600);
    let mm = Math.floor((seconds - hh * 3600) / 60);
    let ss = seconds - (hh * 3600 + mm * 60);
    [hh, mm, ss] = [hh, mm, ss].map((num) => formatNumber(Math.floor(num)));
    let result = `${hh}|${mm}|${ss}`;
    return result;
  };

  let result = String();
  if (strg.trim().length !== 0) {
    let secondsArr = strg
      .split(",")
      .map((hhmmss) => hhmmssToSeconds(hhmmss))
      .sort((a, b) => a - b);

    let range = secondsArr[secondsArr.length - 1] - secondsArr[0];

    let getAverage = (arr) =>
      arr.reduce((prev, curr) => prev + curr, 0) / arr.length;
    let average = getAverage(secondsArr);

    let midpoint = Math.floor(secondsArr.length / 2);
    let median =
      secondsArr.length % 2 === 1
        ? secondsArr[midpoint]
        : getAverage(secondsArr.slice(midpoint - 1, midpoint + 1));

    result = `Range: ${secondsToHhmmss(range)} Average: ${secondsToHhmmss(average)} Median: ${secondsToHhmmss(median)}`;
  }

  return result;
}

const output = stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17");
console.log(output);