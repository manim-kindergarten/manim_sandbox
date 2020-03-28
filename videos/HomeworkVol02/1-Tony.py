# from @鹤翔万里

from manimlib.imports import *
from manim_sandbox.utils.imports import *

class Homework_02(Scene):
    def construct(self):
        self.intro_problem()
        self.main_proof()
    
    def intro_problem(self):
        problem = TexMobject("1^3+2^3+3^3+\\cdots +n^3=?")
        VGroup(problem[0][1], problem[0][4], problem[0][7], problem[0][14]).set_color(GOLD)
        self.wait()
        self.play(Write(problem[0][:15]))
        self.wait()
        self.play(Write(problem[0][15:]))
        self.wait(3)
        self.play(problem.to_edge, UP)
        self.wait()
        self.problem = problem
    
    def main_proof(self):
        unit = 0.4
        sq = VGroup()
        sq.add(Square(side_length=unit).move_to(np.array([-5.2, 2.6, 0])))
        for num in range(2, 6):
            sq.add(VGroup(
                *[
                    Square(side_length=unit*num)
                    for i in range(num)
                ]
            ).arrange(RIGHT, buff=0).next_to(sq[-1], DOWN, aligned_edge=LEFT, buff=0))
        # self.add(sq)
        ver1 = sq[0].get_vertices()
        ver2 = sq[1][-1].get_vertices()
        ver3 = sq[2][-1].get_vertices()
        ver4 = sq[3][-1].get_vertices()
        ver5 = sq[4][-1].get_vertices()
        line = Line(ver1[0], ver5[2]+RIGHT*unit*5)
        line2 = Line(ver5[2]+RIGHT*unit*5, ver5[2])
        # self.add(line, line2)

        area = VGroup(
            VGroup(
                Polygon(ver1[0], mid(ver1[1], ver1[2]), ver1[2], ver1[3], ver1[0]),
                Polygon(ver1[0], mid(ver1[1], ver1[2]), ver1[1], ver1[0])
            ),
            VGroup(
                sq[1][0].copy(),
                Polygon(ver2[0], mid(ver2[1], ver2[2]), ver2[2], ver2[3], ver2[0]),
                Polygon(ver2[0], mid(ver2[1], ver2[2]), ver2[1], ver2[0])
            ),
            VGroup(
                sq[2][0].copy(), sq[2][1].copy(),
                Polygon(ver3[0], mid(ver3[1], ver3[2]), ver3[2], ver3[3], ver3[0]),
                Polygon(ver3[0], mid(ver3[1], ver3[2]), ver3[1], ver3[0])
            ),
            VGroup(
                sq[3][0].copy(), sq[3][1].copy(), sq[3][2].copy(),
                Polygon(ver4[0], mid(ver4[1], ver4[2]), ver4[2], ver4[3], ver4[0]),
                Polygon(ver4[0], mid(ver4[1], ver4[2]), ver4[1], ver4[0])
            ),
            VGroup(
                sq[4][0].copy(), sq[4][1].copy(), sq[4][2].copy(), sq[4][3].copy(),
                Polygon(ver5[0], mid(ver5[1], ver5[2]), ver5[2], ver5[3], ver5[0]),
                Polygon(ver5[0], mid(ver5[1], ver5[2]), ver5[1], ver5[0])
            )
        )
        colors = color_gradient([BLUE, YELLOW], 5)
        for i, mob in enumerate(area):
            mob.set_fill(colors[i], 0.5)
            mob.set_stroke(color=colors[i])
        # for i in range(5):
        #     area[i][-1].rotate(PI, axis=IN, about_point=area[i][-2].get_vertices()[1])

        text = VGroup(
            *[
                TexMobject("{}\\times {}^2".format(i, i)).scale(0.8)
                for i in range(1, 6)
            ]
        )
        text2 = VGroup(
            *[
                TexMobject("{}^3".format(i)).scale(0.8)
                for i in range(1, 6)
            ]
        )
        text3 = VGroup(
            *[
                TexMobject("{}".format(i)).scale(0.8)
                for i in range(1, 6)
            ]
        )
        for i, mob in enumerate(text):
            mob.next_to(sq[i][0], LEFT)
        for i, mob in enumerate(text2):
            mob.next_to(sq[i][0], LEFT)
        for i, mob in enumerate(text3):
            mob.next_to(sq[i][0], LEFT)
        text4 = TexMobject("\\frac{1}{2}n(n+1)").scale(0.6).move_to(text3, aligned_edge=RIGHT)
        text5 = TexMobject("n(n+1)").scale(0.6).next_to(sq[-1][2], DOWN)

        areaeq = TextMobject("Area=").set_color(ORANGE).next_to(self.problem, LEFT)
        ans = TexMobject("\\left(\\frac{1}{2}n(n+1)\\right)^2").move_to(self.problem[0][-1], aligned_edge=LEFT)

        self.wait()
        self.play(ShowCreation(sq), run_time=5, rate_func=linear)
        self.wait()
        for i in range(5):
            self.play(TransformFromCopy(sq[i], text[i]))
        self.wait(2)
        for i in range(5):
            self.play(ReplacementTransform(text[i], text2[i]))
        self.wait()
        for i in range(5):
            self.play(ShowCreation(area[i]))
        self.remove(sq)
        self.play(Write(areaeq))
        self.wait(3)
        for i in range(5):
            self.play(
                Rotating(area[i][-1], radians=PI, axis=IN, about_point=area[i][-2].get_vertices()[1], 
                rate_func=smooth, run_time=1)
            )
        self.wait(2)
        self.play(text2.shift, RIGHT*12)
        self.play(Write(text3))
        self.wait()
        self.play(ReplacementTransform(text3, text4))
        self.wait()
        self.play(Write(text5))
        self.wait(2)
        self.play(FadeOut(self.problem[0][-1]))
        self.play(TransformFromCopy(VGroup(text4, text5), ans))
        self.wait(2)
        target = VGroup(
            self.problem[0][:-1].copy(), ans.copy()
        ).center().scale(1.2).shift(UP*2)
        bg = BackgroundRectangle(target, buff=0.25)
        self.play(
            FadeOut(VGroup(text2, text4, text5)),
            FadeOut(areaeq),
            FadeIn(bg),
            Transform(VGroup(self.problem[0][:-1], ans), target),
        )
        self.wait(4)
        





