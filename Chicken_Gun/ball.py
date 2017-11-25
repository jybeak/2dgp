import random

from pico2d import *

class Ball:

    image = None;

    def __init__(self):
        self.x, self.y = random.randint(200, 790), 60
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
    # fill here


class BigBall(Ball):
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.fall_speed = random.randint(150,300)
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
    def update(self, frame_time):
        self.y -= frame_time*self.fall_speed

        if self.y < 70:
            self.y = 70


    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
    # fill here
