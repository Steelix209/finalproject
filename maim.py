from pygame import *
from random import randint
import pygame_menu

mixer.init()
font.init()
init()

WIDTH = 700
HEIGHT = 500
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Dino")
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def draw(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self):
        super().__init__("dino.png", 200, ground - 75, 75, 75)
        self.speed = 5
        self.hp = 100
        self.gravity = 0
        self.ground = True 
        self.jump_speed = 75
        self.k_jump = 0

    def jump(self):
        self.rect.y -= self.jump_speed
        self.ground = False
        self.gravity = 0
    
    def update (self):
       


               
        if not self.ground:
            self.gravity += 0.25
            self.rect.y += self.gravity
        if ground - 75 < self.rect.y:
            self.rect.y = ground - 75
            self.ground = True
        


class Cactus(GameSprite):
    def __init__(self, x, y, width, height, color = (255, 113, 13)):
        super().__init__("cactus2.png", x, ground - height, width, height)
        self.width = width
        self.height = height
    def update (self):
        global points, points_text
        self.rect.x -= bg_speed
        if self.rect.x <- 100:
            self.kill()
            points += 10
            points_text = font2.render("Points:" + str(points), True, (255,255,255))

run = True
finish = False
ground = HEIGHT - 60
bg1x = 0
bg2x = WIDTH


bg_image  = transform.scale(image.load("2.jpg"), (WIDTH, HEIGHT))
bg_image2 = transform.scale(image.load("2.jpg"), (WIDTH, HEIGHT))
bg_speed = 2
player = Player()
cactus = Cactus(100, 500, 100, 100)
cactuses = sprite.Group()
cactuses.add(cactus)
run = True
game = False
FPS = 60
font2 = font.SysFont("Impact",30)
points = 0 
points_text = font2.render("Points:" + str(points), True, (255,255,255))
result = font2.render("Ти програв" , True, (255,0,0))
def start_the_game():
    global game
    game = True
    menu.disable() 
menu = pygame_menu.Menu('DinoRunner', WIDTH, HEIGHT,
                       theme=pygame_menu.themes.THEME_GREEN)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(window)
while run:


    for e in event.get():
        if e.type == QUIT:
            run = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE and game:
                if player.rect.y > 200:   
                    player.jump()
    if game:

        bg1x = bg1x - bg_speed
        bg2x = bg2x - bg_speed
        if bg1x <-WIDTH:
            bg1x = WIDTH
        if bg2x <-WIDTH:
            bg2x = WIDTH

        rand = randint(0, 400)
        if rand == 99:
            rand_k = randint(1, 4)
            y = 100
            for i in range (rand_k):
                rand_h = randint(50, 100)
                cactus = Cactus(WIDTH + y, ground, int(rand_h/2), rand_h)
                cactuses.add(cactus)
                y += 300
        player.update()
        cactuses.update()
    colide = sprite.spritecollideany(player, cactuses)
    if colide:
        game = False

    window.blit(bg_image, (bg1x,0))
    window.blit(bg_image2, (bg2x,0))

    
    player.draw()
    cactuses.draw(window)
    window.blit(points_text,(20,20))
    if not game:
        window.blit(result,(300,300))
    

    display.update()
    clock.tick(FPS)