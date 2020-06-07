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
    "Axes": BLUE_D,
    "c2p": BLUE_D,
    "p2c": BLUE_D,
    "coords_to_point": BLUE_D,
    "point_to_coords": BLUE_D,
    "number_line_config": ORANGE,
    "x_axis_config": ORANGE,
    "y_axis_config": ORANGE,
    "x(y)_axis_config": ORANGE,
    "center_point": ORANGE,
    "add_coordinates": BLUE_D,
    "get_axis_labels": BLUE_D,
    "y_min": ORANGE,
    "y_max": ORANGE,
    '"unit_size"': GOLD_D,
    '"tick_frequency"': GOLD_D,
}

numberplane_t2c = {
    "NumberPlane": BLUE_D,
    "axis_config": ORANGE,
    '"stroke_color"': GOLD_D,
    "apply_function": BLUE_D,
    "matrix": BLUE_D,
    "prepare_for_nonlinear_transform": BLUE_D,
    "ComplexPlane": BLUE_D,
    "apply_complex_function": BLUE_D,
    "lambda": BLUE,
    "sin": BLUE,
    "cos": BLUE,
    "exp": BLUE,
    "2j": average_color(BLUE, PINK),
}

pf_t2c = {
    "ParametricFunction": BLUE_D,
    "FunctionGraph": BLUE_D,
    "t_min": ORANGE,
    "t_max": ORANGE,
    "def": BLUE_D,
    "PI": average_color(BLUE, PINK),
    "func2": DARK_GRAY,
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
        # "fade_all": False,
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
        CodeLine.CONFIG["t2c"].update(numberline_t2c)
        CodeLine.CONFIG["t2c"].update(axes_t2c)
        CodeLine.CONFIG["size"] = 0.48
        captions = [
            "使用Axes构建一个直角坐标系，默认全屏带箭头",
            "通过x_min,x_max,y_min,y_max来更改最大最小值",
            "传入center_point可以指定原点在屏幕上的位置",
            "通过number_line_config传入一个字典，表示两个轴的通用属性（见上部分）",
            "还可以使用x(y)_axis_config传入字典表示某个轴的特有属性",
            "Axes可以使用add_coordinates传入两个列表(表示x/y轴坐标)来手动添加两轴上的坐标数字",
            "如果没有传入列表，则默认添加出所有数字",
            "通过get_axis_labels方法返回xy轴的标签(一个VGroup包含两个label)",
            "和NumberLine类似，Axes含有c2p和p2c两个常用方法",
            "c2p即coords_to_point，根据Axes坐标系内坐标返回屏幕坐标系内该点坐标",
            "p2c即point_to_coords，是c2p的逆操作",
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        codes = CodeLines(
            ">>> axes = Axes(",
            "~~~~~~~~x_min=-2, x_max=2,",
            "~~~~~~~~y_min=-2, y_max=2,",
            "~~~~~~~~center_point=LEFT*3",
            "~~~~~~~~number_line_config={",
            "~~~~~~~~~~~~\"unit_size\": 1.5,",
            "~~~~~~~~},",
            "~~~~~~~~x_axis_config={",
            "~~~~~~~~~~~~\"tick_frequency\": 0.5",
            "~~~~~~~~},",
            "~~~~)",
            ">>> axes.add_coordinates(",
            "~~~~~~~~[-1, 2], [-2, 1] )",
            ">>> axes.add_coordinates()",
            ">>> self.add(axes.get_axis_labels())",
            ">>> dot = Dot(axes.c2p(1, 2))",
            ">>> axes.p2c(dot.get_center())",
            "(1, 2)",
            buff=0.12,
        )
        codebg = CodeBackground(codes, buff=0.25)
        VGroup(codes, codebg).to_edge(RIGHT, buff=0.7).shift(UP*0.35)

        nlc = {"color": BLACK}
        axes = Axes(number_line_config=nlc, plot_depth=-5)
        axes1 = Axes(
            number_line_config=nlc,
            x_min=-2, x_max=2, y_min=-2, y_max=2,
            center_point=LEFT*3,
            plot_depth=-5,
        )
        nlc2 = {"color": BLACK, "unit_size": 1.5}
        axes2 = Axes(
            number_line_config=nlc2,
            x_min=-2, x_max=2, y_min=-2, y_max=2,
            center_point=LEFT*3,
            plot_depth=-5,
        )
        axes3 = Axes(
            number_line_config=nlc2,
            x_min=-2, x_max=2, y_min=-2, y_max=2,
            center_point=LEFT*3,
            x_axis_config={"tick_frequency": 0.5},
            plot_depth=-5,
        )
        nlc3 = {"color": BLACK, "unit_size": 1.5, "include_numbers": True}
        axes4 = Axes(
            number_line_config=nlc2,
            x_min=-2, x_max=2, y_min=-2, y_max=2,
            center_point=LEFT*3,
            x_axis_config={"tick_frequency": 0.5},
            plot_depth=-5,
        ).add_coordinates([-1, 2], [-2, 1], number_config={"color": BLACK})
        # self.add(codebg, codes)

        self.wait()
        self.play(Write(self.caps[0]))
        self.wait()
        self.play(FadeInFromDown(codebg))
        self.play(Write(VGroup(codes[0], codes[10])))
        self.wait()
        self.play(ShowCreation(axes))
        self.wait(3)

        self.next_caps()
        self.play(Write(codes[1]))
        self.play(Write(codes[2]))
        self.wait(0.5)

        self.next_caps()
        self.play(Write(codes[3]))
        self.wait()
        self.play(Transform(axes, axes1))
        self.wait(3)

        self.next_caps()
        self.play(Write(VGroup(codes[4], codes[6])))
        self.wait(0.5)
        self.play(Write(codes[5]))
        self.wait()
        self.play(Transform(axes, axes2))
        self.wait(3)
        
        self.next_caps()
        self.play(Write(VGroup(codes[7], codes[9])))
        self.wait(0.5)
        self.play(Write(codes[8]))
        self.wait()
        self.play(Transform(axes, axes3))

        self.next_caps()
        self.play(Write(VGroup(codes[11], codes[12])))
        self.wait()
        nc = {"color": BLACK}
        # labels1 = axes.get_coordinate_labels([-1, 2], [-2, 1], number_config=nc)
        self.play(FadeOut(axes), FadeIn(axes4))
        self.wait(3)
        
        self.next_caps()
        self.play(Write(codes[13]))
        self.wait()
        # labels2 = axes.get_coordinate_labels(number_config=nc)
        axes = Axes(
            number_line_config=nlc2,
            x_min=-2, x_max=2, y_min=-2, y_max=2,
            center_point=LEFT*3,
            x_axis_config={"tick_frequency": 0.5},
            plot_depth=-5,
        ).add_coordinates(number_config=nc)
        self.play(FadeOut(axes4), FadeIn(axes))
        self.wait(3)

        self.next_caps()
        self.play(Write(codes[14]))
        self.wait()
        xy_labels = axes.get_axis_labels().set_color(BLACK)
        self.play(Write(xy_labels))
        self.wait(3)
        
        self.next_caps()
        self.wait(2)
        self.next_caps()
        self.play(Write(codes[15]))
        dot = Dot(axes.c2p(1, 2), color=BLUE_D, radius=0.1)
        self.wait()
        self.play(Write(dot))
        self.wait(2)

        self.next_caps()
        self.play(Write(codes[16]))
        self.wait(1)
        self.play(Write(codes[17]))
        self.wait(4)


class NumberPlaneTutorial(Scene_):
    CONFIG = {
        # "fade_all": False,
    }
    def start(self):
        t2c = {"manim": GOLD,
               "NumberPlane": GREEN}
        title = VGroup(
            Text("Chapter III.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("使用NumberPlane构建坐标网格", font="Source Han Sans CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        CodeLine.CONFIG["t2c"].update(numberline_t2c)
        CodeLine.CONFIG["t2c"].update(axes_t2c)
        CodeLine.CONFIG["t2c"].update(numberplane_t2c)
        CodeLine.CONFIG["size"] = 0.48
        captions = [
            "NumberPlane构建的坐标系默认带网格，用法和Axes相同，但一般不做更改",
            "同样使用add_coordinates添加数字标签，c2p与p2c也同样适用",
            "NumberPlane常用于进行变换，可以直接使用apply_function(matrix)进行线性变换",
            "在进行非线性变换前，需要调用prepare_for_nonlinear_transform方法",
            "它有一个子类，ComplexPlane用于展示复平面，用法相同，但是纵轴标签为b·i的形式",
            "使用n2p和p2n来转换坐标与复数（c2p/p2c同时适用）",
            "使用apply_complex_function来施加复变换",
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)\
                    .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in captions
            ]
        )

        codes = CodeLines(
            ">>> grid = NumberPlane(",
            "~~~~~~~~axis_config={\"stroke_color\": BLACK}",
            "~~~~)",
            ">>> grid.add_coordinates()",
            ">>> grid.apply_function(",
            "~~~~~~~~lambda p: p+RIGHT*p[1]",
            "~~~~)",
            ">>> grid.prepare_for_nonlinear_transform()",
            ">>> grid.apply_function(",
            "~~~~~~~~lambda p: p + np.array([",
            "~~~~~~~~~~~~np.sin(p[1]),",
            "~~~~~~~~~~~~np.sin(p[0]),",
            "~~~~~~~~~~~~0,",
            "~~~~~~~~])",
            "~~~~)",
            buff=0.13
        )
        codebg = CodeBackground(codes, buff=0.25)
        VGroup(codes, codebg).to_edge(RIGHT, buff=0.7).shift(UP*0.3)

        grid = NumberPlane(axis_config={"stroke_color": BLACK}, plot_depth=-5)

        self.wait()
        self.play(Write(self.caps[0]))
        self.wait()
        self.play(FadeInFromDown(codebg))
        self.play(Write(codes[:3]))
        self.wait()
        self.play(ShowCreation(grid))
        self.wait(3)

        self.next_caps()
        self.play(Write(codes[3]))
        self.wait()
        labels = grid.get_coordinate_labels(number_config={"color": BLACK})
        labels.set_plot_depth(-5)
        self.play(Write(labels))
        self.wait(3)
        lines = VGroup()
        lines.add(Line(codes[3][4:].get_left(), codes[3][4:].get_right(), color=GRAY, stroke_width=2.5))
        self.play(
            FadeOut(labels),
            ShowCreation(lines[-1])
        )
        
        self.next_caps()
        self.play(Write(VGroup(codes[4], codes[6])))
        self.wait(0.5)
        self.play(Write(codes[5]))
        self.wait(1.5)
        self.play(grid.apply_function,
            lambda p: p + RIGHT*p[1],
            run_time=2
        )
        self.wait(3)
        lines.add(Line(codes[4][4:].get_left(), codes[4][4:].get_right(), color=GRAY, stroke_width=2.5))
        lines.add(Line(codes[5][8:].get_left(), codes[5][8:].get_right(), color=GRAY, stroke_width=2.5))
        lines.add(Line(codes[6][4:].get_left(), codes[6][4:].get_right(), color=GRAY, stroke_width=2.5))
        self.play(
            grid.apply_function,
            lambda p: p - RIGHT*p[1],
            ShowCreation(lines[1]),
            ShowCreation(lines[2]),
            ShowCreation(lines[3]),
            run_time=1
        )

        self.next_caps()
        self.play(Write(codes[7]))
        self.play(WiggleOutThenIn(codes[7]))
        self.wait(2)
        self.play(Write(codes[8:]))
        self.wait()
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait(3)
        self.play(FadeOut(grid), FadeOut(codes), FadeOut(lines), codebg.shift, RIGHT*0.3)
        
        codes = CodeLines(
            ">>> grid = ComplexPlane(",
            "~~~~~~~~axis_config={\"stroke_color\": BLACK}",
            "~~~~)",
            ">>> grid.add_coordinates()",
            ">>> dot = Dot(grid.n2p(-3+2j))",
            ">>> grid.p2n(dot.get_center())",
            "(-3+2j)",
            ">>> grid.prepare_for_nonlinear_transform()",
            ">>> grid.apply_complex_function(",
            "~~~~~~~~lambda z: np.exp(z)",
            "~~~~)",
            buff=0.13
        ).next_to(codebg.get_corner(UL), DR, aligned_edge=UL, buff=0.25)
        self.next_caps()
        self.play(Write(codes[:3]))
        self.wait()
        grid = ComplexPlane(axis_config={"stroke_color": BLACK}, plot_depth=-5)
        self.play(ShowCreation(grid))
        self.wait(2)
        self.play(Write(codes[3]))
        self.wait()
        labels = grid.get_coordinate_labels(number_config={"color": BLACK})
        labels.set_plot_depth(-5)
        self.play(Write(labels))
        self.wait(3)
        self.play(
            FadeOut(labels),
            ShowCreation(Line(codes[3][4:].get_left(), codes[3][4:].get_right(), color=GRAY, stroke_width=2.5))
        )
        self.next_caps()
        self.play(Write(codes[4]))
        self.wait()
        dot = Dot(grid.n2p(-3+2j), radius=0.1, color=BLUE_D)
        self.play(Write(dot))
        self.wait(2)
        self.play(Write(codes[5]))
        self.wait()
        self.play(Write(codes[6]), FadeOut(dot))
        self.wait(3)
        self.next_caps()
        self.play(Write(codes[7:]))
        self.wait()
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_complex_function,
            lambda z: np.exp(z),
            run_time=5
        )
        self.wait(4)


class ParametricFunctionTutorial(Scene_):
    CONFIG = {
        # "fade_all": False,
    }
    def start(self):
        t2c = {"manim": GOLD,
               "ParametricFunction": GREEN}
        title = VGroup(
            Text("Chapter IV.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("使用ParametricFunction绘制参数方程图像", font="Source Han Sans CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        CodeLine.CONFIG["t2c"].update(numberline_t2c)
        CodeLine.CONFIG["t2c"].update(axes_t2c)
        CodeLine.CONFIG["t2c"].update(numberplane_t2c)
        CodeLine.CONFIG["t2c"].update(pf_t2c)
        CodeLine.CONFIG["size"] = 0.55
        captions = [
            "绘制函数图像可以使用ParametricFunction",
            "传入一个参数方程，自变量为参数，返回值为一个点，可以使用def定义函数或者lambda语句",
            "传入t_min和t_max表示参数范围",
            "它有一个子类FunctionGraph，传入一个函数，给出x返回y，并且默认x范围为画面宽度",
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        codes = CodeLines(
            ">>> func = ParametricFunction(",
            "~~~~~~~~lambda t: np.array([",
            "~~~~~~~~~~~~2*np.sin(3*t)*np.cos(t),",
            "~~~~~~~~~~~~2*np.sin(3*t)*np.sin(t),",
            "~~~~~~~~~~~~0,",
            "~~~~~~~~]),",
            "~~~~~~~~t_min=0, t_max=2*PI",
            "~~~~).shift(LEFT*3)",
            ">>> func2 = FunctionGraph(",
            "~~~~~~~~lambda x: x**2",
            "~~~~)",
            buff=0.16
        )
        codebg = CodeBackground(codes, buff=0.25)
        VGroup(codes, codebg).to_edge(RIGHT, buff=0.5).shift(UP*0.3)
        # self.add(codebg, codes)

        self.wait()
        self.play(Write(self.caps[0]))
        self.wait()
        self.play(FadeInFromDown(codebg))
        self.play(Write(VGroup(codes[0], codes[7])))
        self.wait(2)
        self.next_caps()
        self.play(Write(codes[1:6]))
        self.wait(3)
        self.next_caps()
        self.play(Write(codes[6]))
        self.wait()

        t = ValueTracker(0)
        dot = Dot(color=BLACK, background_stroke_color=WHITE, background_stroke_width=2, radius=0.05)
        dot.add_updater(lambda m: m.move_to(
            np.array([
                2*np.sin(3*t.get_value())*np.cos(t.get_value()),
                2*np.sin(3*t.get_value())*np.sin(t.get_value()),
                0
            ])+LEFT*3
        ))
        path = TracedPath(dot.get_center, stroke_color=BLACK, stroke_width=4, plot_depth=-2)
        progress = NumberLine(x_min=0, x_max=2, unit_size=3, tick_frequency=1, color=BLACK).move_to(LEFT*3+DOWN*2.6)
        tick = Triangle(fill_opacity=1).scale(0.2).rotate(PI)
        tick.add_updater(lambda m: m.move_to(progress.n2p(t.get_value() / PI), aligned_edge=DOWN))
        label = VGroup(
            TexMobject("t=", color=BLACK),
            DecimalNumber(0, color=BLACK),
        ).arrange(RIGHT).next_to(progress, RIGHT)
        label[1].add_updater(lambda m: m.set_value(t.get_value()))

        self.add(path)
        self.play(Write(dot))
        self.play(ShowCreation(progress), Write(tick), Write(label))
        self.wait()
        self.play(t.set_value, 2*PI, run_time=10, rate_func=linear)
        self.wait(3)
        self.play(FadeOut(VGroup(dot, progress, tick, label)))
        self.next_caps()
        self.play(Write(codes[8:]))
        self.wait()
        func2 = FunctionGraph(lambda x: x**2, color=GOLD, plot_depth=-5)
        self.play(ShowCreation(func2))
        self.wait(4)
        

class DownProgressBar(Scene_):
    CONFIG = {
        "fade_all": False,
    }
    def construct(self):
        methods_dict = {
            'NumberLine': '0022', 
            'Axes': '0216', 
            'NumberPlane': '0359',
            'ParametricFunction': '0547', 
            'a': '0643'
        }
        total_time = '0655'
        func_time = lambda t: int(t[0:2]) * 60 + int(t[2:])
        func_loc = lambda t: func_time(t)/func_time(total_time) * FRAME_WIDTH * RIGHT + FRAME_WIDTH * LEFT / 2
        p_list = [FRAME_WIDTH * LEFT / 2]
        for v in methods_dict.values():
            p_list.append(func_loc(v))
        p_list.append(func_loc(total_time))

        colors = color_gradient([BLUE, PINK, RED, ORANGE, GREEN], len(methods_dict)+1)

        lines = VGroup(*[Line(p_list[i], p_list[i+1]-0.02*RIGHT, color=colors[i], stroke_width=20) for i in range(len(methods_dict)+1)])
        lines.to_edge(DOWN * 0.22, buff=1)
        texts = VGroup(*[Text(t, color=WHITE, font='Consolas', size=0.33) for t in methods_dict.keys()], plot_depth=1)
        texts[-1].set_color(colors[-1])
        text = Text('空降', color=WHITE, font='庞门正道标题体', size=0.44).to_edge(DOWN * 0.132, buff=1).to_edge(LEFT, buff=0.53)
        text[1].shift(RIGHT*0.03)
        text[0].shift(LEFT*0.01)
        for i in range(len(methods_dict)):
            texts[i].move_to(lines[i+1])

        self.add(lines, texts, text)


class VideoCover(Scene):
    def construct(self):
        background = Polygon(
            LEFT_SIDE * 2 + BOTTOM, BOTTOM, LEFT_SIDE / 2 + TOP, LEFT_SIDE * 2 + TOP,
            fill_opacity=0.7, fill_color=BLACK, stroke_width=0
        ).shift(RIGHT)
        text = VGroup(
            Text("manim教程", font="庞门正道标题体", color=BLUE, size=2).scale(0.9),
            Text("第五讲", font="庞门正道标题体", color=BLUE, size=2).scale(1.1),
            Text("坐标系统与图像", font="庞门正道标题体", color=ORANGE, size=2).scale(1.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        text[2].shift(DOWN*0.4)
        text.center().to_edge(LEFT, buff=0.8).shift(UP*0.5)
        text2 = VGroup(
            Text("manim教程", font="庞门正道标题体", color=BLUE, size=2).scale(0.9).set_stroke(width=12, opacity=0.4),
            Text("第五讲", font="庞门正道标题体", color=BLUE, size=2).scale(1.1).set_stroke(width=12, opacity=0.4),
            Text("坐标系统与图像", font="庞门正道标题体", color=ORANGE, size=2).scale(1.5).set_stroke(width=13, opacity=0.4)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        text2[2].shift(DOWN*0.4)
        text2.center().to_edge(LEFT, buff=0.8).shift(UP*0.5)
        self.add(background, text2, text)


class PreView(Scene_):
    CONFIG = {
        "fade_all": False
    }
    def construct(self):
        grid = NumberPlane(plot_depth=-5)
        self.wait(0.5)
        self.play(ShowCreation(grid, run_time=3, lag_ratio=0.1))

        t = ValueTracker(0)
        dot = Dot(color=BLACK, background_stroke_color=WHITE, background_stroke_width=2, radius=0.06)
        dot.add_updater(lambda m: m.move_to(
            np.array([
                2*np.sin(3*t.get_value())*np.cos(t.get_value()),
                2*np.sin(3*t.get_value())*np.sin(t.get_value()),
                0
            ])
        ))
        path = TracedPath(dot.get_center, stroke_color=BLACK, stroke_width=6, plot_depth=-2)
        progress = NumberLine(x_min=0, x_max=2, unit_size=3, tick_frequency=1, color=BLACK).move_to(DOWN*2.6)
        tick = Triangle(fill_opacity=1).scale(0.2).rotate(PI)
        tick.add_updater(lambda m: m.move_to(progress.n2p(t.get_value() * 2 / PI), aligned_edge=DOWN))
        label = VGroup(
            TexMobject("t=", color=BLACK),
            DecimalNumber(0, color=BLACK),
        ).arrange(RIGHT).next_to(progress, RIGHT)
        label[1].add_updater(lambda m: m.set_value(t.get_value()))

        self.add(path)
        self.play(Write(dot))
        self.play(ShowCreation(progress), Write(tick), Write(label))
        self.wait(0.5)
        self.play(t.set_value, PI, run_time=6, rate_func=linear)
        self.wait()
        self.play(FadeOut(VGroup(dot, progress, tick, label)))

        func = FunctionGraph(lambda x: x**2-4, stroke_width=6, color=GOLD)
        func2 = FunctionGraph(lambda x: 2*np.exp(1)**(-0.25*x**2), stroke_width=6, color=RED)
        self.play(ShowCreation(func), run_time=2)
        self.wait(0.5)
        self.play(ShowCreation(func2), run_time=2)
        self.wait()
        title = VGroup(
            Text("NumberLine()", font="Consolas", color=BLUE_D, t2c={"()": DARK_GRAY}, size=2),
            Text("Axes()", font="Consolas", color=BLUE_D, t2c={"()": DARK_GRAY}, size=2),
            Text("NumberPlane()", font="Consolas", color=BLUE_D, t2c={"()": DARK_GRAY}, size=2),
            Text("ParametricFunction()", font="Consolas", color=BLUE_D, t2c={"()": DARK_GRAY}, size=2),
        ).arrange(DOWN, aligned_edge=LEFT).center()
        bg = BackgroundRectangle(title, color=WHITE, fill_opacity=0.85, buff=0.25)
        self.play(
            FadeInFromDown(bg),
            *[
                FadeInFromDown(each) for each in title
            ],
            run_time=2, lag_ratio=0.5
        )
        self.wait(3)


class NPBG(Scene_):
    CONFIG = {
        "fade_all": False,
    }
    def construct(self):
        grid = NumberPlane(axis_config={"stroke_color": BLACK})
        func = FunctionGraph(lambda x: x**2-4, stroke_width=6, color=GOLD)
        func2 = FunctionGraph(lambda x: 2*np.exp(1)**(-0.25*x**2), stroke_width=6, color=RED)
        self.add(grid, func2)


class NPBG2(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": "#EBEBEB"
        }
    }
    def construct(self):
        grid = NumberPlane(axis_config={"stroke_color": BLACK})
        grid.prepare_for_nonlinear_transform()
        grid.apply_function(
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ])
        )
        self.add(grid)


class NPBG3(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": "#EBEBEB"
        }
    }
    def construct(self):
        grid = NumberPlane(axis_config={"stroke_color": BLACK})
        grid.prepare_for_nonlinear_transform()
        grid.apply_complex_function(
            lambda z: np.exp(z)
        )
        self.add(grid)


class NPBG4(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": "#EBEBEB"
        }
    }
    def construct(self):
        rec = ScreenRectangle(color=DARK_GRAY, height=6)
        self.add(rec)
