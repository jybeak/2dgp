import random
import main_state
from pico2d import *

class Bullet:

    image = None
    def __init__(self):
        self.speed = 1500
        self.x, self.y = 0 ,300
        if Bullet.image == None:
             Bullet.image = load_image('bullet.png')

    def update(self, frame_time):
        distance = self.speed * frame_time
        self.x += distance

        if self.x > 800:
            self.x = main_state.chicken.x+30
            self.y = main_state.chicken.y
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


