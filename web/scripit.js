const gridSize = 10;
const gridElement = document.getElementById('grid');
const messageElement = document.getElementById('message');

function createGrid() {
    gridElement.innerHTML = '';
    for (let y = 0; y < gridSize; y++) {
        for (let x = 0; x < gridSize; x++) {
            const cell = document.createElement('button');
            cell.className = 'cell';
            cell.textContent = '';
            cell.onclick = async () => {
                const result = await eel.check_position(x, y)();
                cell.textContent = 'X';
                cell.classList.add('clicked');
                messageElement.textContent = `(${x}, ${y}) - ${result}`;
            };
            gridElement.appendChild(cell);
        }
        gridElement.appendChild(document.createElement('br'));
    }
}

async function resetGame() {
    await eel.reset_game()();
    createGrid();
    messageElement.textContent = "Novo jogo! Boa sorte!";
}

createGrid();