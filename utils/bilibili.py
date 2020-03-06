# from @鹤翔万里

from manimlib.imports import *

class TripleScene(Scene):
    CONFIG = {
        "good_file": "good",
        "coin_file": "coin",
        "favo_file": "favo",
    }
    def construct(self):
        self.get_svg()
        good = self.good
        coin = self.coin
        favo = self.favo
        self.play(
            FadeInFromPoint(good, good.get_center()),
            FadeInFromPoint(coin, coin.get_center()),
            FadeInFromPoint(favo, favo.get_center())
        )
        self.wait(0.4)
        circle_coin = Circle().scale(0.7).move_to(coin).set_stroke(PINK, 6)
        circle_favo = Circle().scale(0.7).move_to(favo).set_stroke(PINK, 6)
        self.play(
            good.set_color, LIGHT_PINK,
            ShowCreation(circle_coin),
            ShowCreation(circle_favo),
            run_time=1.5
        )
        self.play(
            FadeOut(circle_coin),
            FadeOut(circle_favo),
            Flash(coin.get_center(), color=PINK, line_length=0.7, flash_radius=1.5),
            Flash(favo.get_center(), color=PINK, line_length=0.7, flash_radius=1.5),
            Flash(good.get_center(), color=PINK, line_length=0.7, flash_radius=1.5),
            coin.set_color, LIGHT_PINK,
            favo.set_color, LIGHT_PINK,
            run_time=0.3
        )
        self.wait(2)
        self.play(
            FadeOut(good),
            FadeOut(coin),
            FadeOut(favo),
            run_time=0.8
        )
        self.wait()

    def get_svg(self):
        self.good = SVGMobject(self.good_file).set_height(1).move_to(LEFT*2.5+DOWN*2.7)
        self.coin = SVGMobject(self.coin_file).set_height(1).move_to(DOWN*2.7)
        self.favo = SVGMobject(self.favo_file).set_height(1).move_to(RIGHT*2.5+DOWN*2.7)
