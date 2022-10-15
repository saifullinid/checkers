export class GameData {

    constructor(gameData) {
        this.winner = gameData['winner']
        this.possibleMoves = gameData['possible_moves']
        this.activePlayer = gameData['active_player']

        this.possibleMovesDOM = []
        this.elements = {}

        this.move = gameData['move']
        this.elementsForEnemyMove = []
    }

    filling() {
        this.possibleMoves.forEach(move => {
            let checkerCoord = move[0].join()
            let cellCoord = move[1].join()

            let checkerClass = `.row_${move[0][0]}.column_${move[0][1]}`
            let cellClass = `.cell_row_${move[1][0]}.cell_column_${move[1][1]}`

            let checker = document.querySelector(checkerClass)
            let cell = document.querySelector(cellClass)

            let enemyCheckerClass = 0
            let enemyCheckerCoord = 0
            let enemyChecker = 0
            if (move[2].length) {
                enemyCheckerClass = `.row_${move[2][0]}.column_${move[2][1]}`
                enemyCheckerCoord = move[2].join()
                enemyChecker = document.querySelector(enemyCheckerClass)
                this.elements[enemyCheckerCoord] = enemyChecker
            }

            this.possibleMovesDOM.push([checker, cell, enemyChecker])

            this.elements[checkerCoord] = checker
            this.elements[cellCoord] = cell
        })
    }

    fillingForEnemyMove() {
        let move = this.move['move']

        let checkerClass = `.row_${move[0][0]}.column_${move[0][1]}`
        let cellClass = `.cell_row_${move[1][0]}.cell_column_${move[1][1]}`

        let checker = document.querySelector(checkerClass)
        let cell = document.querySelector(cellClass)

        this.elementsForEnemyMove.push(checker)
        this.elementsForEnemyMove.push(cell)

        let enemyCheckerClass = 0
        let enemyChecker = 0
        if (move[2].length) {
            enemyCheckerClass = `.row_${move[2][0]}.column_${move[2][1]}`
            enemyChecker = document.querySelector(enemyCheckerClass)
            this.elementsForEnemyMove.push(enemyChecker)
        }
    }
}
