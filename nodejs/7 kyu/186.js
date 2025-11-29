// https://www.codewars.com/kata/57f22b0f1b5432ff09001cab/train/javascript

// Passed

function well(x) {
  let allIdeas = [];

  for (const ideas of x) {
    allIdeas = allIdeas.concat(ideas);
  }

  let ideasType = "Fail!";
  let goodIdeas = allIdeas.filter(
    (idea) => typeof idea === "string" && idea.toLowerCase().trim() == "good"
  );
  let numberOfGoodIdeas = goodIdeas.length;
  if (numberOfGoodIdeas > 0 && numberOfGoodIdeas <= 2) {
    ideasType = "Publish!";
  } else if (numberOfGoodIdeas > 2) {
    ideasType = "I smell a series!";
  }

  return ideasType;
}

const output = well([
  ["gOOd", "bad", "BAD", "bad", "bad"],
  ["bad", "bAd", "bad"],
  ["GOOD", "bad", "bad", "bAd"],
]);
console.log(output);