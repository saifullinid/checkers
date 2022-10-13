import {delay} from "./request.js";
import {GameData} from "./gameData.js";
import {Move} from "./service.js";
import {enemyMoveHandling} from "./enemyMoveHandling.js";
import {ownMoveHandling} from "./ownMoveHandling.js";

export function startGameLoop(url) {
    let currentUrl = url.replace('game', 'start')
    localStorage.setItem('move', '');
    (async function loop() {
        let move = ''
        let method = 'GET';
        let winner = ''

        while (!winner) {
            let options = {
                method: method,
                url: currentUrl,
                headers: '',
                responseType: 'json',
                params: move,
            }
            let inputGameData = await delay(options)
            console.log(inputGameData)
            winner = inputGameData['winner']
            if (winner) {
                break
            }

            enemyMoveHandling(inputGameData)
            move = await ownMoveHandling(inputGameData)
        }
        console.log(winner);
    })()
}