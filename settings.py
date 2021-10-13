import pygame
WIN_WIDTH = 800
WIN_HEIGHT = 640
may = (WIN_WIDTH, WIN_HEIGHT)
screen = pygame.display.set_mode(may,0,32)
display= pygame.Surface((200,200))
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FFFFFF"
ANIMATION_DELAY = 0.06
ANIMATION_RIGHT = [pygame.image.load("anim/r1.png").convert_alpha(),pygame.image.load("anim/r2.png").convert_alpha(),pygame.image.load("anim/r3.png").convert_alpha(),pygame.image.load("anim/r4.png").convert_alpha(),pygame.image.load("anim/r5.png").convert_alpha(),pygame.image.load("anim/r6.png").convert_alpha(),pygame.image.load("anim/r7.png").convert_alpha(),pygame.image.load("anim/r8.png").convert_alpha()]
ANIMATION_LEFT = [pygame.image.load("anim/l1.png").convert_alpha(),pygame.image.load("anim/l2.png").convert_alpha(),pygame.image.load("anim/l3.png").convert_alpha(),pygame.image.load("anim/l4.png").convert_alpha(),pygame.image.load("anim/l5.png").convert_alpha(),pygame.image.load("anim/l6.png").convert_alpha(),pygame.image.load("anim/l7.png").convert_alpha(),pygame.image.load("anim/l8.png").convert_alpha()]
ANIMATION_JUMP_RIGHT = [(pygame.image.load("anim/r5.png").convert_alpha(), 0.01)]
ANIMATION_JUMP_LEFT = [(pygame.image.load("anim/l5.png").convert_alpha(), 0.01)]
ANIMATION_JUMP = [(pygame.image.load("anim/r5.png").convert_alpha(), 0.1)]
ANIMATION_STAY = [(pygame.image.load("anim/r1.png").convert_alpha(), 0.01)]
ANIMATION_PRINCESS = [pygame.image.load("data/drug.png").convert_alpha()]
ANIMATION_DIO = [pygame.image.load("data/diooo.png").convert_alpha()]