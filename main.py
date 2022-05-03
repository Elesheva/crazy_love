import pygame
import time

pygame.init()
Weight = 700
Height = 500
screen = pygame.display.set_mode((Weight,Height))
pygame.display.set_caption("Безумная любовь")
white = (255,255,255)
pink_color= (255, 192, 203)
blue_color = (135,206,250)
black_color = (0,0,0)
FPS = 60
font_name = pygame.font.match_font('arial')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
hurt_img = pygame.image.load('разбитое сердце.png')
timee = 0
expl_sound = pygame.mixer.Sound('zvuk-udara4.wav')
shoot_sound = pygame.mixer.Sound('prostoy-vyistrel.wav')
game_over_sound = pygame.mixer.Sound('MS_Realization.wav')
pygame.mixer.music.load('love_song.wav')
pygame.mixer.music.set_volume(0.4)
won_sound = pygame.mixer.Sound('b24eb5669749169.mp3')
you_won = pygame.mixer.Sound('806ca1f3d6e6270.mp3')
background = pygame.image.load('фон.png')
background_rect = background.get_rect()
tttt = 100


class Bullet_Prince (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("сердце.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 15

    def update(self):
        self.rect.x += self.speedx
        if self.rect.bottom > 700:
            self.kill()


class Bullet_Dragon (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("огонь.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 15

    def update(self):
        self.rect.x += self.speedx
        if self.rect.bottom > 700:
            self.kill()


class Bullet_Rizar (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("цветочек.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 15

    def update(self):
        self.rect.x += self.speedx
        if self.rect.bottom > 700:
            self.kill()

class Bullet_Vordalak (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("камень.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 15

    def update(self):
        self.rect.x += self.speedx
        if self.rect.bottom > 700:
            self.kill()

class Bullet (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("разбитое сердце.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = -15

    def update(self):
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()


class Princess (pygame.sprite.Sprite):
    def __init__(self):
        # инициализация пушки
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Принцесса стоит.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.radious = 25
        self.health = tttt
        self.rect.centerx = Weight - 50
        self.rect.bottom = Height / 2
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.speedy = -8
        if keys[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.top > Height-120:
            self.rect.bottom = Height
        if self.rect.bottom < 120:
            self.rect.top = 0

    def shoot(self):
        bullet = Bullet(self.rect.left,self.rect.bottom)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play()

    def damage(self):
        self.health -= 25


class Prince (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("принц.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.radious= 25
        self.rect.centerx = Weight - 640
        self.rect.bottom = Height / 2
        self.speedy = 6
        self.shield = 100
        self.health = 100

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > 370:
            self.speedy = self.speedy * -1
        if self.rect.y < 10:
            self.speedy = self.speedy * -1

    def shoot(self):
        bullet_prince = Bullet_Prince(self.rect.right,self.rect.bottom)
        all_sprites.add(bullet_prince)
        bullets.add(bullet_prince)
        shoot_sound.play()

    def damage (self):
        self.health -= 25


class Dragon (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("дракон.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.radious= 25
        self.rect.centerx = Weight - 640
        self.rect.bottom = Height / 2
        self.speedy = 8
        self.shield = 100
        self.health = 125

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > 370:
            self.speedy = self.speedy * -1
        if self.rect.y < 10:
            self.speedy = self.speedy * -1

    def shoot(self):
        bullet_prince = Bullet_Dragon(self.rect.right,self.rect.bottom)
        all_sprites.add(bullet_prince)
        bullets.add(bullet_prince)
        shoot_sound.play()

    def damage (self):
        self.health -= 25


class Rizar (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("рыцарь.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.radious= 25
        self.rect.centerx = Weight - 640
        self.rect.bottom = Height / 2
        self.speedy = 9
        self.shield = 100
        self.health = 150

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > 370:
            self.speedy = self.speedy * -1
        if self.rect.y < 10:
            self.speedy = self.speedy * -1

    def shoot(self):
        bullet_prince = Bullet_Rizar(self.rect.right,self.rect.bottom)
        all_sprites.add(bullet_prince)
        bullets.add(bullet_prince)
        shoot_sound.play()

    def damage (self):
        self.health -= 25


class Vurdalak (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("вурдалак.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        self.radious= 25
        self.rect.centerx = Weight - 640
        self.rect.bottom = Height / 2
        self.speedy = 6
        self.shield = 100
        self.health = 175

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > 370:
            self.speedy = self.speedy * -1
        if self.rect.y < 10:
            self.speedy = self.speedy * -1

    def shoot(self):
        bullet_prince = Bullet_Vordalak(self.rect.right,self.rect.bottom)
        all_sprites.add(bullet_prince)
        bullets.add(bullet_prince)
        shoot_sound.play()

    def damage (self):
        self.health -= 25

def draw_hurts(surf,x,y,pct):
    if pct <0:
        pct = 0
    BAR_l = 100
    BAR_H = 10
    fill = (pct/100)*BAR_l
    outline= pygame.Rect(x,y,BAR_l,BAR_H)
    fill_rect = pygame.Rect(x,y,fill,BAR_H)
    pygame.draw.rect(surf,pink_color,fill_rect)
    pygame.draw.rect(surf,white,outline,2)

def draw_hurts_prince(surf,x,y,pct):
    if pct <0:
        pct = 0
    BAR_l = 100
    BAR_H = 10
    fill = (pct/100)*BAR_l
    outline= pygame.Rect(x,y,BAR_l,BAR_H)
    fill_rect = pygame.Rect(x,y,fill,BAR_H)
    pygame.draw.rect(surf,blue_color,fill_rect)
    pygame.draw.rect(surf,white,outline,2)

def draw_hurts_dragon(surf,x,y,pct):
    if pct <0:
        pct = 0
    BAR_l = 125
    BAR_H = 10
    fill = (pct/125)*BAR_l
    outline= pygame.Rect(x,y,BAR_l,BAR_H)
    fill_rect = pygame.Rect(x,y,fill,BAR_H)
    pygame.draw.rect(surf,blue_color,fill_rect)
    pygame.draw.rect(surf,white,outline,2)

def draw_hurts_rizar(surf,x,y,pct):
    if pct <0:
        pct = 0
    BAR_l = 150
    BAR_H = 10
    fill = (pct/150)*BAR_l
    outline= pygame.Rect(x,y,BAR_l,BAR_H)
    fill_rect = pygame.Rect(x,y,fill,BAR_H)
    pygame.draw.rect(surf,blue_color,fill_rect)
    pygame.draw.rect(surf,white,outline,2)

def draw_hurts_vordalak(surf,x,y,pct):
    if pct <0:
        pct = 0
    BAR_l = 175
    BAR_H = 10
    fill = (pct/175)*BAR_l
    outline= pygame.Rect(x,y,BAR_l,BAR_H)
    fill_rect = pygame.Rect(x,y,fill,BAR_H)
    pygame.draw.rect(surf,blue_color,fill_rect)
    pygame.draw.rect(surf,white,outline,2)

def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def the_screen():
    screen.blit(background, background_rect)
    draw_text(screen, 'CRAZY LOVE',64,Weight/2,Height/4)
    draw_text(screen,'',22,Weight/2,Height/2)
    draw_text(screen,'Нажмите пробел, чтобы начать',24,Weight/2,Height*2/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def the_screen_prince_kill():
    screen.blit(background, background_rect)
    draw_text(screen, 'Вы разбили принцу сердце!',52,Weight/2,Height/4)
    draw_text(screen,'',22,Weight/2,Height/2)
    draw_text(screen,'Уровень 2',24,Weight/2,Height*2/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def the_screen_princess_kill():
    screen.blit(background, background_rect)
    draw_text(screen, 'Принцесса проиграла!',52,Weight/2,Height/4)
    draw_text(screen,'',22,Weight/2,Height/2)
    draw_text(screen,'Начать сначала?',24,Weight/2,Height*2/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def the_screen_dragon_kill():
    screen.blit(background, background_rect)
    draw_text(screen, 'Вы потушили огонь драконища!', 52, Weight/2, Height/4)
    draw_text(screen, '', 22, Weight/2, Height/2)
    draw_text(screen, 'Уровень 3', 24, Weight/2, Height*2/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def the_screen_vordalak_kill():
    screen.blit(background, background_rect)
    draw_text(screen, 'Вы выйграли!', 52, Weight/2, Height/4)
    draw_text(screen, '', 22, Weight/2, Height/2)
    draw_text(screen, 'Игра окончена', 24, Weight/2, Height*2/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def the_screen_rizar_kill():
    screen.blit(background, background_rect)
    draw_text(screen, 'Вы победили рыцаря!', 52, Weight/2, Height/4)
    draw_text(screen, '', 22, Weight/2, Height/2)
    draw_text(screen, 'Уровень 4', 24, Weight/2, Height*2/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def the_screen_princess():
    screen.blit(background, background_rect)
    draw_text(screen, 'Принцесса проиграла!',52,Weight/2,Height/4)
    draw_text(screen,'',22,Weight/2,Height/2)
    draw_text(screen,'Начать сначала?',24,Weight/2,Height*2/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

prince = Prince()
all_sprites.add(prince)
dragon = Dragon()
all_sprites.add(dragon)
princess = Princess()
all_sprites.add(princess)
vordalak = Vurdalak()
all_sprites.add(vordalak)

# Цикл игры
game_over = True
running = True
pygame.mixer.music.play(loops=-1)
prince_count = 1
while running:
    if game_over:
        game_over= False
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        if prince_count == 1:
            prince = Prince()
            the_screen()
            all_sprites.add(prince)
            tttt = 100
        if prince_count == 2:
            prince = Dragon()
            all_sprites.add(prince)
            with open('result.txt', 'r') as file:
                tttt = int(file.read())
                princess.health = tttt
                print(tttt)
            you_won.play()
            the_screen_prince_kill()
            time.sleep(2)
        if prince_count == 3:
            prince = Rizar()
            all_sprites.add(prince)
            with open('result.txt', 'r') as file:
                tttt = int(file.read())
                princess.health = tttt
            you_won.play()
            the_screen_dragon_kill()
            time.sleep(2)
        if prince_count == 4:
            prince = Vurdalak()
            all_sprites.add(prince)
            with open('result.txt', 'r') as file:
                tttt = int(file.read())
                princess.health = tttt
            you_won.play()
            the_screen_rizar_kill()
            time.sleep(2)
        if prince_count == 5:
            with open('result.txt', 'r') as file:
                tttt = int(file.read())
                princess.health = tttt
            won_sound.play()
            the_screen_vordalak_kill()
            time.sleep(2)
            running = True
            prince_count = 0
        princess = Princess()
        all_sprites.add(princess)
    timee += 1
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                princess.shoot()
    all_sprites.update()
    bullets.update()
    # Здоровье
    princess_hits = pygame.sprite.spritecollide(princess,bullets, True)
    if princess_hits:
        princess.damage(),expl_sound.play()
    prince_hits = pygame.sprite.spritecollide(prince, bullets, True)
    if prince_hits:
        prince.damage(), expl_sound.play()
    if princess.health == 0:
        game_over_sound.play()
        the_screen_princess_kill()
        time.sleep(1)
        game_over = True
        prince_count = 1
    if prince.health == 0:
        prince_count += 1
        with open('result.txt', 'w') as file:
            zdorove = str(princess.health)
            file.write(zdorove)
        game_over = True
    # Пуля принца
    if prince_count == 1:
        if timee % 20 == 0:
            if prince.rect.y + 70 > princess.rect.y and prince.rect.y - 70 < princess.rect.y:
                prince.shoot()
    if prince_count == 2:
        if timee % 15 == 0:
            if prince.rect.y + 90 > princess.rect.y and prince.rect.y - 90 < princess.rect.y:
                prince.shoot()
    if prince_count == 3:
        if timee % 12 == 0:
            if prince.rect.y + 100 > princess.rect.y and prince.rect.y - 100 < princess.rect.y:
                prince.shoot()
    if prince_count == 4:
        if timee % 10 == 0:
            if prince.rect.y + 100 > princess.rect.y and prince.rect.y - 100 < princess.rect.y:
                prince.shoot()
    # Экран
    screen.blit(background,background_rect)
    # Полоска здоровья
    draw_hurts(screen, princess.rect.x - 30, princess.rect.y - 30, princess.health)
    if prince_count == 1:
        draw_hurts_prince(screen,prince.rect.x,prince.rect.y-30,prince.health)
    if prince_count == 2:
        draw_hurts_dragon(screen, prince.rect.x, prince.rect.y - 30, prince.health)
    if prince_count == 3:
        draw_hurts_rizar(screen, prince.rect.x, prince.rect.y - 30, prince.health)
    if prince_count == 4:
        draw_hurts_vordalak(screen, prince.rect.x, prince.rect.y - 30, prince.health)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()






