const board = {}

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
    const result = await response.json()
    console.log(result)
}


// async function updateData() {
//   const response = await fetch("/", {
//     method: "PUT",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(currentData),
//   });
//   const result = await response.json();
//   console.log(result, " testing");
// }

// async function getData() {
//   const response = await fetch("http://127.0.0.1:8000/");
//   const data = await response.json()
//   console.log(data)
//   console.log('getdata function')
// }

const selectBoard = document.querySelectorAll('.box')

for (let i = 1; i < selectBoard.length + 1; i++) {
  selectBoard[i - 1].addEventListener('click', function () {
    if (currentPlayer === "X" && currentData[`box${i}`] === null) {
      currentData[`box${i}`] = "X";
      currentPlayer = "O";
      selectBoard[i - 1].textContent = "X"
    }
    else if (currentPlayer === "O" && currentData[`box${i}`] === null) {
      currentData[`box${i}`] = "O";
      currentPlayer = "X";
      selectBoard[i - 1].textContent = "O";
    }
    sendData(currentData);
    })
}

// Using setInterval in JavaScript
// setInterval(() => {
//   sendData(currentData);
//   console.log("chat");
// }, 1000); // 1000 milliseconds = 1 second
