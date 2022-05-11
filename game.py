import pygame

from direction import Direction
from game_state import GameState
from position import Position

pygame.init()

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

CUBES_NUM = 20
CUBE_SIZE = 25
WIDTH = CUBE_SIZE * CUBES_NUM
screen = pygame.display.set_mode((WIDTH, WIDTH))


def draw_snake_part(pos: Position):
    position = (pos.x * CUBE_SIZE,
                pos.y * CUBE_SIZE,
                CUBE_SIZE,
                CUBE_SIZE)
    pygame.draw.rect(screen, GREEN, position)


def draw_snake(snake: [Position]):
    for element in snake:
        draw_snake_part(element)


def draw_food(pos: Position):
    radius = float(CUBE_SIZE) / 2
    position = (pos.x * CUBE_SIZE + radius,
                pos.y * CUBE_SIZE + radius)
    pygame.draw.circle(screen, BLUE, position, radius)


def fill_bg():
    screen.fill(WHITE)


def draw(snake, food):
    fill_bg()
    draw_snake(snake)
    draw_food(food)
    pygame.display.update()


state = GameState(
    snake=None,
    direction=None,
    food=None,
    field_size=CUBES_NUM,
)
state.set_initial_position()

clock = pygame.time.Clock()
while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                state.turn(Direction.LEFT)

            elif event.key == pygame.K_RIGHT:
                state.turn(Direction.RIGHT)

            elif event.key == pygame.K_UP:
                state.turn(Direction.UP)

            elif event.key == pygame.K_DOWN:
                state.turn(Direction.DOWN)

    state.step()
    draw(state.snake, state.food)
