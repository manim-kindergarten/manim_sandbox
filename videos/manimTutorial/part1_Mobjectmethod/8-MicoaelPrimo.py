#from author @Micoael_Primo
from manimlib.imports import *
class CodeLine(Text):
    CONFIG = {
        't2c': {
            'y': average_color(BLUE, PINK),
            'z': average_color(BLUE, PINK),
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'IN': ORANGE,
            'OUT': ORANGE,
            'ORIGIN': ORANGE,
            'DL': ORANGE,
            'DR': ORANGE,
            'UL': ORANGE,
            'UR': ORANGE,
            'TOP': ORANGE,
            'BOTTOM': ORANGE,
            'LEFT_SIDE': ORANGE,
            'RIGHT_SIDE': ORANGE,
            'manim': GOLD,
            'constants.py': GOLD,
            'FRAME_HEIGHT': BLUE_D,
            'FRAME_WIDTH': BLUE_D,
            'PIXEL_HEIGHT': RED_B,
            'PIXEL_WIDTH': RED_B,
            'np': BLACK,
            'array': BLUE_D,
            'ndarray': BLUE,
            'FadeIn': average_color(RED, ORANGE),
            '"A0"':YELLOW_E,
            '"A1"':YELLOW_E,
            '"A2"':YELLOW_E,
            '"A3"':YELLOW_E,
            '"A4"':YELLOW_E,
            '"B0"':YELLOW_E,
            '"B1"':YELLOW_E,
            '"B2"':YELLOW_E,
            'A[1]':average_color(RED, ORANGE),
            'A[2]':average_color(RED, ORANGE),
            'A[3]':average_color(RED, ORANGE),
            'A[4]':average_color(RED, ORANGE),
            'B[0]':average_color(RED, ORANGE),
            'B[1]':average_color(RED, ORANGE),
            'B[2]':average_color(RED, ORANGE),
            'buff': RED,
            'shift': BLUE_D,
            'VGroup': BLUE_D,
            'TextMobject': BLUE_D,
            'radius': ORANGE,
            'side_length': ORANGE,
            'VMobject': BLUE_D,
            'submobject_to_align':BLUE_D,
            'aligned_edge':BLUE_D,
            'index_of_submobject_to_align':BLUE_D,
            'next_to':BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'Square': BLUE_D,
            'Circle': BLUE_D,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            '~':WHITE
        },
        'font': 'Consolas',
        'size': 0.36,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }
    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class Scene_0(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }
    def construct(_):
        captions = [
            "下面我们来看next_to方法",
            "顾名思义,next_to表示紧挨着一个物体",
            "比如我们想让一个方块挨着一个圆圈就可以这样写",
            "所以可以用a.next_to(b)来快速安排位置"
            
        ]
        commands = [
            "c = Circle(radius=0.5)",
            "sq = Square(side_length=0.5)",
            "c.next_to(sq)",
            
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='SOURCEHANSANSSC-MEDIUM', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        c = Circle(radius=0.5).shift(LEFT*2)
        sq = Square(side_length=0.5,fill_color=BLUE,fill_opacity=1.0).shift(LEFT*2)
        

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.1
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)

        coms = VGroup(
            *[
                CodeLine(com, font='Consolas', size=0.28).move_to(loc)
                for com in commands
            ]
        )

        _.play(FadeInFromDown(tex_bg))
        _.play(Write(caps[0]))
        _.wait()
        _.play(ReplacementTransform(caps[0],caps[1]))
        _.wait(2)

        _.play(ReplacementTransform(caps[1],caps[2]))
        _.wait()
        

        _.play(Write(coms[0]))
        _.play(ShowCreation(c))
        _.play(Write(coms[1].next_to(coms[0],DOWN,aligned_edge=LEFT)))
        _.play(ShowCreation(sq))
        _.play(Write(coms[2].next_to(coms[1],DOWN,aligned_edge=LEFT)))
        _.play(c.next_to,sq)

        _.play(ReplacementTransform(caps[2],caps[3]))
        _.wait()
        

class Scene_1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }
    def construct(_):
        captions = [
            "除此之外,我们可以指定next_to的方向。",
            "分别是UP,DOWN,LEFT,RIGHT",
            "表示相邻的位置",
            "那么就可以用a.next_to(b,方向)排顺序"
            
        ]
        commands = [
            "c.next_to(sq,UP)",
            "c.next_to(sq,DOWN)",
            "c.next_to(sq,LEFT)",
            "c.next_to(sq,RIGHT)"
            
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='SOURCEHANSANSSC-MEDIUM', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        c = Circle(radius=0.5).shift(LEFT*2)
        sq = Square(side_length=0.5,fill_color=BLUE,fill_opacity=1.0).shift(LEFT*2)
        

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.1
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)

        oria =CodeLine("c = Circle(radius=0.5)", font='Consolas', size=0.28).move_to(loc)
        orib = CodeLine("sq = Square(side_length=0.5)", font='Consolas', size=0.28).move_to(loc)
        oric = CodeLine("c.next_to(sq)", font='Consolas', size=0.28).move_to(loc)
        _.add(oria)
        _.add(orib.next_to(oria,DOWN,aligned_edge=LEFT))
        _.add(oric.next_to(orib,DOWN,aligned_edge=LEFT))

        coms = VGroup(
            *[
                CodeLine(com, font='Consolas', size=0.28).next_to(oric,DOWN,aligned_edge=LEFT)
                for com in commands
            ]
        )

        _.add(tex_bg)
        _.add(c,sq)
        c.next_to(sq)

        _.play(Write(caps[0]))
        _.play(ReplacementTransform(caps[0],caps[1]))

        def change(what,where):
            _.play(ReplacementTransform(what[where-1],what[where]))
        _.play(Write(coms[0].next_to(oric,DOWN,aligned_edge=LEFT)))
        _.play(c.shift,UP+LEFT)
        change(coms,1)        
        _.play(c.shift,2*DOWN)
        change(coms,2)        
        _.play(c.shift,UP+LEFT)
        change(coms,3)        
        _.play(c.shift,2*RIGHT)
        change(caps,2)
        _.wait(2)
        change(caps,3)
        _.wait(2)


class Scene_2(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }
    def construct(_):
        captions = [
            "有时候我们还可能实现类似于上/下/左/右对齐的功能",
            "这时候可以加入aligned_edge=方向",
            "这有5种取值方式:UP，DOWN，LEFT，RIGHT，ORIGIN",
            "如果要加入对齐,可以这样写：a.next_to(b,方向,aligned_edge=取值)"
            
        ]
        commands = [
            "c.next_to(sq,RIGHT,aligned_edge=UP)",
            "c.next_to(sq,RIGHT,aligned_edge=DOWN)",
            "c.next_to(sq,DOWN,aligned_edge=LEFT)",
            "c.next_to(sq,DOWN,aligned_edge=RIGHT)",
            "c.next_to(sq,DOWN,aligned_edge=ORIGIN)"
            
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='SOURCEHANSANSSC-MEDIUM', size=0.33).shift(DOWN * 3.4)
                for cap in captions
            ]
        )
        c = Circle(radius=0.5).shift(LEFT*2)
        sq = Square(side_length=0.5,fill_color=BLUE,fill_opacity=1.0).shift(LEFT*2)
        

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)

        oria =CodeLine("c = Circle(radius=0.5)", font='Consolas', size=0.21).move_to(loc)
        orib = CodeLine("sq = Square(side_length=0.5)", font='Consolas', size=0.21).move_to(loc)
        oric = CodeLine("c.next_to(sq)", font='Consolas', size=0.21).move_to(loc)
        _.add(oria)
        _.add(orib.next_to(oria,DOWN,aligned_edge=LEFT))
        _.add(oric.next_to(orib,DOWN,aligned_edge=LEFT))

        coms = VGroup(
            *[
                CodeLine(com, font='Consolas', size=0.21).next_to(oric,DOWN,aligned_edge=LEFT)
                for com in commands
            ]
        )

        _.add(tex_bg)
        _.add(c,sq)
        c.next_to(sq)
        def change(what,where):
            _.play(ReplacementTransform(what[where-1],what[where]))
            _.wait()


        up = c.copy().next_to(sq,RIGHT,aligned_edge=UP)
        down = c.copy().next_to(sq,RIGHT,aligned_edge=DOWN)
        left = c.copy().next_to(sq,DOWN,aligned_edge=LEFT)
        right = c.copy().next_to(sq,DOWN,aligned_edge=RIGHT)
        origin = c.copy().next_to(sq,DOWN,aligned_edge=ORIGIN)

        _.play(Write(caps[0]))
        _.wait()
        change(caps,1)
        _.wait()

        change(caps,2)
        _.wait()
        

        _.play(Write(coms[0]))
        _.play(ReplacementTransform(c,up))
        change(coms,1)  
        _.play(ReplacementTransform(up,down))
        change(coms,2)  
        _.play(ReplacementTransform(down,left))
        change(coms,3)  
        _.play(ReplacementTransform(left,right))
        change(coms,4)  
        _.play(ReplacementTransform(right,origin))
        
        change(caps,3)
        _.wait()


class Scene_3(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }
    def construct(_):
        captions = [
            "如果觉得默认的距离不够好的话",
            "可以加入一些缓冲区buff.",
            "可以写作一个关键词buff=缓冲大小",
            "像这样：a.next_to(b,方向,buff=取值)"
            
        ]
        commands = [
            "c.next_to(sq,RIGHT,aligned_edge=UP)",
            "c.next_to(sq,RIGHT,aligned_edge=DOWN)",
            "c.next_to(sq,DOWN,aligned_edge=LEFT)",
            "c.next_to(sq,DOWN,aligned_edge=RIGHT)",
            "c.next_to(sq,DOWN,aligned_edge=ORIGIN)"
            
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='SOURCEHANSANSSC-MEDIUM', size=0.33).shift(DOWN * 3.4)
                for cap in captions
            ]
        )
        c = Circle(radius=0.5).shift(LEFT*2)
        sq = Square(side_length=0.5,fill_color=BLUE,fill_opacity=1.0).shift(LEFT*2)
        

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = 2.9*UP + RIGHT * 3
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        oria =CodeLine("c = Circle(radius=0.5)", font='Consolas', size=0.28).move_to(loc)
        orib = CodeLine("sq = Square(side_length=0.5)", font='Consolas', size=0.28).move_to(loc)
        oric = CodeLine("c.next_to(sq)", font='Consolas', size=0.28).move_to(loc)
        _.add(oria)
        _.add(orib.next_to(oria,DOWN,aligned_edge=LEFT))
        _.add(oric.next_to(orib,DOWN,aligned_edge=LEFT))
        coms = VGroup(
            *[
                CodeLine(com, font='Consolas', size=0.21).next_to(oric,DOWN,aligned_edge=LEFT)
                for com in commands
            ]
        )

        _.add(tex_bg)
        _.add(c,sq)
        c.next_to(sq,DOWN)
        def change(what,where):
            _.play(ReplacementTransform(what[where-1],what[where]))
            _.wait()
        _.play(Write(caps[0]))
        change(caps,1)
        a = DoubleArrow((sq.get_center()),(c.get_center()),color=BLUE)
        tx = CodeLine("c.next_to(sq,DOWN,buff=2.5)", font='Consolas', size=0.28).next_to(oric,DOWN,aligned_edge=LEFT)
        def upr(obj):
            obj.become(CodeLine("c.next_to(sq,DOWN,buff="+str(round(sq.get_center()[1]-c.get_center()[1]-1+0.25,2))+")", font='Consolas', size=0.28).next_to(oric,DOWN,aligned_edge=LEFT))
            if sq.get_center()[1]-c.get_center()[1]-1+0.25 >0:
                a.become(DoubleArrow((sq.get_center()),(c.get_center()+0.2*UP),color=BLUE))
            else:
                a.become(DoubleArrow((sq.get_center()),(c.get_center()+0.2*DOWN),color=BLUE))
            tx.become(Text("buff="+str(round(sq.get_center()[1]-c.get_center()[1]-1+0.25,2)),size=0.28,font="Consolas",color=BLACK).move_to(a))
        cod=CodeLine("buff="+str(round(sq.get_center()[1]-c.get_center()[1]-1+0.25,2)), font='Consolas', size=0.25).move_to(loc)
        cod.add_updater(upr)
        _.play(Write(cod),Write(a),Write(tx))
        _.play(c.shift,3*DOWN,run_time=3)
        _.play(c.shift,3*UP,run_time=3)
        cod.remove_updater(upr)
        _.wait()
        change(caps,2)



class Scene_4(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }
    def construct(_):
        captions = [
            "其实我们还可以对VGroup进行对齐操作",
            "我们先来加入两个组a和b.",
            "一组有5个文本.另一组有3个文本.如下所示",
            "比如让B[0]和A[1]对齐",
            "传入的A[1]是一个VGroup的一项，B和它左对齐",
            "或者让B[0]和A[2]对齐",
            "传入的A[2]也是一个VGroup的一项，B和它左对齐",
            "如果让B[1]和A[2]对齐怎么办？",
            "我们需要用到属性——submobject_to_align和index_of_submobject_to_align",
            "传入的submobject_to_align是自己要对齐的位置。这里就是让B[1]和目标A[2]对齐",
            "或者还有一种等价的写法。像这样：",
            "我们可以看出，我们这里传入了一个VMobject的列表A",
            "这就相当于A的第index_of_submobject_to_align项和submobject_to_align对齐。",
            
        ]
        commands = [
            """A = VGroup(...)""",
            """B = VGroup(...)""",
            "B.next_to(A[2],DOWN,aligned_edge=LEFT)",
            "B.next_to(A[1],DOWN,aligned_edge=LEFT)",
            """B.next_to(A[2],DOWN,
    submobject_to_align=B[1],
    aligned_edge=LEFT)""",
            """B.next_to(A,DOWN,
    index_of_submobject_to_align=2,
    submobject_to_align=B[1],
    aligned_edge=LEFT)"""
            
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='SOURCEHANSANSSC-MEDIUM', size=0.33).shift(DOWN * 3.4)
                for cap in captions
            ]
        )
        vg1 = VGroup(
            TextMobject("$A_0$",color=BLACK).shift(LEFT*2),
            TextMobject("$A_1$",color=BLACK).shift(LEFT),
            TextMobject("$A_2$",color=BLACK),
            TextMobject("$A_3$",color=BLACK).shift(RIGHT),
            TextMobject("$A_4$",color=BLACK).shift(RIGHT*2),
        ).shift(2*LEFT).shift(UP)
        
        vg2 = VGroup(
            TextMobject("$B_0$",color=BLACK).shift(LEFT),
            TextMobject("$B_1$",color=BLACK),
            TextMobject("$B_2$",color=BLACK).shift(RIGHT)
        ).shift(3*LEFT).shift(UP*2)

        eg = vg2.copy().next_to(vg1[1],DOWN,aligned_edge=LEFT)
        eg3 = vg2.copy().next_to(vg1[2],DOWN,aligned_edge=LEFT)
        eg2 = vg2.copy().next_to(vg1[2],DOWN,submobject_to_align=vg2[1],aligned_edge=LEFT)


        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.6
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)

        coms = VGroup(
            *[
                CodeLine(com, font='Consolas', size=0.21).move_to(loc)
                for com in commands
            ]
        )

        _.add(tex_bg)
        def change(what,where):
            _.play(ReplacementTransform(what[where-1],what[where]))
            _.wait()
        
        _.play(Write(caps[0]))
        _.wait()
        change(caps,1)
        _.wait()
        change(caps,2)
        _.play(Write(coms[0].shift(-0.2*(UP)+1.2*LEFT)))
        _.play(Write(vg1))
        _.play(Write(coms[1].next_to(coms[0],DOWN,aligned_edge=LEFT)))
        _.play(Write(vg2))
        change(caps,3)
        _.wait(1)
        change(caps,4)
        _.play(Write(coms[3].next_to(coms[1],DOWN,aligned_edge=LEFT)))
        _.play(ReplacementTransform(vg2,eg))
        _.wait()
        change(caps,5)
        change(caps,6)
        _.play(FocusOn(coms[3]))
        _.play(ReplacementTransform(coms[3],coms[2].move_to(coms[3].get_center())))
        
        _.play(ReplacementTransform(eg,eg3))
        _.wait(1)

        change(caps,7)
        _.wait(2)
        change(caps,8)
        _.wait(2)
        _.play(FocusOn(coms[2]))
        _.play(FadeOut(coms[2]),FadeIn(coms[4].next_to(coms[1],DOWN,aligned_edge=LEFT)))
        
        _.play(ReplacementTransform(eg3,eg2))
        change(caps,9)

        _.wait(3)
        change(caps,10)
        _.play(FocusOn(coms[4]))
        _.play(FadeOut(coms[4]),FadeIn(coms[5].next_to(coms[1],DOWN,aligned_edge=LEFT)))
        _.wait(3)
        change(caps,11)
        _.wait(3)
        change(caps,12)
        _.wait(3)





