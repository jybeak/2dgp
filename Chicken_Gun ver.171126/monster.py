import random
import main_state
from pico2d import *

blue_hat_monster_time =0

class Blue_hat_monster:

    image = None

    def __init__(self):
        self.x, self.y = 800, random.randint(0, 600)
        self.speed = +500
        if Blue_hat_monster.image is None:
            Blue_hat_monster.image = load_image('blue_hat_monster.png')

    def update(self, frame_time):
        distance = self.speed * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 40, self.y - 50, self.x + 40, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())