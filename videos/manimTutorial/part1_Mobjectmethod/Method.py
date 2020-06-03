from manimlib.imports import *
from manim_sandbox.utils.imports import *
        

class VideoCover(Scene):
    def construct(self):
        background = Rectangle(width=18, height=3.5, fill_opacity=0.7, fill_color=BLACK, stroke_width=0).shift(DOWN*0.5)
        title = VGroup(
            Text("manim教程", font="庞门正道标题体", color=BLUE).scale(1),
            Text("物体的位置与变换", font="庞门正道标题体", color=ORANGE).scale(1.3)
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        title_bg = VGroup(
            Text("manim教程", font="庞门正道标题体", color=BLUE_B).scale(1).set_stroke(width=12, opacity=0.4),
            Text("物体的位置与变换", font="庞门正道标题体", color=ORANGE).scale(1.3).set_stroke(width=12, opacity=0.4)
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.4)
        title.to_edge(RIGHT, buff=1.6).shift(DOWN*0.5)
        title_bg.to_edge(RIGHT, buff=1.6).shift(DOWN*0.5)
        self.add(background, title_bg, title)


class Logo_(Scene):
    CONFIG = {
        "font": "Orbitron",
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
        logo.save_state()

        self.wait(1)
        self.play(DrawBorderThenFill(VGroup(text, logo)), run_time=5)
        self.wait(30)
        self.play(Uncreate(VGroup(text, logo)))
        self.wait(1)


class Red(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": "#5D0001"
        }
    }


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
            ["序. 坐标与位置", "Tony.png", "@鹤翔万里"],
            ["Ⅰ. shift与move_to", "Tony.png", "@鹤翔万里"],
            ["Ⅱ. scale", "widcardw.png", "@widcardw"],
            ["Ⅲ. rotate", "wings.png", "@深蓝初衷"],
            ["Ⅳ. flip", "cigar.png", "@cigar666"],
            ["Ⅴ. stretch", "widcardw.png", "@widcardw"],
            ["Ⅵ. to_corner与to_edge", "cz.png", "@这个橙子好酸"],
            ["Ⅶ. align_to", "fqc.png", "@Fu_Qingchen"],
            ["Ⅷ. next_to", "mp.jpg", "@Micoael_Primo"],
            ["Ⅸ. set_width与set_height", "coreress.png", "@Coreress"]
        ]
        staff_mob = VGroup(*[VGroup() for _ in range(4)])
        for i in range(5):
            staff_mob[0].add(Text(staff[i][0], font="庞门正道标题体", size=0.35, color=BLACK))
            staff_mob[1].add(Text(staff[i][2], font="思源宋体 CN Medium", size=0.3, color=BLUE_E))
        for i in range(5, 10):
            staff_mob[2].add(Text(staff[i][0], font="庞门正道标题体", size=0.35, color=BLACK))
            staff_mob[3].add(Text(staff[i][2], font="思源宋体 CN Medium", size=0.3, color=BLUE_E))
        for i in range(4):
            staff_mob[i].arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        staff_mob.arrange(RIGHT)
        VGroup(staff_mob[:2]).shift(LEFT*0.5)
        VGroup(staff_mob[2:]).shift(RIGHT*0.5)

        self.wait()
        self.play(Write(title))
        self.wait()
        for i in range(5):
            self.play(
                Write(VGroup(staff_mob[0][i], staff_mob[1][i])),
                run_time=0.25
            )
        for i in range(5):
            self.play(
                Write(VGroup(staff_mob[2][i], staff_mob[3][i])),
                run_time=0.25
            )
        self.wait(5)
        self.play(FadeOutAndShift(VGroup(*self.mobjects)))
        self.wait()


