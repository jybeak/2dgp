import game_framework
import title_state
import main_state
from pico2d import *


name = "PauseState"
image = None
logo_time = 0.0
count =0

def enter():
    global image
    image = load_image('char.png')


def exit():
    global image
    del(image)


def update(frame_time):
    global count
    count = (count + 1) % 100
    pass


def draw(frame_time):
    global  image
    clear_canvas()
    main_state.draw_main_scene()
    if count <50:
        image.draw(400, 300)
    update_canvas()



def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()
    pass


def pause(): pass


def resume(): pass
