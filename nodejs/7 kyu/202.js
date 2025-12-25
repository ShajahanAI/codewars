// https://www.codewars.com/kata/53573877d5493b4d6e00050c/train/javascript

// Passed

function capital(capitals) {
  let capitalStrings = capitals.map((capitalObj) => {
    let capitalKey = "capital";
    let countryStateKey = "country";
    if ("state" in capitalObj) {
      countryStateKey = "state";
    }

    let capitalString = `The capital of ${capitalObj[countryStateKey]} is ${capitalObj[capitalKey]}`;
    return capitalString;
  });
  return capitalStrings;
}

const output = capital([
  { state: "Maine", capital: "Augusta" },
  { country: "Spain", capital: "Madrid" },
]);
console.log(output);