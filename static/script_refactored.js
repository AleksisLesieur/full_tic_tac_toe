const board = {}

let receivedData;

const currentData = {}

let currentPlayer = 'X' // true stands for "X" symbol

for (let i = 1; i < 10; i++) {
    board[`box${i}`] = document.querySelector(`.box${i}`)
    currentData[`box${i}`] = null
}

async function sendData() {
    const response = await fetch("http://127.0.0.1:8000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(currentData),
    });
    receivedData = await response.json();
}

console.log(receivedData)

const selectBoard = document.querySelectorAll('.box')

for (let i = 1; i < selectBoard.length + 1; i++) {
  selectBoard[i - 1].addEventListener('click', function () {
    if (currentPlayer === "X" && currentData[`box${i}`] === null) {
      currentData[`box${i}`] = "X";
      selectBoard[i - 1].textContent = receivedData[`box${i}`]
      currentPlayer = "O";
    }
    else if (currentPlayer === "O" && currentData[`box${i}`] === null) {
      currentData[`box${i}`] = "O";
      currentPlayer = "X";
      selectBoard[i - 1].textContent = receivedData[`box${i}`];
    }
    sendData(currentData);
  })
}

// Using setInterval in JavaScript
setInterval(() => {
  sendData(currentData);
  console.log("test");
}, 1000); 
// 1000 milliseconds = 1 second
