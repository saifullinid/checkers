import {EnemyMove} from "./service.js";

export function enemyMoveHandling(inputGameData) {
    let move = inputGameData['move']['move']
    let isActivePlayerChanged = inputGameData['is_active_player_changed']
    let activePlayer = inputGameData['active_player']
    let activeUsername = inputGameData['players'][activePlayer]
    let username = localStorage.getItem('username')

    console.log('enemyMoveHandling', move, isActivePlayerChanged, activeUsername)

    if (move && ((username !== activeUsername) ^ isActivePlayerChanged)) {
        let enemyMove = new EnemyMove(inputGameData)
        enemyMove.makeMove()
    }
}