import {delay} from "./request.js";
import {enemyMoveHandling} from "./enemyMoveHandling.js";
import {ownMoveHandling} from "./ownMoveHandling.js";
import {showWinner} from "./showWinner.js";

export function startGameLoop(url) {
    let currentUrl = url.replace('game', 'start')
    localStorage.setItem('move', '');
    (async function loop() {
        let move = ''
        let method = 'GET';
        let winner = ''

        while (true) {
            let options = {
                method: method,
                url: currentUrl,
                headers: '',
                responseType: 'json',
                params: move,
            }
            let inputGameData = await delay(options)

            enemyMoveHandling(inputGameData)

            winner = inputGameData['winner']
            if (winner) {
                showWinner(inputGameData)
                break
            }

            move = await ownMoveHandling(inputGameData)
        }
    })()
}