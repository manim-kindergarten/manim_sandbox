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
                    center.get_center(), center.get_center() + complex_to_R3(np.exp(sa.get_value() * 1j)), radius=0.5, color=PINK, below_180=True if theta.get_value()<PI else False)))

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

        tex_color = CodeLine('color=BLACK)').next_to(tex_angle, DOWN).align_to(tex_angle, LEFT).set_color_by_t2c(t2c_02)
        tex_color_02 = CodeLine('#~默认是白色', font='思源黑体 Bold', color=GREEN, size=0.25).next_to(tex_color, RIGHT, buff=0.15)

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
        self.play(theta.set_value, 360*DEGREES, rate_func=linear, run_time=2.4)
        self.wait(0.4)
        self.play(theta.set_value, 90*DEGREES, rate_func=linear, run_time=1.2)
        self.wait(0.8)
        self.play(Uncreate(surround), run_time=1.2)

        self.wait(2.5)
        # for mob in self.mobjects:
        #     mob.clear_updaters()
        # self.play(FadeOut(Group(*self.mobjects)), run_time=1.6)
        rect_bg = Rectangle(color=WHITE, fill_color=WHITE, fill_opacity=0).scale(20)
        self.play(rect_bg.set_opacity, 1, run_time=1.6)
        self.wait(1)

from my_manim_projects.my_utils.anim_effects import *

class Subclass_of_Arc(Scene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):

        captions = [
            "Arc类也有很多有用的子类",
            "比如用来表示环扇形的AnnularSector类",
            "用来表示两点加角度画弧的ArcBetweenPoints类",
            "通过添加add_tip方法建立的子类CurvedArrow和CurvedDoubleArrow",
            "以及通过修改Arc起始终止角度而建立的Circle类",
            "当然这些类的各个参数、方法及它们的子类，可以通过源代码继续深入学习"
            ]

        # pinkred = average_color(PINK, RED)
        t2c_02 = {'Arc': ORANGE, '环扇形': ORANGE, 'AnnularSector': ORANGE, "ArcBetweenPoints": ORANGE,
                  "add_tip": ORANGE,  "CurvedArrow": ORANGE, 'CurvedDoubleArrow': ORANGE, 'Circle': ORANGE, '源代码': BLUE_D}

        captions_mob = VGroup(
            *[
                CodeLine(cap, font='思源黑体 Bold', size=0.32).to_edge(DOWN * 1.2).set_color_by_t2c(t2c_02)
                for cap in captions
            ]
        )

        arc = Arc(color=BLUE, plot_depth=2).scale(1.4)

        circle = Circle(color=BLUE).scale(0.85)

        annular_sector = AnnularSector(color=BLUE).scale(0.8)

        arc_02 = ArcBetweenPoints(LEFT, RIGHT, color=BLUE).scale(1.25)

        curved_arrow = CurvedArrow(LEFT, RIGHT, color=BLUE).scale(1.25)

        curved_double_arrow = CurvedDoubleArrow(LEFT, RIGHT, color=BLUE).scale(1.25)

        r_round = 0.16
        tex_arc = CodeLine('Arc()', size=0.3).next_to(arc, DOWN * 0.6)
        sr_a = SurroundingRectangle(VGroup(tex_arc, arc), color=GRAY).scale(1.1).round_corners(r_round)
        group_a = VGroup(tex_arc, arc, sr_a)

        tex_circle = CodeLine('Circle()', size=0.3).next_to(circle, DOWN * 0.6)
        sr_c = SurroundingRectangle(VGroup(tex_circle, circle), color=GRAY).scale([1.08, 1.05, 1]).round_corners(r_round)
        group_c = VGroup(tex_circle, circle, sr_c)

        tex_as = CodeLine('AnnularSector()', size=0.25).next_to(annular_sector, DOWN * 0.6)
        sr_as = SurroundingRectangle(VGroup(tex_as, annular_sector), color=GRAY).scale(1.08).round_corners(r_round)
        group_as = VGroup(tex_as, annular_sector, sr_as)

        tex_arc_02 = CodeLine('ArcBetweenPoints(p1, p2, angle)', size=0.22).next_to(arc_02, DOWN * 0.6)
        sr_a2 = SurroundingRectangle(VGroup(tex_arc_02, arc_02), color=GRAY).scale(1.08).round_corners(r_round)
        group_a2 = VGroup(tex_arc_02, arc_02, sr_a2).scale(1.05)

        tex_curved_arrow = CodeLine('CurvedArrow(p1, p2, angle)', size=0.24).next_to(curved_arrow, DOWN * 0.6)
        sr_ca = SurroundingRectangle(VGroup(tex_curved_arrow, curved_arrow), color=GRAY).scale(1.08).round_corners(r_round)
        group_ca = VGroup(tex_curved_arrow, curved_arrow, sr_ca)

        tex_curved_double_arrow = CodeLine('CurvedDoubleArrow(p1, p2, angle)', size=0.21).next_to(curved_double_arrow, DOWN * 0.6)
        sr_cda = SurroundingRectangle(VGroup(tex_curved_double_arrow, curved_double_arrow), color=GRAY).scale(1.08).round_corners(r_round)
        group_cda = VGroup(tex_curved_double_arrow, curved_double_arrow, sr_cda)

        dots_01 = CodeLine('...', size=0.5)
        sr_d_01 = SurroundingRectangle(dots_01, color=GRAY).scale([1.6, 2, 1])
        sr_d_01.round_corners(sr_d_01.get_height()/2.001)
        group_d1 = VGroup(sr_d_01, dots_01)
        dots_02 = CodeLine('...', size=0.5)
        sr_d_02 = SurroundingRectangle(dots_02, color=GRAY).scale([1.6, 2, 1])
        sr_d_02.round_corners(sr_d_02.get_height()/2.001)
        group_d2 = VGroup(sr_d_02, dots_02)

        # tex_circle_subclass = CodeLine('')

        group_a.move_to(LEFT* 5.4 + UP * 0.5)

        group_a2.next_to(group_a, RIGHT, buff=0.8)
        group_as.next_to(group_a2, UP).align_to(group_a2, LEFT)
        group_c.next_to(group_a2, DOWN).align_to(group_a2, LEFT)

        group_d1.next_to(group_as, RIGHT, buff=0.8)
        group_d2.next_to(group_c, RIGHT, buff=0.8)

        group_ca.set_width(group_cda.get_width()).next_to(group_a2, RIGHT, buff=0.8).shift(UP * 0.9)
        group_cda.next_to(group_ca, DOWN).align_to(group_ca, LEFT)

        ##
        line_01 = self.link(group_a, group_as, color=GRAY)
        line_02 = self.link(group_a, group_a2, color=GRAY)
        line_03 = self.link(group_a, group_c, color=GRAY)

        line_04 = self.link(group_a2, group_ca, color=GRAY)
        line_05 = self.link(group_a2, group_cda, color=GRAY)

        line_06 = self.link(group_as, group_d1, color=GRAY)
        line_07 = self.link(group_c, group_d2, color=GRAY)

        # line_group = VGroup(line_01, line_02, line_03, line_04, line_05, line_06, line_07)

        # self.add(group_a, group_c, group_a2, group_as, group_ca, group_cda, line_group)

        self.wait(0.5)
        self.play(WriteRandom(captions_mob[0]), run_time=1.5)
        self.wait(0.3)
        self.play(FadeInFromLarge(group_a), run_time=1.5)
        # self.play(WiggleOutThenIn(group_a[1], scale_value=1.15, rotation_angle=0.02 * TAU), run_time=1.2)
        self.wait(1.6)

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]), run_time=1.)
        self.wait(0.4)
        self.play(FadeInFromLarge(group_as), run_time=1.2)
        self.play(ShowCreation(line_01), run_time=0.6)
        self.play(WiggleOutThenIn(group_as[1], scale_value=1.15, rotation_angle=0.02 * TAU), run_time=1.2)
        self.wait(1.8)

        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]), run_time=1.)
        self.wait(0.4)
        self.play(FadeInFromLarge(group_a2), run_time=1.2)
        self.play(ShowCreation(line_02), run_time=0.6)
        self.play(WiggleOutThenIn(group_a2[1], scale_value=1.15, rotation_angle=0.02 * TAU), run_time=1.2)
        self.wait(1.8)

        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]), run_time=1.)
        self.wait(0.4)
        self.play(FadeInFromLarge(group_ca), run_time=1.2)
        self.play(ShowCreation(line_04), run_time=0.6)
        self.play(WiggleOutThenIn(group_ca[1], scale_value=1.15, rotation_angle=0.02 * TAU), run_time=1.2)
        self.wait(0.5)

        self.play(FadeInFromLarge(group_cda), run_time=1.2)
        self.play(ShowCreation(line_05), run_time=0.6)
        self.play(WiggleOutThenIn(group_cda[1], scale_value=1.15, rotation_angle=0.02 * TAU), run_time=1.2)
        self.wait(1.8)

        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]), run_time=1.)
        self.wait(0.4)
        self.play(FadeInFromLarge(group_c), run_time=1.2)
        self.play(ShowCreation(line_03), run_time=0.6)
        self.play(WiggleOutThenIn(group_c[1], scale_value=1.15, rotation_angle=0.025 * TAU), run_time=1.2)
        self.wait(1.8)

        self.play(ReplacementTransform(captions_mob[4], captions_mob[5]), run_time=1.)
        self.wait(0.2)

        self.play(ShowCreation(line_06), run_time=0.5)
        self.play(ShowCreation(group_d1), run_time=0.8)
        self.wait(0.2)
        self.play(ShowCreation(line_07), run_time=0.5)
        self.play(ShowCreation(group_d2), run_time=0.8)
        self.wait(4)

    @staticmethod
    def link(mob_a, mob_b, **kwargs):
        return Line(mob_a.get_right(), mob_b.get_left(), **kwargs)

class Staff(Scene):
    CONFIG = {
        "font": "Orbitron",
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        title = Text("制作人员", font="庞门正道标题体", color=RED_D, size=0.75).to_edge(UP)
        line = Line(LEFT_SIDE, RIGHT_SIDE, color=RED_D).next_to(title, DOWN)
        title.add(line)
        staff = [
            ["Ⅰ. Line+arrow", " ", "@widcardw"],
            ["Ⅱ. Arc", " ", "@cigar666"],
            ["Ⅲ. Circle+Dot+Ellipse", " ", "@深蓝初衷"],
            ["Ⅳ. Annulus+AnnulusScetor+Scetor", " ", "@Shy_Vector"],
            ["Ⅴ. Polygon+RegularPolygon+Triangle", " ", "@二茂铁Fe"],
            ["Ⅵ. Rectangle+Square+RoundedRectangle", " ", "@_emat_"],
            ["Ⅶ. VGroup", " ", "@鹤翔万里"],
        ]
        staff_mob = VGroup(*[VGroup() for _ in range(2)])
        for i in range(7):
            staff_mob[0].add(Text(staff[i][0], font="庞门正道标题体", size=0.36, color=DARK_GRAY))
            staff_mob[1].add(Text(staff[i][2], font="思源黑体 Bold", size=0.3, color=BLUE_D))
        for i in range(2):
            staff_mob[i].arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        for i in range(7):
            staff_mob[1][i].align_to(staff_mob[0][i], DOWN)
        staff_mob.arrange(RIGHT)
        staff_mob[0].shift(LEFT * 0.5 + DOWN * 0.4)
        staff_mob[1].shift(RIGHT * 0.5 + DOWN * 0.4)

        self.wait()
        self.play(Write(title))
        self.wait()
        for i in range(7):
            self.play(
                Write(VGroup(staff_mob[0][i], staff_mob[1][i])),
                run_time=0.5
            )
            self.wait(0.1)

        self.wait(4.5)
        self.play(FadeOut(VGroup(*self.mobjects)), run_time=1.6)
        self.wait()

class Opening_Scene(Scene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):

        t2c = {"manim-kindergarten": average_color(PINK, RED), "manim": average_color(PINK, RED),
               "几何类": ORANGE}
        text_color = DARK_GRAY

        font = "庞门正道标题体"
        text_1 = Text("大家好!", font=font, color=text_color, size=1, t2c=t2c).to_edge(UP * 2, buff=1)
        text_2 = Text("欢迎来到manim视频教程", font=font,
                      color=text_color, size=1, t2c=t2c).to_edge(UP * 3.2, buff=1)
        text_3 = Text("这一期我们将学习manim中", font=font, color=text_color, size=1, t2c=t2c).to_edge(UP * 1.8, buff=1)
        text_4 = Text("常见的几何类", font=font, color=text_color, size=1, t2c=t2c).to_edge(UP * 3., buff=1)
        text_34, text_12 = VGroup(text_3, text_4), VGroup(text_1, text_2)

        # self.add(picture)
        self.wait(0.5)
        self.play(Write(text_1))
        self.wait(0.5)
        self.play(WriteRandom(text_2), run_time=1.5)
        self.wait(1.8)
        self.play(ReplacementTransform(text_12, text_34), run_time=1.2)
        self.wait(4)
        self.play(FadeOutRandom(text_3),
                  FadeOutRandom(text_4), run_time=1.8)
        self.wait(1)

from manim_sandbox.utils.imports import *
class Ending(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }
    def construct(self):

        text_01 = Text("感 谢 观 看", font='庞门正道标题体', color=BLUE_D, size=1.25)
        text_02 = Text('代码见~https://github.com/manim-kindergarten/manim_sandbox',
                       font='思源黑体 Bold', color=ORANGE, size=0.36, t2c={'~': WHITE}).next_to(text_01, DOWN * 1.2, buff=1)

        self.play(Write(text_01), run_time=2)
        self.wait(0.8)
        self.play(WriteRandom(text_02), run_time=2)

        self.wait(6)

class Progress_Bar(Scene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):

        chapters_dict={
            ' ': '0040',
            'Line+arrow': '0258',
            'Arc': '0459',
            'Circle+Dot+Ellipse': '0707',
            'Annulus+AnnulusScetor+Scetor': '0922',
            'Polygon': '1015',
            'Rectangle': '1312',
            'VGroup': '1526',
        }

        vpr = VideoProgressBar(methods_dict=chapters_dict, total_hight='1549')
        self.add(vpr)
        self.wait()

class 空降标记(Scene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):

        chapters_dict={
            'Line+arrow': '0040',
            'Arc': '0258',
            'Circle+Dot+Ellipse': '0459',
            'Annulus+AnnulusScetor': '0707',
            'Polygon': '0922',
            'Rectangle': '1015',
            'VGroup': '1312',
            ' ': '1526',
        }

        total_time = '1549'
        func_time = lambda t: int(t[0:2]) * 60 + int(t[2:])
        func_loc = lambda t: func_time(t)/func_time(total_time) * FRAME_WIDTH * RIGHT + FRAME_WIDTH * LEFT / 2
        p_list = [FRAME_WIDTH * LEFT / 2]
        for v in chapters_dict.values():
            p_list.append(func_loc(v))
        p_list.append(func_loc(total_time))

        colors = color_gradient([BLUE, PINK, RED, ORANGE, GREEN], len(chapters_dict)+1)

        lines = VGroup(*[Line(p_list[i], p_list[i+1]-0.02*RIGHT, color=colors[i], stroke_width=20) for i in range(len(chapters_dict)+1)])
        lines.to_edge(DOWN * 0.22, buff=1)
        texts = VGroup(*[Text(t, color=WHITE, font='Consolas', size=0.14) for t in chapters_dict.keys()], plot_depth=1)
        # texts[0].become(Text(' ', color=WHITE, font='思源黑体 CN Bold', size=0.15))
        # text = Text('空降', color=WHITE, font='庞门正道标题体', size=0.22).to_edge(DOWN * 0.132, buff=1).to_edge(LEFT, buff=0.125)
        # text[1].shift(RIGHT*0.03)
        # text[0].shift(LEFT*0.01)
        for i in range(len(chapters_dict)):
            texts[i].move_to(lines[i+1])

        self.add(lines, texts)
        self.wait(5)

