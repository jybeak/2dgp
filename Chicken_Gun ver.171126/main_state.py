from pico2d import *
import os
import game_framework
import pause_state
import title_state
import end_state


from chicken import Chicken     # import Chicken class from chicken.py
from bullet import Bullet
from monster import *


name = "MainState"


score = 0
current_time = get_time()

chicken = None
bullet = None
blue_hat_monsters = None
fire_on = False

def create_world():
    global chicken, bullet, blue_hat_monsters
    chicken = Chicken()
    bullet = Bullet()
    blue_hat_monsters = []
    pass


def destroy_world():
    global chicken, bullet, blue_hat_monsters

    del(chicken)
    del(bullet)
    del(blue_hat_monsters)



def enter():
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    global fire_on
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            # p를 누르면 pause_state로 간다.
            elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
                game_framework.push_state(pause_state)
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if fire_on == False:
                    fire_on = True
                elif fire_on == True:
                    fire_on = False
            else:
                chicken.handle_event(event)





def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def draw_main_scene():
    global fire_on, blue_hat_monsters
    chicken.draw()
    chicken.draw_bb()
    for monster in blue_hat_monsters:
        monster.draw()
    if fire_on == True:
        bullet.draw()
        bullet.draw_bb()




def update(frame_time):
    global fire_on, bullet, blue_hat_monsters, blue_hat_monster_time
    chicken.update(frame_time)
    blue_hat_monster_time += frame_time
    if blue_hat_monster_time > 0.7:
        new_blue_hat_monster = Blue_hat_monster()
        blue_hat_monsters.append(new_blue_hat_monster)
        blue_hat_monster_time = 0
    for monster in blue_hat_monsters:
        monster.update(frame_time)
    if fire_on == True:
        bullet.update(frame_time)









def draw(frame_time):
    clear_canvas()
    for monster in blue_hat_monsters:
        monster.draw()
    chicken.draw()
    #brick.draw()\
    chicken.draw_bb()

    if fire_on == True:
        bullet.draw()
        bullet.draw_bb()
    pass

    update_canvas()



