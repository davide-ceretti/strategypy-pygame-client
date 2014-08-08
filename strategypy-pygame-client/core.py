import pygame

import settings


class Game(object):
    def __init__(self, data):
        self.data = data
        self.init_screen()
        self.done = False

    def init_screen(self):
        """
        Initialize screen
        """
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.fps = settings.FPS
        self.screen_size = settings.get_screen_size(self.data['grid_size'])

    def event_loop(self):
        """
        Fetch for events
        """
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                self.done = True

    def draw(self, frame_id):
        """
        Main drawing function called in the infinite loop
        """
        self.screen.fill(settings.BG_COLOR)
        self.draw_grid()
        self.draw_units(frame_id)

    def draw_units(self, frame_id):
        """
        Draw all the units in their position according to the
        relative frame
        """
        try:
            frame = self.data['frames'][frame_id]
        except IndexError:
            frame = self.data['frames'][-1]
        for player_id, units_dict in frame.iteritems():
            player_color = settings.get_player_color(int(player_id))
            for x, y in units_dict.itervalues():
                surface = pygame.display.get_surface()
                pygame.draw.rect(
                    surface, player_color, settings.cell(x, y)
                )

    def draw_grid(self):
        """
        Draw a grid according to the game settings
        """
        X, Y = self.screen_size
        gap_x, gap_y = settings.UNIT_SIZE
        for i in xrange(0, X+1, gap_x):
            pygame.draw.line(
                self.screen,
                settings.GRID_COLOR,
                (i, 0),
                (i, Y),
                1,
            )
        for i in xrange(0, Y+1, gap_y):
            pygame.draw.line(
                self.screen,
                settings.GRID_COLOR,
                (0, i),
                (X, i),
                1,
            )

    def display_caption(self):
        """
        Show the program's FPS in the window handle
        """
        fps = self.clock.get_fps()
        caption = "{0} - FPS: {1:.2f}".format(settings.CAPTION, fps)
        pygame.display.set_caption(caption)

    def main_loop(self):
        """
        The main loop of the game, can be interrupted by events
        """
        frame_id = 0
        while not self.done:
            self.event_loop()
            self.draw(frame_id)
            pygame.display.update()
            self.clock.tick(self.fps)
            self.display_caption()
            frame_id += 1
