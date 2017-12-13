import main_state
from monster import *
from pico2d import *


class Door:
    image = None
    sound = None
    def __init__(self):

        self.x, self.y = 1000, 300
        if Door.image == None:
            Door.image = load_image('resouce/image/door_image.png')

    def update(self,frame_time):

        if main_state.boss_monster.life <= 0 and self.x > 600:
            self.x -= 500 * frame_time / 3


    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20,\
               self.x + 20, self.y + 20