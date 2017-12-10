import main_state
from pico2d import *


class Door:
    image = None
    sound = None
    def __init__(self):

        self.x, self.y = 1000, 300
        if Door.image == None:
            Door.image = load_image('resouce/image/door_image.png')
        if Door.sound == None:
            Door.sound = load_wav('resouce/sound/door_sound.wav')
            Door.sound.set_volume(32)

    def update(self,frame_time):
        if main_state.ui.score >= 300 and self.x > 600:
            self.x -= 500 * frame_time / 3


    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20,\
               self.x + 20, self.y + 20