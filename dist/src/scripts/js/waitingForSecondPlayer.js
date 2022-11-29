import {delay} from "./request.js";
import {startGameLoop} from "./gameLoop.js";

export async function waitingForSecondPlayer(url) {
    let currentUrl = url.replace('game', 'waiting_for_second_player')
    let options = {
        method: 'GET',
        url: currentUrl,
        headers: '',
        responseType: 'json',
        params: '',
    }
    while (true) {
        let res = await delay(options)
        if (res && res['msg'] === 'start') {
            break
        }
    }
    let waitingTablet = document.querySelector('.waiting')
    waitingTablet.classList.add('hidden')
    startGameLoop(url)
}