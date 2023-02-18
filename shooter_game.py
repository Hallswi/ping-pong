from pygame import *
from random import randint
from time import time as timer

win_width = 700
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))
background = (200, 255, 255)

clock = time.Clock()
FPS = 60
run = True
finish = False
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
#конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

L_Player = Player('racket.png', 5, win_height - 150, 80, 150, 10)
R_Player = Player('racket.png', 615 , win_height - 150, 80, 150, 10)
Ball = Player('ball.png', 270, win_height - 300, 75, 50, 10)

ballx = 5
bally = 5


while run:
    #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not finish:
        window.fill(background)
        L_Player.update_L()
        L_Player.reset()

        R_Player.update_R()
        R_Player.reset()   

        Ball.rect.x += ballx
        Ball.rect.y += bally
        if Ball.rect.y > win_height - 100 or Ball.rect.y < 0:
            bally*= - 1

        Ball.reset()
    
    
    
    
    
    
    display.update()
    clock.tick(FPS)
