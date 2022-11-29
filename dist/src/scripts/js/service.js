import {GameData} from "./gameData.js";

export class Move {
    constructor(inputGameData) {
        this.gameData = new GameData(inputGameData)
        this.gameData.filling()
    }

    getActiveCheckers() {
        let checkersSet = new Set()
        let possibleMovesDOM = this.gameData.possibleMovesDOM
        possibleMovesDOM.forEach(move => {
            checkersSet.add(move[0])
        })
        return Array.from(checkersSet)
    }

    addRemoveActiveCheckersClass(checker, activeCheckers) {
        checker.classList.toggle('active_checker')

        activeCheckers.forEach(el => {
            if (el !== checker) {
                el.classList.remove('active_checker')
            }
        })
    }

    getActiveCells(checker) {
        let possibleMovesDOM = this.gameData.possibleMovesDOM
        let isActiveClassFound = checker.classList.value.includes('active_checker')
        let activeCellsArr = []
        let passiveCellsArr = []
        possibleMovesDOM.forEach(move => {
            if (move[0] === checker && isActiveClassFound) {
                activeCellsArr.push(move[1])
            } else {
                passiveCellsArr.push(move[1])
            }
        })
        passiveCellsArr = passiveCellsArr.filter(cell => !activeCellsArr.includes(cell))
        return [activeCellsArr, passiveCellsArr]
    }

    addCellsActiveClass(activeCells) {
        activeCells.forEach(el => {
            el.classList.add('active_cell')
        })
    }

    removeCellsActiveClass(passiveCells) {
        passiveCells.forEach(el => {
            el.classList.remove('active_cell')
        })
    }

    getEnemyChecker(checker, cell) {
        let possibleMovesDOM = this.gameData.possibleMovesDOM
        let enemyChecker = 0
        possibleMovesDOM.forEach(move => {
            if (move[0] === checker && move[1] === cell) {
                enemyChecker = move[2]
            }
        })
        return enemyChecker
    }

    getMoveAndElements(checker, cell) {
        let elements = this.gameData.elements
        let enemyChecker = this.getEnemyChecker(checker, cell)
        let enemyCoord = []
        let checkerCoord = []
        let cellCoord = []

        for (let key in elements) {
            let element = elements[key]
            switch(element) {
                case checker:
                    checkerCoord = key.split(',').map(str => parseInt(str, 10))
                    break
                case cell:
                    cellCoord = key.split(',').map(str => parseInt(str, 10))
                    break
                case enemyChecker:
                    enemyCoord = key.split(',').map(str => parseInt(str, 10))
                    break
            }
        }
        return [[checkerCoord, cellCoord, enemyCoord], [checker, cell, enemyChecker]]
    }

    makeMove(move, elements) {
        let activePlayer = this.gameData.activePlayer
        let ownChecker = elements[0]
        let enemyChecker = elements[2]
        ownChecker.style.cssText = `--row:${move[1][0]}; --column:${move[1][1]};`

        let removeClass = [`row_${move[0][0]}`, `column_${move[0][1]}`]
        let addClass = [`row_${move[1][0]}`, `column_${move[1][1]}`]
        ownChecker.classList.remove(removeClass[0], removeClass[1])
        ownChecker.classList.add(addClass[0], addClass[1])

        if (activePlayer === 'black' && move[1][0] === 7) {
            ownChecker.classList.add('queen')
        } else if (activePlayer === 'white' && move[1][0] === 0) {
            ownChecker.classList.add('queen')
        }

        if (enemyChecker) {
            enemyChecker.remove()
        }
    }

    cloneAllElements() {
        let elements = this.gameData.elements
        for (let key in elements) {
            if (elements[key]) {
                elements[key].classList.remove('active_checker')
                elements[key].classList.remove('hovered')
                elements[key].classList.remove('active_cell')
                let clone = elements[key].cloneNode(true)
                elements[key].replaceWith(clone)
            }
        }
    }

    cloneCells(activeCells, passiveCells) {
        let elements = [...activeCells, ...passiveCells]
        elements.forEach(el => {
            let clone = el.cloneNode(true)
            el.replaceWith(clone)
        })
    }

    movePromise = moveThis => {
        return new Promise(function(resolve, reject) {
            let activeCheckers = moveThis.getActiveCheckers()
            activeCheckers.forEach(el => {
                el.classList.add('hovered')
            })

            activeCheckers.forEach(checker => {
                checker.addEventListener('click', () => {
                    moveThis.addRemoveActiveCheckersClass(checker, activeCheckers)

                    let activeCells
                    let passiveCells
                    [activeCells, passiveCells] = moveThis.getActiveCells(checker)
                    moveThis.addCellsActiveClass(activeCells)
                    moveThis.removeCellsActiveClass(passiveCells)
                    moveThis.cloneCells(activeCells, passiveCells)
                    moveThis.gameData.filling();
                    [activeCells, ] = moveThis.getActiveCells(checker)

                    activeCells.forEach(cell => {
                        cell.addEventListener('click', () => {
                            let elements
                            let move
                            [move, elements] = moveThis.getMoveAndElements(checker, cell)
                            moveThis.makeMove(move, elements)

                            moveThis.cloneAllElements()
                            resolve(move)
                        })
                    })
                })
            })
        })
    }
}

export class EnemyMove {
    constructor(inputGameData) {
        this.gameData = new GameData(inputGameData)
        this.gameData.fillingForEnemyMove()
    }
    makeMove() {
        let ownChecker = this.gameData.elementsForEnemyMove[0]
        let enemyChecker = this.gameData.elementsForEnemyMove[2]
        let move = this.gameData.move['move']
        let playerColor = this.gameData.move['color']

        ownChecker.style.cssText = `--row:${move[1][0]}; --column:${move[1][1]};`

        let removeClass = [`row_${move[0][0]}`, `column_${move[0][1]}`]
        let addClass = [`row_${move[1][0]}`, `column_${move[1][1]}`]
        ownChecker.classList.remove(removeClass[0], removeClass[1])
        ownChecker.classList.add(addClass[0], addClass[1])

        if (playerColor === 'black' && move[1][0] === 7) {
            ownChecker.classList.add('queen')
        } else if (playerColor === 'white' && move[1][0] === 0) {
            ownChecker.classList.add('queen')
        }

        if (enemyChecker) {
            enemyChecker.remove()
        }
    }
}