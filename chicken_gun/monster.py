import random
import main_state
from pico2d import *

blue_hat_monster_time = 0
red_plant_monster_time = 0

class Blue_hat_monster:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 80.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    blue_hat_monster_image = None

    def __init__(self):
        self.x, self.y = 800, random.randint(0, 600)
        if Blue_hat_monster.blue_hat_monster_image is None:
            Blue_hat_monster.blue_hat_monster_image = load_image('resouce/blue_hat_monster.png')

    def update(self, frame_time):
        distance = Blue_hat_monster.RUN_SPEED_PPS * frame_time
        self.x -= distance



    def draw(self):
        self.blue_hat_monster_image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Red_plant_monster:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    red_plant_monster_image = None

    def __init__(self):
        self.x, self.y = 800, random.randint(0, 600)
        self.life =3
        if Red_plant_monster.red_plant_monster_image is None:
            Red_plant_monster.red_plant_monster_image = load_image('resouce/red_plant_monster.png')

    def update(self, frame_time):
        distance = Red_plant_monster.RUN_SPEED_PPS * frame_time
        self.x -= distance



    def draw(self):
        self.red_plant_monster_image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())