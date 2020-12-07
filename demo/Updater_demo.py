# from @cigar666

"""
除了demo_01都是些以前零零散散写的updater的相关代码，都是很短的场景，主要用来熟悉updater的相关操作
应该还有好些没整理上去，有空再弄了
"""

from manimlib.imports import *
from manim_sandbox.Logo.Logo import *

# demo_01
class Logo_bounce_around(Scene):

    def construct(self):

        logo = Logo(size=4., plot_depth=-1).shift(UP)#.set_opacity(0.12)
        self.logo_velocity = (RIGHT * 2 + UP) * 2e-2
        self.rotate_speed = 2.5 * DEGREES

        def update_logo(l, dt):
            l.shift(self.logo_velocity)
            l.rotate(self.rotate_speed)
            if abs(l.get_center()[1]) > (FRAME_HEIGHT - l.get_height())/2:
                self.logo_velocity *= DR # or we can use self.logo_velocity[1] *= -1
                self.rotate_speed *= -1
            if abs(l.get_center()[0]) > (FRAME_WIDTH - l.get_width())/2:
                self.logo_velocity *= UL # or we can use self.logo_velocity[0] *= -1
                self.rotate_speed *= -1

        logo.add_updater(update_logo)
        self.add(logo)

        # self.wait(1)
        # self.play(Write(TexMobject('xgnb!!!').scale(2.5)), run_time=2)

        self.wait(25)

# demo_02

class Draw_Ellipse(Scene):

    def construct(self):

        s = 0.8 # scale_factor
        F1 = LEFT * 4 * s
        F2 = RIGHT * 4 * s
        P = UP * 3 * s

        dot_F1 = Dot(F1, color=RED).scale(1.5)
        dot_F2 = Dot(F2, color=RED).scale(1.5)
        dot_P = Dot(P, color=PINK).scale(1.5)

        F1P = Line(F1, P, color=BLUE)
        F2P = Line(F2, P, color=BLUE)

        text_F1 = TexMobject('F_{1}', color=RED).next_to(F1, DOWN * 0.8)
        text_F2 = TexMobject('F_{2}', color=RED).next_to(F2, DOWN * 0.8)

        theta = ValueTracker()
        ellipse = VGroup()
        def get_P(theta):
            return (5 * RIGHT * np.cos(theta + PI/2) + 3 * UP * np.sin(theta + PI/2)) * s

        self.add(text_F1, text_F2, F1P, F2P, ellipse, dot_F1, dot_F2, dot_P)
        self.wait()

        dot_P.add_updater(lambda d: d.move_to(get_P(theta.get_value())))
        F1P.add_updater(lambda l: l.put_start_and_end_on(F1, get_P(theta.get_value())))
        F2P.add_updater(lambda l: l.put_start_and_end_on(F2, get_P(theta.get_value())))

        dt = 1/self.camera.frame_rate
        p_old = dot_P.get_center()

        # 这里使用短直线来画椭圆，每过一帧更新动点位置以及其他随之而变的物体
        for i in range(360):
            p_new = dot_P.get_center()
            ellipse.add(Line(p_old, p_new, stroke_width=3, color=PINK))
            p_old = p_new
            theta.increment_value(2 * DEGREES) # 这里每次theta加2°，所以会转两周
            self.wait(dt)

        self.wait(2)

# demo_03

class Show_Coords_of_MovingPoint(Scene):

    def construct(self):
        np = NumberPlane()
        self.play(ShowCreation(np))

        p = Dot(RIGHT * 3, color=GREEN)
        value_x = DecimalNumber(p.get_center()[0], color=GREEN, num_decimal_places=2).scale(0.8)
        value_y = DecimalNumber(p.get_center()[1], color=GREEN, num_decimal_places=2).scale(0.8)
        text = TexMobject('(', '-', ',', '-', ')').scale(0.8)
        # coords_xy = VGroup(text[0:6:2], value_x.move_to(text[1]), value_y.move_to(text[3]))
        coords_xy = VGroup(text[0], value_x.move_to(text[1]), text[2], value_y.move_to(text[3]), text[4])

        def update_xy(c):
            for i in range(1, len(c)):
                c[i].next_to(c[i-1], RIGHT * 0.5).align_to(c[0], DOWN)
            c[0].shift(c[1].get_center()[1]-c[0].get_center()[1])
            c[-1].shift(c[1].get_center()[1]-c[0].get_center()[1])
            c.next_to(p, DOWN * 0.2)

        value_x.add_updater(lambda x: x.set_value(p.get_center()[0]))
        value_y.add_updater(lambda y: y.set_value(p.get_center()[1]))
        coords_xy.add_updater(update_xy)

        self.play(ShowCreation(p))
        self.wait(0.5)
        self.play(ShowCreation(coords_xy))

        self.wait()

        self.play(Rotating(p, radians=TAU, about_point=ORIGIN), run_time=10)

        self.wait(4)

#demo_04

class Intro_lnX(GraphScene):

    CONFIG = {
        'rects_color': [PINK, ORANGE],
        "x_min": 0,
        "x_max": 4,
        "x_axis_width": 4 * 2.5,
        "x_tick_frequency": 1,
        "x_labeled_nums": None,
        "x_axis_label": "$x$",
        "y_min": 0,
        "y_max": 2.5,
        "y_axis_height": 2.5 * 2.5,
        "y_tick_frequency": 1,
        "y_labeled_nums": None,
        "y_axis_label": "$y$",
        "axes_color": WHITE,
        "graph_origin": 3.25 * DOWN + LEFT * 5.5,

        'curve_points_num': 100,
    }

    def construct(self):

        self.setup_axes(animate=True)

        func_graph = self.get_graph(self.func, x_min=0.4, x_max=3.75)
        func_graph.set_color(BLUE)
        fx = self.get_graph_label(func_graph, label="f(x)=\\frac{1}{x}", color=BLUE).scale(1.1).move_to(self.coords_to_point(1.2, 2))

        self.play(ShowCreation(func_graph))
        self.play(Write(fx))

        init_x = 2.5
        p1 = self.coords_to_point(1, 0)
        p2 = self.coords_to_point(init_x, 0)

        dot_1 = Dot(p1, color=YELLOW)
        dot_2 = Dot(p2, color=GREEN)
        dot_e = Dot(self.coords_to_point(np.e, 0), color=PINK)

        tex_1 = TexMobject('1', color=YELLOW).scale(0.9).next_to(dot_1, DOWN * 0.25)
        tex_2 = TexMobject('x', color=GREEN).scale(1).next_to(dot_2, DOWN * 0.3)
        tex_e = TexMobject('e', color=PINK).next_to(dot_e, UP * 0.3)

        line_1 = DashedLine(p1, self.coords_to_point(1, self.func(1)), color=YELLOW)
        line_2 = DashedLine(p2, self.coords_to_point(init_x, self.func(init_x)), color=GREEN)

        area = self.create_area()

        text_x = TexMobject('x', '=').set_color_by_tex_to_color_map({'x': GREEN}).to_corner(LEFT * 18 + UP * 1.5)
        text_area = TexMobject('A', '(', 'x', ')', '=').set_color_by_tex_to_color_map({'A': BLUE, 'x': GREEN}).to_corner(LEFT * 18 + UP * 2.75)
        text_lnX = TexMobject('ln', '(', 'x', ')', '=').set_color_by_tex_to_color_map({'ln': PINK, 'x': GREEN}).to_corner(LEFT * 18 + UP * 4.25)

        value_x = DecimalNumber(self.point_to_coords(dot_2.get_center())[0], color=GREEN, num_decimal_places=6).next_to(text_x, RIGHT * 0.5)
        value_area = DecimalNumber(np.log(self.point_to_coords(dot_2.get_center())[0]), color=GREEN, num_decimal_places=3).next_to(text_area, RIGHT * 0.5)
        value_lnX = DecimalNumber(np.log(self.point_to_coords(dot_2.get_center())[0]), color=GREEN, num_decimal_places=3).next_to(text_lnX, RIGHT * 0.5)

        ## updaters
        def update_line_2(line):
            x_new = self.point_to_coords(dot_2.get_center())[0]
            line.put_start_and_end_on(dot_2.get_center(), self.coords_to_point(x_new, self.func(x_new)))

        tex_2.add_updater(lambda t: t.next_to(dot_2, DOWN * 0.3))
        line_2.add_updater(update_line_2)
        area.add_updater(lambda a: a.become(self.create_area(1, self.point_to_coords(dot_2.get_center())[0])))
        value_x.add_updater(lambda v: v.set_value(self.point_to_coords(dot_2.get_center())[0]))
        value_area.add_updater(lambda v: v.set_value(np.log(self.point_to_coords(dot_2.get_center())[0])))
        value_lnX.add_updater(lambda v: v.set_value(np.log(self.point_to_coords(dot_2.get_center())[0])))

        ## anim
        self.play(ShowCreation(dot_1), Write(tex_1))
        self.play(ShowCreation(line_1))
        self.wait(1)
        self.play(ShowCreation(dot_2), Write(tex_2))
        self.play(ShowCreation(line_2))
        self.wait(1)
        self.play(ShowCreation(area), run_time=1)
        self.wait(0.4)
        self.play(Write(text_x), ShowCreation(value_x))
        self.play(TransformFromCopy(area, text_area), run_time=1.5)
        self.play(ShowCreation(value_area))
        self.play(Write(text_lnX), ShowCreation(value_lnX))

        # move x
        self.play(ApplyMethod(dot_2.shift, RIGHT * 2.5), run_time=3)
        self.wait(0.5)
        self.play(ApplyMethod(dot_2.shift, LEFT * 2.5 * 2), run_time=4)
        self.wait(1)
        self.play(ShowCreation(dot_e), Write(tex_e))
        self.wait(0.6)
        self.play(ApplyMethod(dot_2.move_to, self.coords_to_point(np.e, 0)), run_time=3)

        self.wait()
        conclusion = TexMobject('\\therefore\\, ', 'A' , '(', 'x', ')', '=', 'ln', '(', 'x', ')',)
        conclusion.set_color_by_tex_to_color_map({'A': BLUE, 'ln': PINK, 'x': GREEN})
        conclusion.to_corner(LEFT * 18 + UP * 5.75)

        self.play(Write(conclusion), run_time=2)

        self.wait(4)

    @staticmethod
    def func(x):
        return 1/x

    def create_area(self, x0=1, x1=2.5):

        point_0 = self.coords_to_point(x0, 0)
        point_1 = self.coords_to_point(x1, 0)

        x_arr = np.linspace(x0, x1, self.curve_points_num)
        y_arr = self.func(x_arr)
        curve_vertices = [self.coords_to_point(x_arr[i], y_arr[i]) for i in range(self.curve_points_num)]
        area = Polygon(point_0, *curve_vertices, point_1, color=BLUE, stroke_width=2.5, fill_color=BLUE, fill_opacity=0.5)
        return area

class Endocycloid(Scene):

    def construct(self):

        R, r = 3.2, 3.2 * 0.6
        big_circle = Circle(radius=R, color=BLUE, stroke_width=8)
        small_circle = Circle(radius=r, color=YELLOW, stroke_width=8)
        dot = Dot(color=RED).scale(1.6).shift(r * LEFT)
        w = ValueTracker(0.)

        def update_rotating(rg, dt):
            rg.rotate(w.get_value(), about_point=ORIGIN)
            rg.rotate(-R/r * w.get_value(), about_point=rg[0].get_center())

        rotate_group = VGroup(small_circle, dot, plot_depth=2).shift((R - r) * RIGHT).add_updater(update_rotating)
        path = TracedPath(dot.get_center, stroke_color=RED, stroke_width=5, min_distance_to_new_point=0.02)
        self.add(big_circle, rotate_group, path)
        self.wait(1)
        self.play(w.set_value, 2.5 * DEGREES, run_time=4)
        self.wait(16)








# TODO 有空继续写一些
