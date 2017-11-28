import random
import math
import main_state
from pico2d import *


class Bullet:

    image = None
    def __init__(self):
        self.speed = 2000
        self.mouse_pos_x = 0
        self.mouse_pos_y = 0
        self.x, self.y = main_state.chicken.x+40 ,main_state.chicken.y-10
        if Bullet.image == None:
             Bullet.image = load_image('resouce/bullet.png')

    def update(self, frame_time):
        distance_between_mousecursor_chicken_x = self.mouse_pos_x - main_state.chicken.x + 40
        distance_between_mousecursor_chicken_y = self.mouse_pos_y - main_state.chicken.y
        distance_between_mousecursor_chicken =                                                                      \
            math.sqrt(math.pow(distance_between_mousecursor_chicken_x, 2) +                                         \
                      pow(distance_between_mousecursor_chicken_y, 2))

        cos_theta = distance_between_mousecursor_chicken_x / distance_between_mousecursor_chicken
        sin_theta = distance_between_mousecursor_chicken_y / distance_between_mousecursor_chicken
        self.x += (cos_theta * self.speed * frame_time)
        self.y += (sin_theta * self.speed * frame_time)

        print(self.mouse_pos_x ,self.mouse_pos_y )


        if self.x > 800 or self.x < 0 or self.y > 600 or self.y < 0:
            self.x, self.y = main_state.chicken.x + 40, main_state.chicken.y
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.mouse_pos_x, self.mouse_pos_y = event.x, 600 - event.y


