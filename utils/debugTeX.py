# from @鹤翔万里

from manimlib.imports import *
import itertools

def debugTeX(self, texm):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="Consolas").scale(0.3).set_color(PURPLE)
        tex_id.move_to(j)
        self.add(tex_id)