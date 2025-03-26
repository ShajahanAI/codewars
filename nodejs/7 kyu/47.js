// https://www.codewars.com/kata/59414b46d040b7b8f7000021/train/javascript

// Passed

function tacofy(word) {
  const ingredients = {
    a: "beef",
    e: "beef",
    i: "beef",
    o: "beef",
    u: "beef",
    t: "tomato",
    l: "lettuce",
    c: "cheese",
    g: "guacamole",
    s: "salsa",
  };

  let taco = ["shell"];
  taco = taco.concat(
    word
      .toLowerCase()
      .split("")
      .map((char) => (ingredients[char] ? ingredients[char] : ""))
      .filter((ingredient) => ingredient !== "")
  );
  taco.push("shell");
  return taco;
}

const output = tacofy("ydjkpwqrzto");
console.log(output);