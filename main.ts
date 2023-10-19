function aa2 () {
    if (operation == 1) {
        basic.showString("+")
    } else if (operation == 2) {
        basic.showString("-")
    } else if (operation == 3) {
        basic.showString("*")
    } else if (operation == 4) {
        basic.showString("/")
    }
}
function _ () {
    if (operation == 1) {
        answer = n1 + n2
        basic.showNumber(answer)
        reset()
    } else if (operation == 2) {
        answer = n1 - n2
        basic.showNumber(answer)
        reset()
    } else if (operation == 3) {
        answer = n1 * n2
        basic.showNumber(answer)
        reset()
    } else if (operation == 4) {
        answer = n1 / n2
        basic.showNumber(answer)
        reset()
    }
}
input.onButtonPressed(Button.A, function () {
    if (n2 == 0) {
        n1 += 1
        basic.showNumber(n1)
    } else if (operation > 0) {
        _()
    }
})
input.onButtonPressed(Button.AB, function () {
    if (n1 != 0 && n2 != 0) {
        if (operation < 4) {
            operation += 1
            aa2()
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (n1 != 0) {
        n2 += 1
        basic.showNumber(n2)
    }
})
function reset () {
    n1 = 0
    n2 = 0
    operation = 0
}
let n2 = 0
let n1 = 0
let answer = 0
let operation = 0
reset()
