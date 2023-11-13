const currentData = {}

let updatedData = {}

let currentPlayer = 'X' 

let updatedScore = 1 

const button = document.querySelector('button')

let gameId = null;

let count = 0

button.addEventListener('click', function () {
  gameId++
  createNewGame()
})

async function createNewGame() {
  const url = `http://127.0.0.1:8000/received/${gameId}`;

  const backendData = {
    id: gameId,
    cell_1_1: currentData.box1,
    cell_1_2: currentData.box2,
    cell_1_3: currentData.box3,
    cell_1_4: currentData.box4,
    cell_1_5: currentData.box5,
    cell_1_6: currentData.box6,
    cell_1_7: currentData.box7,
    cell_1_8: currentData.box8,
    cell_1_9: currentData.box9,
  };

  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(backendData),
  });
  const result = await response.json();
  console.log(result)
  return result;
}


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
    await sendData()
    currentPlayer = currentPlayer === "X" ? "O" : "X";
  }
}

async function getData() {
  const result = await fetch(`http://127.0.0.1:8000/received`);
  const finalResult = await result.json()
  updatedData = finalResult[finalResult.length - 1]
  gameId = updatedData.id + 1
  console.log(gameId)
  delete updatedData.id
  for (const data in updatedData) {
    let lastChar = data.charAt(data.length - 1)
    document.querySelector(`.box${lastChar}`).textContent = updatedData[data] || ''
  }
}

getData()

async function sendData() {
  const url = gameId === null ? "http://127.0.0.1:8000/game" : `http://127.0.0.1:8000/game/${gameId}`;
  const method = gameId === null ? "POST" : "PUT";

  const backendData = {
    id: gameId,
    cell_1_1: currentData.box1,
    cell_1_2: currentData.box2,
    cell_1_3: currentData.box3,
    cell_1_4: currentData.box4,
    cell_1_5: currentData.box5,
    cell_1_6: currentData.box6,
    cell_1_7: currentData.box7,
    cell_1_8: currentData.box8,
    cell_1_9: currentData.box9,
  };

  const response = await fetch(url, {
    method: method,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(backendData),
  });
  const result = await response.json()

  return result
}

console.log(currentData)