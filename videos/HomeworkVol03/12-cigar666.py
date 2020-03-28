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

class Envelope_curve(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        R = 3
        r = 0.6

        circle_0 = Circle(radius=R, color=RED)
        circle_1 = Circle(radius=r, color=ORANGE).rotate(PI).shift((r+R) * RIGHT)
        circle_2 = Circle(radius=1.6, color=PINK, stroke_width=2.5)
        dot_2 = Dot(color=PINK)

        curve_1 = VGroup()
        t = 0.64
        arrow = Arrow(buff=0, color=PINK).add_updater(lambda a: a.put_start_and_end_on(circle_1.get_center(), circle_1.get_center() + t * (circle_1.get_start() - circle_1.get_center())))

        # self.add(circle_0, circle_1, curve_1, arrow)
        self.play(ShowCreation(circle_0), run_time=1.2)
        self.play(ShowCreation(circle_1), run_time=1.2)
        self.play(FadeIn(arrow), run_time=1.)
        self.wait(0.5)
        self.add(curve_1)
        p_old = circle_1.get_center() + t * (circle_1.get_start() - circle_1.get_center())
        w = 1.

        for i in range(int(360/w)):
            circle_1.rotate(w * DEGREES, about_point=ORIGIN)
            circle_1.rotate(R/r * w * DEGREES)
            p_new = circle_1.get_center() + t * (circle_1.get_start() - circle_1.get_center())
            curve_1.add(Line(p_old, p_new, stroke_width=2, color=PINK))
            p_old = p_new
            self.wait(1/self.camera.frame_rate)
        self.wait()

        circle_group = VGroup()
        circle_2.move_to(curve_1[0].get_start())

        self.play(FadeIn(circle_2), FadeIn(dot_2), run_time=1.2)
        self.add(circle_group)

        for i in range(len(curve_1)):
            circle_2.move_to(curve_1[i].get_start())
            circle_group.add(circle_2.copy().set_stroke(width=1.25))
            dot_2.move_to(curve_1[i].get_start())
            self.wait(1/self.camera.frame_rate)

        self.wait(2)

class 骗三连(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        R = 3
        r = 0.6

        circle_0 = Circle(radius=R, color=RED)
        circle_1 = Circle(radius=r-0.05, color=ORANGE, stroke_width=10).rotate(PI).shift((r+R) * RIGHT)
        circle_2 = Circle(radius=1.6 - 0.12, color=PINK, stroke_width=24)
        dot_2 = Dot(color=PINK)

        path = 'my_manim_projects\\my_projects\\resource\\svg_files\\'
        good = SVGMobject(path + 'good.svg', color=PINK).set_width(0.7 * 2 * 1.6).move_to(circle_2)
        coin = SVGMobject(path + 'coin.svg', color=ORANGE, plot_depth=2).set_width(0.72 * 2 * r).rotate(-PI/2).move_to(circle_1)
        favo = SVGMobject(path + 'favo.svg', color=RED).set_width(0.75 * 2 * R).rotate(15 * DEGREES).move_to(circle_0)
        g_3 = VGroup(Circle(radius=R-0.25, color=RED, stroke_width=50), favo)

        g_1 = VGroup(circle_1, coin, plot_depth=2)

        curve_1 = VGroup()
        t = 0.64
        arrow = Arrow(buff=0, color=PINK).add_updater(lambda a: a.put_start_and_end_on(circle_1.get_center(), circle_1.get_center() + t * (circle_1.get_start() - circle_1.get_center())))

        # self.add(circle_0, circle_1, curve_1, arrow)
        self.play(ShowCreation(circle_0), run_time=1.2)
        self.play(FadeIn(g_1), run_time=1.2)
        self.play(FadeIn(arrow), run_time=1.)
        self.wait(0.5)
        self.add(curve_1)
        p_old = circle_1.get_center() + t * (circle_1.get_start() - circle_1.get_center())
        w = 1.

        for i in range(int(360/w)):
            g_1.rotate(w * DEGREES, about_point=ORIGIN)
            g_1.rotate(R/r * w * DEGREES, about_point=circle_1.get_center())
            p_new = circle_1.get_center() + t * (circle_1.get_start() - circle_1.get_center())
            curve_1.add(Line(p_old, p_new, stroke_width=2, color=PINK))
            p_old = p_new
            self.wait(1/self.camera.frame_rate)
        for i in range(int(135/w)):
            g_1.rotate(w * DEGREES, about_point=ORIGIN)
            g_1.rotate(R/r * w * DEGREES, about_point=circle_1.get_center())
            self.wait(1/self.camera.frame_rate)
        self.wait(0.8)

        circle_group = VGroup()
        g_2 = VGroup(circle_2, good, plot_depth=2)
        circle_2.move_to(curve_1[0].get_start())
        self.add(good)
        good.add_updater(lambda mob: mob.move_to(circle_2).shift(UR * 0.1))

        self.play(FadeIn(circle_2), run_time=1.2)
        self.add(circle_group)

        for i in range(len(curve_1)):
            circle_2.move_to(curve_1[i].get_start())
            circle_group.add(circle_2.copy().set_stroke(width=1.25))
            dot_2.move_to(curve_1[i].get_start())
            self.wait(1/self.camera.frame_rate)

        self.wait(0.5)
        self.play(FadeOut(circle_group), FadeIn(g_3), run_time=1.5)
        self.wait(0.2)

        r = 1.6
        c_01 = Circle(radius=r-0.1, stroke_width=20, color=PINK).move_to(LEFT * 2.4 * r)
        c_02 = Circle(radius=r-0.1, stroke_width=20, color=ORANGE).move_to(LEFT * 0)
        c_03 = Circle(radius=r-0.1, stroke_width=20, color=RED).move_to(RIGHT * 2.4 * r)

        good_ = SVGMobject(path + 'good.svg', color=PINK).set_width(0.7 * 2 * r).move_to(c_01).shift(UR * 0.06)
        coin_ = SVGMobject(path + 'coin.svg', color=ORANGE).set_height(0.7 * 2 * r).move_to(c_02)
        favo_ = SVGMobject(path + 'favo.svg', color=RED).set_height(0.7 * 2 * r).move_to(c_03).shift(UR * 0.05)

        group_1 = VGroup(c_01, good_)
        group_2 = VGroup(c_02, coin_)
        group_3 = VGroup(c_03, favo_)
        self.play(ReplacementTransform(g_2, group_1), ReplacementTransform(g_1, group_2),
                  ReplacementTransform(g_3, group_3), run_time=1.8)

        self.wait(2)
