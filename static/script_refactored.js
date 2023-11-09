const currentData = {}

let updatedData = {}

let currentPlayer = 'X' 

let updatedScore = 1 

const button = document.querySelector('button')

let count = 0

button.addEventListener('click', function () {
  count = count + 1

  console.log(count)
})


for (let i = 1; i < 10; i++) {
  currentData[`box${i}`] = null
  document.querySelector(`.box${i}`).addEventListener('click', function (event) {
    makeMove(i)
  })
}

async function makeMove(index) {
  let boxKey = `box${index}`
  if (currentData[boxKey] === null) {
    currentData[boxKey] = currentPlayer
    document.querySelector(`.${boxKey}`).textContent = currentPlayer
    await sendData()
    currentPlayer = currentPlayer === "X" ? "O" : "X";
  }
}

let gameId = null;

async function getData() {
  const result = await fetch(`http://127.0.0.1:8000/received`);
  const finalResult = await result.json()
  updatedData = finalResult[finalResult.length - 1]
  console.log(updatedData)
}

getData()

async function sendData() {
  console.log('send data first')
  const url = gameId === null ? "http://127.0.0.1:8000/game" : `http://127.0.0.1:8000/game/${gameId}`;
  const method = gameId === null ? "POST" : "PUT";

  const backendData = {
    id: gameId,
    cell_1_1: currentData.box1,
    cell_1_2: currentData.box2,
    cell_1_3: currentData.box3,
    cell_2_1: currentData.box4,
    cell_2_2: currentData.box5,
    cell_2_3: currentData.box6,
    cell_3_1: currentData.box7,
    cell_3_2: currentData.box8,
    cell_3_3: currentData.box9,
  };

  const response = await fetch(url, {
    method: method,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(backendData),
  });
  
  const result = await response.json();
  console.log(result);
  
  if (gameId === null) {
    gameId = result.id; // Save the game ID after the first move
  }
  console.log("send data second");
  updateBoard(result);
}

function updateBoard(data) {
  for (let i = 1; i <= 9; i++) {
    let boxKey = `box${i}`;
    let box = document.querySelector(`.${boxKey}`);
    if (box) {
      box.textContent = data[boxKey] || "";
    } else {
      console.log(`Box ${boxKey} not found in DOM`); 
    }
  }
}
