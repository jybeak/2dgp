from pico2d import *
import main_state
import game_framework

name = "TitleState"

BackGround_Image = None
Push_Spacebar_image = None


def enter():
    global BackGround_Image, Push_Spacebar_image
    open_canvas()
    BackGround_Image = load_image('resouce/title.png')
    Push_Spacebar_image = load_image('resouce/space.png')
    game_framework.reset_time()


def exit():
    global BackGround_Image, Push_Spacebar_image

    del (BackGround_Image, Push_Spacebar_image)
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
            elif (event.type, event.key)==(SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(main_state)




def update(frame_time):
    pass




def draw(frame_time):
    global BackGround_Image, Push_Spacebar_image
    clear_canvas()
    BackGround_Image.draw(400, 300)
    Push_Spacebar_image.draw (400, 100)
    update_canvas()






