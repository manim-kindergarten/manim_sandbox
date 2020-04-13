from manimlib.imports import *
from manim_sandbox.utils.mobjects.Arc_group import *
from manim_sandbox.videos.HomeworkVol04.test_present_style import *

class Explain_Arc(Scene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):

        captions = [
            "Arc类用来绘制圆弧",
            "默认的Arc如图所示",
            "我们将缺省的默认参数填入，并看看修改后的效果",
            "arc_center用来控制Arc的圆心",
            "radius用来控制Arc的半径",
            "stroke_width用来控制Arc的线条粗细",
            "start_angle用来控制Arc的起始角度",
            "angle用来控制Arc的圆心角大小",

            ]

        # pinkred = average_color(PINK, RED)
        t2c_02 = {'Arc': RED, 'arc_center': ORANGE, 'radius': ORANGE, "stroke_width": ORANGE,
                  "start_angle": ORANGE,  "angle": ORANGE, 'color': ORANGE}

        captions_mob = VGroup(
            *[
                CodeLine(cap, font='思源黑体 Bold', size=0.32).to_edge(DOWN * 1.2).set_color_by_t2c(t2c_02)
                for cap in captions
            ]
        )

        axes = ThreeDAxes(
            color=BLACK,
            x_min=-FRAME_X_RADIUS, x_max=FRAME_X_RADIUS,
            y_min=-FRAME_Y_RADIUS, y_max=FRAME_Y_RADIUS,
            number_line_config={"color": BLACK}
        ).set_stroke(width=2)

        center = Dot(color=RED) # arc_center
        r = ValueTracker(1.) # radius
        sw = ValueTracker(4.) # stroke_width
        sa = ValueTracker(0*DEGREES) # start_angle
        theta = ValueTracker(90 * DEGREES) # angle

        arc = Arc(color=BLACK)
        arc.add_updater(lambda a: a.become(Arc(color=BLACK, arc_center=center.get_center(), radius=r.get_value(),
                                               start_angle=sa.get_value(), angle=theta.get_value(),
                                               stroke_width=sw.get_value())))
        p0 = ORIGIN
        arc_start_angle = Angle(p0+1, p0, p0-1).add_updater(lambda a: a.become(Angle(center.get_center() + complex_to_R3(np.exp(sa.get_value() * 1j)),
                                center.get_center(), center.get_center() + RIGHT, radius=0.5, color=ORANGE)))

        arc_angle = Angle(p0+1, p0, p0-1).add_updater(lambda a: a.become(Angle(center.get_center() + complex_to_R3(np.exp((sa.get_value() + theta.get_value()) * 1j)),
                    center.get_center(), center.get_center() + complex_to_R3(np.exp(sa.get_value() * 1j)), radius=0.5, color=PINK)))

        line_0 = DashedLine().add_updater(lambda l: l.become(DashedLine(center.get_center(), center.get_center() + r.get_value() * RIGHT * 1.6, color=BLUE_D)))
        line_1 = DashedLine().add_updater(lambda l: l.become(DashedLine(center.get_center(), center.get_center() + r.get_value() * complex_to_R3(np.exp(sa.get_value() * 1j)) * 1.6, color=BLUE_D)))
        line_2 = DashedLine().add_updater(lambda l: l.become(DashedLine(center.get_center(), center.get_center() + r.get_value() * complex_to_R3(np.exp((sa.get_value() + theta.get_value()) * 1j)) * 1.6, color=BLUE_D)))

        vect_r = Arrow().add_updater(lambda vect: vect.become(Arrow(center.get_center(), center.get_center() + complex_to_R3(r.get_value() * np.exp((sa.get_value() + theta.get_value()) / 2 * 1j)), color=ORANGE, buff=0)))

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=2)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        loc = UP * 2.9 + RIGHT * 2.

        tex_arc = CodeLine('arc=Arc()').move_to(loc).set_color_by_t2c(t2c_02)
        tex_add = CodeLine('self.add(arc)').next_to(tex_arc, DOWN).align_to(tex_arc, LEFT).set_color_by_t2c(t2c_02)

        tex_arc_01 = CodeLine('arc=Arc(').align_to(tex_arc, UL).set_color_by_t2c(t2c_02)
        tex_center = CodeLine('arc_center=ORIGIN').next_to(tex_arc_01, RIGHT, buff=0.08).set_color_by_t2c(t2c_02)
        tex_center_new = CodeLine('arc_center=').next_to(tex_arc_01, RIGHT, buff=0.08).set_color_by_t2c(t2c_02)
        left_value = CodeLine('xgnb').add_updater(lambda t: t.become(CodeLine('%.1f*LEFT,' % (-center.get_center()[0])).next_to(tex_center_new, RIGHT * 0.08, buff=1)))

        tex_r = CodeLine('radius=').next_to(tex_center, DOWN).align_to(tex_center, LEFT).set_color_by_t2c(t2c_02)
        r_value = CodeLine('xgnb').add_updater(lambda t: t.become(CodeLine('%.1f,' % r.get_value()).next_to(tex_r, RIGHT * 0.08, buff=1)))

        tex_sw = CodeLine('stroke_width=').next_to(tex_r, DOWN).align_to(tex_r, LEFT).set_color_by_t2c(t2c_02)
        sw_value = CodeLine('xgnb').add_updater(lambda t: t.become(CodeLine('%.1f,' % sw.get_value()).next_to(tex_sw, RIGHT * 0.08, buff=1)))

        tex_sa = CodeLine('start_angle=').next_to(tex_sw, DOWN).align_to(tex_sw, LEFT).set_color_by_t2c(t2c_02)
        sa_value = CodeLine('xgnb').add_updater(lambda t: t.become(CodeLine('%.f*DEGREES,' % (sa.get_value()/DEGREES)).next_to(tex_sa, RIGHT * 0.08, buff=1)))

        tex_angle = CodeLine('angle=').next_to(tex_sa, DOWN).align_to(tex_sa, LEFT).set_color_by_t2c(t2c_02)
        angle_value = CodeLine('xgnb').add_updater(lambda t: t.become(CodeLine('%.f*DEGREES,' % (theta.get_value()/DEGREES)).next_to(tex_angle, RIGHT * 0.08, buff=1)))

        tex_color = CodeLine('color=BLACK').next_to(tex_angle, DOWN).align_to(tex_angle, LEFT).set_color_by_t2c(t2c_02)
        tex_color_02 = CodeLine('# 默认是白色', font='思源黑体 Bold', color=GREEN, size=0.25).next_to(tex_color, RIGHT, buff=0.15)

        new_arc_tex = VGroup(tex_arc_01, tex_center, tex_r, r_value, tex_sw, sw_value,
                             tex_sa, sa_value, tex_angle, angle_value, tex_color, tex_color_02)

        self.wait(0.5)
        self.play(FadeIn(axes))
        self.play(Write(captions_mob[0]), run_time=1.5)
        self.wait(0.8)
        self.play(FadeInFromLarge(tex_bg), run_time=1.)
        self.wait(0.4)
        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]), run_time=1.2)
        self.wait(0.2)
        self.play(Write(tex_arc), run_time=0.8)
        self.wait(0.1)
        self.play(Write(tex_add))
        self.wait(0.2)
        self.play(ShowCreation(arc), run_time=0.5)
        self.wait(0.1)
        self.play(WiggleOutThenIn(arc), run_time=1.2)
        self.wait(1)
        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]), run_time=1.2)
        self.wait(0.5)
        self.play(ReplacementTransform(tex_arc, new_arc_tex), tex_add.shift, DOWN * new_arc_tex.get_height() + UP * 0.24, run_time=1.6)
        self.wait()

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]), run_time=1.2)
        self.wait(0.6)

        # change arc_center
        surround = SurroundingRectangle(left_value).add_updater(lambda s: s.become(SurroundingRectangle(left_value)))
        center_new = Dot(color=RED)
        self.play(TransformFromCopy(tex_center, center_new), run_time=1.2)
        self.add(center), self.remove(center_new)
        self.wait(0.4)
        self.remove(tex_center)
        self.add(tex_center_new, left_value)

        self.play(center.shift, LEFT * 4.5, ShowCreation(surround), run_time=1.5)
        self.wait(0.2)
        self.play(center.shift, RIGHT * 1.5, run_time=0.8)
        self.wait()
        self.play(Uncreate(surround), run_time=1.2)
        self.wait(0.5)

        # change radius
        surround = SurroundingRectangle(r_value).add_updater(lambda s: s.become(SurroundingRectangle(r_value)))
        center_new = Dot(color=RED)
        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]), run_time=1.2)
        self.wait(0.2)
        self.play(ShowCreation(surround))
        self.wait(0.2)
        vect_r_02 = vect_r.copy().clear_updaters().shift(LEFT * 3)
        self.play(TransformFromCopy(tex_r, vect_r_02))
        self.add(vect_r), self.remove(vect_r_02)
        self.wait(0.4)
        self.play(r.set_value, 3, rate_func=linear, run_time=1.6)
        self.wait(0.2)
        self.play(r.set_value, 2, rate_func=linear, run_time=1.)
        self.wait()
        self.play(Uncreate(surround), Uncreate(vect_r), run_time=1.2)

        self.wait(0.5)

        # change stroke_width
        surround = SurroundingRectangle(sw_value).add_updater(lambda s: s.become(SurroundingRectangle(sw_value)))
        center_new = Dot(color=RED)
        self.play(ReplacementTransform(captions_mob[4], captions_mob[5]), run_time=1.2)
        self.wait(0.2)
        self.play(ShowCreation(surround))
        self.wait(0.2)
        self.play(sw.set_value, 80, rate_func=linear, run_time=2)
        self.wait(0.2)
        self.play(sw.set_value, 1, rate_func=linear, run_time=2)
        self.wait(0.2)
        self.play(sw.set_value, 20, rate_func=linear, run_time=1.2)
        self.wait()
        self.play(Uncreate(surround), run_time=1.2)
        self.wait(0.5)

        # change start_angle
        surround = SurroundingRectangle(sa_value).add_updater(lambda s: s.become(SurroundingRectangle(sa_value)))
        center_new = Dot(color=RED)
        self.play(ReplacementTransform(captions_mob[5], captions_mob[6]), run_time=1.2)
        self.wait(0.4)
        self.play(ShowCreation(line_0), ShowCreation(line_1), run_time=1.2)
        self.wait(0.2)
        self.play(ShowCreation(surround))
        self.wait(0.2)
        self.add(arc_start_angle)
        self.play(sa.set_value, PI/3, rate_func=linear, run_time=1.)
        self.wait(0.4)
        self.play(sa.set_value, -PI/6, rate_func=linear, run_time=1.2)
        self.wait(0.2)
        self.play(sa.set_value, PI/4, rate_func=linear, run_time=1.2)
        self.wait()
        self.play(Uncreate(surround), run_time=1.2)

        self.wait(0.5)

        # change angle
        surround = SurroundingRectangle(angle_value).add_updater(lambda s: s.become(SurroundingRectangle(angle_value)))
        center_new = Dot(color=RED)
        self.play(ReplacementTransform(captions_mob[6], captions_mob[7]), run_time=1.2)
        self.wait(0.2)
        self.play(ShowCreation(surround))
        self.wait(0.2)
        self.play(ShowCreation(line_2), run_time=1.2)
        self.play(ShowCreation(arc_angle), run_time=1.2)
        self.wait(0.2)
        self.play(theta.set_value, 150*DEGREES, rate_func=linear, run_time=1.25)
        self.wait(0.25)
        self.play(theta.set_value, 30*DEGREES, rate_func=linear, run_time=1.5)
        self.wait(0.25)
        self.play(theta.set_value, 179.9*DEGREES, rate_func=linear, run_time=1.6)
        self.wait(0.08)
        self.play(theta.set_value, 90*DEGREES, rate_func=linear, run_time=1.2)
        self.wait(0.8)
        self.play(Uncreate(surround), run_time=1.2)

        self.wait(2)
        self.play(FadeOut(VGroup(*self.mobjects)), run_time=1.6)
        self.wait(1)


