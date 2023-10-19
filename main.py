# button a
def on_button_pressed_a():
    if n2 < 1:
        n1 + 1
        basic.show_number(n1)
        
# button b
def on_button_pressed_b():
    if n2 < 1:
        n1 + 1
        basic.show_number(n1)

n2 = 0
operation = 0
n1 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_a)