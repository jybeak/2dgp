from pico2d import *
from chicken import *
import main_state
class Ui:
    image_life = None
    font_score = None
    font_life = None

    def __init__(self):
        self.score = 0
        if Ui.image_life == None:
            Ui.image_life = load_image('resouce/chicken_life.png')
        if Ui.font_score == None:
            Ui.font_score = load_font('resouce/ENCR10B.TTF', 25)
        if Ui.font_life == None:
            Ui.font_life = load_font('resouce/ENCR10B.TTF', 25)

    def draw(self):
        self.font_score.draw(40, 570, 'Score:%d' % self.score, (0, 0, 0))
        self.font_life.draw(190, 570, 'Life:', (0, 0, 0))
        if main_state.chicken.life == 3:
            self.image_life.clip_draw(0,0,126,75,330,570)
        elif main_state.chicken.life == 2:
            self.image_life.clip_draw(0, 0, 84, 75, 309, 570)
        elif main_state.chicken.life == 1:
            self.image_life.clip_draw(0, 0, 42, 75, 288, 570)
        else :
            pass