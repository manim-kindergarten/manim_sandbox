# from @GZTime

from manimlib.imports import *
from public.imports import *
from manim_sandbox.utils.imports import *

class CubicSum(Scene):
    def construct(self):
        titles = [Text("Manim Homework Vol.2", font='Orbitron Medium', stroke_width=0),
            Text("@GZTime", font='Orbitron Medium', stroke_width=0).scale(0.5)]
        titles[0].move_to(UP*0.5)
        titles[1].move_to(DOWN*0.5)
        self.play(*[Write(title) for title in titles])
        self.wait(2)
        self.play(*[FadeOut(title) for title in titles])

        colors = [BLUE,YELLOW,GREEN,RED]
        
        texts = [[TexMobject(str(i) + '\\times',str(i) + '^2')
            .move_to((i**2)/8 * DOWN + (i**2)/8 * LEFT + LEFT * i/8 + LEFT)
            for i in range(1,6)]]

        texts.append([])
        texts.append([TexMobject('\\dots').move_to(LEFT * 5 + DOWN * 2)])

        squares = [Square(side_length=i/4,stroke_width=4)
            .set_fill(color=BLUE_D,opacity=1)
            .move_to((i**2)/8 * DOWN + (i**2)/8 * LEFT)
            for i in range(1,6)]

        group = []

        for i in range(5):
            self.play(ShowCreation(squares[i]),Write(texts[0][i][1]))
            self.wait(0.5)
            group.append(squares[i])
            last = squares[i]
            for k in range(i):
                sq = last.copy()
                self.play(sq.shift,RIGHT * (i + 1)/4,run_time=1/(i+1))
                group.append(sq)
                last = sq
            self.play(Write(texts[0][i][0]))
            self.wait(0.5)
            self.play(texts[0][i].move_to,LEFT * 5 + UP * (3 - i),run_time=0.5,rate_func=smooth)
            texts[2].append(TexMobject(str(i + 1) + '^3').move_to(texts[0][i]))
            self.play(ReplacementTransform(texts[0][i],texts[2][i + 1]),run_time=0.5)
            self.wait(0.5)
        
        self.play(Write(texts[2][0]))
        
        blues = VGroup(*group)
        colors = [BLUE_D,YELLOW_D,GREEN_D,RED]
        parts = [blues]

        self.wait(1)

        texts[1].append(TexMobject('4','\\times','\\sum_{k=1}^n k^3','=').move_to(LEFT * 5))

        self.play(ReplacementTransform(VGroup(*texts[2]),texts[1][0][2]))
        self.wait(0.5)

        for i in range(1,4):
            parts.append(parts[i-1].copy().set_fill(color=colors[i]))
            self.play(Rotating(parts[i],radians=PI/2,about_point=ORIGIN,run_time=1,rate_func=smooth))
            self.wait(0.5)
        
        self.play(Write(texts[1][0][0:2]))
        self.wait(1)

        brackets = [Brace(VGroup(*parts[1][10:]),direction=RIGHT),
                    Brace(VGroup(*parts[2][10]),direction=RIGHT)]

        texts[1].append(TexMobject('n','\\times','n').move_to(parts[1][12].get_center() + RIGHT * 2))
        texts[1].append(TexMobject('n').move_to(parts[2][10].get_center() + RIGHT * 1.5))
        
        texts.append([TexMobject('=','(n^2+n)^2').move_to(RIGHT * 5)])

        self.play(FadeIn(brackets[0]),Write(texts[1][1]))
        self.wait(0.5)
        self.play(FadeIn(brackets[1]),Write(texts[1][2]))
        self.wait(0.5)

        big_square = Square(side_length=15/2).set_fill(color=WHITE,opacity=0.5)

        self.play(ShowCreationThenDestruction(big_square,run_time=3,rate_func=lambda t: smooth(t,inflection=20)))

        self.play(ReplacementTransform(VGroup(*brackets,texts[1][1],texts[1][2]),texts[3][0][1]))
        
        self.play(VGroup(*parts).scale,0.2)
        self.play(VGroup(*texts[1][0]).next_to,VGroup(*parts),LEFT,
            VGroup(*texts[3][0]).next_to,VGroup(*parts),RIGHT)

        result = TexMobject('\\sum_{k=1}^n k^3','=','\\frac{(n^2+n)^2}{4}')
        self.wait(2)
        self.play(ReplacementTransform(VGroup(VGroup(*texts[1][0]),VGroup(*texts[3][0])),result),
            FadeOut(VGroup(*parts)))

        self.wait(2)
        self.play(result.scale,2)

        QED = TextMobject('Q.E.D.').scale(2).next_to(result,DOWN,buff=0.5)
        self.play(Write(QED))
        self.wait(2)
