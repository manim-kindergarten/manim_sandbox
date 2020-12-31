from manimlib.imports import *
from manim_sandbox.utils.imports import *


class HappyNewYear(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": "#222222"
        }
    }
    def construct(self):
        line1 = Text(
            "self.play(ReplacementTransform(", 
            font="Consolas",
            t2s={"self": ITALIC},
            t2c={"self.": "#AFABB4", "play": "#75CB87", "(": WHITE, "ReplacementTransform": BLUE}
        ).to_edge(UP)
        line1[9].set_color("#E4C104")
        line1[30].set_color("#C768C3")
        line2 = VGroup(
            Text(
                "2020", font="DIN Black"
            ).scale(3),
            Text(",", font="Consolas", color="#AFABB4"),
            Text(
                "2021", font="DIN Black"
            ).scale(3),
        ).arrange(RIGHT, aligned_edge=DOWN)
        line2.next_to(line1[4], DOWN, aligned_edge=LEFT, buff=0.45)
        line3 = Text("), run_time=1, rate_func=smooth)", font="Consolas",
            t2c={",": "#AFABB4", "run_time": "#F18D50", "=": "#E95C84", "1": "#8A81D1", "rate_func": "#F18D50"}
        ).next_to(line2, DOWN, buff=0.45).align_to(line1, LEFT)
        line3[0].set_color("#C768C3")
        line3[-1].set_color("#E4C104")
        line4 = Text(
            "self.wait(31536000)",
            font="Consolas",
            color="#8A81D1",
            t2s={"self": ITALIC},
            t2c={"self.": "#AFABB4", "wait": "#75CB87", "(": "#E4C104", ")": "#E4C104"}
        ).next_to(line3, DOWN, aligned_edge=LEFT)

        for each in line2[0][1:]:
            line2[0][0].append_points(each.points)
            line2[0].remove(each)
        line2[0].set_sheen_direction(DR)
        line2[0].set_color([RED, BLUE])
        for each in line2[2][1:]:
            line2[2][0].append_points(each.points)
            line2[2].remove(each)
        line2[2].set_sheen_direction(DR)
        line2[2].set_color([BLUE, GREEN])

        code = VGroup(line1, line2, line3, line4).scale(1.3).center()
        self.add(code)

class WaterMark(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        logo = Logo(black_bg=False).set_height(2)
        text = VGroup(
            Text("Manim-Kindergarten", font="Orbitron", color=DARK_GRAY),
            Text("鹤翔万里", font="庞门正道标题体", color=BLACK, size=2.3)
        ).scale(1.2).arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(logo, buff=0.5)
        self.add(logo, text)
        VGroup(*self.mobjects).set_fill(color=WHITE, opacity=0.5).center()
