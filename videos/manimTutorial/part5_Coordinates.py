from manimlib.imports import *
from manim_sandbox.utils.imports import *
from manim_sandbox.videos.manimTutorial.utils import *
from manim_projects.tony_useful.imports import *


numberline_t2c = {
    "NumberLine": BLUE_D,
    "x_min": ORANGE,
    "x_max": ORANGE,
    "include_ticks": ORANGE,
    "include_tip": ORANGE,
    "include_numbers": ORANGE,
    "unit_size": ORANGE,
    "tick_frequency": ORANGE,
    "label_direction": ORANGE,
    "n2p": BLUE_D,
    "p2n": BLUE_D,
    "number_to_point": BLUE_D,
    "point_to_number": BLUE_D,
    "add_numbers": BLUE_D,
    "Dot": BLUE_D,
    "get_center": BLUE_D,
}

axes_t2c = {
    
}


class OpeningScene(Scene_):
    def construct(self):
        t2c = {"manim": average_color(PINK, RED),
               "坐标系": BLUE, "图像": GREEN}
        text_color = DARK_GRAY

        font = "庞门正道标题体"
        text_1 = Text("大家好!", font=font, color=text_color, size=2, t2c=t2c).to_edge(UP * 2, buff=1)
        text_2 = Text("欢迎来到manim视频教程", font=font,
                      color=text_color, size=2, t2c=t2c).to_edge(UP * 3.2, buff=1)
        text_3 = Text("这一期我们将学习manim中", font=font, color=text_color, size=2, t2c=t2c).to_edge(UP * 1.8, buff=1)
        text_4 = Text("坐标系与图像的相关知识", font=font, color=text_color, size=2, t2c=t2c).to_edge(UP * 3., buff=1)
        text_34, text_12 = VGroup(text_3, text_4), VGroup(text_1, text_2)


        methods = [["NumberLine", "ticks", "tips", "numbers", "n2p", "p2n"],
                   ["Axes", "labels", "coordinates", "c2p", "p2c"],
                   ["NumerPlane", "ComplexPlane", "nonlinear_transform"],
                   ["ParametricFunction", "FunctionGraph"]]
        m_group_1 = VGroup(*[Text(tex + ', ', size=0.84, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[0]]).arrange(RIGHT)
        m_group_2 = VGroup(*[Text(tex + ', ', size=0.84, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[1]]).arrange(RIGHT)
        m_group_3 = VGroup(*[Text(tex, size=0.84, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[2]]).arrange(RIGHT)
        m_group_4 = VGroup(*[Text(tex, size=0.84, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[3]]).arrange(RIGHT)
        m_group = VGroup(m_group_1, m_group_2, m_group_3, m_group_4).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        methodes_group = VGroup(*m_group_1, *m_group_2, *m_group_3, *m_group_4).next_to(text_34, DOWN, buff=0.5)

        # self.add(picture)
        self.wait(0.5)
        self.play(Write(text_1))
        self.wait(0.5)
        self.play(WriteRandom(text_2), run_time=1.5)
        self.wait(1.8)
        self.play(ReplacementTransform(text_12, text_34), run_time=1.2)
        self.wait(1.2)
        self.play(FadeInRandom(methodes_group), run_time=2.4)
        self.wait(2.6)
        self.play(FadeOutRandom(methodes_group), FadeOutRandom(text_3),
                  FadeOutRandom(text_4), run_time=1.8)
        self.wait(1)


class NumberLineTutorial(Scene_):
    CONFIG = {
        # "fade_all": False,
    }
    def start(self):
        t2c = {"manim": GOLD,
               "NumberLine": GREEN}
        title = VGroup(
            Text("Chapter Ⅰ.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("使用NumberLine构建数轴", font="Source Han Sans CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        CodeLine.CONFIG["t2c"].update(numberline_t2c)
        CodeLine.CONFIG["size"] = 0.55
        captions = [
            "在manim中，可以使用NumberLine构建一个数轴",
            "通过x_min和x_max调整数轴的最小值最大值",
            "数轴默认附带刻度，可以通过设置include_ticks取消刻度",
            "使用include_tip添加箭头，include_numbers添加默认刻度数字",
            "unit_size表示数轴上的单位长度为manim中的多少单位",
            "tick_frequency表示数轴上添加刻度的频率（每...个单位一个）",
            "label_direction表示刻度数字在对应刻度的位置，默认为DOWN",
            "除了使用默认刻度数字之外，还可以通过add_numbers手动添加需要的数字",
            "构建了数轴之后，可以使用它的相关方法，最常用的是n2p和p2n",
            "n2p是number_to_point的缩写，给出一个数字，返回数轴上这个点的坐标",
            "p2n是point_to_number的缩写，与n2p正好相反",
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        codes = CodeLines(
            ">>> axis = NumberLine(",
            "~~~~~~~~x_min=-2, x_max=2,",
            "~~~~~~~~include_ticks=False,",
            "~~~~~~~~include_tip=True,",
            "~~~~~~~~include_numbers=True,",
            "~~~~~~~~unit_size=1.5,",
            "~~~~~~~~tick_frequency=0.5,",
            "~~~~~~~~label_direction=UP,",
            "~~~~).shift(LEFT*3)",
            ">>> axis.add_numbers(-1, 2)",
            ">>> dot = Dot(axis.n2p(1))",
            ">>> axis.p2n(dot.get_center())",
            "1",
        )
        codebg = CodeBackground(codes, buff=0.3)
        VGroup(codes, codebg).to_edge(RIGHT, buff=0.6).shift(UP*0.3)
        axis = NumberLine(color=BLACK, plot_depth=-2)
        axis2 = NumberLine(color=BLACK, x_min=-2, x_max=2, plot_depth=-2).shift(LEFT*3)
        axis3 = NumberLine(color=BLACK, x_min=-2, x_max=2, plot_depth=-2, include_ticks=False).shift(LEFT*3)
        axis4 = NumberLine(color=BLACK, x_min=-2, x_max=2, plot_depth=-2, include_tip=True).shift(LEFT*3)
        axis5 = NumberLine(color=BLACK, x_min=-2, x_max=2, plot_depth=-2, include_tip=True, include_numbers=True).shift(LEFT*3)
        axis6 = NumberLine(color=BLACK, x_min=-2, x_max=2, unit_size=1.5, include_tip=True, include_numbers=True).shift(LEFT*3)
        axis7 = NumberLine(color=BLACK, x_min=-2, x_max=2, unit_size=1.5, include_tip=True, include_numbers=True, tick_frequency=0.5).shift(LEFT*3)
        axis8 = NumberLine(color=BLACK, x_min=-2, x_max=2, unit_size=1.5, include_tip=True, include_numbers=True, tick_frequency=0.5, label_direction=UP).shift(LEFT*3)
        
        self.wait()
        self.play(Write(self.caps[0]))
        self.wait()
        self.play(FadeInFromDown(codebg))
        self.play(Write(VGroup(codes[0], codes[8][4])))
        self.wait()
        self.play(ShowCreation(axis))
        self.wait(3)

        self.next_caps()
        self.play(Write(codes[1]))
        self.play(Write(codes[8][5:]))
        self.wait()
        self.play(Transform(axis, axis2))
        self.wait(2)

        self.next_caps()
        self.play(Write(codes[2]))
        self.wait()
        self.play(Transform(axis, axis3))
        self.wait(2)
        self.play(Transform(
            codes[2][-6:], CodeLine("True,").move_to(codes[2][-6:], aligned_edge=LEFT)
        ))
        self.wait()
        self.play(Transform(axis, axis2))
        self.wait()

        self.next_caps()
        self.play(Write(codes[3]))
        self.play(Write(codes[4]))
        self.wait()
        self.play(FadeOut(axis), FadeIn(axis5))
        self.wait(2)

        self.next_caps()
        self.play(Write(codes[5]))
        self.wait()
        self.play(Transform(axis5, axis6))
        self.wait()
        brace = Brace(Line(axis5.n2p(0), axis5.n2p(1)), UP, color=DARK_GRAY)
        text = CodeLine("1.5", size=0.72).next_to(brace, UP)
        self.play(FadeInFrom(VGroup(brace, text), UP))
        self.wait(2)
        self.play(FadeOut(VGroup(brace, text)))

        self.next_caps()
        self.play(Write(codes[6]))
        self.wait()
        self.play(Transform(axis5, axis7))
        self.wait(3)

        self.next_caps()
        self.play(Write(codes[7]))
        self.wait()
        self.play(FadeOut(axis5), FadeIn(axis8))
        self.wait(2)
        self.play(Transform(
            codes[4][-5:], CodeLine("False,").move_to(codes[4][-5:], aligned_edge=LEFT)
        ))
        self.wait()
        axis = NumberLine(color=BLACK, x_min=-2, x_max=2, unit_size=1.5, include_tip=True, tick_frequency=0.5, label_direction=UP).shift(LEFT*3)
        self.play(FadeOut(axis8), FadeIn(axis))
        self.wait(0.5)

        self.next_caps()
        self.play(Write(codes[9]))
        self.wait()
        self.play(FadeInFromDown(axis.get_number_mobjects(-1, 2)))
        self.wait(3)

        self.next_caps()
        self.wait(2)
        self.next_caps()
        self.play(Write(codes[10]))
        self.wait()
        dot = Dot(axis.n2p(1), color=BLUE_D, radius=0.1)
        self.play(Write(dot))
        self.wait(3)
        self.next_caps()
        self.play(Write(codes[11]))
        self.wait()
        self.play(Write(codes[12]))
        self.wait(4)


class AxesTutorial(Scene_):
    CONFIG = {
        "fade_all": False,
    }
    def start(self):
        t2c = {"manim": GOLD,
               "Axes": GREEN}
        title = VGroup(
            Text("Chapter II.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("使用Axes构建坐标系", font="Source Han Sans CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        CodeLine.CONFIG["t2c"].update(axes_t2c)
        CodeLine.CONFIG["size"] = 0.55
        captions = [
            
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

