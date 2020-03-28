from manimlib.imports import *
from manim_sandbox.utils.imports import *

class Dashed_Circle(VGroup):

    CONFIG = {
        'arc_ratio': 0.6,
        'arc_num': 36,
        'arc_config':{
            'color': WHITE,
            'stroke_width': 2.5,
        },
    }

    def __init__(self, radius=1, center=ORIGIN, **kwargs):
        VGroup.__init__(self, **kwargs)
        theta = TAU/self.arc_num
        for i in range(self.arc_num):
            arc_i = Arc(radius=radius, angle=theta * self.arc_ratio, **self.arc_config)
            arc_i.rotate(theta * i, about_point=ORIGIN)
            self.add(arc_i)
        self.move_to(center)

class Gear_envelope_curve(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        r = 2
        gear = Gear_outline(pitch_circle_radius=2, tooth_hight=0.36, tooth_num=17, color=PINK)
        gear_02 = Gear_outline(pitch_circle_radius=2, tooth_hight=0.36, tooth_num=17, color=RED,
                               arc_segments=4, curve_segments=5, plot_depth=2).shift(2 * r * RIGHT)
        dot_center = Dot(color=RED)

        w = 1
        g_group = VGroup()
        def rotate_gear_01(g, dt):
            g.rotate(w * DEGREES, about_point=ORIGIN)
            g.rotate(w * DEGREES, about_point=g.get_center())

        def rotate_gear(g, dt):
            g.rotate(w * DEGREES, about_point=ORIGIN)
            g.rotate(w * DEGREES, about_point=g.get_center())
            g_group.add(g.copy().remove_updater(rotate_gear).set_stroke(color=ORANGE, width=1))
            g_n = len(g_group)
            max_num = 360 + 10
            if g_n < max_num:
                for i in range(g_n):
                    g_group[i].set_stroke(opacity=((i+1)/g_n))
            else:
                g_group.remove(g_group[0])
                for i in range(g_n-1):
                    g_group[i].set_stroke(opacity=((i+1)/g_n))

        self.play(FadeIn(dot_center), ShowCreation(gear), run_time=1.5)
        self.play(ShowCreation(gear_02), run_time=1.5)
        self.wait()
        gear_02.add_updater(rotate_gear_01)
        self.wait(6)
        self.add(g_group)
        gear_02.remove_updater(rotate_gear_01)
        gear_02.add_updater(rotate_gear)
        self.play(FadeOut(gear), run_time=4)
        self.wait(12)
