import pygame
from pygame import *
from settings import *
from characters import *
from platformes import *
from settings import *
from pygame import mixer
from pygame.locals import *
import sys
import os
pygame.init()
pygame.display.set_caption("JOJO: REBORN")
bg = Surface((WIN_WIDTH, WIN_HEIGHT))
start_image = pygame.image.load('data/main_theme.jpg')
bg1 = pygame.image.load('data/bcqgr_best1.png')
platforms = []
timer = pygame.time.Clock()
entities = pygame.sprite.Group()
animatedEntities = pygame.sprite.Group()
#звук
pygame.mixer.pre_init(441000,-16,1,512)
mixer.init()
mainClock = pygame.time.Clock()
sound = pygame.mixer.Sound('data/JoJo.ogg')
sound.play(-1)
#видео
def startvideo():
    os.startfile("data/jotaro.mpg")
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    def reverse(self, pos):
        return pos[0] - self.state.left, pos[1] - self.state.top
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2
    l = min(0, l)
    l = max(-(camera.width-WIN_WIDTH), l)
    t = max(-(camera.height-WIN_HEIGHT), t)
    t = min(0, t)
    return Rect(l, t, w, h)
def load_level(name):
    fullname = 'levels' +'/' + name
    with open(fullname, 'r') as map_file:
        level_map = []
        for line in map_file:
            line = line.strip('/n')
            level_map.append(line)
    return level_map
font = pygame.font.SysFont(None, 20)
def start1():
    men = True
    while men:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                men = False
                return game()
        screen.fill((0,0,0))
        screen.blit(bg1, (0,0))
        pygame.display.update()
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
click = False
def main_menu():
    while True:
        screen.blit(start_image,start_image.get_rect())
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(311, 509, 200, 50)
        button_2 = pygame.Rect(354, 565, 100, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                start1()
        if button_2.collidepoint((mx, my)):
            if click:
                goodbie()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
def goodbie():
    sys.exit(0)
def game():
    bg = pygame.image.load('data/bg1.png')
    hero = Player(55, 55)
    left = right = False
    up = False
    entities.add(hero)
    level = load_level("level_1.txt")
    x = y = 0
    for i in level:
        for j in i:
            if j == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if j == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "#":
                bd = lavadead(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "P":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)
                animatedEntities.add(pr)
            x += PLATFORM_WIDTH
        x = 0
        y += PLATFORM_HEIGHT
    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)
    while True:
        screen.fill((0, 0, 0))
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        if not pygame.sprite.collide_rect(hero, pr):
            screen.blit(bg, (0, 0))
            animatedEntities.update()
            camera.update(hero)
            hero.update(left, right, up, platforms)
            for e in entities:
                screen.blit(e.image, camera.apply(e))
        else:
            animatedEntities.empty()
            entities.empty()
            platforms.clear()
            return level2()
        pygame.display.update()
def level2():
    bg = pygame.image.load('data/bg2.jpg')
    hero = Player(55,630)
    left = right = False
    up = False
    entities.add(hero)
    level = load_level("level_2.txt")
    x = y = 0
    for i in level:
        for j in i:
            if j == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if j == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "#":
                bd = lavadead(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "P":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)
                animatedEntities.add(pr)
            x += PLATFORM_WIDTH
        x = 0
        y += PLATFORM_HEIGHT
    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)
    while True:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        if not pygame.sprite.collide_rect(hero, pr):
            screen.blit(bg, (0, 0))
            animatedEntities.update()
            camera.update(hero)
            hero.update(left, right, up, platforms)
            for e in entities:
                screen.blit(e.image, camera.apply(e))
        else:
            animatedEntities.empty()
            entities.empty()
            platforms.clear()
            return level3()
        pygame.display.update()
def level3():
    bg = pygame.image.load('data/bg3.png')
    hero = Player(160,580)
    left = right = False
    up = False
    entities.add(hero)
    level= load_level("level_3.txt")
    x = y = 0
    for i in level:
        for j in i:
            if j == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if j == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "#":
                bd = lavadead(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "P":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)
                animatedEntities.add(pr)
            x += PLATFORM_WIDTH
        x = 0
        y += PLATFORM_HEIGHT
    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)
    while True:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        if not pygame.sprite.collide_rect(hero, pr):
            screen.blit(bg, (0, 0))
            animatedEntities.update()
            camera.update(hero)
            hero.update(left, right, up, platforms)
            for e in entities:
                screen.blit(e.image, camera.apply(e))
        else:
            animatedEntities.empty()
            entities.empty()
            platforms.clear()
            return level4()
        pygame.display.update()
def level4():
    bg = pygame.image.load('data/bg4.jpg')
    hero = Player(130,580)
    left = right = False
    up = False
    entities.add(hero)
    level = load_level("level_4.txt")
    x = y = 0
    for i in level:
        for j in i:
            if j == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if j == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "#":
                bd = lavadead(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "P":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)
                animatedEntities.add(pr)
            x += PLATFORM_WIDTH
        x = 0
        y += PLATFORM_HEIGHT
    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)
    while True:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        if not pygame.sprite.collide_rect(hero, pr):
            screen.blit(bg, (0, 0))
            animatedEntities.update()
            camera.update(hero)
            hero.update(left, right, up, platforms)
            for e in entities:
                screen.blit(e.image, camera.apply(e))
        else:
            animatedEntities.empty()
            entities.empty()
            platforms.clear()
            return level5()
        pygame.display.update()
def level5():
    bg = pygame.image.load('data/bg5.png')
    hero = Player(500,400)
    entities.add(hero)
    left = right = False
    up = False
    level = load_level("level_5.txt")
    x = y = 0
    for i in level:
        for j in i:
            if j == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if j == "#":
                bd = lavadead(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "D":
                pr = Dio(x, y)
                entities.add(pr)
                platforms.append(pr)
                animatedEntities.add(pr)
            x += PLATFORM_WIDTH
        x = 0
        y += PLATFORM_HEIGHT
    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)
    while True:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        if not pygame.sprite.collide_rect(hero, pr):
            screen.blit(bg, (0, 0))
            animatedEntities.update()
            camera.update(hero)
            hero.update(left, right, up, platforms)
            for e in entities:
                screen.blit(e.image, camera.apply(e))
        else:
            os.startfile("jojo.mpg")
            sys.exit(0)
            animatedEntities.empty()
            entities.empty()
            sound.stop()
        pygame.display.update()
main_menu()