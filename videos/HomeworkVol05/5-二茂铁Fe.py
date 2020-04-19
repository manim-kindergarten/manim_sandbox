from manimlib.imports import *

class CodeLine(Text):

    CONFIG = {
        't2c': {
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'UR': ORANGE,
            'UL': ORANGE,
            'DR': ORANGE,
            'DL': ORANGE,
            'ORIGIN': ORANGE,
            'FadeIn': average_color(RED, ORANGE),
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            'set_fill': BLUE_D,
            'round_corners': BLUE_D,
            'np': BLACK,
            'array': BLUE,
            'Polygon': RED,
            'RegularPolygon': RED,
            'Triangle': RED,
            'color': RED_C,
            'opacity': RED_C,
            'width': RED_C,
            'radius':RED_C,
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
            'self': PINK,
            'mob': RED_D,
            'p1': BLACK,
            'p2': BLACK,
            'p3': BLACK,
            '~': WHITE, # 随便搞个不常用的字符设成白色，以便在有时不能用空格占位时（比如涉及Transform）当空格用
        },
        'font': 'Consolas',
        # 'size': 0.36,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        # digest_config(self, kwargs)
        Text.__init__(self, text, **kwargs)
        self.scale(0.36)


class PolygonsShow(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }
    def construct(self):
        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.5
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        self.play(ShowCreation(tex_bg))
        self.wait()
        p1 = np.array([-1, 0, 0])
        p2 = np.array([-1, 1.25, 0])
        p3 = np.array([1, 0, 0])
        pGroup = [p1, p2, p3]
        d1 = Dot(p1,color=BLUE).scale(0.2)
        d2 = Dot(p2, color=BLUE).scale(0.2)
        d3 = Dot(p3, color=BLUE).scale(0.2)
        dGroup = VGroup(d1,d2,d3)
        tri = Polygon(*pGroup, stroke_width=1, color=BLUE).set_stroke(width=2)
        triangle = VGroup(dGroup, tri).shift(LEFT*2.5).scale(3)

        Pentagon = RegularPolygon(5, color=ORANGE, fill_color=ORANGE, fill_opacity=0.7).scale(2.3).shift(LEFT*4.8)
        vl = Pentagon.get_vertices()
        Pentagram = Polygon(vl[0], vl[2], vl[-1], vl[1],vl[3],color=ORANGE, fill_color=ORANGE, fill_opacity=0.7).move_to(LEFT*1.1)
        p7 = RegularPolygon(7, color=ORANGE, fill_color=BLUE_A, fill_opacity=0.7).scale(2.3).shift(LEFT*2.3)
        p6 = RegularPolygon(6, color=ORANGE, fill_color=YELLOW_B, fill_opacity=0.7).scale(2.3).shift(LEFT * 2.3)
        Regtri = Triangle().next_to(Pentagon,buff=1).shift(2.5*UP).scale(1.5).set_fill(BLUE, 0.8)

        c1 = CodeLine('p1 = np.array([-1, 0, 0])').move_to(loc).scale(0.8)
        c2 = CodeLine('p2 = np.array([-1, 1.25, 0])').next_to(c1, DOWN).scale(0.8).align_to(c1, LEFT)
        c3 = CodeLine('p3 = np.array([1, 0, 0])').next_to(c2, DOWN).scale(0.8).align_to(c2, LEFT)
        c4 = CodeLine('triangle = Polygon(p1, p2, p3)').next_to(c3, DOWN).scale(0.8).align_to(c3, LEFT)
        c5 = CodeLine(
                    '''
                    triangle.set_fill(color=ORANGE,
                    opacity=0.8)
                    '''
                      ).next_to(c4, DOWN).scale(0.8).align_to(c4, LEFT)
        c6 = CodeLine('triangle.set_fill(opacity=0.2)').next_to(c5, DOWN).scale(0.8).align_to(c5, LEFT)
        c7 = CodeLine('''
                      triangle.set_stroke(color=ORANGE,
                      width=2)
                      ''').next_to(c6, DOWN).scale(0.7).align_to(c6, LEFT)
        c8 = CodeLine('triangle.round_corners(0.2)').next_to(c7, DOWN).scale(0.8).align_to(c7, LEFT)

        c11 = CodeLine('Reghep= RegularPolygon(7)').move_to(loc).scale(0.8)
        c12 = CodeLine('Hexagon = RegularPolygon(6)').next_to(c11, DOWN).scale(0.8).align_to(c11, LEFT)
        c9 = CodeLine('Pentagon = RegularPolygon(5)').next_to(c12, DOWN).scale(0.8).align_to(c12, LEFT)
        c10 = CodeLine('Regtri = Triangle()').next_to(c9, DOWN).scale(0.8).align_to(c9, LEFT)




        loc_02 = DOWN * 1.2
        t1 = CodeLine('manim中通过点的位置来确定多边形的形状与位置', font='思源黑体').to_edge(loc_02)
        t2 = CodeLine('我们可以设置其内部的填充效果(set_fill)', font='思源黑体').to_edge(loc_02)
        t3 = CodeLine('改变颜色(color)或不透明度(opacity)', font='思源黑体').to_edge(loc_02)
        t4 = CodeLine('通过(set_stroke)改变其线宽(width)及线的颜色(color)', font='思源黑体').to_edge(loc_02)
        t5 = CodeLine('设置圆角半径(radius)，获得圆角效果', font='思源黑体').to_edge(loc_02)

        t6 = CodeLine('但更多时候我们需要的是规则正多边形', font='思源黑体').to_edge(loc_02)
        t7 = CodeLine('而正三角形更具独特性,因此用的也更多', font='思源黑体').to_edge(loc_02)

        self.play(
                  ShowCreation(dGroup),
                  FadeIn(t1),
                  Write(c1),
                  run_time=1,
        )
        self.play(
            Write(c2),
            Write(c3),
        )
        self.play(ShowCreation(tri),
                  Write(c4))
        self.wait(1.1)

        self.play(
            ReplacementTransform(t1, t2),
            ApplyMethod(tri.set_fill, ORANGE, 0.8),
            Write(c5),
            run_time=1.3
        )
        self.wait(3.5)

        self.play(
            ReplacementTransform(t2, t3),
            Write(c6),
            ApplyMethod(tri.set_fill, ORANGE, 0.2),
        )
        self.wait(3.5)

        self.play(
            ReplacementTransform(t3, t4),
            Write(c7),
            ApplyMethod(tri.set_stroke, GRAY, 4),
            run_time=1.5
        )
        self.wait(3.5)

        self.play(
            Write(c8),
            FadeOut(d1),
            FadeOut(d2),
            FadeOut(d3),
            ApplyMethod(tri.round_corners, 0.2),
            ReplacementTransform(t4, t5),
            run_time=1.2
        )
        self.wait(3.5)

        self.play(
            FadeOut(c1),
            FadeOut(c2),
            FadeOut(c3),
            FadeOut(c4),
            FadeOut(c5),
            FadeOut(c6),
            FadeOut(c7),
            FadeOut(c8),
            FadeOut(tri),
            run_time = 1
        )
        self.wait(0.5)

        self.play(
            ReplacementTransform(t5,t6),
            Write(c11),
            ShowCreation(p7),
            run_time=1.4
        )
        self.wait(3)
        self.play(
            ReplacementTransform(p7, p6),
            Write(c12),
            run_time=1.3
        )
        self.wait(2)
        self.play(
            ReplacementTransform(p6, Pentagon),
            Write(c9),
            run_time=1.2
        )
        self.wait(4)

        self.play(
            ReplacementTransform(t6, t7),
            Write(c10),
            ShowCreation(Regtri),
        )
        self.wait(4)

        self.play(
            FadeOut(Regtri),
            FadeOut(t7),
            ApplyMethod(Pentagon.move_to, ORIGIN+LEFT*1.1)
        )
        self.play(
            ReplacementTransform(Pentagon, Pentagram),
            run_time=1.3
        )

        self.wait(5)
