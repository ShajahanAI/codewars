// https://www.codewars.com/kata/58999425006ee3f97c00011f/train/javascript

// Passed

function passed(list) {
  const passedStudents = list.filter((marks) => marks <= 18);
  const average = passedStudents.reduce((prev, curr) => prev + curr, 0) / passedStudents.length;
  return average ? Math.round(average) : "No pass scores registered.";
}

const output = passed([10, 10, 10, 18, 20, 20]);
console.log(output);
