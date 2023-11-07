const currentData = {}

let currentPlayer = 'X' 

for (let i = 1; i < 10; i++) {
  currentData[`box${i}`] = null
  document.querySelector(`.box${i}`).addEventListener('click', function () {
    makeMove(i)
  })
}

async function makeMove(index) {
  let boxKey = `box${index}`
  if (currentData[boxKey] === null) {
    currentData[boxKey] = currentPlayer
    document.querySelector(`.${boxKey}`).textContent = currentPlayer
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    await sendData()
  }
}


async function sendData() {
    const response = await fetch("http://127.0.0.1:8000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(currentData),
    });
    const result = await response.json();
    updateBoard(result);
}

function updateBoard(data) {
  for (let i = 1; i < 10; i++) {
    let boxKey = `box${i}`
    let box = document.querySelector(`.${boxKey}`)
    if (box) {
      box.textContent = data[boxKey]
    }
  }
}

setInterval(() => {
  sendData(currentData);
  console.log("test");
}, 1000); 


// const selectBoard = document.querySelectorAll(".box");

// for (let i = 1; i < selectBoard.length + 1; i++) {
//   selectBoard[i - 1].addEventListener('click', function () {
//     if (currentPlayer === "X" && currentData[`box${i}`] === null) {
//       currentData[`box${i}`] = "X";
//       selectBoard[i - 1].textContent = downloadedData[`box${i}`]
//       currentPlayer = "O";
//     }
//     else if (currentPlayer === "O" && currentData[`box${i}`] === null) {
//       currentData[`box${i}`] = "O";
//       currentPlayer = "X";
//       selectBoard[i - 1].textContent = downloadedData[`box${i}`]
//     }
//     console.log(currentData);
//     sendData(currentData);
//   })
// }

