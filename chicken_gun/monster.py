import random
import math
import main_state
from pico2d import *

blue_hat_monster_time = 0
red_plant_monster_time = 0
boss_monster_music_on = None
th = 0

class Blue_hat_monster:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 80.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    blue_hat_monster_image = None
    monster_hit_sound = None
    monster_death_sound = None

    def __init__(self):
        self.x, self.y = 800, random.randint(0, 600)
        if Blue_hat_monster.blue_hat_monster_image is None:
            Blue_hat_monster.blue_hat_monster_image = load_image('resouce/image/blue_hat_monster_image.png')

        if Blue_hat_monster.monster_death_sound == None:
            Blue_hat_monster.monster_death_sound = load_wav('resouce/sound/monster_death_sound.wav')
            Blue_hat_monster.monster_death_sound.set_volume(15)

    def update(self, frame_time):
        distance = Blue_hat_monster.RUN_SPEED_PPS * frame_time
        self.x -= distance



    def draw(self):
        self.blue_hat_monster_image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Red_plant_monster:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    red_plant_monster_image = None
    monster_hit_sound = None
    monster_death_sound = None

    def __init__(self):
        self.x, self.y = 800, random.randint(0, 600)
        self.life =3
        if Red_plant_monster.red_plant_monster_image is None:
            Red_plant_monster.red_plant_monster_image = load_image('resouce/image/red_plant_monster_image.png')
        if Red_plant_monster.monster_death_sound == None:
            Red_plant_monster.monster_death_sound = load_wav('resouce/sound/monster_death_sound.wav')
            Red_plant_monster.monster_death_sound.set_volume(15)

    def update(self, frame_time):
        distance = Red_plant_monster.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.red_plant_monster_image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Boss_monster:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    boss_monster_image = None
    boss_monster_music = None
    monster_death_sound = None

    def __init__(self):
        self.x, self.y = 1000, 300
        self.life = 20
        self.boss_monster_time = 0
        if Boss_monster.boss_monster_image is None:
            Boss_monster.boss_monster_image = load_image('resouce/image/boss_monster_image.png')
        if Boss_monster.boss_monster_music == None:
            Boss_monster.boss_monster_music = load_music('resouce/sound/boss_monster_music.mp3')
            Boss_monster.boss_monster_music.set_volume(15)
        if main_state.ui.score == 10:
            main_state.background.bgm.pause()
            Boss_monster.boss_monster_music.repeat_play()


    def update(self, frame_time):
        global th, boss_monster_music_on, boss_moster_dead

        if main_state.ui.score >= 200:
            distance = Boss_monster.RUN_SPEED_PPS * frame_time
            self.boss_monster_time += frame_time
            if self.life > 0 and self.x < 700 and boss_monster_music_on == None:
                boss_monster_music_on = True

            if self.life > 0 and boss_monster_music_on == True:
                boss_monster_music_on = False
                main_state.background.bgm.stop()
                Boss_monster.boss_monster_music.repeat_play()

            if self.x >= 600:
                self.x -= distance

            if self.x < 600 and self.boss_monster_time > 6:
                th += 1/2
                self.y = 300 + 150 * math.sin(math.radians(th))
            if self.life <= 0 and boss_monster_music_on == False:
                boss_monster_music_on = True
            if self.life <= 0 and boss_monster_music_on == True:
                print(boss_monster_music_on)
                boss_monster_music_on = None
                Boss_monster.boss_monster_music.stop()
                main_state.background.bgm.play()

    def draw(self):
        if main_state.ui.score >=200 and self.life > 0:
            self.boss_monster_image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 60, self.y - 80, self.x + 60, self.y + 80

    def draw_bb(self):
        if main_state.ui.score >= 200 and self.life > 0:
            draw_rectangle(*self.get_bb())