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
red_plant_monsters = None
fire_mode_on = False

def create_world():
    global chicken, bullet, blue_hat_monsters, red_plant_monsters
    chicken = Chicken()
    bullet = Bullet()
    blue_hat_monsters = []
    red_plant_monsters = []
    pass


def destroy_world():
    global chicken, bullet, blue_hat_monsters, red_plant_monsters

    del(chicken)
    del(bullet)
    del(blue_hat_monsters)
    del(red_plant_monsters)



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
    global fire_mode_on
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
                game_framework.push_state(pause_state)
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if fire_mode_on == False:
                    fire_mode_on = True
                elif fire_mode_on == True:
                    fire_mode_on = False
            else:
                chicken.handle_event(event)
                bullet.handle_event(event)





def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def check_collision_chicken_monters():
    global chicken, bullet, blue_hat_monsters, red_plant_monsters

    for monster in blue_hat_monsters:
        if collide(chicken, monster):
            blue_hat_monsters.remove(monster)
            chicken.life-=1

    for monster in red_plant_monsters:
        if collide(chicken, monster):
            red_plant_monsters.remove(monster)
            chicken.life-=1

def check_collision_bullet_monters():
    global chicken, bullet, blue_hat_monsters, red_plant_monsters

    for monster in blue_hat_monsters:
        if collide(bullet, monster):
            bullet.x, bullet.y = chicken.x + 40, chicken.y
            blue_hat_monsters.remove(monster)

    for monster in red_plant_monsters:
        if collide(bullet, monster):
            bullet.x, bullet.y = chicken.x+40, chicken.y

def draw_main_scene():
    global fire_mode_on, blue_hat_monsters, red_plant_monsters
    chicken.draw()
    chicken.draw_bb()
    for monster in blue_hat_monsters:
        monster.draw()
        monster.draw_bb()

    for monster in red_plant_monsters:
        monster.draw()
        monster.draw_bb()

    if fire_mode_on == True:
        bullet.draw()
        bullet.draw_bb()




def update(frame_time):
    global fire_mode_on, bullet, blue_hat_monsters, blue_hat_monster_time, red_plant_monsters ,red_plant_monster_time

    chicken.update(frame_time)
    check_collision_chicken_monters()
    check_collision_bullet_monters()
    blue_hat_monster_time += frame_time
    red_plant_monster_time += frame_time

    if blue_hat_monster_time > 0.7:
        new_blue_hat_monster = Blue_hat_monster()
        blue_hat_monsters.append(new_blue_hat_monster)
        blue_hat_monster_time = 0

    if red_plant_monster_time > 1.2:
        new_red_plant_monster = Red_plant_monster()
        red_plant_monsters.append(new_red_plant_monster)
        red_plant_monster_time = 0

    for monster in blue_hat_monsters:
        monster.update(frame_time)

    for monster in red_plant_monsters:
        monster.update(frame_time)

    if fire_mode_on == True:
        bullet.update(frame_time)

    if chicken.life == 0:
        chicken.life =3
        blue_hat_monsters = []
        red_plant_monsters = []
        game_framework.push_state(end_state)







def draw(frame_time):
    global chicken, bullet, blue_hat_monsters, red_plant_monsters
    clear_canvas()
    for monster in blue_hat_monsters:
        monster.draw()
        monster.draw_bb()

    for monster in red_plant_monsters:
        monster.draw()
        monster.draw_bb()

    chicken.draw()
    chicken.draw_bb()

    if fire_mode_on == True:
        bullet.draw()
        bullet.draw_bb()
    pass

    update_canvas()



