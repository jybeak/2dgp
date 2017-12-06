import random
import math
import main_state
from pico2d import *

bullet_between_bullet_time = 0
mouse_pos_x, mouse_pos_y =0,0

class Bullet:


    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 200.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    image = None
    def __init__(self):
        self.x, self.y = main_state.chicken.x+40 ,main_state.chicken.y
        if Bullet.image == None:
             Bullet.image = load_image('resouce/bullet.png')

    def update(self, frame_time):
        global mouse_pos_x, mouse_pos_y
        distance_between_mousecursor_chicken_x = mouse_pos_x - main_state.chicken.x
        distance_between_mousecursor_chicken_y = mouse_pos_y - main_state.chicken.y
        distance_between_mousecursor_chicken =                                                                      \
            math.sqrt(math.pow(distance_between_mousecursor_chicken_x, 2) +                                         \
                      pow(distance_between_mousecursor_chicken_y, 2))

        cos_theta = distance_between_mousecursor_chicken_x / distance_between_mousecursor_chicken
        sin_theta = distance_between_mousecursor_chicken_y / distance_between_mousecursor_chicken

        if main_state.chicken.bullet_state == main_state.chicken.BULLET_LEVEL01 :
            self.x += (Bullet.RUN_SPEED_PPS * frame_time)
        elif main_state.chicken.bullet_state == main_state.chicken.BULLET_LEVEL02 :
            self.x += (cos_theta * Bullet.RUN_SPEED_PPS * frame_time)
            self.y += (sin_theta * Bullet.RUN_SPEED_PPS * frame_time)





    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_event(self, event):
        global mouse_pos_x, mouse_pos_y
        if event.type == SDL_MOUSEMOTION:
            mouse_pos_x, mouse_pos_y = event.x, 600 - event.y


class Bullet_level_up:
    image = None

    def __init__(self):

        self.x, self.y = 1000, random.randint(50, 550)
        if Bullet_level_up.image == None:
            Bullet_level_up.image = load_image('resouce/bullet_level_up.png')

    def update(self,frame_time):
        if main_state.ui.score >= 10:
            self.x -= 500 * frame_time / 3

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 20,\
               self.x + 30, self.y + 20


