export class Service {
    constructor(gameData) {
        this.possibleMoves = gameData.possibleMoves
        this.activePlayer = gameData.activePlayer

        this.possibleMovesDOM = gameData.possibleMovesDOM
        this.elements = gameData.elements
    }

    getActiveCheckers() {
        let checkersSet = new Set()
        this.possibleMovesDOM.forEach(move => {
            checkersSet.add(move[0])
        })
        console.log('possibleMovesDOM', this.possibleMovesDOM);
        return Array.from(checkersSet)
    }

    addRemoveActiveCheckersClass(checker, activeCheckers) {
        checker.classList.toggle('active_checker')

        activeCheckers.forEach(el => {
            if (el != checker) {
                el.classList.remove('active_checker')
            }
        })
    }

    getActiveCells(checker) {
        let isActiveClassFound = checker.classList.value.includes('active_checker') ? true : false
        let activeCellsArr = []
        let passiveCellsArr = []
        this.possibleMovesDOM.forEach(move => {
            if (move[0] == checker & isActiveClassFound) {
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
        let enemyChecker = 0
        this.possibleMovesDOM.forEach(move => {
            if (move[0] == checker & move[1] == cell) {
                console.log('move\n', move);
                console.log('!!! in getEnemyChecker !!!\n');
                console.log('enemyChecker', move[2]);
                enemyChecker = move[2]
            }
        })
        return enemyChecker
    }

    getMoveAndElements(checker, cell) {
        let enemyChecker = this.getEnemyChecker(checker, cell)
        let enemyCoord = []
        let checkerCoord = []
        let cellCoord = []

        for (let key in this.elements) {
            let element = this.elements[key]
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
        elements[0].style.cssText = `--row:${move[1][0]}; --column:${move[1][1]};`

        let removeClass = [`row_${move[0][0]}`, `column_${move[0][1]}`]
        let addClass = [`row_${move[1][0]}`, `column_${move[1][1]}`]
        elements[0].classList.remove(removeClass[0], removeClass[1])
        elements[0].classList.add(addClass[0], addClass[1])

        if (this.activePlayer == 'black' & move[1][0] == 7) {
            elements[0].classList.add('queen')
        } else if (this.activePlayer == 'white' & move[1][0] == 0) {
            elements[0].classList.add('queen')
        }

        if (elements[2]) {
            elements[2].remove()
        }
    }

    cloneElements() {
        for (let key in this.elements) {
            if (this.elements[key] == null) {
                continue
            } else {
                this.elements[key].classList.remove('active_checker')
                this.elements[key].classList.remove('hovered')
                this.elements[key].classList.remove('active_cell')
                let clone = this.elements[key].cloneNode(true)
                this.elements[key].replaceWith(clone)
            }
        }
    }

    turnField() {
        let field = document.querySelector('.field')
        if (this.activePlayer == 'white') {
            field.classList.remove('turned')
        } else {
            field.classList.add('turned')
        }
    }

    servicePromiseOne = serviceThis => {
        return new Promise(function(resolve, reject) {
            serviceThis.turnField()
            let activeCheckers = serviceThis.getActiveCheckers()
            activeCheckers.forEach(el => {
                // console.log('servicePromiseOne\n', activeCheckers, '\n', el);
                el.classList.add('hovered')
            })

            activeCheckers.forEach(checker => {
                checker.addEventListener('click', () => {
                    serviceThis.addRemoveActiveCheckersClass(checker, activeCheckers)

                    let activeCells
                    let passiveCells
                    [activeCells, passiveCells] = serviceThis.getActiveCells(checker)
                    serviceThis.addCellsActiveClass(activeCells)
                    serviceThis.removeCellsActiveClass(passiveCells)

                    resolve([activeCells, checker, serviceThis])
                })
            })
        })
    }

    servicePromiseTwo = function(activeCells, checker, serviceThis) {
        return new Promise(function(resolve, reject) {
            activeCells.forEach(cell => {
                cell.addEventListener('click', () => {
                    let elements
                    let move
                    [move, elements] = serviceThis.getMoveAndElements(checker, cell)
                    serviceThis.makeMove(move, elements)

                    serviceThis.cloneElements()
                    // console.log('!!! in addEventOnCells !!!\n', move);
                    resolve(move)
                })
            })
        })
    }

    async servicePromise(obj) {
        let temp = await this.servicePromiseOne(obj)
        let move = await this.servicePromiseTwo(temp[0], temp[1], temp[2])
        return move
    }
}