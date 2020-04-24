# from @鹤翔万里
# 使用-st导出带alpha通道的png图片

from manimlib.imports import *

class Nameplate4K_white(Scene):
    CONFIG = {
        "text_color": WHITE,
    }
    def construct(self):
        k = Text("4K", font="Orbitron", color=self.text_color).scale(2.6).shift(UP*0.6)
        rec1 = RoundedRectangle(height=4, width=7, color=GOLD, fill_opacity=0, stroke_width=30)
        rec2 = Rectangle(height=1.3, width=6.8, color=GOLD, fill_opacity=1).next_to(rec1.get_bottom(), UP, buff=0.1)
        recs = VGroup(rec1, rec2)
        rec1.set_sheen(0.4, RIGHT)
        rec2.set_sheen(0.4, RIGHT)
        ultraHD = VGroup(
            Text("ULTRA", font="Source Han Sans CN Light", color=BLACK).scale(1.2),
            Text("HD", font="Source Han Sans CN Bold", color=BLACK).scale(1.2)
        ).arrange(RIGHT, buff=0.5).move_to(rec2).shift(DOWN*0.1)

        self.add(recs, k, ultraHD)


class Nameplate4K_black(Nameplate4K_white):
    CONFIG = {
        "text_color": BLACK,
    }


class Nameplate4K_gold(Nameplate4K_white):
    CONFIG = {
        "text_color": GOLD,
    }