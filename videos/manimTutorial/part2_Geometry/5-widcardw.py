#from widcardw

'''
1.Line+Arrow
具体内容：
line+arrow默认参数情况
line的start和end参数及线宽stroke_width参数
put_start_and_end_on方法
arrow的各个参数，尤其是buff的影响
提一下DashedLine和Vector，不用展开讲，给个默认效果就ok
如何更改Arrow箭头(tip)的大小，以及Line的add_tip方法
提一下双箭头
'''

from manimlib.imports import *
from manim_sandbox.imports import *


class Line_tutorial(Scene):

    CONFIG = {"camera_config":{"background_color":"#ffffff"}}

    def construct(self):
        bg_rect = Rectangle(width=6, height=6.5, stroke_color="#aaaaaa",
                            fill_color="#aaaaaa", fill_opacity=0.3, plot_depth=-1).shift(RIGHT * 3.5)
        buff_value = ValueTracker(0.)
        stroke_value = ValueTracker(6.)
        axes = Axes()
        t2c_0 = {
            "line_1": DARK_GRAY,
        }
        code_list = ["line_1=Line()",
               """line_1=Line(np.array([-4,-3,0]),
            np.array([0,3,0]))""",
               """line_1=Line(np.array([-4,-3,0]),
            np.array([0,3,0]),
            buff=0)""",
               """line_1=Line(np.array([-4,-3,0]),
            np.array([0,3,0]),
            stroke_width=6)"""
               ]
        code = VGroup(
            CodeLine(code_list[0],size=0.32).shift(UP*2.8+RIGHT*1.8),
            CodeLine(code_list[1],size=0.32),
            CodeLine(code_list[2],size=0.32),
            CodeLine(code_list[3],size=0.32),
        )
        code[1].align_to(code[0], UL)
        code[2].align_to(code[0], UL)
        code[3].align_to(code[0], UL)
        text_list = [
            "关于Line的使用方法",
            "首先我们画出一条默认的线",
            "可见默认情况它下是二维坐标下从(-1,0)到(1,0)的一条线段",
            "现在传入两个坐标,改变Line的起止位置",
            "当然还可以传入buff参数来调整与目标点的距离",
            "传入stroke_width参数调整线的宽度",
        ]
        text = VGroup(*[CodeLine(obj, size=0.32,font="思源黑体 CN Bold") for obj in text_list])
        text.to_edge((DOWN*1.2))

        l_1=Line(color="#000000")
        l_2=Line(np.array([-4,-3,0]),
            np.array([0,3,0]), color=GOLD)
        dot_0_0=CodeLine("(-4,-3)",size=0.3).next_to(l_2.get_start(),DOWN, buff=0.1)
        d_0_0=Dot(np.array([-4,-3,0]),color=RED)
        dot_0_1=CodeLine("(0,3)",size=0.3).next_to(l_2.get_end(),UP, buff=0.1)
        d_0_1=Dot(np.array([0,3,0]),color=RED)
        dot_0_g=VGroup(dot_0_0,dot_0_1,d_0_0,d_0_1)
        self.play(ShowCreation(axes),Write(text[0]), FadeIn(bg_rect))
        self.wait(2)
        self.play(ReplacementTransform(text[0],text[1]),
                  Write(code[0]))
        self.play(ShowCreation(l_1))
        self.wait(2)
        self.play(RT(text[1],text[2]))
        self.wait(3)
        self.play(RT(text[2],text[3]), FadeOut(code[0]), Write(code[1]))
        self.play(RT(l_1,l_2), Write(dot_0_g))
        self.wait(2.5)
        rect_0=Rectangle(width=3.6,height=0.3,color=YELLOW,fill_color=YELLOW,fill_opacity=0.9,plot_depth=-0.5)
        rect_0.align_to(code[2],DR)
        self.play(RT(text[3],text[4]),FadeOut(code[1]),FadeIn(code[2]),FadeIn(rect_0))
        l_2.add_updater(lambda l:l.become(
            Line(np.array([-4,-3,0]), np.array([0,3,0]), color=GOLD, buff=buff_value.get_value())
        ))
        code[2].add_updater(lambda t:t.become(
            CodeLine("""line_1=Line(np.array([-4,-3,0]),
            np.array([0,3,0]),
            buff=%.1f)""" % buff_value.get_value(), size=0.32).align_to(code[0],UL)
        ))
        self.add(code[2],l_2)
        self.play(buff_value.set_value, 3, run_time=1, rate_func=linear)
        self.play(buff_value.set_value, 0, run_time=1, rate_func=linear)
        l_2.clear_updaters()
        code[2].clear_updaters()
        self.wait(2.5)
        self.play(RT(text[4],text[5]),FadeOut(code[2]),FadeIn(code[3]))
        l_2.add_updater(lambda l: l.become(
            Line(np.array([-4, -3, 0]), np.array([0, 3, 0]), color=GOLD, stroke_width=stroke_value.get_value())
        ))
        code[3].add_updater(lambda t: t.become(
            CodeLine("""line_1=Line(np.array([-4,-3,0]),
            np.array([0,3,0]),
            stroke_width=%.1f)""" % stroke_value.get_value(), size=0.32).align_to(code[0], UL)
        ))
        self.add(l_2,code[3])
        self.play(stroke_value.set_value, 60, run_time=1, rate_func=linear)
        self.play(stroke_value.set_value, 6, run_time=1, rate_func=linear)
        l_2.clear_updaters()
        code[3].clear_updaters()
        self.play(FadeOut(rect_0))
        self.wait(2)


class Line_tutorial_2(Scene):

    CONFIG = {"camera_config": {"background_color": "#ffffff"}}

    def construct(self):
        bg_rect = Rectangle(width=6, height=6.5, stroke_color="#aaaaaa",
                            fill_color="#aaaaaa", fill_opacity=0.3, plot_depth=-1).shift(RIGHT * 3.5)
        axes=Axes()
        l_2 = Line(np.array([-4, -3, 0]),
                   np.array([0, 3, 0]), color=GOLD)
        dot_0_0 = CodeLine("(-4,-3)", size=0.3).next_to(l_2.get_start(), DOWN, buff=0.1)
        d_0_0 = Dot(np.array([-4, -3, 0]), color=RED)
        dot_0_1 = CodeLine("(0,3)", size=0.3).next_to(l_2.get_end(), UP, buff=0.1)
        d_0_1 = Dot(np.array([0, 3, 0]), color=RED)
        dot_0_g = VGroup(dot_0_0, dot_0_1, d_0_0, d_0_1)
        code_list = [
            """line_1=Line(np.array([-4,-3,0]),
            np.array([0,3,0]),
            stroke_width=6.0)""",
            """line_1.put_start_and_end_on(
      np.array([-2,2,0]),
      np.array([0,-2,0]))""",
            "line_1.scale(3)",
            """line_2=DashedLine(
      np.array([-2,-2,0]),
      np.array([0,2,0]))""",
            """line_3=Line(
      np.array([-2,-2,0]),
      np.array([-2,2,0]),
      path_arc=None)""",
            "#~line_1.scale(3)",
        ]
        code = VGroup(
            CodeLine(code_list[0]).shift(UP*2.6+RIGHT*3.5),
            CodeLine(code_list[1]),
            CodeLine(code_list[2]),
            CodeLine(code_list[3]),
            CodeLine(code_list[4]),
            CodeLine(code_list[-1]).set_color(GREEN_D),
        )
        code[1].align_to(code[0],UL)
        code[2].next_to(code[1], DOWN, aligned_edge=LEFT)
        code[-1].next_to(code[1], DOWN, aligned_edge=LEFT)
        code[-1][1].set_opacity(0)
        code[3].next_to(code[2], DOWN, aligned_edge=LEFT)
        code[4].next_to(code[3], DOWN, aligned_edge=LEFT)
        text_list = [
            "传入stroke_width参数调整线的宽度",
            "使用put_start_and_end_on可以以两点确定一条直线",
            "对Line使用scale,只会改变其长度,而不会改变其粗细",
            "DashedLine继承于Line,用法与Line类似,大家可以自己研究其参数",
            "Line还有一个参数:path_arc,可以将直线变成弧线",
            "path_arc即为弧线的圆心角",

        ]
        text = VGroup(*[CodeLine(obj, font="思源黑体 CN Bold") for obj in text_list]).to_edge(DOWN*1.2)
        self.add(axes, bg_rect, code[0], text[0], dot_0_g, l_2)
        self.play(RT(text[0], text[1]), FadeOut(code[0]), FadeIn(code[1]))
        self.play(l_2.put_start_and_end_on,np.array([-2,2,0]), np.array([0,-2,0]),
                  dot_0_0.become, CodeLine("(-2,2)", size=0.3),
                  dot_0_0.move_to, np.array([-2, 2.4, 0]),
                  d_0_0.become, Dot(np.array([-2, 2, 0]), color=RED),
                  dot_0_1.become, CodeLine("(0,-2)", size=0.3),
                  dot_0_1.move_to, np.array([0,-2.4,0]),
                  d_0_1.become, Dot(np.array([0, -2, 0]), color=RED))
        self.wait(2.5)
        self.play(RT(text[1], text[2]), Write(code[2]))
        self.play(l_2.scale, 3)
        self.play(l_2.scale, 1/3, RT(code[2], code[-1]))
        self.wait(2)
        l_3=DashedLine(np.array([-2,-2,0]), np.array([0,2,0]), color=PURPLE)
        self.play(FadeOut(dot_0_g),RT(text[2], text[3]))
        self.play(Write(code[3]),ShowCreation(l_3))
        self.wait(2.5)
        arc_fac=ValueTracker(0.)
        l_4=Line(np.array([-2,-2,0]), np.array([-2,2,0]),color=RED_D)
        y_bg=Rectangle(height=0.3,width=3.6, plot_depth=-0.5,color=YELLOW,fill_opacity=1).align_to(code[4], DR)
        self.play(RT(text[3], text[4]), Write(code[4]), ShowCreation(l_4))
        self.play(FadeIn(y_bg))
        code[4].add_updater(lambda a:a.become(
            CodeLine("""line_3=Line(
      np.array([-2,-2,0]),
      np.array([-2,2,0]),
      path_arc=%.2f)"""%arc_fac.get_value()).next_to(code[3], DOWN, aligned_edge=LEFT)
        ))
        l_4.add_updater(lambda l: l.become(
            Line(np.array([-2, -2, 0]), np.array([-2, 2, 0]), color=RED_D, path_arc=arc_fac.get_value())
        ))
        self.add(code[4], l_4)
        self.play(arc_fac.set_value, PI,rate_func=linear)
        self.play(arc_fac.set_value, -3*PI/2, rate_func=linear, run_time=2)
        self.play(RT(text[4],text[5]))
        code[4].clear_updaters()
        l_4.clear_updaters()
        self.wait(2.5)
        self.play(*[FadeOut(obj) for obj in self.mobjects])


class ArrowTutorial(Scene):

    CONFIG={"camera_config":{"background_color":"#ffffff"}}

    def construct(self):
        t2c_01={
            "vec_1": DARK_GREY,
            "vec_2": DARK_GREY,
            "vec_3": DARK_GREY,
        }
        axes=NumberPlane().set_color(GREY).set_opacity(0.2)
        bg_rect = Rectangle(width=6.8, height=6, stroke_color="#aaaaaa",
                            fill_color="#aaaaaa", fill_opacity=0.3, plot_depth=-1).shift(RIGHT * 3.4)
        text_list=[
            "Arrow继承于Line类,只是在Line的基础上在尾部加了箭头",
            "这里给出一个例子,可以看到两者几乎一样",
            "只是在stroke_width,buff等方面不同",
            "Arrow带有默认的参数buff=0.25",
            "可以改变buff的值来改变与目标点的距离",
            "改变tip_length的值可以改变箭头的大小",
            "传入max_tip_length_to_length_ratio,可以在线长不变的情况下设置箭头的最大大小比例",
            "传入max_stroke_width_to_length_ratio,可以在箭头大小不变的情况下设置线宽的最大值比例",
        ]
        text=VGroup(*[CodeLine(obj, font="思源黑体 CN Bold")for obj in text_list]).to_edge(DOWN*1.2)
        code_list=[
            """line_1=Line(np.array([-4,-2,0]),
            np.array([-4,2,0]))""",
            "line_1.add_tip()",
            """vec_1=Arrow(np.array([-2,-2,0]),
            np.array([-2,2,0]))""",
        ]
        code=VGroup(*[CodeLine(obj) for obj in code_list])
        code[0].shift(UP*2.3+RIGHT*3.05)
        code[1].next_to(code[0], DOWN, aligned_edge=LEFT)
        code[2].next_to(code[1], DOWN, aligned_edge=LEFT)
        self.play(ShowCreation(axes,lag_ratio=0.1),
                  Write(text[0]))
        self.wait(2.5)
        l_1=Line(np.array([-4,-2,0]),np.array([-4,2,0]),color=GOLD).add_tip()
        vec_1=Arrow(np.array([-2,-2,0]),np.array([-2,2,0]),color=GOLD)
        self.play(RT(text[0],text[1]),FadeInFromLarge(bg_rect))
        self.play(Write(code[0:3]), ShowCreation(l_1),ShowCreation(vec_1))
        self.wait(2)
        self.play(RT(text[1],text[2]))
        text_l=CodeLine("Line").next_to(l_1,DOWN)
        text_v=CodeLine("Arrow").next_to(vec_1, DOWN, buff=0.52)
        self.play(Write(text_l),Write(text_v))
        self.wait(2)
        y_bg=Rectangle(height=0.3,width=1.8,color=YELLOW,fill_opacity=1,plot_depth=-0.5)
        buf_fac=ValueTracker(0.25)
        code[2].add_updater(lambda a:a.become(
            CodeLine("""vec_1=Arrow(np.array([-2,-2,0]),
            np.array([-2,2,0]),
            buff=%.1f)"""%buf_fac.get_value()).next_to(code[1],DOWN,aligned_edge=LEFT)
        ))
        vec_1.add_updater(lambda v:v.become(
            Arrow(np.array([-2,-2,0]),np.array([-2,2,0]),color=GOLD,buff=buf_fac.get_value())
        ))
        y_bg.move_to(code[0].get_center()+DOWN*1.9)
        self.play(RT(text[2],text[3]))
        self.add(code[2],vec_1,y_bg)
        self.play(buf_fac.set_value, 1, rate_func=linear)
        self.wait(0.2)
        self.play(RT(text[3],text[4]))
        self.play(buf_fac.set_value, 0, rate_func=linear)
        code[2].clear_updaters()
        vec_1.clear_updaters()
        self.wait(2)
        buf_fac.set_value(0.35)
        code[2].add_updater(lambda a: a.become(
            CodeLine("""vec_1=Arrow(np.array([-2,-2,0]),
            np.array([-2,2,0]),
            buff=0,
            tip_length=%.2f)""" % buf_fac.get_value()).next_to(code[1], DOWN, aligned_edge=LEFT)))
        vec_1.add_updater(lambda a:a.become(Arrow(np.array([-2,-2,0]),np.array([-2,2,0]),buff=0,color=GOLD,
                                                  tip_length=buf_fac.get_value())))
        self.add(code[2],vec_1)
        self.play(RT(text[4], text[5]),
                  y_bg.become, Rectangle(height=0.3, width=4.5, color=YELLOW,
                                         fill_opacity=1, plot_depth=-0.5).align_to(code[2], DR))
        self.play(buf_fac.set_value, 2, rate_func=linear)
        self.wait(0.5)
        self.play(buf_fac.set_value, 0.35, rate_func=linear)
        code[2].clear_updaters()
        vec_1.clear_updaters()
        self.wait(2.5)

        buf_fac.set_value(0.25)
        code[2].add_updater(lambda a: a.become(
            CodeLine("""vec_1=Arrow(np.array([-2,-2,0]),
            np.array([-2,2,0]),
            buff=0,
max_tip_length_to_length_ratio=%.2f)""" % buf_fac.get_value()).next_to(code[1], DOWN, aligned_edge=LEFT)))
        vec_1.add_updater(lambda a:a.become(Arrow(np.array([-2,-2,0]),np.array([-2,2,0]),buff=0,color=GOLD,
                                                  max_tip_length_to_length_ratio=buf_fac.get_value())))
        self.add(code[2],vec_1)
        self.play(RT(text[5],text[6]),
                  y_bg.become,Rectangle(height=0.3,width=6.4,color=YELLOW,
                                        fill_opacity=1,plot_depth=-0.5).align_to(code[2],DR))
        self.play(buf_fac.set_value, 0.02, rate_func=linear)
        self.wait(0.2)
        self.play(buf_fac.set_value, 1, rate_func=linear)
        code[2].clear_updaters()
        vec_1.clear_updaters()
        self.wait(2.5)
        buf_fac.set_value(5)
        vec_1.add_updater(lambda a: a.become(Arrow(np.array([-2, -2, 0]), np.array([-2, 2, 0]), buff=0, color=GOLD,
                                                   max_stroke_width_to_length_ratio=buf_fac.get_value())))
        code[2].add_updater(lambda a: a.become(
            CodeLine("""vec_1=Arrow(np.array([-2,-2,0]),
            np.array([-2,2,0]),
            buff=0,
max_stroke_width_to_length_ratio=%.1f)""" % buf_fac.get_value()).next_to(code[1], DOWN, aligned_edge=LEFT)))
        self.add(code[2],vec_1)
        self.play(RT(text[6],text[7]))
        self.play(buf_fac.set_value, 0.1, rate_func=linear)
        self.wait(0.2)
        self.play(buf_fac.set_value, 5, rate_func=linear)
        code[2].clear_updaters()
        vec_1.clear_updaters()
        self.wait(3)
        self.play(*[FadeOut(obj) for obj in [text[6],code,l_1,vec_1,y_bg,text_l,text_v]])


class VectorTutorial(Scene):

    CONFIG={"camera_config":{"background_color":"#ffffff"}}

    def construct(self):
        axes=NumberPlane().set_color(GREY).set_opacity(0.2)
        bg_rect = Rectangle(width=6, height=6, stroke_color="#aaaaaa",
                            fill_color="#aaaaaa", fill_opacity=0.3, plot_depth=-1).shift(RIGHT * 3.4)
        self.add(axes,bg_rect)
        text_list = [
            "当然这些物件的应用还很多",
            "例如Vector,但只需传入一个坐标,表示由原点开始的向量,默认buff值为0",
            "可以使用shift对它进行移动",
            "DoubleArrow可以表示双箭头",
            "圆弧Arc也可以添加箭头",
            "对add_tip传入参数at_start=True,可以在它的起点也添加箭头",
            "使用TangentLine可以给物件作切线,alpha取值范围为0到1",
        ]
        t=ValueTracker(0.)
        text = VGroup(*[CodeLine(obj, font="思源黑体 CN Bold") for obj in text_list]).to_edge(DOWN * 1.2)
        code_list = [
            "vec_1=Vector(UP*2+LEFT*1)",
            "vec_1.shift(UP*2+LEFT*1)",
            """vec_2=DoubleArrow(
      np.array([-2,-2,0]),
      np.array([-1,0,0]))""",
            "arc_1=Arc(angle=TAU/3).add_tip()",
            "arc_1.shift(LEFT*3)",
            "arc_1.add_tip(at_start=True)",
            "cir=Circle()",
            """line=TangentLine(cir,alpha=%.2f,
                 length=5)"""%t.get_value(),
        ]
        code=VGroup(*[CodeLine(obj) for obj in code_list])
        code[0].shift(UP*2.6+RIGHT*2.8)
        for i in range(len(code_list)-1):
            code[i+1].next_to(code[i],DOWN,aligned_edge=LEFT)

        vec_1=Vector(UP*2+LEFT*1,color=GOLD)
        vec_2 = DoubleArrow(
            np.array([-2, -2, 0]),
            np.array([-1, 0, 0]),color=RED)
        arc_1=Arc(angle=TAU/3,color=ORANGE).add_tip().shift(LEFT*3)
        arc_2=Arc(angle=TAU/3,color=ORANGE).add_tip().shift(LEFT*3)
        arc_2.add_tip(at_start=True)
        self.play(Write(text[0]))
        self.wait(1.5)
        self.play(RT(text[0],text[1]),Write(code[0]))
        self.play(ShowCreation(vec_1))
        self.wait(3)
        self.play(RT(text[1],text[2]),Write(code[1]))
        self.play(vec_1.shift, UP*2+LEFT*1)
        self.wait(2)
        self.play(RT(text[2],text[3]),Write(code[2]))
        self.play(ShowCreation(vec_2))
        self.wait(2)
        self.play(RT(text[3],text[4]),Write(code[3:5]))
        self.play(ShowCreation(arc_1))
        self.wait(2)
        self.play(RT(text[4],text[5]),Write(code[5]))
        self.play(RT(arc_1,arc_2))
        self.wait(2)
        cir=Circle().shift(np.array([-5,-1,0]))
        line=TangentLine(cir,0,length=5).set_color(PURPLE)
        self.play(RT(text[5],text[6]),Write(code[6:8]))
        self.play(ShowCreation(cir),ShowCreation(line))
        code[7].add_updater(lambda a:a.become(
            CodeLine("""line=TangentLine(cir,alpha=%.2f,
                 length=5)"""%t.get_value()).next_to(code[6],DOWN,aligned_edge=LEFT)
        ))
        line.add_updater(lambda a:a.become(
            TangentLine(cir,t.get_value(),length=5).set_color(PURPLE)
        ))
        self.add(code[7],line)
        self.play(t.set_value, 1, run_time=5,rate_func=linear)
        code[7].clear_updaters()
        line.clear_updaters()
        self.wait(2.5)



class TestLine(Scene):
    def construct(self):
        l_1=Arrow(LEFT*2,RIGHT*2,buff=0,
                  max_tip_length_to_length_ratio=0.05,
                  max_stroke_width_to_length_ratio=5)
        self.add(l_1)
