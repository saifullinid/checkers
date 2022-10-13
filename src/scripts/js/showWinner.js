export function showWinner(inputGameData) {
    let winnerColor = inputGameData['winner']
    let winnerUsername = inputGameData['players'][winnerColor]

    let p = document.createElement('p')
    p.innerHTML(winnerUsername)
    let winnerTablet = document.querySelector('.winner_tablet')

    winnerTablet.classList.remove('hidden')
    winnerTablet.classList.add('visible')

    winnerTablet.append(p)
}