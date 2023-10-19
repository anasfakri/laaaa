def aa2():
    if operation == 1:
        basic.show_string("+")
    elif operation == 2:
        basic.show_string("-")
    elif operation == 3:
        basic.show_string("*")
    elif operation == 4:
        basic.show_string("/")
def _2():
    global answer
    if operation == 1:
        answer = n1 + n2
        basic.show_number(answer)
        reset()
    elif operation == 2:
        answer = n1 - n2
        basic.show_number(answer)
        reset()
    elif operation == 3:
        answer = n1 * n2
        basic.show_number(answer)
        reset()
    elif operation == 4:
        answer = n1 / n2
        basic.show_number(answer)
        reset()

def on_button_pressed_a():
    global n1
    if n2 == 0:
        n1 += 1
        basic.show_number(n1)
    elif operation > 0:
        _2()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global operation
    if n1 != 0 and n2 != 0:
        operation += 1
        aa2()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global n2
    if n1 != 0:
        n2 += 1
        basic.show_number(n2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def reset():
    global n1, n2, operation
    n1 = 0
    n2 = 0
    operation = 0
n2 = 0
n1 = 0
answer = 0
operation = 0
reset()