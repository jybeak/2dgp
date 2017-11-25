import random

from pico2d import *

class Brick:
    LEFT_MOVE, RIGHT_MOVE = 0,1
    image = None

    def __init__(self):
        self.x, self.y = 0, 200
        self.speed = 100
        self.state = self.RIGHT_MOVE

        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')

    def update(self, frame_time):
        if self.state ==self.RIGHT_MOVE:
            self.x += frame_time * self.speed
        elif self.state ==self.LEFT_MOVE:
            self.x -= frame_time * self.speed
        if self.x > 800:
            self.x =800
            self.state = self.LEFT_MOVE
        elif self.x <0:
            self.x =0
            self.state = self.RIGHT_MOVE

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-90, self.y-20, self.x+90, self.y+20

    def handle_event(self, event):
        pass