
"""
关于logo创意：

	1.  基础元素为M和K的负空间设计

	2.  白色部分创意来自弦图

	3.  整体图案本身可生成一个不错的分形

	4.  配色致敬3B1B（具体的蓝色和棕色还得再微调一下）

 logo主要创意由@GrakePCH提供，@GZTime、@cigar666、@鹤翔万里都提供了不少宝贵意见。目前设计工作还在继续完善，希望大家多提意见和建议

"""

from manimlib.imports import *

class Logo(VGroup):

    CONFIG = {
        'color_1': [WHITE, BLUE_B, BLUE_D],
        'color_2': [WHITE, '#C59978', '#8D5630'],

        # 'color_3': [average_color("#CCCCCC", BLUE_C), BLUE_C, BLUE_D],
        # 'color_4': [average_color("#CCCCCC", "#C59978"), '#C59978', '#8D5630'],

        'color_3': [average_color(WHITE, BLUE_C), BLUE_C, BLUE_D],
        'color_4': [average_color(WHITE, "#C59978"), '#C59978', '#8D5630'],

        'center': ORIGIN,
        'size': 2,
        'shift_out': ORIGIN,
        'black_bg': True,
        'add_bg_square': False,
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.create_logo()

    def create_logo(self):

        p1 = Polygon(ORIGIN, RIGHT, 2 * UP, stroke_width=0).set_fill(self.color_1[0], 1)
        p2 = Polygon(1.5 * RIGHT, 3 * UR, 3 * UP, stroke_width=0).set_fill(self.color_1[1], 1)
        p3 = Polygon(2 * RIGHT, 3 * RIGHT, 3 * RIGHT + 2 * UP, stroke_width=0).set_fill(self.color_1[2], 1)
        if not self.black_bg:
            p1.set_fill(self.color_3[0], 1), p2.set_fill(self.color_3[1], 1), p3.set_fill(self.color_3[2], 1)

        self.bg = Square(stroke_width=0, fill_color=BLACK if self.black_bg else WHITE, fill_opacity=1).set_height(self.size * 2.5)
        if self.add_bg_square:
            self.add(self.bg)

        self.part_ur = VGroup(p1, p2, p3).move_to([2.5, 1., 0] + self.shift_out)
        self.part_ul = self.part_ur.copy().rotate(PI / 2, about_point=ORIGIN)
        self.part_dl = self.part_ur.copy().rotate(PI, about_point=ORIGIN)
        self.part_dr = self.part_ur.copy().rotate(3 * PI / 2, about_point=ORIGIN)

        self.add(self.part_ur, self.part_ul, self.part_dl, self.part_dr)
        self.set_height(self.size).move_to(self.center)
        if self.black_bg:
            self.part_ur[0].set_fill(self.color_2[0], 1), self.part_ur[1].set_fill(self.color_2[1], 1), self.part_ur[2].set_fill(self.color_2[2], 1)
        else:
            self.part_ur[0].set_fill(self.color_4[0], 1), self.part_ur[1].set_fill(self.color_4[1], 1), self.part_ur[2].set_fill(self.color_4[2], 1)

        self.inner_triangles = VGroup(self.part_ur[0], self.part_ul[0], self.part_dl[0], self.part_dr[0])
        self.mid_triangles = VGroup(self.part_ur[1], self.part_ul[1], self.part_dl[1], self.part_dr[1])
        self.outer_triangles = VGroup(self.part_ur[2], self.part_ul[2], self.part_dl[2], self.part_dr[2])

class Logo_image(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': GRAY,
        }
    }

    def construct(self):

        logo_black_bg = Logo(size=4.5, add_bg_square=True).shift(LEFT * 3)

        logo_white_bg = Logo(size=4.5, black_bg=False, add_bg_square=True).shift(RIGHT * 3)

        self.add(logo_white_bg, logo_black_bg)

        self.wait(2)

class Logo_01(Scene):

    def construct(self):

        logo = Logo(size=3.2)

        square = VGroup(*[Polygon(ORIGIN, UR, UL), Polygon(ORIGIN, UL, DL), Polygon(ORIGIN, DL, DR), Polygon(ORIGIN, DR, UR),])
        square.set_fill(WHITE, 1).set_stroke(width=0.5, color=WHITE).rotate(np.arctan(0.5)).set_height(logo.inner_triangles.get_height())

        self.add(square)
        self.wait(0.5)
        self.play(ReplacementTransform(square, logo.inner_triangles), run_time=1.5)

        self.wait(0.4)
        self.play(TransformFromCopy(logo.inner_triangles, logo.mid_triangles),
                  TransformFromCopy(logo.inner_triangles, logo.outer_triangles), run_time=2)
        self.wait(0.6)

        big_black_rect = Rectangle(stroke_width=0, fill_color=BLACK, fill_opacity=1).scale(100).align_to(LEFT * 1.4, RIGHT)
        big_black_rect_02 = big_black_rect.copy()
        big_black_rect_02.add_updater(lambda b: b.align_to(logo, RIGHT).shift(RIGHT * 0.15))
        text_font = '思源黑体 Bold'
        text_manim = Text('Manim', font=text_font, size=2.3).align_to(LEFT * 1.4, LEFT).align_to(logo.part_ur, DOWN)
        text_manim.set_color_by_t2c({'M': logo.color_2[2]})
        text_kindergarten = Text('Kindergarten', font=text_font, size=2.3).align_to(logo.part_dr, UP).align_to(text_manim, LEFT)
        text_kindergarten.set_color_by_t2c({'K': logo.color_1[2]})
        text = VGroup(text_manim, text_kindergarten).shift(LEFT * 8).set_plot_depth(-2)
        self.add(text, big_black_rect, big_black_rect_02)
        self.play(logo.shift, LEFT * 3.6, text.shift, RIGHT * 8, run_time=2)

        self.wait(4)

class Logo_02(Scene):
    CONFIG = {
        "font": "Orbitron Bold",
    }

    def construct(self):

        logo = Logo(size=8/3)

        text = VGroup(
            Text("Manim", font=self.font),
            Text("Kindergarten", font=self.font)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).set_height(2).next_to(logo, buff=1.2).shift(DOWN*0.2)
        text[1][0].set_color(logo.color_2[2])
        text[0][0].set_color(logo.color_1[2])
        all_logo = VGroup(logo, text).center()

        line = Line(UP, DOWN, stroke_width=8).move_to(mid(logo.get_right(), text.get_left()))
        line.set_length(1.4)
        text.add(line)

        bg = Rectangle(height=10, width=10, fill_color=BLACK, fill_opacity=1, stroke_width=0)
        bg.add_updater(lambda m: m.move_to(logo, aligned_edge=RIGHT).shift(RIGHT*0.2))

        text.save_state()
        text.shift((text.get_right()[0]-bg.get_right()[0]+0.2)*LEFT)
        logo.save_state()
        logo.move_to(ORIGIN)
        logo.scale(1.2)
        logo.rotate(TAU, axis=IN)
        
        self.add(text, bg)
        self.play(FadeIn(logo[0]))
        self.wait(0.25)
        for i in range(3):
            self.play(MyTransform(logo[i], logo[i+1], about_point=logo.get_center()), run_time=0.2, rate_func=smooth)
        self.wait(0.5)
        self.play(
            text.restore, logo.restore,
            rate_func=smooth, run_time=1
        )
        self.wait()

class Fractal_by_logo(Scene):

    def construct(self):

        logo = Logo(size=5)
        start = logo.part_ur.copy().move_to(ORIGIN).set_height(5)
        to_be_replaced = VGroup(start)

        self.add(start)
        self.wait()
        time_01 = 2.5
        for i in range(5):
            n = len(to_be_replaced)
            to_be_replaced_new = VGroup()
            s = 0
            for m in to_be_replaced:
                to_replace_m = logo.copy().move_to(m.get_center()).set_height(m.get_height() * 1.335)
                if time_01/n < 1/self.camera.frame_rate:
                    self.remove(m)
                    self.add(to_replace_m)
                    s+=1
                    if s *  time_01/n > 1/self.camera.frame_rate:
                        self.wait(s *  time_01 / n)
                        s = 0
                else:
                    self.play(ReplacementTransform(m, to_replace_m), run_time=time_01/n)
                to_be_replaced_new.add(*to_replace_m)
            self.wait(0.8)
            to_be_replaced = to_be_replaced_new
        self.wait(4)

class MyTransform(Animation):
    CONFIG = {
        "radians": PI/2,
        "axis": OUT,
        "about_point": None,
        "remover": True,
    }

    def __init__(self, mobject, target, **kwargs):
        digest_config(self, kwargs)
        self.mobject = mobject.copy()
        self.target = target

    def clean_up_from_scene(self, scene):
        if self.is_remover():
            scene.remove(self.mobject)
            scene.add(self.target)

    def interpolate_mobject(self, alpha):
        now = self.starting_mobject.copy()
        now.rotate(
            alpha * self.radians,
            axis=self.axis,
            about_point=self.about_point,
        )
        for i in range(3):
            now[i].set_color(interpolate_color(self.starting_mobject[i].get_color(), self.target[i].get_color(), alpha))
        self.mobject.become(now)

# final

class Logo_black(Scene):

    CONFIG = {
        "font": "Orbitron Bold",
    }

    def construct(self):

        logo = Logo(size=8/3)
        squares = VGroup(*[Polygon(ORIGIN, UR, UL), Polygon(ORIGIN, UL, DL), Polygon(ORIGIN, DL, DR), Polygon(ORIGIN, DR, UR),])
        squares.set_fill(WHITE, 1).set_stroke(width=0.5, color=WHITE).rotate(np.arctan(0.5)).set_height(logo.inner_triangles.get_height())
        for s in squares:
            s.scale(0.8)

        text = VGroup(
            Text("Manim", font=self.font),
            Text("Kindergarten", font=self.font)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).set_height(2.1).next_to(logo, buff=1.5).shift(DOWN*0.2)
        text[1][0].set_color(logo.color_2[2])
        text[0][0].set_color(logo.color_1[2])
        all_logo = VGroup(logo, text).center()

        line = Line(UP, DOWN, stroke_width=8).move_to(mid(logo.get_right(), text.get_left()))
        line.set_length(1.4)
        text.add(line)

        bg = Rectangle(height=10, width=10, fill_color=BLACK, fill_opacity=1, stroke_width=0)
        bg.add_updater(lambda m: m.move_to(logo, aligned_edge=RIGHT).shift(RIGHT*0.2))

        text.save_state()
        text.shift((text.get_right()[0]-bg.get_right()[0]+0.2)*LEFT)
        logo.save_state()
        logo.move_to(ORIGIN)
        logo.scale(1.5)

        tris = logo.inner_triangles.copy().rotate(-PI)
        self.add(text, bg)

        self.wait(0.3)
        self.add(tris)
        self.wait(0.3)
        self.remove(tris)

        self.wait(0.2)
        self.add(tris)
        self.wait(0.15)
        self.remove(tris)

        self.wait(0.1)
        self.add(tris)
        self.wait(0.1)
        self.remove(tris)
        
        self.wait(0.075)
        self.add(tris)
        self.wait(0.075)
        self.remove(tris)

        self.wait(0.05)
        self.add(tris)
        self.wait(0.05)
        self.remove(tris)
        # square = Square().set_height(tris.get_height()).set_stroke(width=0.5, color=WHITE)
        # self.play(ReplacementTransform(square, tris), run_time=1)
        self.wait(0.2)
        self.play(ShowSubmobjectsOneByOne(tris), rate_func=linear, run_time=0.4)
        for i in tris:
            self.add(i)
            self.wait(0.1)
        self.play(*[ReplacementTransform(tris[i], squares[i]) for i in range(4)], 
            rate_func=rush_from, run_time=0.6)
        #self.play(ReplacementTransform(tris, squares), rate_func=linear, run_time=0.8)
        self.wait(0.1)
        self.play(*[ReplacementTransform(squares[i], logo[i]) for i in range(4)], 
            rate_func=rush_from, run_time=0.6)
        #self.play(ReplacementTransform(squares, logo), rate_func=linear, run_time=1.5)
        self.wait(0.1)
        self.play(
            text.restore, logo.restore,
            rate_func=rush_from, run_time=0.8
        )
        self.wait(1)
        self.play(FadeOut(VGroup(*self.mobjects)))


class Logo_white(Scene):
    CONFIG = {
        "font": "Orbitron Bold",
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):

        logo = Logo(size=8/3, black_bg=False)
        squares = VGroup(*[Polygon(ORIGIN, UR, UL), Polygon(ORIGIN, UL, DL), Polygon(ORIGIN, DL, DR), Polygon(ORIGIN, DR, UR),])
        squares.set_fill(BLUE_C, 1).set_stroke(width=0.5, color=BLUE_C).rotate(np.arctan(0.5)).set_height(logo.inner_triangles.get_height())
        squares[0].set_fill('#C59978', 1).set_stroke(width=0.5, color='#C59978')
        for s in squares:
            s.scale(0.8)

        text = VGroup(
            Text("Manim", font=self.font, color=BLACK),
            Text("Kindergarten", font=self.font, color=BLACK)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).set_height(2.1).next_to(logo, buff=1.5).shift(DOWN*0.2)
        text[1][0].set_color(logo.color_2[2])
        text[0][0].set_color(logo.color_1[2])
        all_logo = VGroup(logo, text).center()

        line = Line(UP, DOWN, stroke_width=8, color=BLACK).move_to(mid(logo.get_right(), text.get_left()))
        line.set_length(1.4)
        text.add(line)

        bg = Rectangle(height=10, width=10, fill_color=WHITE, fill_opacity=1, stroke_width=0)
        bg.add_updater(lambda m: m.move_to(logo, aligned_edge=RIGHT).shift(RIGHT*0.2))

        text.save_state()
        text.shift((text.get_right()[0]-bg.get_right()[0]+0.2)*LEFT)
        logo.save_state()
        logo.move_to(ORIGIN)
        logo.scale(1.5)

        tris = logo.inner_triangles.copy().rotate(-PI)
        tris.set_color(BLUE_C)
        tris[0].set_color('#C59978')
        self.add(text, bg)

        self.wait(0.3)
        self.add(tris)
        self.wait(0.3)
        self.remove(tris)

        self.wait(0.2)
        self.add(tris)
        self.wait(0.15)
        self.remove(tris)

        self.wait(0.1)
        self.add(tris)
        self.wait(0.1)
        self.remove(tris)
        
        self.wait(0.075)
        self.add(tris)
        self.wait(0.075)
        self.remove(tris)

        self.wait(0.05)
        self.add(tris)
        self.wait(0.05)
        self.remove(tris)
        # square = Square().set_height(tris.get_height()).set_stroke(width=0.5, color=WHITE)
        # self.play(ReplacementTransform(square, tris), run_time=1)
        self.wait(0.2)
        self.play(ShowSubmobjectsOneByOne(tris), rate_func=linear, run_time=0.4)
        for i in tris:
            self.add(i)
            self.wait(0.1)
        self.play(*[ReplacementTransform(tris[i], squares[i]) for i in range(4)], 
            rate_func=rush_from, run_time=0.6)
        #self.play(ReplacementTransform(tris, squares), rate_func=linear, run_time=0.8)
        self.wait(0.1)
        self.play(*[ReplacementTransform(squares[i], logo[i]) for i in range(4)], 
            rate_func=rush_from, run_time=0.6)
        #self.play(ReplacementTransform(squares, logo), rate_func=linear, run_time=1.5)
        self.wait(0.1)
        self.play(
            text.restore, logo.restore,
            rate_func=rush_from, run_time=0.8
        )
        self.wait(1)
        self.play(FadeOut(VGroup(*self.mobjects)))


class Logo_Rotate_Out(Scene):

    CONFIG = {
        "font": "Orbitron",
    }

    def construct(self):

        logo = Logo(size=8/3)
        squares = VGroup(*[Polygon(ORIGIN, UR, UL), Polygon(ORIGIN, UL, DL), Polygon(ORIGIN, DL, DR), Polygon(ORIGIN, DR, UR),])
        squares.set_fill(WHITE, 1).set_stroke(width=0.5, color=WHITE).rotate(np.arctan(0.5)).set_height(logo.inner_triangles.get_height())
        for s in squares:
            s.scale(0.8)

        text = VGroup(
            VGroup(*[Text(t, font=self.font) for t in 'Manim']).arrange(direction=RIGHT * 0.5, aligned_edge=DOWN),
            VGroup(*[Text(t, font=self.font) for t in 'Kindergarten']).arrange(direction=RIGHT * 0.5, aligned_edge=DOWN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).set_height(2.1).next_to(logo, buff=1.5).shift(DOWN*0.2)
        text[1][6].align_to(text[1][5], UP)
        text[1][0].set_color(logo.color_2[2])
        text[0][0].set_color(logo.color_1[2])
        all_logo = VGroup(logo, text).center()

        line = Line(UP, DOWN, stroke_width=8).move_to(mid(logo.get_right(), text.get_left()))
        line.set_length(1.4)
        text.add(line)

        bg = Rectangle(height=10, width=10, fill_color=BLACK, fill_opacity=1, stroke_width=0)
        bg.add_updater(lambda m: m.move_to(logo, aligned_edge=RIGHT).shift(RIGHT*0.2))

        text.save_state()
        text.shift((text.get_right()[0]-bg.get_right()[0]+0.2)*LEFT)
        logo.save_state()
        logo.move_to(ORIGIN)
        logo.scale(1.5)

        tris = logo.inner_triangles.copy().rotate(-PI)
        self.add(text, bg)

        self.wait(0.3)
        self.add(tris)
        self.wait(0.3)
        self.remove(tris)

        self.wait(0.2)
        self.add(tris)
        self.wait(0.15)
        self.remove(tris)

        self.wait(0.1)
        self.add(tris)
        self.wait(0.1)
        self.remove(tris)

        self.wait(0.075)
        self.add(tris)
        self.wait(0.075)
        self.remove(tris)

        self.wait(0.05)
        self.add(tris)
        self.wait(0.05)
        self.remove(tris)
        # square = Square().set_height(tris.get_height()).set_stroke(width=0.5, color=WHITE)
        # self.play(ReplacementTransform(square, tris), run_time=1)
        self.wait(0.2)
        self.play(ShowSubmobjectsOneByOne(tris), rate_func=linear, run_time=0.4)
        for i in tris:
            self.add(i)
            self.wait(0.1)
        self.play(*[ReplacementTransform(tris[i], squares[i]) for i in range(4)],
            rate_func=rush_from, run_time=0.6)
        #self.play(ReplacementTransform(tris, squares), rate_func=linear, run_time=0.8)
        self.wait(0.1)
        self.play(*[ReplacementTransform(squares[i], logo[i]) for i in range(4)],
            rate_func=rush_from, run_time=0.6)
        #self.play(ReplacementTransform(squares, logo), rate_func=linear, run_time=1.5)
        self.wait(0.1)
        self.play(
            text.restore, logo.restore,
            rate_func=rush_from, run_time=0.8
        )
        self.wait(0.75)
        self.play(VGroup(*self.mobjects).shift, UP * 1.2)
        self.wait(0.5)
        s = ValueTracker(-7)
        def rotate_out(a, dt):
            w = 1.
            if a.get_center()[0] < s.get_value() or a.get_center()[-1] != 0:
                a.rotate(w * (1 + 2.5 * np.random.random()) * DEGREES, axis=UR, about_point=RIGHT * s.get_value() + OUT * 0.25)
                # a.rotate(w * (1 + 2 * np.random.random()) * DEGREES, axis=UR, about_point=RIGHT * s.get_value() + OUT * (0.12+s.get_value()*0.2))

        for i in range(4):
            for mob in logo[i]:
                mob.add_updater(rotate_out)
        for tex in text[0]:
            tex.add_updater(rotate_out)
        for tex in text[1]:
            tex.add_updater(rotate_out)
        line.add_updater(rotate_out)
        self.remove(bg)
        # s_speed = 0.16
        # for i in range(160):
        #     s.increment_value(s_speed)
        #     self.wait(1/self.camera.frame_rate)
        self.play(s.set_value, 10, rate_func=rush_into, run_time=3.6)

        self.wait(1)

