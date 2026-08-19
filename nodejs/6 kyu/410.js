// https://www.codewars.com/kata/5e7e4b7cd889f7001728fd4a/train/javascript

// Passed

function toTable(data, headers = false, index = false) {
  let tableRows = data.map((row, idx) => {
    if (headers && idx === 0) {
      return "";
    }

    let tableData =
      (index ? `<td>${headers ? idx : idx + 1}</td>` : "") +
      row
        .map((datapoint) => `<td>${datapoint !== null ? datapoint : ""}</td>`)
        .join("");
    let tableRow = `<tr>${tableData}</tr>`;
    return tableRow;
  });

  let tableHeader = "";
  if (headers) {
    let headerRow = data[0];
    let tableHeaderData =
      (index ? `<th></th>` : "") +
      headerRow
        .map((header) => `<th>${header !== null ? header : ""}</th>`)
        .join("");
    tableHeader = `<thead><tr>${tableHeaderData}</tr></thead>`;
  }

  let table = `<table>${tableHeader}<tbody>${tableRows.join("")}</tbody></table>`;
  return table;
}

const output = toTable(
  [
    ["id", "name", "price", "quantity"],
    [24351, "pen", 2.41, 500],
    [null, "pencil", 0.99, 25],
    [63401, "grizzly bear", null, 1],
    [3532, "rubber duck", 5.45, 24],
    [1523, null, 3.0, 6.8],
    [11765, "caviar", 67.95, null],
  ],
  true,
);
console.log(output);