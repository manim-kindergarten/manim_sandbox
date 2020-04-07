# from @cigar666

from manimlib.imports import *
from manim_sandbox.videos.HomeworkVol04.test_present_style import *

class Explain_Flip_2d(Scene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):

        self.set_camera_orientation(distance=1000)

        captions = [
            "往场景中添加一个奇怪的物体（用mob表示）",
            "mob.flip()的默认效果如图，",
            "它将mob进行了左右翻转，对称轴为过其中心的竖直直线",
            "我们可以通过调整一些参数修改来对称轴方向及经过的点",
            "通过axis我们可以修改翻转时对称轴的方向",
            "比如我们将axis设为RIGHT，那么对称轴为水平向右，物体则被上下翻转",
            "通过about_point我们能定义对称轴的位置",
            "比如我们使axis=RIGHT且about_point=ORIGIN",
            "则对称轴为水平过原点的直线，此时mob沿对称轴被上下翻转",
            "我们也可以同时修改这两个参数来得到沿任意轴的翻折效果，如图所示",
            ]

        t2c_02 = {'axis': PINK, 'about_point': PINK}
        captions_mob = VGroup(
            *[
                CodeLine(cap, font='思源黑体 Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        axes = ThreeDAxes(
            color=BLACK,
            x_min=-FRAME_X_RADIUS, x_max=FRAME_X_RADIUS,
            y_min=-FRAME_Y_RADIUS, y_max=FRAME_Y_RADIUS,
            number_line_config={"color": BLACK}
        ).set_stroke(width=2)

        emote = Emote_new(color=BLACK, height=2.4).shift(LEFT * 3 + UP * 1.6)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=2)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        loc = UP * 2.9 + RIGHT * 2.64
        tex_add = CodeLine('self.add(mob)').move_to(loc)
        tex_flip = CodeLine('mob.flip()').next_to(tex_add, DOWN).align_to(tex_add, LEFT)
        tex_flip_1 = CodeLine('mob.flip(axis=RIGHT)').next_to(tex_flip, DOWN).align_to(tex_flip, LEFT)
        tex_flip_2 = CodeLine('mob.flip(axis=RIGHT,').next_to(tex_flip_1, DOWN).align_to(tex_flip_1, LEFT)
        tex_flip_2_ = CodeLine('about_point=ORIGIN)').next_to(tex_flip_2, DOWN).align_to(tex_flip_2, LEFT)
        tex_flip_3 = CodeLine('mob.flip(axis=UR,').next_to(tex_flip_2_, DOWN).align_to(tex_flip_2_, LEFT)
        tex_flip_3_ = CodeLine('about_point=LEFT*2.5)').next_to(tex_flip_3, DOWN).align_to(tex_flip_3, LEFT)

        self.wait()
        self.play(FadeInFromDown(tex_bg), ShowCreation(axes), run_time=1.5)
        self.wait(0.8)
        self.play(Write(tex_add), Write(captions_mob[0]), run_time=1.8)
        self.wait(0.2)
        self.play(WiggleOutThenIn(emote), run_time=1)
        self.wait(0.8)

        # 默认效果
        direction = UP
        about_p = emote.get_center() + DOWN * 0.3 + RIGHT * 0.1
        dot = Dot(about_p, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]), Write(tex_flip), run_time=1.5)
        self.wait(0.4)
        self.play(emote.flip, {'about_point': about_p}, run_time=1.8)
        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]), run_time=1.2)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line), run_time=1.2)
        self.wait(1)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=1.2)
        self.wait(1.2)
        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]), run_time=1.2)
        self.wait(2.4)

        # 上下翻转
        direction = RIGHT
        about_p = emote.get_center() + DOWN * 0.3 - RIGHT * 0.1
        dot = Dot(about_p, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]), Write(tex_flip_1), run_time=1.2)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line))
        self.wait(0.6)
        self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.8)
        self.wait(0.6)
        self.play(ReplacementTransform(captions_mob[4], captions_mob[5]), run_time=1.2)
        self.wait(0.2)
        self.play(WiggleOutThenIn(axis_line))
        self.wait(0.5)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=1.2)
        self.wait(0.8)
        self.play(ReplacementTransform(captions_mob[5], captions_mob[6]), run_time=1.2)
        self.wait(1.5)

        # 关于y=0上下翻转
        direction = RIGHT * 2.
        about_p = LEFT * 2.5
        dot = Dot(ORIGIN, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(ReplacementTransform(captions_mob[6], captions_mob[7]), Write(tex_flip_2), run_time=1.2)
        self.play(Write(tex_flip_2_))
        self.wait(0.2)
        self.play(TransformFromCopy(tex_flip_2_, dot), run_time=1.5)
        self.wait(0.6)
        self.play(ShowCreation(axis_line), run_time=1.)
        self.wait(0.4)
        self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.8)
        self.wait()
        self.play(ReplacementTransform(captions_mob[7], captions_mob[8]), run_time=1.2)
        self.wait(0.2)
        self.play(WiggleOutThenIn(axis_line))
        self.play(WiggleOutThenIn(dot))
        self.wait(0.5)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=1.25)
        self.wait(1)

        # 自定义对称轴
        direction = UR * 1.2
        about_p = LEFT * 3.5 + DOWN
        dot = Dot(LEFT * 2.5, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(ReplacementTransform(captions_mob[8], captions_mob[9]), Write(tex_flip_3), run_time=1.2)
        self.play(Write(tex_flip_3_))
        self.wait(0.2)
        self.play(TransformFromCopy(tex_flip_3_, dot), run_time=1.5)
        self.wait(0.6)
        self.play(ShowCreation(axis_line))
        self.wait(0.4)
        self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.8)
        self.wait(0.25)
        self.play(WiggleOutThenIn(axis_line))
        self.play(WiggleOutThenIn(dot))
        self.wait(0.5)
        self.play(FadeOut(axis_line), FadeOut(dot), un_time=1.2)

        self.wait(4)

class Explain_Flip_3d(ThreeDScene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "open_plot_depth": False,
        }
    }

    def construct(self):

        # captions = [
        #     "往场景中添加一个奇怪的物体（用mob表示）",
        #     "mob.flip()的默认效果如图，",
        #     "它将mob进行了左右翻转，对称轴为过其中心的竖直直线",
        #     "我们可以通过调整一些参数修改来对称轴方向及经过的点",
        #     "通过axis我们可以修改翻转时对称轴的方向",
        #     "比如我们将axis设为RIGHT，那么对称轴为水平向右，物体则被上下翻转",
        #     "通过about_point我们能定义对称轴的位置",
        #     "如我们使axis=RIGHT且about_point=ORIGIN，",
        #     "则对称轴为水平过原点的直线，此时mob沿对称轴被上下翻转",
        #     "我们也可以同时修改这两个参数来得到沿任意轴的翻折效果，如图所示",
        #     ]

        captions = [
            "flip变换实际上是用在三维空间中的旋转变换实现的",
            "这样在降维打击后的二维场景中就反映出对称翻折的效果",
            "让我们在三维场景下细品一下刚才的操作",
            ]

        captions_mob = VGroup(
            *[
                CodeLine(cap, font='思源黑体 Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        axes = ThreeDAxes(
            color=BLACK,
            x_min=-FRAME_X_RADIUS, x_max=FRAME_X_RADIUS,
            y_min=-FRAME_Y_RADIUS, y_max=FRAME_Y_RADIUS,
            number_line_config={"color": BLACK}
        ).set_stroke(width=2)

        self.camera.add_fixed_in_frame_mobjects(captions_mob)

        emote = Emote_new(color=BLACK, height=2.4).shift(LEFT * 3 + UP * 1.6)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=2)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        loc = UP * 2.9 + RIGHT * 2.64
        tex_add = CodeLine('self.add(mob)').move_to(loc)
        tex_flip = CodeLine('mob.flip()').next_to(tex_add, DOWN).align_to(tex_add, LEFT)
        tex_flip_1 = CodeLine('mob.flip(axis=RIGHT)').next_to(tex_flip, DOWN).align_to(tex_flip, LEFT)
        tex_flip_2 = CodeLine('mob.flip(axis=RIGHT,').next_to(tex_flip_1, DOWN).align_to(tex_flip_1, LEFT)
        tex_flip_2_ = CodeLine('about_point=ORIGIN)').next_to(tex_flip_2, DOWN).align_to(tex_flip_2, LEFT)
        tex_flip_3 = CodeLine('mob.flip(axis=UR,').next_to(tex_flip_2_, DOWN).align_to(tex_flip_2_, LEFT)
        tex_flip_3_ = CodeLine('about_point=LEFT*2.5)').next_to(tex_flip_3, DOWN).align_to(tex_flip_3, LEFT)
        tex_group = VGroup(tex_bg, tex_add, tex_flip, tex_flip_1, tex_flip_2, tex_flip_2_, tex_flip_3, tex_flip_3_)
        self.camera.add_fixed_in_frame_mobjects(tex_group)

        self.wait()
        self.play(Write(captions_mob[0]), run_time=1.5)
        self.wait(2)
        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]), run_time=1.)
        self.wait(0.5)
        self.play(ShowCreation(axes))
        self.wait(1.5)
        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]), FadeInFromDown(tex_bg), run_time=1.)
        self.wait(0.6)
        self.play(Write(tex_add), run_time=1.)
        self.wait(0.1)
        self.play(WiggleOutThenIn(emote), run_time=1)
        self.wait(0.5)
        self.move_camera(phi=54*DEGREES, theta=-140*DEGREES)

        # 默认效果
        direction = UP
        about_p = emote.get_center() + DOWN * 0.3 + RIGHT * 0.1
        dot = Dot(about_p, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(Write(tex_flip), run_time=1.)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line), run_time=1.)
        self.wait(0.2)
        # self.play(emote.flip, {'about_point': about_p}, run_time=1.5)
        self.play(Rotating(emote, radians=PI, axis=direction, about_point=about_p, run_time=1.5))
        self.wait(0.2)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=1.)
        self.wait(0.9)

        # 上下翻转
        direction = RIGHT
        about_p = emote.get_center() + DOWN * 0.3 - RIGHT * 0.1
        dot = Dot(about_p, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(Write(tex_flip_1), run_time=1.)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line))
        self.wait(0.2)
        # self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.5)
        self.play(Rotating(emote, radians=PI, axis=direction, about_point=about_p, run_time=1.5))
        self.wait(0.2)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=1.)
        self.wait(0.9)

        # 关于y=0上下翻转
        direction = RIGHT * 2.
        about_p = LEFT * 2.5
        dot = Dot(ORIGIN, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(Write(tex_flip_2), run_time=1.)
        self.play(Write(tex_flip_2_), run_time=0.8)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line))
        self.wait(0.2)
        # self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.5)
        self.play(Rotating(emote, radians=PI, axis=direction, about_point=about_p, run_time=1.5))
        self.wait(0.2)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=1.)
        self.wait(0.9)

        # 自定义对称轴
        direction = UR * 1.2
        about_p = LEFT * 3.5 + DOWN
        dot = Dot(LEFT * 2.5, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(Write(tex_flip_3), run_time=1.)
        self.play(Write(tex_flip_3_), run_time=0.8)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line))
        self.wait(0.2)
        # self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.5)
        self.play(Rotating(emote, radians=PI, axis=direction, about_point=about_p, run_time=1.5))
        self.wait(0.2)
        self.play(FadeOut(axis_line), FadeOut(dot), un_time=1.)
        self.wait(2.)
        self.move_camera(phi=0*DEGREES, theta=-90*DEGREES)
        self.wait(2.)

class Explain_Flip(ThreeDScene):

    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "open_plot_depth": False,
        }
    }

    def construct(self):

        captions = [
            "往场景中添加一个奇怪的物体（用mob表示）",
            "mob.flip()的默认效果如图，",
            "它将mob进行了左右翻转，对称轴为过其中心的竖直直线",
            "我们可以通过调整一些参数修改来对称轴方向及经过的点",
            "通过axis我们可以修改翻转时对称轴的方向",
            "比如我们将axis设为RIGHT，那么对称轴为水平向右，物体则被上下翻转",
            "通过about_point我们能定义对称轴的位置",
            "比如我们使axis=RIGHT且about_point=ORIGIN，",
            "则对称轴为水平过原点的直线，此时mob沿对称轴被上下翻转",
            "我们也可以同时修改这两个参数来得到沿任意对称轴的翻折效果，如图所示",
            ]
        t2c_02 = {'axis': PINK, 'about_point': PINK, '对称轴': ORANGE, "翻转": BLUE_D}
        captions_mob = VGroup(
            *[
                CodeLine(cap, font='思源黑体 Bold', size=0.32).to_edge(DOWN * 1.2).set_color_by_t2c(t2c_02)
                for cap in captions
            ]
        )
        axes = ThreeDAxes(
            color=BLACK,
            x_min=-FRAME_X_RADIUS, x_max=FRAME_X_RADIUS,
            y_min=-FRAME_Y_RADIUS, y_max=FRAME_Y_RADIUS,
            number_line_config={"color": BLACK}
        ).set_stroke(width=2)

        emote = Emote_new(color=BLACK, height=2.4).shift(LEFT * 3 + UP * 1.6)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=2)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        loc = UP * 2.9 + RIGHT * 2.64
        tex_add = CodeLine('self.add(mob)').move_to(loc)
        tex_flip = CodeLine('mob.flip()').next_to(tex_add, DOWN).align_to(tex_add, LEFT)
        tex_flip_1 = CodeLine('mob.flip(axis=RIGHT)').next_to(tex_flip, DOWN).align_to(tex_flip, LEFT)
        tex_flip_2 = CodeLine('mob.flip(axis=RIGHT,').next_to(tex_flip_1, DOWN).align_to(tex_flip_1, LEFT)
        tex_flip_2_ = CodeLine('about_point=ORIGIN)').next_to(tex_flip_2, DOWN).align_to(tex_flip_2, LEFT)
        tex_flip_3 = CodeLine('mob.flip(axis=UR,').next_to(tex_flip_2_, DOWN).align_to(tex_flip_2_, LEFT)
        tex_flip_3_ = CodeLine('about_point=LEFT*2.5)').next_to(tex_flip_3, DOWN).align_to(tex_flip_3, LEFT)

        self.wait()
        self.play(FadeInFromDown(tex_bg), ShowCreation(axes), run_time=1.5)
        self.wait(0.8)
        self.play(Write(tex_add), Write(captions_mob[0]), run_time=1.8)
        self.wait(0.2)
        self.play(WiggleOutThenIn(emote), run_time=1)
        self.wait(0.8)

        # 默认效果
        direction = UP
        about_p = emote.get_center() + DOWN * 0.3 + RIGHT * 0.1
        dot = Dot(about_p, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]), Write(tex_flip), run_time=1.5)
        self.wait(0.4)
        self.play(emote.flip, {'about_point': about_p}, run_time=1.8)
        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]), run_time=1.2)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line), run_time=1.2)
        self.wait(1)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=1.2)
        self.wait(0.8)
        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]), run_time=1.2)
        self.wait(2.2)

        # 上下翻转
        direction = RIGHT
        about_p = emote.get_center() + DOWN * 0.3 - RIGHT * 0.1
        dot = Dot(about_p, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]), Write(tex_flip_1), run_time=1.2)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line))
        self.wait(0.6)
        self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.8)
        self.wait(0.6)
        self.play(ReplacementTransform(captions_mob[4], captions_mob[5]), run_time=1.2)
        self.wait(0.2)
        self.play(WiggleOutThenIn(axis_line))
        self.wait(0.5)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=1.2)
        self.wait(0.8)
        self.play(ReplacementTransform(captions_mob[5], captions_mob[6]), run_time=1.2)
        self.wait(2)

        # 关于y=0上下翻转
        direction = RIGHT * 2.
        about_p = LEFT * 2.5
        dot = Dot(ORIGIN, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(ReplacementTransform(captions_mob[6], captions_mob[7]), Write(tex_flip_2), run_time=1.2)
        self.play(Write(tex_flip_2_))
        self.wait(0.2)
        self.play(TransformFromCopy(tex_flip_2_, dot), run_time=1.5)
        self.wait(0.6)
        self.play(ShowCreation(axis_line), run_time=1.)
        self.wait(0.4)
        self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.8)
        self.wait()
        self.play(ReplacementTransform(captions_mob[7], captions_mob[8]), run_time=1.2)
        self.wait(0.2)
        self.play(WiggleOutThenIn(axis_line))
        self.play(WiggleOutThenIn(dot))
        self.wait(0.5)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=1.25)
        self.wait(1)

        # 自定义对称轴
        direction = UR * 1.2
        about_p = LEFT * 3.5 + DOWN
        dot = Dot(LEFT * 2.5, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(ReplacementTransform(captions_mob[8], captions_mob[9]), Write(tex_flip_3), run_time=1.2)
        self.play(Write(tex_flip_3_))
        self.wait(0.2)
        self.play(TransformFromCopy(tex_flip_3_, dot), run_time=1.5)
        self.wait(0.6)
        self.play(ShowCreation(axis_line))
        self.wait(0.4)
        self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.8)
        self.wait(0.25)
        self.play(WiggleOutThenIn(axis_line))
        self.play(WiggleOutThenIn(dot))
        self.wait(0.5)
        self.play(FadeOut(axis_line), FadeOut(dot), un_time=1.2)
        self.wait(2.)
        self.play(FadeOut(captions_mob[-1]))
        self.wait(0.5)


        captions = [
            "flip变换实际上是用在三维空间中的旋转变换实现的",
            "这样在降维打击后的二维场景中就反映出对称翻折的效果",
            "让我们在三维场景下细品一下刚才的操作",
            ]
        t2c_02 = {'三维': RED, '二维': PINK}
        captions_mob = VGroup(
            *[
                CodeLine(cap, font='思源黑体 Bold', size=0.32).to_edge(DOWN * 1.2).set_color_by_t2c(t2c_02)
                for cap in captions
            ]
        )

        self.play(Write(captions_mob[0]), run_time=1.2)
        tex_g = VGroup(tex_add, tex_flip, tex_flip_1, tex_flip_2, tex_flip_2_, tex_flip_3, tex_flip_3_)
        self.play(FadeOut(tex_g), Uncreate(emote), run_time=1.2)
        self.wait(1)

        self.camera.add_fixed_in_frame_mobjects(captions_mob)

        emote = Emote_new(color=BLACK, height=2.4).shift(LEFT * 3 + UP * 1.6)

        loc = UP * 2.9 + RIGHT * 2.64
        tex_add = CodeLine('self.add(mob)').move_to(loc)
        tex_flip = CodeLine('mob.flip()').next_to(tex_add, DOWN).align_to(tex_add, LEFT)
        tex_flip_1 = CodeLine('mob.flip(axis=RIGHT)').next_to(tex_flip, DOWN).align_to(tex_flip, LEFT)
        tex_flip_2 = CodeLine('mob.flip(axis=RIGHT,').next_to(tex_flip_1, DOWN).align_to(tex_flip_1, LEFT)
        tex_flip_2_ = CodeLine('about_point=ORIGIN)').next_to(tex_flip_2, DOWN).align_to(tex_flip_2, LEFT)
        tex_flip_3 = CodeLine('mob.flip(axis=UR,').next_to(tex_flip_2_, DOWN).align_to(tex_flip_2_, LEFT)
        tex_flip_3_ = CodeLine('about_point=LEFT*2.5)').next_to(tex_flip_3, DOWN).align_to(tex_flip_3, LEFT)
        tex_group = VGroup(tex_bg, tex_add, tex_flip, tex_flip_1, tex_flip_2, tex_flip_2_, tex_flip_3, tex_flip_3_)
        self.camera.add_fixed_in_frame_mobjects(tex_group)

        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]), run_time=1.)
        self.wait()
        self.play(Write(tex_add), run_time=0.9)
        self.wait(0.2)
        self.play(WiggleOutThenIn(emote), run_time=0.9)
        self.wait(0.5)
        self.play(ReplacementTransform(captions_mob[1], captions_mob[2]), run_time=1.)
        self.wait(0.5)
        self.move_camera(phi=54*DEGREES, theta=-140*DEGREES)

        # 默认效果
        direction = UP
        about_p = emote.get_center() + DOWN * 0.3 + RIGHT * 0.1
        dot = Dot(about_p, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(Write(tex_flip), run_time=1.)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line), run_time=1.)
        self.wait(0.2)
        # self.play(emote.flip, {'about_point': about_p}, run_time=1.5)
        self.play(Rotating(emote, radians=PI, axis=direction, about_point=about_p, run_time=1.5))
        self.wait(0.2)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=0.8)
        self.wait(0.8)

        # 上下翻转
        direction = RIGHT
        about_p = emote.get_center() + DOWN * 0.3 - RIGHT * 0.1
        dot = Dot(about_p, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(Write(tex_flip_1), run_time=1.)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line))
        self.wait(0.2)
        # self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.5)
        self.play(Rotating(emote, radians=PI, axis=direction, about_point=about_p, run_time=1.5))
        self.wait(0.2)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=0.8)
        self.wait(0.8)

        # 关于y=0上下翻转
        direction = RIGHT * 2.
        about_p = LEFT * 2.5
        dot = Dot(ORIGIN, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(Write(tex_flip_2), run_time=1.)
        self.play(Write(tex_flip_2_), run_time=0.8)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line))
        self.wait(0.2)
        # self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.5)
        self.play(Rotating(emote, radians=PI, axis=direction, about_point=about_p, run_time=1.5))
        self.wait(0.2)
        self.play(FadeOut(axis_line), FadeOut(dot), run_time=0.8)
        self.wait(0.8)

        # 自定义对称轴
        direction = UR * 1.2
        about_p = LEFT * 3.5 + DOWN
        dot = Dot(LEFT * 2.5, color=PINK, plot_depth=4).scale(1.6)
        axis_line = DashedLine(about_p + direction * 2, about_p - direction * 2, color=RED, plot_depth=-1)
        self.play(Write(tex_flip_3), run_time=1.)
        self.play(Write(tex_flip_3_), run_time=0.8)
        self.wait(0.2)
        self.play(FadeInFromLarge(dot), ShowCreation(axis_line))
        self.wait(0.2)
        # self.play(emote.flip, {'about_point': about_p, 'axis': direction}, run_time=1.5)
        self.play(Rotating(emote, radians=PI, axis=direction, about_point=about_p, run_time=1.5))
        self.wait(0.2)
        self.play(FadeOut(axis_line), FadeOut(dot), un_time=0.8)
        self.wait(2.)
        self.move_camera(phi=0*DEGREES, theta=-90*DEGREES)
        self.wait(2.5)

