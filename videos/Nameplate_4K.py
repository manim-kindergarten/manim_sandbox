# from @鹤翔万里
# 使用-st导出带alpha通道的png图片

from manimlib.imports import *

class Nameplate4K_white(Scene):
    CONFIG = {
        "text_color": WHITE,
        "sheen_fac": 0.4,
        "text_sheen_dir": RIGHT,
    }
    def construct(self):
        k = Text("4K", font="Orbitron").scale(5.2).shift(UP*0.6).set_color(self.text_color).set_sheen_direction(self.text_sheen_dir)
        rec1 = RoundedRectangle(height=4, width=7, color=GOLD, fill_opacity=0, stroke_width=30)
        rec2 = Rectangle(height=1.3, width=6.8, color=GOLD, fill_opacity=1).next_to(rec1.get_bottom(), UP, buff=0.1)
        recs = SVGMobject("manim_sandbox/assets/svg_images/boundary.svg").set_height(4)
        light_color = hex_to_rgb(GOLD_E)
        light_color[:3] += self.sheen_fac
        clip_in_place(light_color, 0, 1)
        recs.set_color([GOLD_E, rgb_to_color(light_color), GOLD_E])
        ultraHD = VGroup(
            Text("ULTRA", font="Source Han Sans CN Light", color=BLACK).scale(2.4),
            Text("HD", font="Source Han Sans CN Bold", color=BLACK).scale(2.4)
        ).arrange(RIGHT, buff=0.5).move_to(rec2).shift(UP*0)

        self.add(recs, k, ultraHD)


class Nameplate4K_black(Nameplate4K_white):
    CONFIG = {
        "text_color": BLACK,
        "sheen_fac": 0.4,
    }


# 这个比较好看
class Nameplate4K_gold(Nameplate4K_white):
    CONFIG = {
        "text_color": [GOLD_E, GOLD_A],
        "sheen_fac": 0.4,
        "text_sheen_dir": UL,
    }