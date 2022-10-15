import {EnemyMove} from "./service.js";

export function enemyMoveHandling(inputGameData) {
    let move = inputGameData['move']['move']
    let storageMove = localStorage.getItem('move')
    let isActivePlayerChanged = inputGameData['is_active_player_changed']
    let activePlayer = inputGameData['active_player']
    let activeUsername = inputGameData['players'][activePlayer]
    let username = localStorage.getItem('username')

    if (move && ((username !== activeUsername) ^ isActivePlayerChanged)) {
        move = move.join(',')
        if (storageMove !== move) {
            let enemyMove = new EnemyMove(inputGameData)
            enemyMove.makeMove()
            localStorage.setItem('move', move)
        }
    }
}