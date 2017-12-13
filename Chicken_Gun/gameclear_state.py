from pico2d import *
import main_state
import title_state
import game_framework
from ui import *
name = "GameclearState"

gameclear_image = None
gameclear_music = None


def enter():
    global gameclear_image, gameclear_music
    gameclear_image = load_image('resouce/image/gameclear_image.png')
    if gameclear_music == None:
        gameclear_music = load_music('resouce/sound/gameclear_music.mp3')
    gameclear_music.set_volume(20)
    gameclear_music.play()


def exit():
    global gameclear_image, gameclear_music

    del (gameclear_image)
    del (gameclear_music)


def update(frame_time):
    pass




def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def draw(frame_time):
    global gameclear_image
    clear_canvas()
    gameclear_image.draw(400, 300)
    main_state.ui.font_score.draw(320, 200, 'Score:%d' % main_state.ui.score, (0, 0, 0))
    update_canvas()