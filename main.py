#hello
import random
import sys
from time import sleep

from pygame import *
window = display.set_mode((1280,720))
display.set_caption('FNAF')

class GameSprite(sprite.Sprite):
    def __init__(self, filename, size_x, size_y, pos_x, pos_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Enemy(GameSprite):
    def update(self):
        coord = [[130, 160],[110, 170],[500, 270],[450, 500], [260, 600],[280, 60], [880, 380], [880, 60], [1000, 60]]
        coord_choice = random.choice(coord)
        sleep(1)
        self.rect.x = coord_choice[0]
        self.rect.y = coord_choice[1]
class Door(sprite.Sprite):
    def __init__(self, width, height,  pos_x, pos_y, color_r, color_g, color_b):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill((color_r, color_g, color_b))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.visible = True
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


background = GameSprite("background.jpg", 1280,720, 0, 0, 0)
enemy = Enemy('animatronic.png', 120, 70, 1000, 60, 1)
door = Door(100, 10, 260, 550, 139,69,19)
player = GameSprite('animatronic.png', 120, 70, 260, 600, 1)
clock = time.Clock()
font.init()
font = font.Font(None, 70)
win = font.render('You Won', True, (0, 255, 0))
loose = font.render('You Lose', True, (255, 0, 0))

gameOver = False
timer = 0
while True:
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if door.visible:
                    door.visible = False
                else:
                    door.visible = True

    background.draw()
    enemy.draw()
    player.draw()
    if not gameOver and timer <= 10:
        enemy.update()
    if door.visible:
        door.draw()

    if not door.visible and enemy.rect.x == 260 and enemy.rect.y == 600 or timer > 10:
        gameOver = True

    if gameOver:
        window.blit(loose, (250, 250))

    timer += 1
    if timer > 10 and not gameOver:
        window.blit(win, (250, 250))

    display.update()
    clock.tick(75)
