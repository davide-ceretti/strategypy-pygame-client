"""
All the settings/constants of the game
"""
import pygame


# Screen & grid
CAPTION = "StrategyPY"
FPS = 25
BG_COLOR = (0, 0, 0)
UNIT_SIZE = (10, 10)
GRID_COLOR = (50, 50, 50)
u_x, u_y = UNIT_SIZE
cell = lambda x, y: (u_x*x, u_y*y, u_x, u_y)

# Player colors

DEFAULT_COLOR_NAME = pygame.Color(100, 100, 100)
COLORS = [
    pygame.Color(255, 0, 0),
    pygame.Color(0, 255, 0),
    pygame.Color(0, 0, 255),
    pygame.Color(255, 255, 0),
    pygame.Color(0, 255, 255),
    pygame.Color(255, 0, 255),
]


def get_player_color(index):
    try:
        return COLORS[index]
    except IndexError:
        return DEFAULT_COLOR_NAME


def get_screen_size(grid_size):
    x, y = UNIT_SIZE
    X, Y = grid_size
    return x*X, y*Y
