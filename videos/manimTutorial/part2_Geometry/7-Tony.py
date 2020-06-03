# from @鹤翔万里

from manimlib.imports import *


class Scene_07(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        },
    }
    def construct(self):
        captions = [
            "VGroup类似于python中的列表",                                 # 0
            "可以使用类似append的add方法,将物体添加到VGroup中",              # 1
            "也可以使用add_to_back和remove方法",                          # 2
            "也可以通过下标索引来对元素进行访问",                            # 3
            "但VGroup整体也是一个VMobject,所以可以使用相应方法(list不能)",    # 4
            "例如,可以对子物体进行移动,也可以对整体进行移动",                  # 5
            "VGroup中每个子物体都是独立个体,不会与其他子物体相关联",           # 6
            "VGroup的arrange方法可以对子物体安装索引顺序进行排列",            # 7
            "arrange方法的使用与next_to相同",                             # 8
            "本质上是对每两个(索引)相邻子物体进行同样的next_to操作",           # 9
            "当参数center为True时(默认),将在对齐后将整体移动到中心",          # 10
            "同时VGroup也可以进行嵌套使用",                                # 11
            "VGroup中只能含有VMobject及子类,所以例如ImageMobject是无法放入的"# 12
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        line = Line(LEFT, RIGHT, stroke_width=1, stroke_color=GRAY).set_width(5.4).move_to(tex_bg)
        loc = Line(LEFT, RIGHT, stroke_width=1, stroke_color=GRAY).set_width(5.4).move_to(tex_bg.get_top())

        code1 = [
            ">>> a = [...]",
            ">>> a.append(3)",
            ">>> a.remove(2)",
        ]
        code2 = [
            ">>> b = VGroup(...)",
            ">>> b.add(mob3)",
            ">>> b.add_to_back(mob)",
            ">>> b.remove(mob2)",
        ]
        codes1 = VGroup(
            *[
                CodeLine(code) for code in code1
            ]
        ).arrange(DOWN, aligned_edge=LEFT).next_to(loc, DOWN, aligned_edge=LEFT).shift(RIGHT*0.2)
        codes2 = VGroup(
            *[
                CodeLine(code) for code in code2
            ]
        ).arrange(DOWN, aligned_edge=LEFT).next_to(line, DOWN, aligned_edge=LEFT).shift(RIGHT*0.2)

        lis = Rectangle(width=6, height=1, stroke_width=1, stroke_color=DARK_GREY).move_to(LEFT*2.5+UP*1.5)
        lis_num = VGroup(
            *[
                CodeLine(s) for s in ["0", "1", "2", "3"]
            ]
        ).arrange(RIGHT, buff=0.5).next_to(lis.get_left(), RIGHT, buff=0.5)

        vg = Rectangle(width=6, height=1, stroke_width=1, stroke_color=DARK_GREY).move_to(LEFT*2.5+DOWN*1.5)
        vg_mob = VGroup(
            *[
                CodeLine(s) for s in ["mob0", "mob1", "mob2", "mob3"]
            ]
        ).arrange(RIGHT, buff=0.3).next_to(vg.get_left(), RIGHT, buff=0.3)
        mob = CodeLine("mob").move_to(vg_mob[0])
        for i, j in zip(lis_num, vg_mob):
            i.move_to(j, coor_mask=np.array([1, 0, 0]))
        
        lis_index = VGroup(
            *[
                CodeLine("a[{}]".format(i)) for i in [0, 1, 2]
            ]
        )
        for each, j in zip(lis_index, lis_num):
            each.next_to(j, UP, buff=1)
            
        vg_index = VGroup(
            *[
                CodeLine("b[{}]".format(i)) for i in [0, 1, 2, 3]
            ]
        )
        for each, j in zip(vg_index, vg_mob):
            each.next_to(j, UP, buff=1)

        lis_name = CodeLine("a: list", size=0.25).next_to(lis, LEFT)
        vg_name = CodeLine("b: VGroup", size=0.25).next_to(vg, LEFT)
        

        self.wait()
        self.play(Write(caps[0]), FadeInFromDown(VGroup(tex_bg, line)))
        self.play(Write(codes1[0]), Write(codes2[0]))
        self.play(
            Write(lis), Write(vg),
            Write(lis_name), Write(vg_name)
        )
        self.play(Write(lis_num[:3]), Write(vg_mob[:3]))
        self.wait(3)
        self.play(Transform(caps[0], caps[1]))
        self.play(Write(codes1[1]))
        self.play(FadeInFrom(lis_num[3], RIGHT))
        self.wait()
        self.play(Write(codes2[1]))
        self.play(FadeInFrom(vg_mob[3], RIGHT))
        self.wait(2)
        self.play(Transform(caps[0], caps[2]))
        self.play(Write(codes2[2]))
        self.play(vg_mob.shift, (vg_mob[1].get_center() - vg_mob[0].get_center()))
        self.play(FadeInFrom(mob, LEFT))
        self.wait(2)
        self.play(Write(codes1[2]))
        self.play(FadeOutAndShift(lis_num[2], UP), lis_num[3].shift, (lis_num[0].get_center() - lis_num[1].get_center()))
        self.wait()
        self.play(Write(codes2[3]))
        self.play(FadeOutAndShift(vg_mob[2], UP), vg_mob[3].shift, (vg_mob[0].get_center() - vg_mob[1].get_center()))
        self.wait(2)
        self.play(Transform(caps[0], caps[3]))
        self.wait(2)
        arrow1 = Arrow(lis_index[0].get_bottom(), lis_num[0].get_top(), color=ORANGE, buff=0.1)
        arrow2 = Arrow(vg_index[0].get_bottom(), mob.get_top(), color=ORANGE, buff=0.1)
        self.play(Write(lis_index[0]), Write(arrow1))
        self.play(Write(vg_index[0]), Write(arrow2))
        self.wait()
        self.play(
            Transform(lis_index[0], lis_index[1]),
            Transform(vg_index[0], vg_index[1]),
            arrow1.shift, (lis_num[1].get_center() - lis_num[0].get_center()),
            arrow2.shift, (lis_num[1].get_center() - lis_num[0].get_center()),
        )
        self.wait()
        self.play(
            Transform(lis_index[0], lis_index[2]),
            Transform(vg_index[0], vg_index[2]),
            arrow1.shift, (lis_num[1].get_center() - lis_num[0].get_center()),
            arrow2.shift, (lis_num[1].get_center() - lis_num[0].get_center()),
        )
        self.wait()
        self.play(
            Transform(vg_index[0], vg_index[3]),
            arrow2.shift, (lis_num[1].get_center() - lis_num[0].get_center()),
        )
        self.wait()
        self.play(FadeOut(VGroup(arrow1, arrow2, lis_index[0], vg_index[0])))
        self.wait()
        self.play(FadeOut(VGroup(vg_mob, vg, vg_name, lis, lis_name, lis_num, codes1, codes2, line, mob)))
        self.wait(2)

        # self.add(vg_index, lis_index)

        code3 = [
            "~~~ vg = VGroup(a, b, c)",
            ">>> vg.shift(UP)",
            ">>> vg[0].shift(DOWN*2)",
            ">>> b.shift(DOWN)",
            ">>> vg.arrange(DOWN,",
            "~~~~~~~~center=True,",
            "~~~~~~~~aligned_edge=LEFT",
            "~~~~).shift(LEFT*3)"
        ]
        code4 = [
            "~~~ vg2 = VGroup(d, e)",
            "~~~ VG = VGroup(vg, vg2)",
            ">>> img = ImageMobject(..)",
            ">>> VG.add(img)"
        ]
        codes3 = VGroup(
            *[
                CodeLine(code) for code in code3
            ]
        ).arrange(DOWN, aligned_edge=LEFT).next_to(loc, DOWN, aligned_edge=LEFT).shift(RIGHT*0.2)
        codes4 = VGroup(
            *[
                CodeLine(code) for code in code4
            ]
        ).arrange(DOWN, aligned_edge=LEFT).next_to(codes3[0], DOWN, aligned_edge=LEFT)

        a = Square(color=BLUE_D, side_length=1.7)
        b = Circle(color=ORANGE)
        c = RegularPolygon(6, color=LIGHT_BROWN)
        d = Square(color=GREEN_D, side_length=1.7)
        e = Circle(color=GREEN_E)
        a.add(CodeLine("a", color=BLUE_D).move_to(a))
        b.add(CodeLine("b", color=ORANGE).move_to(b))
        c.add(CodeLine("c", color=LIGHT_BROWN).move_to(c))
        d.add(CodeLine("d", color=GREEN_D).move_to(d))
        e.add(CodeLine("e", color=GREEN_E).move_to(e))
        vg2 = VGroup(d, e).arrange(DOWN, aligned_edge=RIGHT).shift(LEFT*2)
        vg = VGroup(a, b, c)
        vg.arrange(RIGHT, aligned_edge=ORIGIN).shift(LEFT*3)
        VG = VGroup(vg, vg2)
        
        self.play(Transform(caps[0], caps[4]))
        self.play(Write(codes3[0]), GrowFromEdge(vg, DOWN))
        self.wait(3)
        self.play(Transform(caps[0], caps[5]))
        self.wait()
        self.play(Write(codes3[1]))
        self.play(vg.shift, UP)
        self.wait()
        self.play(Write(codes3[2]))
        self.play(vg[0].shift, DOWN*2)
        self.wait(2)
        self.play(Transform(caps[0], caps[6]))
        self.wait()
        self.play(Write(codes3[3]))
        self.play(b.shift, DOWN)
        self.wait(2)
        self.play(Transform(caps[0], caps[7]))
        self.wait()
        self.play(Write(codes3[4:]))
        self.play(
            vg.arrange, DOWN, {"aligned_edge": LEFT},
            vg.shift, LEFT*3
        )
        self.wait(2)
        self.play(Transform(caps[0], caps[8]))
        self.wait(3)
        self.play(Transform(caps[0], caps[9]))
        self.wait()
        
        arrow_1 = Arrow(b.get_center(), a.get_center(), color=GOLD, buff=0.25)
        arrow_2 = Arrow(c.get_center(), b.get_center(), color=GOLD, buff=0.25)
        dline = DashedLine(UP*3.5, DOWN*3, color=BLUE).move_to(vg.get_left(), coor_mask=np.array([1, 0, 0]))

        # self.add(arrow_1, arrow_2, dline)
        self.play(Write(dline), Write(arrow_1))
        self.wait()
        self.play(Write(arrow_2))
        self.wait(2)
        self.play(Transform(caps[0], caps[10]), FadeOut(VGroup(arrow_1, arrow_2, dline)))
        self.wait()
        self.play(ShowCreationThenDestructionAround(codes3[5][8:-1], surrounding_rectangle_config={"color": BLUE}))
        self.wait()
        self.play(Transform(caps[0], caps[11]), FadeOut(codes3[1:]), vg.shift, LEFT*1.5)
        self.wait()
        self.play(Write(codes4[0]), FadeIn(vg2))
        self.wait()
        self.play(Write(codes4[1]))
        self.wait()
        vg_rec = DashedVMobject(SurroundingRectangle(vg, color=RED_A, fill_opacity=1, plot_depth=5), num_dashes=40)
        vg2_rec= DashedVMobject(SurroundingRectangle(vg2, color=RED_C, fill_opacity=1, plot_depth=5), num_dashes=40)
        VG_rec = DashedVMobject(SurroundingRectangle(VG, color=RED_E, plot_depth=5, buff=0.25), num_dashes=40)
        vg_lab = Text("vg", size=0.4, color=RED_A, font="Consolas", plot_depth=10).move_to(vg)
        vg2_lab= Text("vg2",size=0.4, color=RED_C, font="Consolas", plot_depth=10).move_to(vg2)
        VG_lab = Text("VG", size=0.5, color=RED_E, font="Consolas", plot_depth=10).move_to(VG)
        self.play(Write(vg_rec), Write(vg2_rec), Write(vg_lab), Write(vg2_lab))
        self.wait()
        self.play(Write(VG_rec), Write(VG_lab))
        self.wait(3)
        self.play(FadeOut(VGroup(vg_rec, vg2_rec, VG_rec, vg_lab, vg2_lab, VG_lab)))
        self.play(Transform(caps[0], caps[12]))
        self.wait()
        img = ImageMobject("Tony.png").set_height(1.2)
        self.play(FadeIn(img), Write(codes4[2]))
        self.wait()
        self.play(Write(codes4[3]))
        cross = Cross(codes4[3][4:], plot_depth=100).set_plot_depth(1000)
        self.play(Write(cross))
        self.wait(3)
        self.play(FadeOut(Group(img, codes4[2:], cross)))
        self.wait(2)
        self.play(FadeOut(VGroup(*self.mobjects)))



class CodeLine(Text):
    CONFIG = {
        't2c': {
            'x': average_color(BLUE, PINK),
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
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'arrange': BLUE_D,
            'VGroup': BLUE_D,
            'VMobject': BLUE_D,
            'ImageMobject': BLUE_D,
            'list': BLUE_D,
            'append': BLUE_D,
            'remove': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'add_to_back': BLUE_D,
            'vector': ORANGE,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            'aligned_edge': RED,
            'center': RED,
            ">>>": RED,
            'coor_mask': RED,
            'point_or_mobject': RED,
            'python': GOLD,
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'True': average_color(BLUE, PINK),
            '2D': RED_B,
            '3D': RED_B,
            'self': PINK,
            'mob': RED_D,
            'mob1': RED_D,
            'mob2': RED_D,
            'mob3': RED_D,
            'mob0': RED_D,
            "~": "#EBEBEB",
            "vg2": DARK_GRAY,
        },
        'font': 'Consolas',
        'size': 0.36,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }
    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)

