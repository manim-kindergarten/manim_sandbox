# from @鹤翔万里

from manimlib.imports import *

def debugTeX(self, texm, scale_factor=0.6, text_color=PURPLE):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="Consolas").scale(scale_factor).set_color(text_color)
        tex_id.move_to(j)
        self.add(tex_id)