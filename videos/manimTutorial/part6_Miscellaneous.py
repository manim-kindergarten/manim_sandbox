from manimlib.imports import *
from manim_sandbox.utils.imports import *
from manim_sandbox.videos.manimTutorial.utils import *
from manim_projects.tony_useful.imports import *


tracedpath_t2c = {
    "TracedPath": BLUE_D,
    "get_center": BLUE_D,
    "min_distance_to_new_point": ORANGE,
    "Dot": BLUE_D,
    "BLUE_D": BLUE_E,
    "stroke_color": ORANGE,
    "stroke_width": ORANGE,
    "Rotating": BLUE_D,
    "radians": ORANGE,
    "about_point": ORANGE,
    "PI": PURPLE,
    "run_time": ORANGE,
}

decimalnumber_t2c = {
    "DecimalNumber": BLUE_D,
    
}


class OpeningScene(Scene_):
    def construct(self):
        t2c = {"manim": average_color(PINK, RED),
               "剩余": BLUE, "物体": GREEN}
        text_color = DARK_GRAY

        font = "庞门正道标题体"
        text_1 = Text("大家好!", font=font, color=text_color, size=2, t2c=t2c).to_edge(UP * 2, buff=1)
        text_2 = Text("欢迎来到manim视频教程", font=font,
                      color=text_color, size=2, t2c=t2c).to_edge(UP * 3.2, buff=1)
        text_3 = Text("这一期我们将学习manim中", font=font, color=text_color, size=2, t2c=t2c).to_edge(UP * 1.8, buff=1)
        text_4 = Text("剩余的常用物体", font=font, color=text_color, size=2, t2c=t2c).to_edge(UP * 3., buff=1)
        text_34, text_12 = VGroup(text_3, text_4), VGroup(text_1, text_2)


        methods = [["TracedPath", "DecimalNumber", "Integer"],
                   ["shape_matchers: ", "SurroundingRectangle, "],
                   ["BackgroundRectangle, ", "Cross, ", "Brace, "],
                   ["BraceLabel, ", "BraceText, ", "Underline"]]
        m_group_1 = VGroup(*[Text(tex + ', ', size=0.84, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[0]]).arrange(RIGHT)
        m_group_2 = VGroup(*[Text(tex, size=0.84, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[1]]).arrange(RIGHT)
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


class TracedPathTutorial(Scene_):
    CONFIG = {
        # "fade_all": False,
        "en": True,
    }
    def start(self):
        t2c = {"manim": GOLD,
               "TracedPath": GREEN}
        title = VGroup(
            Text("Chapter Ⅰ.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("使用TracedPath记录移动轨迹", font="Source Han Sans CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        title_en = VGroup(
            Text("Chapter Ⅰ.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("Use TracedPath to trace a path", font="Source Han Sans CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        if self.en:
            title = title_en
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        CodeLine.CONFIG["t2c"].update(tracedpath_t2c)
        CodeLine.CONFIG["size"] = 0.55
        captions = [
            "在manim中可以使用TracedPath来记录一个点运动的轨迹",
            "传入一个没有输入的函数，返回值为坐标，一般使用get_center等获取位置的函数",
            "可以传入关键字参数来修改路径的样式",
            "特有的min_distance_to_new_point参数表示两点之间的最小距离(默认为0.1)",
            "新点距离旧点距离小于此值的将会被舍去",
            "但是曲线的精度只能通过运动速度来调节，速度过快则会出现折角"
        ]
        captions_en = [
            "TracedPath can be used in manim to record the trajectory of a point movement",
            "Pass in a function without input, generally use methods such as get_center to get the position",
            "We can pass in kwargs to modify the style of the path",
            "min_distance_to_new_point parameter indicates the minimum distance between two points",
            "The new point whose distance from the old point is less than this value will be discarded",
            "But the accuracy of the path can only be adjusted by the speed of the movement"
        ]
        if self.en:
            captions = captions_en
        self.caps = VGroup(
            *[
                CodeLine(
                    cap, 
                    font='Source Han Sans CN Bold', 
                    size=0.64 if not self.en else 0.58
                ).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        codes = CodeLines(
            ">>> dot = Dot().shift(LEFT*2)",
            ">>> path = TracedPath(",
            "~~~~~~~~dot.get_center,",
            "~~~~~~~~stroke_color=BLUE_D, stroke_width=4,",
            "~~~~~~~~min_distance_to_new_point=0.1",
            "~~~~)",
            ">>> self.play(dot.shift, UP*2)",
            ">>> self.play(Rotating(dot, radians=PI,",
            "~~~~~~~~about_point=LEFT*2))",
            ">>> self.play(Rotating(dot, radians=PI,",
            "~~~~~~~~about_point=LEFT*2), run_time=0.25)"
        )
        codebg = CodeBackground(codes, buff=0.25)
        VGroup(codes, codebg).to_edge(RIGHT, buff=0.7).shift(UP*0.35)
        dot = Dot(color=BLUE_E, background_stroke_color=WHITE, background_stroke_width=2).shift(LEFT*2)
        path = TracedPath(dot.get_center, stroke_color=BLUE_D, stroke_width=4, plot_depth=-10)
        self.add(path)

        self.wait()
        self.play(Write(self.caps[0]))
        self.play(FadeInFromDown(codebg))
        self.play(Write(codes[0]))
        self.play(Write(dot))
        self.wait()
        self.play(Write(VGroup(codes[1], codes[5])))
        self.wait(2)
        self.next_caps()
        self.play(Write(codes[2]))
        self.wait(4)
        self.next_caps()
        self.play(Write(codes[3]))
        self.wait(4)
        self.next_caps()
        self.play(Write(codes[4]))
        self.wait()
        self.next_caps()
        self.wait(3)
        self.add(path)
        self.play(Write(codes[6]))
        self.wait()
        self.play(dot.shift, UP*2)
        self.wait(2)
        self.play(Write(VGroup(codes[7], codes[8])))
        self.wait()
        self.play(Rotating(dot, radians=PI, about_point=LEFT*2))
        self.wait(3)
        self.next_caps()
        self.play(Write(VGroup(codes[9], codes[10])))
        self.wait()
        self.play(Rotating(dot, radians=PI, about_point=LEFT*2), run_time=0.25)
        self.wait(4)


class DecimalNumberTutorial(Scene_):
    CONFIG = {
        "fade_all": False,
        "en": False,
    }
    def start(self):
        t2c = {"manim": GOLD,
               "DecimalNumber": GREEN}
        title = VGroup(
            Text("Chapter ⅠI.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("使用DecimalNumber来显示数字", font="Source Han Sans CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        title_en = VGroup(
            Text("Chapter ⅠI.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("Use DecimalNumber to display numbers", font="Source Han Sans CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        if self.en:
            title = title_en
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        CodeLine.CONFIG["t2c"].update(decimalnumber_t2c)
        CodeLine.CONFIG["size"] = 0.55
        captions = [
            ""
        ]
        captions_en = [
            ""
        ]
        if self.en:
            captions = captions_en
        self.caps = VGroup(
            *[
                CodeLine(
                    cap, 
                    font='Source Han Sans CN Bold', 
                    size=0.64 if not self.en else 0.58
                ).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
