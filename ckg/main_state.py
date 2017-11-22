import random
import json
import os

from pico2d import *

import game_framework
import title_state

from chicken import Chicken



name = "MainState"

chicken = None
bullet = None
object1= None
object2= None
object3= None
object4= None


class Bullet:
    def __init__(self):
        self.image = load_image('kong.png')


class Object1:
    def __init__(self):
        self.image = load_image('object1.png')

    def draw(self):
        self.image.draw(0, 30)

class Object2:
    def __init__(self):
        self.image = load_image('object2.png')

    def draw(self):
        self.image.draw(150, 30)

class Object3:
    def __init__(self):
        self.image = load_image('object3.png')

    def draw(self):
        self.image.draw(300, 30)

class Object4:
    def __init__(self):
        self.image = load_image('object4.png')

    def draw(self):
        self.image.draw(450, 30)








def enter():
    global chicken, bullet, object1, object2, object3, object4
    chicken = Chicken()
    bullet = Bullet()
    object1 = Object1()
    object2 = Object2()
    object3 = Object3()
    object4 = Object4()
    pass


def exit():
    global chicken, bullet, object1, object2, object3, object4
    del(chicken)
    del(bullet)
    del(object1)
    del(object2)
    del(object3)
    del(object4)

    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)


    pass


def update():
    chicken.update()
    pass


def draw():
    clear_canvas()
    chicken.draw()
    object1.draw()
    object2.draw()
    object3.draw()
    object4.draw()
    update_canvas()
    pass


