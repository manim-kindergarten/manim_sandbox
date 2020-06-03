# from @鹤翔万里

from manimlib.imports import *
from manim_sandbox.utils.imports import *

class Intro(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        t2c = {
            "线簇": BLUE,
            "包络线": GOLD,
            "曲线": GREEN
        }
        text = VGroup(
            Text("无数条同类型线组成一簇线簇", font="思源黑体 CN Medium", color=BLACK, t2c=t2c, size=0.45),
            Text("若存在一条曲线 该曲线处处与线簇中的一条线相切", font="思源黑体 CN Medium", color=BLACK, t2c=t2c, size=0.45),
            Text("则这条曲线为这个线簇的包络线", font="思源黑体 CN Medium", color=BLACK, t2c=t2c, size=0.45)
        ).arrange(DOWN, buff=0.4).shift(UP*2.6)
        intro = VGroup(
            Text("那么现在", font="庞门正道标题体", color=BLACK, t2c=t2c, size=0.8),
            Text("来欣赏十二个包络线动画吧", font="庞门正道标题体", color=BLACK, t2c=t2c, size=0.8)
        ).arrange(DOWN, buff=0.8).center()

        self.wait()
        for t in text:
            self.play(Write(t))
            self.wait(2)
        self.wait(5)
        self.play(Transform(text, intro))
        self.wait(3)


class VideoCover(Scene):
    def construct(self):
        background = Rectangle(width=18, height=3.5, fill_opacity=0.7, fill_color=BLACK, stroke_width=0).shift(DOWN*0.5)
        title = VGroup(
            Text("十二例", font="庞门正道标题体", color=BLUE).scale(1.1),
            Text("包 络 线", font="庞门正道标题体", color=ORANGE).scale(1.5)
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        title_bg = VGroup(
            Text("十二例", font="庞门正道标题体", color=BLUE_B).scale(1.1).set_stroke(width=12, opacity=0.4),
            Text("包 络 线", font="庞门正道标题体", color=ORANGE).scale(1.5).set_stroke(width=12, opacity=0.4)
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        title.to_edge(RIGHT, buff=1.6).shift(DOWN*0.5)
        title_bg.to_edge(RIGHT, buff=1.6).shift(DOWN*0.5)
        self.add(background, title_bg, title)


class Anim1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅰ. 抛物线", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("fdd.png").set_height(0.8),
            Text("@范滇东", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*4)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim2(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅱ. 抛物线", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("Fe.png").set_height(0.8),
            Text("@二茂铁Fe", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*4)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim3(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅲ. 椭圆", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("Tony.png").set_height(0.8),
            Text("@鹤翔万里", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*4)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim4(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅳ. 椭圆", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("xwx.png").set_height(0.8),
            Text("@爱动脑的小王欣", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*5)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim5(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅴ. 椭圆", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("lz.png").set_height(0.8),
            Text("@心灵的绿洲zveabh", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*5)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim6(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅵ. 双曲线", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("widcardw.png").set_height(0.8),
            Text("@widcardw", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*4)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim7(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅶ. 蜗线", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("widcardw.png").set_height(0.8),
            Text("@widcardw", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*4)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim8(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅷ. 外摆线", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("tf.png").set_height(0.8),
            Text("@有一种悲伤叫颓废", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*5)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim9(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅸ. 三角星形线", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("SV.png").set_height(0.8),
            Text("@Shy_Vector", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*5)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim10(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅹ. 四角星形线", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("mp.jpg").set_height(1.2),
            Text("@Micoael_Primo", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*5)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim11(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅺ. 追逐曲线", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("zgh.jpg").set_height(0.8),
            Text("@zgh2000", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*5)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class Anim12(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        title = Text("Ⅻ. 齿轮", font="庞门正道标题体", color=BLACK, size=0.7)
        author = Group(
            ImageMobject("cigar.png").set_height(0.8),
            Text("@cigar666", font="思源宋体 CN Medium", color=BLUE_E, size=0.5)
        ).arrange(RIGHT, buff=0.1).next_to(title, DOWN).save_state()
        author.shift(RIGHT*5)
        self.add(author)
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(author.restore)
        self.wait(5)


class End(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        thanks = Text("感 谢 观 看", font="庞门正道标题体", color=BLUE_E, size=1.2)
        code = Text("代码见 https://github.com/manim-kindergarten/manim_sandbox",font="思源宋体 CN Medium",color=GOLD,size=0.4)
        code.next_to(thanks, DOWN, buff=1)
        self.wait()
        self.play(DrawBorderThenFill(thanks))
        self.wait()
        self.play(FadeInFromDown(code))
        self.wait(5)
