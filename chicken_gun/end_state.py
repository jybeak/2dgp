from pico2d import *
import main_state
import title_state
import game_framework

name = "EndState"

gameover_image = None


def enter():
    global gameover_image
    gameover_image = load_image('resouce/gameover.png')
    game_framework.reset_time()


def exit():
    global gameover_image

    del (gameover_image)


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
            elif (event.type, event.key)==(SDL_KEYDOWN, SDLK_SPACE):
                game_framework.pop_state()




def update(frame_time):
    pass




def draw(frame_time):
    global gameover_image
    clear_canvas()
    gameover_image.draw(400, 300)
    update_canvas()






