// https://www.codewars.com/kata/595910299197d929a10005ae/train/javascript

// Passed

function pizzaRewards(customers, minOrders, minPrice) {
  let eligibleCustomers = [];
  Object.keys(customers).forEach((customer) => {
    let eligibleOrders = customers[customer].filter(
      (orderValue) => orderValue >= minPrice
    );
    if (eligibleOrders.length >= minOrders) eligibleCustomers.push(customer);
  });

  return eligibleCustomers;
}

const output = pizzaRewards(
  {
    "John Doe": [22, 30, 11, 17, 15, 52, 27, 12],
    "Jane Doe": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45],
  },
  5,
  20
);

console.log(output);