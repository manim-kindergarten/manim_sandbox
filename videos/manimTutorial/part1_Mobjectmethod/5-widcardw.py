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
        bg_rect = Rectangle(height=3.6, width=5.5, fill_color="#dddddd",
                            fill_opacity=0.4, stroke_color="#999999").shift(RIGHT*3+UP*1)
        code_list = [
            "self.play(FadeIn(mob))",
            "mob.stretch(factor=2, dim=0)",
            "mob.stretch(factor=2, dim=1)",
            "mob.stretch(factor=3, dim=2)",
        ]
        codes = VGroup(*[CodeLine(code, size=0.32) for code in code_list])\
            .arrange(DOWN, aligned_edge=LEFT, buff=0.15).shift(RIGHT*3+UP*1.5)
        text_list = [
            "使用stretch对物件进行拉伸变换",
            "stretch函数中要传入两个参数,factor和dim",
            "factor表示拉伸的倍数,dim(dimension)表示拉伸的方向(维度)",
            "将mur猫沿x轴方向拉伸至2倍",
            "将mur猫沿y轴方向拉伸至2倍",
            "将mur猫沿z轴方向拉伸至3倍",
            "奇怪的停顿增加了!",
            "为什么?因为纸片人再怎样拉伸,它终究是平的!",
            "现在我们将mur猫旋转一下,使它与z轴平行",
            "接着重新对它进行沿z轴方向的拉伸,やったー!",
            "现在全部还原",
            "传入参数about_point,将mur猫以(-3,-3,0)为基准沿y轴拉伸2倍",
            "传入另一个点和另一个方向,可以达到类似的效果",
            "传入参数about_edge,将mur猫以物件自身的某一边缘拉伸"
        ]
        texts = VGroup(*[CodeLine(text, size=0.32, font="思源黑体 CN Bold") for text in text_list])\
            .to_edge(DOWN*1.2)
        mur0 = SVGMobject(r'C:\Users\row31976300\Pictures\manim_test\manimlib\files\emote_01.svg',
                          color=BLACK).set_height(1.8).shift(UP*0.5+LEFT*3)
        mur = Emote_new(color=BLACK).set_height(1.8).shift(UP*0.5+LEFT*3)
        self.play(*[FadeIn(obj)for obj in [mur0[4], mur0[7],
                                           mur0[8], mur0[10], mur0[11], mur0[12], mur0[13], mur0[14]]])
        self.add(mur)
        self.remove(mur0)
        self.play(FadeIn(bg_rect), Write(codes[0]),
                  FadeIn(texts[0]))
        self.wait(2)
        border = BorderNoneUpdate(mur)
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
        self.move_camera(phi=PI/3, theta=-100*DU)
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
        codes_1 = VGroup(*[CodeLine(code, size=0.32, font="Consolas")
                           for code in code_list_1[0:-1]])
        code_last = CodeLine(code_list_1[-1], font="思源黑体 CN Bold", size=0.32)
        codes_1.add(code_last)
        codes_1.arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(RIGHT*3)
        for i in range(1, 4):
            codes_1[i].set_color(GREEN_E)
        codes_1[-1].set_color(GREEN_E)
        bg_rect_2 = Rectangle(height=6.5, width=7, fill_color="#dddddd",
                              fill_opacity=0.4, stroke_color="#999999").shift(RIGHT*3)
        bg_rect_2.plot_depth = -1
        self.play(Write(texts[10]),
                  ReplacementTransform(bg_rect, bg_rect_2), FadeOut(codes), FadeIn(codes_1[:4]))
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
        self.wait(3)
        arrow_up = Arrow(LEFT*5+UP*3, LEFT*3+UP*4, color=GOLD)
        about_text = CodeLine("about_edge", size=0.3).next_to(
            arrow_up, LEFT+DOWN, buff=0.1)
        self.play(FadeOut(dot_ul), FadeOut(arrow_ul),
                  ReplacementTransform(texts[12], texts[13]),
                  Write(codes_1[6]), Write(about_text), Write(arrow_up))
        self.play(mur2.stretch, {"factor": 2, "dim": 1, "about_edge": UP})
        self.wait(2)
        self.play(Write(codes_1[7]),
                  arrow_up.become, Arrow(
                      LEFT*5+UP*2, LEFT*3+UP*0.4, color=GOLD),
                  about_text.shift, DOWN)
        self.play(mur2.stretch, {"factor": 0.5, "dim": 1, "about_edge": DOWN})
        self.wait(2)
        self.play(FadeOut(texts[13]), Write(codes_1[-1]),
                  FadeOut(arrow_up), FadeOut(about_text))
        self.wait(2)


class Scale_tutorial(Scene):
    CONFIG = {"camera_config": {"background_color": WHITE}, "balck_bg": False}

    def construct(self):
        code_list = [
            "self.play(FadeIn(mob))",
            "mob.scale(2)",
            "mob.scale(0.5)",
            "mob.scale(1.5,about_edge=UP)",
            "mob.scale(0.3,about_edge=RIGHT)",
            """mob.scale(2,
    about_point=np.array([-2,-2,0]))""",
            "self.play(mob.scale,1.5)",
            """self.play(mob.scale,
    {'scale_factor':0.6,
     'about_edge':LEFT})""",
        ]
        codes = VGroup(*[CodeLine(i, size=0.32)for i in code_list])
        codes.arrange(DOWN, aligned_edge=LEFT, buff=0.15).shift(RIGHT*3)
        text_list = [
            "使用scale可以对物件进行缩放",
            "scale()中可以传入的参数不仅仅只有缩放倍数",
            "还可以传入about_edge,about_point等参数",
            "将mur猫以自身为中心放大至2倍",
            "再将它缩小至现在的0.5倍",
            "传入about_edge参数,使它以自身上边缘为基准放大至1.5倍",
            "同样的方法,使它以自身右边缘缩小至0.3倍",
            "传入about_point参数,使它以(-2,-2)为基准放大至2倍",
            "当然这些都必须放在self.play()中才能达到播放动画的效果",
            "具体请看代码框中的实例",
        ]
        texts = VGroup(*[CodeLine(i, size=0.32, font="思源黑体 CN Bold")
                         for i in text_list]).to_edge(DOWN*1.2)

        mur = Emote(color=BLACK).set_height(2).shift(LEFT*3+UP*0.5)
        bg_rect = Rectangle(height=5, width=6.5, fill_color="#dddddd",
                            fill_opacity=0.4, stroke_color="#999999", plot_depth=-1).shift(RIGHT*3)
        border = BorderNoneUpdate(mur)
        brace_l = Brace(border, LEFT, color=BLACK)
        brace_d = Brace(border, DOWN, color=BLACK)
        num_h = DecimalNumber(2.0, num_decimal_places=1,
                              include_sign=False, color=BLACK).next_to(brace_l, LEFT, buff=0.1)
        num_w = DecimalNumber(2.1, num_decimal_places=1,
                              include_sign=False, color=BLACK).next_to(brace_d, DOWN, buff=0.1)

        def border_update(border):
            border.become(BorderNoneUpdate(mur))

        self.play(FadeIn(bg_rect), Write(texts[0]))
        self.wait(2)
        self.play(FadeIn(mur), RT(texts[0], texts[1]), Write(codes[0]))
        self.wait(2)
        self.play(FadeIn(border), RT(texts[1], texts[2]),
                  FadeIn(brace_l), FadeIn(brace_d),
                  FadeIn(num_h), FadeIn(num_w))
        self.wait(2.8)

        border.add_updater(border_update)
        brace_l.add_updater(lambda b: b.become(
            Brace(border, LEFT, color=BLACK)))
        brace_d.add_updater(lambda b: b.become(
            Brace(border, DOWN, color=BLACK)))
        num_h.add_updater(lambda a: a.set_value(mur.get_height()))
        num_h.add_updater(lambda a: a.next_to(brace_l, LEFT, buff=0.1))
        num_w.add_updater(lambda a: a.set_value(mur.get_width()))
        num_w.add_updater(lambda a: a.next_to(brace_d, DOWN, buff=0.1))
        self.add(border, brace_l, brace_d, num_h, num_w)

        self.play(RT(texts[2], texts[3]), Write(codes[1]))
        self.play(mur.scale, 2)
        self.wait(2)
        self.play(RT(texts[3], texts[4]), Write(codes[2]))
        self.play(mur.scale, 0.5)
        self.wait(2)
        self.play(RT(texts[4], texts[5]), Write(codes[3]))
        l_1x = Line(LEFT*3.5, RIGHT*3.5, color=BLUE).next_to(border,
                                                             UP, buff=-Dot().get_width()/2)
        self.play(ShowCreation(l_1x))
        self.play(mur.scale, {"scale_factor": 1.5, "about_edge": UP})
        self.play(Uncreate(l_1x))
        self.wait(2)
        self.play(RT(texts[5], texts[6]), Write(codes[4]))
        l_x2 = Line(UP*3, DOWN*3, color=BLUE).next_to(border,
                                                      RIGHT, buff=-Dot().get_width()/2)
        self.play(ShowCreation(l_x2))
        self.play(mur.scale, {"scale_factor": 0.3, "about_edge": RIGHT})
        self.play(Uncreate(l_x2))
        self.wait(2)

        dot_2 = Dot(np.array([-2, -2, 0]), color=RED)
        array2 = CodeLine("(-2,-2)", size=0.3).next_to(dot_2, DOWN)
        l_0 = DashedLine(LEFT, RIGHT, color=GOLD)\
            .add_updater(lambda l: l.put_start_and_end_on(
                np.array([-2, -2, 0]), BackgroundRectangle(border, buff=0).get_vertices()[0]))
        l_1 = DashedLine(LEFT, RIGHT, color=GOLD)\
            .add_updater(lambda l: l.put_start_and_end_on(
                np.array([-2, -2, 0]), BackgroundRectangle(border, buff=0).get_vertices()[1]))
        l_2 = DashedLine(LEFT, RIGHT, color=GOLD)\
            .add_updater(lambda l: l.put_start_and_end_on(
                np.array([-2, -2, 0]), BackgroundRectangle(border, buff=0).get_vertices()[2]))
        l_3 = DashedLine(LEFT, RIGHT, color=GOLD)\
            .add_updater(lambda l: l.put_start_and_end_on(
                np.array([-2, -2, 0]), BackgroundRectangle(border, buff=0).get_vertices()[3]))

        self.play(RT(texts[6], texts[7]), Write(codes[5]), Write(dot_2), Write(array2),
                  *[ShowCreation(obj)for obj in [l_1, l_2, l_3, l_0]])
        self.play(mur.scale, {"scale_factor": 2,
                              "about_point": np.array([-2, -2, 0])})
        self.wait(2)
        for i in [l_0, l_1, l_2, l_3]:
            i.clear_updaters()
        self.play(*[FadeOut(i)for i in [dot_2, array2, l_0, l_1, l_2, l_3]])
        self.play(RT(texts[7], texts[8]), Write(codes[6]))
        self.play(mur.scale, 1.5)
        self.wait(2)
        self.play(RT(texts[8], texts[9]), Write(codes[7]))
        l_x3 = Line(UP*3, DOWN*3, color=BLUE).next_to(border,
                                                      LEFT, buff=-Dot().get_width()/2)
        self.play(ShowCreation(l_x3))
        self.play(mur.scale, {'scale_factor': 0.6, 'about_edge': LEFT})
        self.play(Uncreate(l_x3))
        self.wait(3)
        self.play(*[FadeOut(i) for i in [texts[9], codes, bg_rect]],
                  mur.move_to, ORIGIN)
        self.wait(1)
        self.play(mur.scale, 3)
        self.wait(2)
