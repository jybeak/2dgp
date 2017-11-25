from pico2d import *
import os
import game_framework
import pause_state
import title_state

from boy import Boy # import Boy class from boy.py
from ball import Ball, BigBall
from grass import Grass
from brick import Brick

name = "MainState"

boy = None
balls = None
big_balls = None
grass = None
brick = None

def create_world():
    global boy, grass, balls, big_balls, brick
    boy = Boy()
    big_balls = [BigBall() for i in range(20)]
    balls = [Ball() for i in range(10)]
    balls = big_balls + balls
    grass = Grass()
    brick = Brick()
    pass


def destroy_world():
    global boy, grass, balls, big_balls, brick

    del(boy)
    del(balls)
    del(grass)
    del(big_balls)
    del(brick)



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
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            # p를 누르면 pause_state로 간다.
            elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
                game_framework.push_state(pause_state)
            else:
                boy.handle_event(event)



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def draw_main_scene():
    grass.draw()
    boy.draw()
    brick.draw()
    for ball in balls:
        ball.draw()


def update(frame_time):
    boy.update(frame_time)
    brick.update(frame_time)
    for ball in balls:
        ball.update(frame_time)

    for ball in balls:
        if collide(brick, ball) :
            if brick.state == brick.RIGHT_MOVE:
                ball.x += frame_time * brick.speed
            elif brick.state == brick.LEFT_MOVE:
                ball.x -= frame_time * brick.speed
            if brick.x > 800:
                ball.x = 800
                brick.state = brick.LEFT_MOVE
            elif brick.x < 0:
                ball.x = 0
                brick.state = brick.RIGHT_MOVE
            ball.y = brick.y + 40




def draw(frame_time):
    clear_canvas()
    grass.draw()
    boy.draw()
    brick.draw()
    for ball in balls:
        ball.draw()

    grass.draw_bb()
    boy.draw_bb()
    brick.draw_bb()
    for ball in balls:
        ball.draw_bb()
    pass

    update_canvas()






