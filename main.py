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
rifle = Actor("rifle")

score = 0


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
    rifle.topleft = pos


def on_mouse_down(pos):
    global score

    print(pos)
    if target1.collidepoint(pos):
        target1.right = 0
        target1.y = random.randint(0, HEIGHT)
        score = score + 10
    if target2.collidepoint(pos):
        target2.right = 0
        target2.y = random.randint(0, HEIGHT)
        score = score + 10
    if target3.collidepoint(pos):
        target3.right = 0
        target3.y = random.randint(0, HEIGHT)
        score = score + 10

    print(score)


def draw():
    screen.clear()
    target1.draw()
    target2.draw()
    target3.draw()
    cursor.draw()
    rifle.draw()
    screen.draw.text(f"{score}", (20, 20), fontsize=100)


pgzrun.go()
