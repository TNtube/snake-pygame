import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((400, 420))

run = True

clock = pygame.time.Clock()

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

APPLE = pygame.Surface((20, 20))
APPLE.fill(RED)
x_apple = randint(0, 19)*20
y_apple = randint(1, 20)*20

SNAKE = pygame.Surface((20, 20))
SNAKE.fill(GREEN)
snake_pos = [(0, 20), (20, 20), (40, 20)]

BG = pygame.Surface((400, 20))
BG.fill(WHITE)

dx = 20
dy = 0

score = 0
score_surf = pygame.font.SysFont("Arial", 20)


def isGameOver():
    for i in snake_pos[:-1]:
        if snake_pos[-1] == i:
            return True
    if not 0 <= snake_pos[-1][0] <= 380 or not 20 <= snake_pos[-1][1] <= 400:
        return True


def move(dx, dy):
    snake_pos.append((snake_pos[-1][0]+dx, snake_pos[-1][1]+dy))
    if not snake_pos[-1] == (x_apple, y_apple):
        del snake_pos[0]
    else:
        return new_pos()


def draw_snake(pos):
    for i in pos:
        screen.blit(SNAKE, i)


def new_pos():
    return randint(0, 19)*20, randint(0, 19)*20


while run:
    # show on the screen the elements
    screen.fill((0, 0, 0))
    screen.blit(BG, (0, 0))
    screen.blit(APPLE, (x_apple, y_apple))
    draw_snake(snake_pos)
    sc = score_surf.render(f"Score : {score}", True, BLACK)
    screen.blit(sc, (screen.get_width()//2 - sc.get_width()//2, 0))

    pygame.display.flip()

    # actions
    a = move(dx, dy)
    if a:
        score += 1
        x_apple, y_apple = a
    if isGameOver():
        break

    # events to get the keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if dy != -20:
                    dx = 0
                    dy = 20
            if event.key == pygame.K_UP:
                if dy != 20:
                    dx = 0
                    dy = -20
            if event.key == pygame.K_LEFT:
                if dx != 20:
                    dx = -20
                    dy = 0
            if event.key == pygame.K_RIGHT:
                if dx != -20:
                    dx = 20
                    dy = 0

    clock.tick(15)
