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

class Frontcloud:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 15.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.x, self.y = 400, 400
        if Frontcloud.image == None:
            Frontcloud.image = load_image('resouce/image/front_cloud_image.png')

    def update(self, frame_time):
         self.x -= (Frontcloud.RUN_SPEED_PPS * frame_time)
         if self.x < -450:
             self.x += 1550

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

class Backcloud:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.x, self.y = 400, 550
        if Backcloud.image == None:
            Backcloud.image = load_image('resouce/image/back_cloud_image.png')

    def update(self, frame_time):
         self.x -= (Backcloud.RUN_SPEED_PPS * frame_time)
         if self.x < -450:
             self.x += 1550

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
