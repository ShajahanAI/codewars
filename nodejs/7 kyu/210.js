// https://www.codewars.com/kata/5b203de891c7469b520000b4/train/javascript

// Passed

function playerManager(players) {
  let playersData = [];
  if (!players) return playersData;

  let ungroupedData = players.split(", ");
  for (let idx = 0; idx < ungroupedData.length; idx += 2) {
    let [name, phone] = ungroupedData.slice(idx, idx + 2);
    phone = Number(phone);
    let playerData = {
      player: name,
      contact: phone,
    };
    playersData.push(playerData);
  }

  return playersData;
}

const output = playerManager("John Doe, 8167238327, Jane Doe, 8163723827");
console.log(output);