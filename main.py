import random

import pgzrun

WIDTH = 720
HEIGHT = 480

target1 = Actor("duck_target_yellow")
target1.x = WIDTH / 2
target1.y = HEIGHT / 2

target2 = Actor("duck_target_brown")
target2.x = WIDTH / 2
target2.y = 100

target3 = Actor("duck_target_white")
target3.x = WIDTH / 2
target3.y = 400

cursor = Actor("crosshair_red_large")


def update():
    target1.x = 5 + target1.x
    if target1.left > WIDTH:
        target1.right = 0
        target1.y = random.randint(0, HEIGHT)
    target2.x = 5 + target2.x
    if target2.left > WIDTH:
        target2.right = 0
        target2.y = random.randint(0, HEIGHT)
    target3.x = 5 + target3.x
    if target3.left > WIDTH:
        target3.right = 0
        target3.y = random.randint(0, HEIGHT)


def on_mouse_move(pos):
    cursor.pos = pos


def on_mouse_down(pos):
    print(pos)


def draw():
    screen.clear()
    target1.draw()
    target2.draw()
    target3.draw()
    cursor.draw()


pgzrun.go()
