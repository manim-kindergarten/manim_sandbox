# from @鹤翔万里

from manimlib.imports import *

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
            '2D': RED_B,
            '3D': RED_B,
            'self': PINK,
            'mob': RED_D,
        },
        'font': 'Consolas',
        'size': 0.36,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)

class Scene_0(ThreeDScene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }
    def construct(self):
        self.set_camera_orientation(distance=1000)
        captions = [
            "在manim中，使用三维ndarray表示一个点的坐标",
            "在2D场景中，第三维度的坐标常设为0",
            "一个单位的长度取决于constants.py中的FRAME_HEIGHT",
            "FRAME_HEIGHT默认为8，即整个画面的总高度为8个单位",
            "画面的宽度由FRAME_HEIGHT和长宽比同时决定",
            "manim中，画面中心为坐标原点，向右为x轴正方向，向上为y轴正方向",
            "在constants.py中定义了一些常用的方向常量",
            "RIGHT为右一个单位，UP为上一个单位，同理LEFT，DOWN",
            "还有UR,UL,DR,DL等组合的沿对角线的方向",
            "以及四边TOP,BOTTOM,LEFT_SIDE,RIGHT_SIDE",
            "在3D中，还有OUT向外一个单位，IN向内一个单位",
            "同时，坐标之间可以根据向量的计算法则进行运算"
        ]
        captions_mob = VGroup(
            *[
                CodeLine(cap, font='思源黑体 CN Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        for i in [5, 6, 7, 8, 9, 10, 11]:
            captions_mob[i].add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
        plane = NumberPlane(
            axis_config={"stroke_color": BLACK}
        ).set_shade_in_3d()
        axes = ThreeDAxes(
            color=BLACK, 
            x_min=-FRAME_X_RADIUS, x_max=FRAME_X_RADIUS,
            y_min=-FRAME_Y_RADIUS, y_max=FRAME_Y_RADIUS,
            number_line_config={"color": BLACK}
        ).set_stroke(width=2)

        ndarray = CodeLine("np.array([x, y, z])", size=0.5)
        ndarray_2D = CodeLine("np.array([x, y, 0])", size=0.5)

        self.wait(2)
        self.play(Write(captions_mob[0]))
        self.play(Write(ndarray))
        self.wait(3)
        self.play(Transform(captions_mob[0], captions_mob[1]))
        self.play(Transform(ndarray, ndarray_2D))
        self.wait(3)
        self.add(captions_mob[0])

        self.play(Transform(captions_mob[0], captions_mob[2]), FadeOut(ndarray))
        arrow1 = DoubleArrow(np.array([4, 4, 1]), np.array([4, -4, 1]), color=GRAY, buff=0)
        frame_height = CodeLine("FRAME_HEIGHT=8", size=0.5)\
            .add_background_rectangle(color=WHITE, buff=0.2).move_to(np.array([4, -0.5, 2]))
        arrow2 = DoubleArrow(np.array([-FRAME_X_RADIUS, 1.5, 1]), np.array([FRAME_X_RADIUS, 1.5, 1]), color=GRAY, buff=0)
        frame_width = VGroup(
            CodeLine("FRAME_WIDTH=FRAME_HEIGHT*", size=0.4),
            CodeLine("PIXEL_WIDTH", size=0.4),
            CodeLine("PIXEL_HEIGHT", size=0.4),
            Line(ORIGIN, RIGHT, color=DARK_GRAY),
            CodeLine("≈14", size=0.4),
        )
        frame_width[-2].set_length(frame_width[-3].get_width())
        frame_width[-2].next_to(frame_width[0], RIGHT, buff=0.1)
        frame_width[1].next_to(frame_width[-2], UP, buff=0.1)
        frame_width[2].next_to(frame_width[-2], DOWN, buff=0.1)
        frame_width[-1].next_to(frame_width[-2], RIGHT, buff=0.1)
        frame_width.add_background_rectangle(color=WHITE, buff=0.2).move_to(np.array([-1, 1.5, 2]))
        # self.add(arrow1, arrow2, frame_height, frame_width)
        self.play(Write(arrow1))
        self.play(Write(frame_height[:-2]))
        self.wait(3)
        self.play(Transform(captions_mob[0], captions_mob[3]))
        self.play(Write(frame_height[-2:]))
        self.wait(3)
        self.play(Transform(captions_mob[0], captions_mob[4]))
        self.play(Write(arrow2))
        self.play(Write(frame_width[:-1]))
        self.wait()
        self.play(Write(frame_width[-1]))
        self.wait(4)

        self.play(Transform(captions_mob[0], captions_mob[5]), FadeOut(VGroup(arrow1, arrow2, frame_height, frame_width)))
        self.play(ShowCreation(plane))
        self.play(ShowCreation(axes))
        self.play(Write(plane.get_coordinate_labels(y_vals=[1, 2, 3, -1, -2], number_config={"color": BLACK})))
        origin = VGroup(
            Dot(color=ORANGE),
            CodeLine("ORIGIN=np.array([0, 0, 0])", size=0.4).add_background_rectangle(color=WHITE, buff=0.1)
        )
        origin[1].next_to(ORIGIN, DR, buff=0.1)
        self.play(Write(origin))
        self.wait(3)

        self.play(Transform(captions_mob[0], captions_mob[6]), FadeOut(origin))
        self.wait(2)
        self.play(Transform(captions_mob[0], captions_mob[7]))
        right = VGroup(
            Vector(RIGHT, color=ORANGE),
            CodeLine("RIGHT=np.array([1, 0, 0])", size=0.4).add_background_rectangle(color=WHITE, buff=0.1)
        )
        right[1].next_to(RIGHT, UR, buff=0.1)
        up = VGroup(
            Vector(UP, color=ORANGE),
            CodeLine("UP=np.array([0, 1, 0])", size=0.4).add_background_rectangle(color=WHITE, buff=0.1)
        )
        up[1].next_to(UP, UR, buff=0.1)
        left = VGroup(
            Vector(LEFT, color=ORANGE),
            CodeLine("LEFT=np.array([-1, 0, 0])", size=0.4).add_background_rectangle(color=WHITE, buff=0.1)
        )
        left[1].next_to(LEFT, LEFT, aligned_edge=RIGHT, buff=0.1)
        down = VGroup(
            Vector(DOWN, color=ORANGE),
            CodeLine("DOWN=np.array([0, -1, 0])", size=0.4).add_background_rectangle(color=WHITE, buff=0.1)
        )
        down[1].next_to(DOWN, RIGHT, buff=0.1)
        in_ = VGroup(
            Vector(UP, color=ORANGE),
            CodeLine("IN=np.array([0, 0, -1])", size=0.3).add_background_rectangle(color=WHITE, buff=0.1)
        )
        in_[1].next_to(IN, RIGHT, buff=0.1)
        out = VGroup(
            Vector(UP, color=ORANGE),
            CodeLine("OUT=np.array([0, 0, 1])", size=0.3).add_background_rectangle(color=WHITE, buff=0.1)
        )
        out[1].next_to(OUT, RIGHT, buff=0.1)
        out[0].rotate(PI/2, axis=RIGHT, about_point=ORIGIN)
        in_[0].rotate(PI/2, axis=LEFT, about_point=ORIGIN)
        self.play(Write(right))
        self.play(Write(up))
        self.wait(2)
        self.play(FadeIn(left), FadeIn(down))
        self.wait(4)

        self.play(FadeOut(VGroup(right, up, down, left)))
        self.play(Transform(captions_mob[0], captions_mob[8]))
        diag = VGroup(
            VGroup(
                Vector(UR, color=ORANGE),
                CodeLine("UR", size=0.5).add_background_rectangle(color=WHITE, buff=0.2).next_to(UR, UP)
            ),
            VGroup(
                Vector(UL, color=ORANGE),
                CodeLine("UL", size=0.5).add_background_rectangle(color=WHITE, buff=0.2).next_to(UL, UP)
            ),
            VGroup(
                Vector(DR, color=ORANGE),
                CodeLine("DR", size=0.5).add_background_rectangle(color=WHITE, buff=0.2).next_to(DR, DOWN)
            ),
            VGroup(
                Vector(DL, color=ORANGE),
                CodeLine("DL", size=0.5).add_background_rectangle(color=WHITE, buff=0.2).next_to(DL, DOWN)
            ),
        )
        self.play(FadeIn(diag))
        self.wait(4)
        self.play(FadeOut(diag))
        
        self.play(Transform(captions_mob[0], captions_mob[9]))
        large = VGroup(
            VGroup(
                Vector(TOP, color=ORANGE),
                CodeLine("TOP", size=0.5).add_background_rectangle(color=WHITE, buff=0.3).next_to(TOP, DOWN)
            ),
            VGroup(
                Vector(BOTTOM, color=ORANGE),
                CodeLine("BOTTOM", size=0.5).add_background_rectangle(color=WHITE, buff=0.3).next_to(BOTTOM, UP)
            ),
            VGroup(
                Vector(LEFT_SIDE, color=ORANGE),
                CodeLine("LEFT_SIDE", size=0.5).add_background_rectangle(color=WHITE, buff=0.3).next_to(LEFT_SIDE, RIGHT)
            ),
            VGroup(
                Vector(RIGHT_SIDE, color=ORANGE),
                CodeLine("RIGHT_SIDE", size=0.5).add_background_rectangle(color=WHITE, buff=0.3).next_to(RIGHT_SIDE, LEFT)
            ),
        )
        self.play(FadeIn(large))
        self.wait(4)
        self.play(FadeOut(large))

        self.play(Transform(captions_mob[0], captions_mob[10]))
        self.wait()
        self.move_camera(phi=PI/3, theta=-120*DEGREES)
        self.play(Write(in_), Write(out))
        self.wait(4)
        self.play(FadeOut(in_), FadeOut(out))
        self.move_camera(phi=0, theta=-90*DEGREES)
        self.wait()

        self.play(Transform(captions_mob[0], captions_mob[11]))
        right = VGroup(
            Vector(RIGHT, color=ORANGE),
            CodeLine("RIGHT").add_background_rectangle(color=WHITE, buff=0.1)
        )
        right[1].next_to(RIGHT, DOWN, buff=0.2)
        up = VGroup(
            Vector(UP, color=ORANGE),
            CodeLine("UP").add_background_rectangle(color=WHITE, buff=0.1)
        )
        up[1].next_to(UP, LEFT, buff=0.2)
        right3 = VGroup(
            Vector(RIGHT*3, color=ORANGE),
            CodeLine("3*RIGHT").add_background_rectangle(color=WHITE, buff=0.1)
        )
        right3[1].next_to(RIGHT*3, DOWN, buff=0.2)
        up2 = VGroup(
            Vector(UP*2, color=ORANGE),
            CodeLine("2*UP").add_background_rectangle(color=WHITE, buff=0.1)
        )
        up2[1].next_to(UP*2, LEFT, buff=0.2)
        self.play(Write(right), Write(up))
        self.wait()
        self.play(Transform(right, right3), Transform(up, up2))
        self.wait(2)
        tar = VGroup(
            Vector(RIGHT*3+UP*2, color=RED),
            CodeLine("3*RIGHT+2*UP").add_background_rectangle(color=WHITE, buff=0.1)
        )
        tar[1].next_to(RIGHT*3+UP*2, UP, buff=0.2)
        self.play(Write(tar))
        tond = CodeLine("np.array([3,2,0])").add_background_rectangle(color=WHITE, buff=0.1)
        tond.next_to(RIGHT*3+UP*2, UP, buff=0.2)
        self.wait()
        self.play(Transform(tar[1], tond))
        self.wait(4)
        self.play(FadeOut(tar), FadeOut(right), FadeOut(up), FadeOut(captions_mob[0]))
        self.wait(3)



