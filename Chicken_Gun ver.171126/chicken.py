import random

from pico2d import *

class Chicken:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



    #TIME_PER_ACTION = 0.5
    #ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    #FRAMES_PER_ACTION = 8

    image = None

    LEFT_FLYING, RIGHT_FLYING, STAND, JUMP = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 0, 350
        self.life_time = 0.0
        self.dir = 0

        self.fall_speed = -60
        self.state = self.STAND
        if Chicken.image == None:
            Chicken.image = load_image('chicken.png')


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Chicken.RUN_SPEED_PPS * frame_time
        height = self.fall_speed * frame_time

        self.x += (self.dir * distance)

        self.y += height

        self.x = clamp(0, self.x, 800)




    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if self.state in (self.STAND, self.JUMP, self.RIGHT_FLYING):
                self.state = self.LEFT_FLYING
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            if self.state in (self.STAND, self.JUMP, self.LEFT_FLYING):
                self.state = self.RIGHT_FLYING
                self.dir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            if self.state in (self.LEFT_FLYING, self.JUMP,):
                self.state = self.STAND
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_d):
            if self.state in (self.RIGHT_FLYING, self.JUMP,):
                self.state = self.STAND
                self.dir = 0


    def chicken_position(self):
        return self.x, self.y


