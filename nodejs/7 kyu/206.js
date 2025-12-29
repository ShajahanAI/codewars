// https://www.codewars.com/kata/5a8d1c82373c2e099d0000ac/train/javascript

// Passed

function solve(st, a, b) {
  let result =
    st.slice(0, a) +
    st
      .slice(a, b + 1)
      .split("")
      .reverse()
      .join("") +
    st.slice(b + 1);
  return result;
}

const output = solve("codewars", 1, 5);
console.log(output);