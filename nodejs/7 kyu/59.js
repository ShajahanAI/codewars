// https://www.codewars.com/kata/5667525f0f157f7a0a000004/train/javascript

// Passed

function bucketOf(str) {
  water_words = ["water", "wet", "wash"];
  slime_words = ["i don't know", "slime"];
  let result = "air";
  str = str.toLowerCase();
  const contains_water_words = water_words.some((word) => str.includes(word));
  const contains_slime_words = slime_words.some((word) => str.includes(word));
  if (contains_water_words && contains_slime_words) {
    result = "sludge";
  } else if (contains_water_words) {
    result = "water";
  } else if (contains_slime_words) {
    result = "slime";
  }

  return result;
}

const output = bucketOf("What is that, WATER?!?");
console.log(output);