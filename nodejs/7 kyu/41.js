// https://www.codewars.com/kata/569b5cec755dd3534d00000f/train/javascript

// Passed

function newAvg(arr, newavg) {
  const totalDonationsTillNow = arr.reduce((prev, curr) => prev + curr, 0);
  const possibleTotalDonations = arr.length + 1;
  const donationToBeMade =
    newavg * possibleTotalDonations - totalDonationsTillNow;

  if (donationToBeMade > 0)
    return donationToBeMade % 1 !== 0
      ? Math.ceil(donationToBeMade)
      : donationToBeMade;

  throw new Error("Expected New Average is too low");
}

const output = newAvg([14, 30, 5, 7, 9, 11, 16], 90, 628);
console.log(output);
