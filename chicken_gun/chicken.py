import random
import gameover_state
from pico2d import *

class Chicken:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    hurt_sound = None
    bullet_shot_sound = None
    image = None
    LEFT_FLYING, RIGHT_FLYING, STAND = 0, 1, 2
    BULLET_LEVEL01, BULLET_LEVEL02 = 0, 1
    def __init__(self):
        self.x, self.y = 0, 350
        self.life_time = 0.0
        self.flying_dir = 0
        self.jump_dir = 0
        self.jump_state = False
        self.fall_speed = -200
        self.life = 3
        self.state = self.STAND
        self.bullet_state = self.BULLET_LEVEL01
        if Chicken.image == None:
            Chicken.image = load_image('resouce/image/chicken_image.png')
        if Chicken.bullet_shot_sound == None:
            Chicken.bullet_shot_sound = load_wav('resouce/sound/bullet_shot_sound.wav')
            Chicken.bullet_shot_sound.set_volume(32)


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance_x = Chicken.RUN_SPEED_PPS * frame_time
        distance_y = Chicken.RUN_SPEED_PPS * frame_time
        height = self.fall_speed * frame_time

        self.x += (self.flying_dir * distance_x)

        self.y += (height + self.jump_dir*distance_y)

        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)

        if self.y < 1:
            self.life-=1
            self.y = 500





    def draw(self):
        self.image.draw(self.x, self.y)
        #Chicken.font.draw(self.x - 40, self.y + 50, 'Score : %d' % self.score, (0, 0, 0))  help

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if self.state in (self.STAND,self.RIGHT_FLYING):
                self.state = self.LEFT_FLYING
                self.flying_dir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            if self.state in (self.STAND, self.LEFT_FLYING):
                self.state = self.RIGHT_FLYING
                self.flying_dir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            if self.state in (self.LEFT_FLYING,):
                self.state = self.STAND
                self.flying_dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_d):
            if self.state in (self.RIGHT_FLYING,):
                self.state = self.STAND
                self.flying_dir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state in (self.STAND, self.LEFT_FLYING, self.RIGHT_FLYING):
                self.jump_dir = 1.5
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            if self.state in (self.STAND, self.LEFT_FLYING, self.RIGHT_FLYING):
                self.jump_dir = 0

    def shot_sound(self):
        self.bullet_shot_sound.play()

