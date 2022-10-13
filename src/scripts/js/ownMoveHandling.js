import {Move} from "./service.js";

export async function ownMoveHandling(inputGameData) {
    let activePlayer = inputGameData['active_player']
    let activeUsername = inputGameData['players'][activePlayer]
    let username = localStorage.getItem('username')

    if (username === activeUsername) {
        let ownMove = new Move(inputGameData)
        return await ownMove.movePromise(ownMove)
    } else {
        return ''
    }
}