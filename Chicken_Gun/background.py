from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('resouce/image/background_image.png')
        self.bgm = load_music('resouce/sound/background_music.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()
        # fill here


    def draw(self):
        self.image.draw(400, 300)

    def draw_bb(self):
        #draw_rectangle(*self.get_bb())
        pass

    def __del__(self):
        del self.image
        del self.bgm