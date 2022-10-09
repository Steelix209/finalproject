from pygame import *


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
        self.img = transform.scale(image.load(image_name), (width, height))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def draw(self):
        window.blit(self.img, self.rect)

class Player(GameSprite):
    def __init__(self):
        super().__init__("dino.png", 200, 200, 75, 75)
        self.speed = 5
        self.hp = 100


    def update (self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect. ax > 0:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < WIDTH - self.width:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[k_DOWM] and self.rect.y <HEIGTH - self.height:
            self.rect.y += self.speed


class Cactus(GameSprite):
    def __init__(self, x, y, width, height, color = (255, 113, 13)):
        super().__init__("cactus2.png", x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
run = True
finish = False



bg_image  = transform.scale(image.load("2.jpg"), (WIDTH, HEIGHT))
player = Player()
cactus = Cactus(100, 100, 50, 50)
run = True
game = False
FPS = 60
while run:


    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(bg_image, (0,0))
    player.draw()
    cactus.draw()
    

    display.update()
    clock.tick(FPS)