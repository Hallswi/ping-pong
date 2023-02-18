from pygame import *
from random import randint
from time import time as timer

win_width = 700
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))
background = (200, 255, 255)
window.fill(background)

clock = time.Clock()
FPS = 60
run = True


while run:
    #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)