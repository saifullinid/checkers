import {waitingForSecondPlayer} from "./waitingForSecondPlayer.js";
import {getUsername} from "./getUsername.js";

let url = window.location.href

if (url.indexOf('login') !== -1) {
    getUsername()
} else if (url.indexOf('game') !== -1) {
    waitingForSecondPlayer(url)
}






