from pico2d import *


class Chicken:
    image = None
    UP, DWN, LEFT, RIGHT, STAND = 0, 1, 2, 3, 4
    def __init__(self):
        self.x, self.y = 100, 200
        self.frame = 0
        self.image = load_image('char.png')
        self.dir = 1
        self.state = self.STAND



    def update(self):
        events = get_events()
        for event in events:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
                self.y += 10
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
                self.y -= 10
            if (event.type, event.key) == (SDL_KEYUP, SDLK_a):
                self.x -= 10
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_d):
                self.x += 10

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self):
        pass