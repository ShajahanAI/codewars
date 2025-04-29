// https://www.codewars.com/kata/5356ad2cbb858025d800111d/train/javascript

// Passed

function capMe(names) {
  const result = names.map((name) =>
    name[0].toUpperCase().concat(name.slice(1).toLowerCase())
  );
  return result;
}

const output = capMe(["RALPH", "GEORGIA", "CHRISTINA"]);
console.log(output);
