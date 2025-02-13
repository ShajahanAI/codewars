function boredom(staff) {
  const departmentBoredomMap = {
    accounts: 1,
    finance: 2,
    canteen: 10,
    regulation: 3,
    trading: 6,
    change: 6,
    IS: 8,
    retail: 5,
    cleaning: 4,
    "pissing about": 25,
  };

  const boredomScore = Object.values(staff)
    .map((department) => departmentBoredomMap[department])
    .reduce((prev, curr) => prev + curr, 0);

  if (boredomScore >= 100) {
    return "party time!!";
  } else {
    return boredomScore <= 80 ? "kill me now" : "i can handle this";
  }
}

const output = boredom({
  tim: "change",
  jim: "accounts",
  randy: "canteen",
  sandy: "change",
  andy: "change",
  katie: "IS",
  laura: "change",
  saajid: "IS",
  alex: "trading",
  john: "accounts",
  mr: "finance",
});

console.log(output);