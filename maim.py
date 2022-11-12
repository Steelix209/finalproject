from pygame import *
from random import randint

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
    
    
    def update (self):
        keys = key.get_pressed()
        if keys[K_SPACE]:
            if self.k_jump<= 3:
                self.k_jump += 1
                if self.k_jump == 4:
                    self.k_jump = 0 
                self.rect.y -= self.jump_speed
                self.ground = False


               
        if not self.ground:
            self.gravity += 1
            self.rect.y += self.gravity
        if ground < self.rect.y:
            self.rect.y = ground - 75
            self.ground = True
        


class Cactus(GameSprite):
    def __init__(self, x, y, width, height, color = (255, 113, 13)):
        super().__init__("cactus2.png", x, ground - height, width, height)
        self.width = width
        self.height = height
    def update (self):
        self.rect.x -= bg_speed
        if self.rect.x <- 100:
            self.kill()
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
while run:


    for e in event.get():
        if e.type == QUIT:
            run = False
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
            rand_h = randint(50, 150)
            cactus = Cactus(WIDTH + y, ground, int(rand_h/2), rand_h)
            cactuses.add(cactus)
            y += 200
    player.update()
    cactuses.update()
    window.blit(bg_image, (bg1x,0))
    window.blit(bg_image2, (bg2x,0))

    
    player.draw()
    cactuses.draw(window)
    

    display.update()
    clock.tick(FPS)