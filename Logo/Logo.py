
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
        'color_1': [WHITE, BLUE_B, BLUE_C],
        'color_2': [WHITE, '#C59978', '#8D5630'],
        'center': ORIGIN,
        'size': 2,
        'shift_out': ORIGIN,
    }

    def __init__(self, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.create_logo()

    def create_logo(self):

        p1 = Polygon(ORIGIN, RIGHT, 2 * UP, stroke_width=0).set_fill(self.color_1[0], 1)
        p2 = Polygon(1.5 * RIGHT, 3 * UR, 3 * UP, stroke_width=0).set_fill(self.color_1[1], 1)
        p3 = Polygon(2 * RIGHT, 3 * RIGHT, 3 * RIGHT + 2 * UP, stroke_width=0).set_fill(self.color_1[2], 1)

        self.part_ur = VGroup(p1, p2, p3).move_to([2.5, 1., 0] + self.shift_out)
        self.part_ul = self.part_ur.copy().rotate(PI / 2, about_point=ORIGIN)
        self.part_dl = self.part_ur.copy().rotate(PI, about_point=ORIGIN)
        self.part_dr = self.part_ur.copy().rotate(3 * PI / 2, about_point=ORIGIN)

        self.add(self.part_ur, self.part_ul, self.part_dl, self.part_dr)
        self.set_height(self.size).move_to(self.center)
        self[0][0].set_fill(self.color_2[0], 1), self[0][1].set_fill(self.color_2[1], 1), self[0][2].set_fill(self.color_2[2], 1)

        self.inner_triangles = VGroup(self.part_ur[0], self.part_ul[0], self.part_dl[0], self.part_dr[0])
        self.mid_triangles = VGroup(self.part_ur[1], self.part_ul[1], self.part_dl[1], self.part_dr[1])
        self.outer_triangles = VGroup(self.part_ur[2], self.part_ul[2], self.part_dl[2], self.part_dr[2])

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
        text_manim = Text('Manim', font=text_font, size=1.15).align_to(LEFT * 1.4, LEFT).align_to(logo.part_ur, DOWN)
        text_manim.set_color_by_t2c({'M': logo.color_2[2]})
        text_kindergarten = Text('Kindergarten', font=text_font, size=1.15).align_to(logo.part_dr, UP).align_to(text_manim, LEFT)
        text_kindergarten.set_color_by_t2c({'K': logo.color_1[2]})
        text = VGroup(text_manim, text_kindergarten).shift(LEFT * 8).set_plot_depth(-2)
        self.add(text, big_black_rect, big_black_rect_02)
        self.play(logo.shift, LEFT * 3.6, text.shift, RIGHT * 8, run_time=2)

        self.wait(4)

class Fractal_by_logo(Scene):

    def construct(self):

        logo = Logo(size=5, color_2=[WHITE, BLUE_B, BLUE_C])
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

