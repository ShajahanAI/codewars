// https://www.codewars.com/kata/562f91ff6a8b77dfe900006e/train/javascript

// Passed

function movie(card, ticket, perc) {
  let systemACost = 0;
  let systemBCost = card;
  let systemBTicketCost = ticket * perc;
  let result = 0;

  while (systemACost <= Math.ceil(systemBCost)) {
    systemACost += ticket;
    systemBCost += systemBTicketCost;
    systemBTicketCost *= perc;
    result++;
  }

  return result;
}

const output = movie(500, 15, 0.9);
console.log(output);