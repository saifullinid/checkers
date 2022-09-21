import { GameData } from './GameData.js'
import { delay } from './request.js'
import { Service } from './Service.js'

let btn_start_game = document.querySelector('.start_button')

btn_start_game.addEventListener('click', start_game)

function start_game() {
    btn_start_game.classList.add('start_button-hidden');

    (async function loop() {
        let move = ''
        let method = 'GET';
        let winner = ''

        while (!winner) {
            let options = {
                method: method,
                url: 'http://127.0.0.1:8000/start',
                headers: '',
                responseType: 'json',
                params: move,
            }
            let inputGameData = await delay(options)
            let gameData = new GameData(inputGameData)
            let service = new Service(gameData)

            move = await service.servicePromise(service)
            winner = gameData.winner
            method = 'POST'
        }
        console.log(winner);
    })()

}

