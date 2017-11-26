from pico2d import *
import main_state
import title_state
import game_framework

name = "EndState"

GameOver_Image = None


def enter():
    global GameOver_Image
    GameOver_Image = load_image('gameover.png')
    game_framework.reset_time()


def exit():
    global GameOver_Image

    del (GameOver_Image)


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
                game_framework.run(title_state)




def update(frame_time):
    pass




def draw(frame_time):
    global GameOver_Image
    GameOver_Image.draw(400, 300)
    update_canvas()






