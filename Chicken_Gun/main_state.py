from pico2d import *
import os
import game_framework
import pause_state
import title_state
import end_state
import random


from chicken import *     # import Chicken class from chicken.py
from bullet import *
from monster import *
from ui import *
from background import *



name = "MainState"

score = 0
current_time = get_time()

chicken = None
bullets = None
bullet_level_up = None
blue_hat_monsters = None
red_plant_monsters = None
background = None
ui = None


def create_world():
    global chicken, ui, bullets, blue_hat_monsters, red_plant_monsters, bullet_level_up, background
    chicken = Chicken()
    ui = Ui()
    bullet_level_up = Bullet_level_up()
    background = Background()
    bullets = []
    blue_hat_monsters = []
    red_plant_monsters = []

    pass


def destroy_world():
    global chicken, ui,bullets, blue_hat_monsters, red_plant_monsters, bullet_level_up, background

    del(chicken)
    del(bullets)
    del(bullet_level_up)
    del(blue_hat_monsters)
    del(red_plant_monsters)
    del(ui)
    del(background)



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
    global bullets
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
                game_framework.push_state(pause_state)
            elif event.type == SDL_MOUSEBUTTONDOWN:
                new_bullet = Bullet()
                bullets.append(new_bullet)
                chicken.shot_sound()
            else:
                chicken.handle_event(event)
                for bullet in bullets:
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
    global chicken, bullets, blue_hat_monsters, red_plant_monsters, ui
    for monster in blue_hat_monsters:
        for bullet in bullets:
            if collide(bullet, monster):
                bullets.remove(bullet)
                monster.monster_hit_sound.play()
                blue_hat_monsters.remove(monster)

                ui.score += 10

    for monster in red_plant_monsters:
        for bullet in bullets:
            if collide(bullet, monster):
                bullets.remove(bullet)
                monster.life -=1
                if monster.life == 0:
                    monster.monster_hit_sound.play()
                    red_plant_monsters.remove(monster)
                    ui.score += 20

def check_collision_chicken_bulletLevelUp():
    global chicken, bullet_level_up
    if collide(chicken, bullet_level_up):
        bullet_level_up.y = 800
        bullet_level_up.bullet_level_up_sound.play()
        chicken.bullet_state = chicken.BULLET_LEVEL02

    pass

def draw_main_scene():
    global blue_hat_monsters, red_plant_monsters, bullets, bullet_level_up,background
    chicken.draw()
    bullet_level_up.draw()
    ui.draw()
    background.draw()
    for monster in blue_hat_monsters:
        monster.draw()

    for monster in red_plant_monsters:
        monster.draw()

    for bullet in bullets:
        bullet.draw()




def update(frame_time):
    global bullets, blue_hat_monsters, blue_hat_monster_time, red_plant_monsters ,\
        red_plant_monster_time, bullet_level_up

    chicken.update(frame_time)
    bullet_level_up.update(frame_time)
    check_collision_chicken_monters()
    check_collision_bullet_monters()
    check_collision_chicken_bulletLevelUp()
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

    for bullet in bullets:
        bullet.update(frame_time)
        if bullet.x > 800 or bullet.x < 0 or bullet.y > 600 or bullet.y < 0:
            bullets.remove(bullet)

    if chicken.life == 0:
        chicken.bullet_state = chicken.BULLET_LEVEL01
        chicken.life =3
        bullet_level_up.x, bullet_level_up.y = 1000, random.randint(0, 600)

        blue_hat_monsters = []
        red_plant_monsters = []
        bullets= []
        game_framework.push_state(end_state)







def draw(frame_time):
    global chicken, ui,bullets, blue_hat_monsters, red_plant_monsters
    clear_canvas()
    background.draw()
    for monster in blue_hat_monsters:
        monster.draw()

    for monster in red_plant_monsters:
        monster.draw()

    chicken.draw()
    bullet_level_up.draw()
    for bullet in bullets:
        bullet.draw()
    ui.draw()
    pass

    update_canvas()



