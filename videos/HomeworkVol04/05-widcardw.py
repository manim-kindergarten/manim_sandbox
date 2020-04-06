# from @widcardw

from manimlib.imports import *
from dalao_s_project.homeworkvol04sample import *
# 上面这行其实是调用的cigar666的CodeLine和Emote(在test_present_style.py中)
# from test_present_style.py import *


class CtrlT(VGroup):  # 自动更新的边框(Homework04中没有用到)
    CONFIG = {"buff": SMALL_BUFF, "black_bg": False,
              "add_corner": True}

    def __init__(self, obj, **kwargs):
        VGroup.__init__(self, **kwargs)
        if not self.black_bg:
            border = Rectangle(width=4, height=2).add_updater(
                lambda b: b.become(Rectangle(width=obj.get_width()+2*self.buff, height=obj.get_height()+2*self.buff,
                                             stroke_width=1, stroke_color="#000000").move_to(obj.get_center())))
            corner_group = VGroup()
            if self.add_corner:
                dot_0 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#ffffff", stroke_width=1,
                        stroke_color="#000000").move_to(border.get_vertices()[0])
                ))
                dot_1 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#ffffff", stroke_width=1,
                        stroke_color="#000000").move_to(border.get_vertices()[1])
                ))
                dot_2 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#ffffff", stroke_width=1,
                        stroke_color="#000000").move_to(border.get_vertices()[2])
                ))
                dot_3 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#ffffff", stroke_width=1,
                        stroke_color="#000000").move_to(border.get_vertices()[3])
                ))
                corner_group.add(dot_0, dot_1, dot_2, dot_3)
        else:
            border = Rectangle(width=obj.get_width()+2*self.buff, height=obj.get_height()+2*self.buff,
                               stroke_color="#ffffff", stroke_width=1).add_updater(
                lambda b: b.move_to(obj.get_center())
            )
            corner_group = VGroup()
            if self.add_corner:
                dot_0 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#000000", stroke_width=1,
                        stroke_color="#ffffff").move_to(border.get_vertices()[0])
                ))
                dot_1 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#000000", stroke_width=1,
                        stroke_color="#ffffff").move_to(border.get_vertices()[1])
                ))
                dot_2 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#000000", stroke_width=1,
                        stroke_color="#ffffff").move_to(border.get_vertices()[2])
                ))
                dot_3 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#000000", stroke_width=1,
                        stroke_color="#ffffff").move_to(border.get_vertices()[3])
                ))
                corner_group.add(dot_0, dot_1, dot_2, dot_3)
        self.add(border, corner_group)


class BorderNoneUpdate(VGroup):  # 非自动更新的边框
    CONFIG = {"buff": SMALL_BUFF, "black_bg": False,
              "add_corner": True}

    def __init__(self, obj, **kwargs):
        VGroup.__init__(self, **kwargs)
        if not self.black_bg:
            border = Rectangle(width=obj.get_width()+2*self.buff, height=obj.get_height()+2*self.buff,
                               stroke_width=1, stroke_color="#000000").move_to(obj.get_center())
            corner_group = VGroup()
            if self.add_corner:
                dot_0 = Dot(color="#ffffff", stroke_width=1,
                            stroke_color="#000000").move_to(border.get_vertices()[0])
                dot_1 = Dot(color="#ffffff", stroke_width=1,
                            stroke_color="#000000").move_to(border.get_vertices()[1])
                dot_2 = Dot(color="#ffffff", stroke_width=1,
                            stroke_color="#000000").move_to(border.get_vertices()[2])
                dot_3 = Dot(color="#ffffff", stroke_width=1,
                            stroke_color="#000000").move_to(border.get_vertices()[3])
                corner_group.add(dot_0, dot_1, dot_2, dot_3)
        else:
            border = Rectangle(width=obj.get_width()+2*self.buff, height=obj.get_height()+2*self.buff,
                               stroke_width=1, stroke_color="#ffffff").move_to(obj.get_center())
            corner_group = VGroup()
            if self.add_corner:
                dot_0 = Dot(color="#000000", stroke_width=1,
                            stroke_color="#ffffff").move_to(border.get_vertices()[0])
                dot_1 = Dot(color="#000000", stroke_width=1,
                            stroke_color="#ffffff").move_to(border.get_vertices()[1])
                dot_2 = Dot(color="#000000", stroke_width=1,
                            stroke_color="#ffffff").move_to(border.get_vertices()[2])
                dot_3 = Dot(color="#000000", stroke_width=1,
                            stroke_color="#ffffff").move_to(border.get_vertices()[3])
                corner_group.add(dot_0, dot_1, dot_2, dot_3)
        self.add(border, corner_group)


class Stretch_tutorial(ThreeDScene):
    CONFIG = {"camera_config": {"background_color": WHITE}, "balck_bg": False}

    def construct(self):
        bg_rect = Rectangle(height=5.5, width=5.5, fill_color="#dddddd",
                            fill_opacity=0.4, stroke_color="#999999").shift(RIGHT*3)
        code_list = [
            "self.play(FadeIn(mob))",
            "mob.stretch(factor=2, dim=0)",
            "mob.stretch(factor=2, dim=1)",
            "mob.stretch(factor=3, dim=2)",
        ]
        codes = VGroup(*[CodeLine(code, size=0.32) for code in code_list])\
            .arrange(DOWN, aligned_edge=LEFT, buff=0.15).shift(RIGHT*3+UP*1.5)
        bg_rect.set_height(codes.get_height()+0.8)\
            .set_width(codes.get_width()+0.8).move_to(codes.get_center())
        text_list = [
            "使用stretch对物件进行拉伸变换",
            "stretch函数中要传入两个参数 factor和dim",
            "factor表示拉伸的倍数,dim(dimension)表示拉伸的方向(维度)",
            "将mur猫沿x轴方向拉伸至2倍",
            "将mur猫沿y轴方向拉伸至2倍",
            "将mur猫沿z轴方向拉伸至3倍",
            "奇怪的停顿增加了!",
            "为什么?因为纸片人再怎样拉伸,它终究是平的!",
            "现在我们将mur猫旋转一下 使它与z轴平行",
            "接着重新对它进行沿z轴方向的拉伸 やったー!",
            "现在全部还原",
            "传入参数about_point,将mur猫以(-3,-3,0)为基准沿y轴拉伸2倍",
            "传入另一个点和另一个方向,可以达到类似的效果",
            "传入参数about_edge,将mur猫以物件自身的某一边缘拉伸"
        ]
        texts = VGroup(*[CodeLine(text, size=0.32, font="思源黑体 CN Bold") for text in text_list])\
            .to_edge(DOWN*1.2)
        mur = Emote_new(color=BLACK).set_height(1.8).shift(UP*0.5+LEFT*3)
        border = BorderNoneUpdate(mur)
        self.play(FadeIn(bg_rect), Write(codes[0]),
                  FadeIn(mur), FadeIn(texts[0]))
        self.wait(2)
        self.play(FadeIn(border), ReplacementTransform(texts[0], texts[1]))
        self.wait(2)
        border.add_updater(lambda b: b.become(BorderNoneUpdate(mur)))
        self.add(border)
        self.play(ReplacementTransform(texts[1], texts[2]))
        self.wait(3)
        self.play(Write(codes[1]), ReplacementTransform(texts[2], texts[3]))
        self.play(mur.stretch, {"factor": 2, "dim": 0})
        self.wait(2)
        self.play(Write(codes[2]), ReplacementTransform(texts[3], texts[4]))
        self.play(mur.stretch, {"factor": 2, "dim": 1})
        self.wait(2)
        self.play(Write(codes[3]), ReplacementTransform(texts[4], texts[5]))
        self.play(mur.stretch, {"factor": 3, "dim": 2})
        self.wait(2)
        self.play(ReplacementTransform(texts[5], texts[6]))
        self.wait(2)
        self.play(ReplacementTransform(texts[6], texts[7]))
        self.wait(4)
        axes = ThreeDAxes(color="#555555")
        self.play(ShowCreation(axes), ReplacementTransform(texts[7], texts[8]))
        self.move_camera(phi=PI/3, theta=-2*PI/3)
        border.clear_updaters()
        vg_m_b = VGroup(mur, border)
        self.play(Rotating(vg_m_b, axis=RIGHT, radians=PI / 2, rate_func=smooth),
                  run_time=0.9)
        self.wait(2)
        self.play(Write(codes[3]), ReplacementTransform(texts[8], texts[9]))
        self.play(vg_m_b.stretch, {"factor": 3, "dim": 2})
        self.wait(2)
        mur2 = Emote_new(color="#000000").set_height(
            1.8).shift(DOWN*0.5+LEFT*3)
        border.add_updater(lambda b: b.become(BorderNoneUpdate(mur2)))
        self.play(FadeOut(texts[9]), ReplacementTransform(vg_m_b, mur2),
                  FadeOut(axes), run_time=0.9)
        self.add(border)
        self.move_camera(phi=0, theta=-PI/2)
        code_list_1 = [
            "self.play(FadeIn(mob))",
            "# mob.stretch(factor=2, dim=0)",
            "# mob.stretch(factor=2, dim=1)",
            "# mob.stretch(factor=3, dim=2)",
            '''mob.stretch(factor=2, dim=1,
    about_point=np.array([-3,-3,0]))''',
            '''mob.stretch(factor=0.5, dim=1,
    about_point=LEFT_SIDE+TOP)''',
            '''mob.stretch(factor=2, dim=1,
    about_edge=UP)''',
            '''mob.stretch(factor=0.5, dim=1,
    about_edge=DOWN)''',
            '''# 同样的,所有mob的变换均为瞬间完成
# 但为了演示变换过程,
# 视频中执行的是将变换放入
# self.play()后对应的动画过程'''
        ]
        codes_1 = VGroup(*[CodeLine(code, size=0.32, font="Microsoft YaHei Mono") for code in code_list_1])\
            .arrange(DOWN, aligned_edge=LEFT, buff=0.15).shift(RIGHT*3)
        for i in range(1, 4):
            codes_1[i].set_color(GREEN_E)
        codes_1[-1].set_color(GREEN_E)
        self.play(ReplacementTransform(codes, codes_1[:4]), Write(texts[10]),
                  bg_rect.set_width, codes_1.get_width()+0.8,
                  bg_rect.set_height, codes_1.get_height()+0.8,
                  bg_rect.move_to, codes_1.get_center())
        self.wait(1.5)
        dot_2_0 = Dot(np.array([-3, -3, 0]), color=RED).scale(0.7)
        dot_2_t = CodeLine("(-3,-3,0)", size=0.3)\
            .next_to(dot_2_0, UP, buff=0.1)
        self.play(*[Write(obj)for obj in[codes_1[4], dot_2_0, dot_2_t]],
                  ReplacementTransform(texts[10], texts[11]))
        self.play(mur2.stretch, {"factor": 2, "dim": 1,
                                 "about_point": np.array([-3, -3, 0])})
        self.wait(2)
        arrow_ul = Arrow(LEFT*6+UP*3, LEFT_SIDE+TOP, color=RED)
        dot_ul = CodeLine("LEFT_SIDE+TOP", size=0.25)\
            .next_to(arrow_ul, DOWN+RIGHT, buff=0)
        self.play(ReplacementTransform(texts[11], texts[12]),
                  Write(codes_1[5]), ReplacementTransform(dot_2_0, dot_ul),
                  ReplacementTransform(dot_2_t, arrow_ul))
        self.play(mur2.stretch, {"factor": 0.5, "dim": 1,
                                 "about_point": LEFT_SIDE+TOP})
        self.wait(2)
        arrow_up = Arrow(LEFT*5+UP*3, LEFT*3+UP*4, color=GOLD)
        about_text = CodeLine("about_edge", size=0.3).next_to(
            arrow_up, LEFT+DOWN, buff=0.1)
        self.play(FadeOut(dot_ul), FadeOut(arrow_ul),
                  ReplacementTransform(texts[12], texts[13]),
                  Write(codes_1[6]), Write(about_text), Write(arrow_up))
        self.play(mur2.stretch, {"factor": 2, "dim": 1, "about_edge": UP})
        self.wait(1)
        self.play(Write(codes_1[7]),
                  arrow_up.become, Arrow(
                      LEFT*5+UP*2, LEFT*3+UP*0.4, color=GOLD),
                  about_text.shift, DOWN)
        self.play(mur2.stretch, {"factor": 0.5, "dim": 1, "about_edge": DOWN})
        self.wait(2)
        self.play(FadeOut(texts[13]), Write(codes_1[-1]),
                  FadeOut(arrow_up), FadeOut(about_text))
        self.wait()
