# from @cigar666

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
            'DEGREES': ORANGE,
            'BLACK': ORANGE,
            'Arc': ORANGE,
            'Circle': ORANGE,
            'AnnularSector': ORANGE,
            'ArcBetweenPoints': ORANGE,
            'CurvedArrow': ORANGE,
            'CurvedDoubleArrow': ORANGE,
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
            'p1': average_color(BLUE, PINK),
            'p2': average_color(BLUE, PINK),
            'angle': average_color(BLUE, PINK),
            'self': PINK,
            'mob': RED_D,
            '~': WHITE, # 随便搞个不常用的字符设成白色，以便在有时不能用空格占位时（比如涉及Transform）当空格用
        },
        'font': 'Consolas',
        'size': 0.3,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        # digest_config(self, kwargs)
        Text.__init__(self, text, **kwargs)

class Emote(SVGMobject):

    CONFIG = {
        'file_name': r'E:\GitHub\manim\my_manim_projects\my_projects\resource\svg_files\emote_01.svg',
        'shake_color': average_color(YELLOW, ORANGE),
    }
    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        SVGMobject.__init__(self, file_name=self.file_name, **kwargs)
        self.list = [0, 1, 2, 3, 5, 6, 9]
        for i in self.list:
            self[i].set_fill(self.shake_color, 0)

        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
        # self.add_updater(self.update_emote)

    def update_emote(self, mob):
        h, w, c = self.get_height(), self.get_width(), self.get_center()

        add_shake = not((h == self.attribute_list[0]) and (w == self.attribute_list[1])
                        and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]

        if add_shake:
            for i in self.list:
                self[i].set_opacity(1)
        else:
            for i in self.list:
                self[i].set_opacity(0)

    # def update_emote_02(self, mob):
    #     h, w, c = self.get_height(), self.get_width(), self.get_center()
    #
    #     add_shake = not((h == self.attribute_list[0]) and (w == self.attribute_list[1])
    #                     and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
    #     self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
    #
    #     if add_shake:
    #         self.set_opacity(1)
    #     else:
    #         self.set_opacity(0)

    def shake_on(self):
        self.set_opacity(1)
        return self

    def shake_off(self):
         for i in self.list:
            self[i].set_fill(self.shake_color, 0)
         return self

class Emote_new(VGroup):
    CONFIG = {
        'file_name': r'E:\GitHub\manim\my_manim_projects\my_projects\resource\svg_files\emote_01.svg',
        'shake_color': average_color(YELLOW, ORANGE),
        'height': 2.5,
    }
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.emote = SVGMobject(self.file_name, **kwargs).set_height(self.height)
        self.emote_02 = SVGMobject(self.file_name, **kwargs).set_height(self.height)
        self.center_dot = Dot().move_to(self.emote.get_center()).shift((DOWN + RIGHT*0.4) * self.height * 0.18).set_opacity(0)
        list = [0, 1, 2, 3, 5, 6, 9]
        for i in list:
            self.emote[i].set_fill(self.shake_color, 0)
            self.emote_02[i].set_fill(self.shake_color, 0)
        self.add(self.emote_02, self.center_dot, self.emote)
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
        self.emote_02.add_updater(self.update_emote)

    def update_emote(self, mob):
        h, w, c = self.get_height(), self.get_width(), self.get_center()

        add_shake = not((h == self.attribute_list[0]) and (w == self.attribute_list[1])
                        and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]

        if add_shake:
            mob.set_opacity(1)
        else:
            mob.set_opacity(0)

    def shake_on(self):
        self.emote_02.set_opacity(1)
        return self
    def shake_off(self):
        self.emote_02.set_opacity(0)
        return self

class 代码风格测试(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        emote = Emote_new(color=BLACK, plot_depth=1).set_height(2.4).shift(LEFT * 4 + UP)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 2.64
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        tex_add = CodeLine('self.add(mob)').move_to(loc)
        tex_shift_l = CodeLine('mob.shift(LEFT)').next_to(tex_add, DOWN).align_to(tex_add, LEFT)
        tex_flip_1 = CodeLine('mob.flip()').next_to(tex_shift_l, DOWN).align_to(tex_shift_l, LEFT)
        tex_flip_2 = CodeLine('mob.flip()').next_to(tex_flip_1, DOWN).align_to(tex_flip_1, LEFT)
        tex_shift_r2 = CodeLine('mob.shift(RIGHT * 2)').next_to(tex_flip_2, DOWN).align_to(tex_flip_2, LEFT)
        tex_scale_2 = CodeLine('mob.scale(2)').next_to(tex_shift_r2, DOWN).align_to(tex_shift_r2, LEFT)
        tex_annotation = CodeLine('# 所有对mob的变换均为瞬间完成的，\n\n'
                                  '# 但为了演示变换过程，\n\n'
                                  '# 实际执行的是将变换放入\n\n'
                                  '# self.play()后的对应动画过程', font='思源黑体 Bold', size=0.29)\
                        .next_to(tex_scale_2, DOWN).align_to(tex_scale_2, LEFT).set_color(GREEN)

        loc_02 = DOWN * 1.2
        caption_add = CodeLine('使用self.add(mob)将物体（mob）加入场景', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_shift_1 = CodeLine('使用mob.shift(LEFT)将mob向左移动1个单位', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_flip_1 = CodeLine('使用mob.flip()将mob翻转', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_flip_2 = CodeLine('使用mob.flip()将mob再次翻转', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_shift_r2 = CodeLine('使用mob.shift(RIGHT*2)将mob向右移动2个单位', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_scale_2 = CodeLine('使用mob.scale(2)将mob沿自身中心放大2倍', font='思源黑体 Bold', size=0.32).to_edge(loc_02)

        self.wait()
        self.play(FadeInFromDown(tex_bg))
        self.play(Write(tex_add), Write(caption_add), run_time=1.5)
        self.add(emote)
        self.wait()

        self.play(Write(tex_shift_l), ReplacementTransform(caption_add, caption_shift_1), run_time=1.5)
        self.play(emote.shift, LEFT, run_time=1.6)
        self.wait()

        self.play(Write(tex_flip_1), ReplacementTransform(caption_shift_1, caption_flip_1), run_time=1.5)
        self.play(emote.flip, run_time=1.25)
        self.wait(0.5)
        self.play(Write(tex_flip_2), ReplacementTransform(caption_flip_1, caption_flip_2), run_time=1.5)
        self.play(emote.flip, run_time=1.25)
        self.wait()

        self.play(Write(tex_shift_r2), ReplacementTransform(caption_flip_2, caption_shift_r2), run_time=1.5)
        self.play(emote.shift, RIGHT * 2, run_time=1.6)
        self.wait()

        self.play(Write(tex_scale_2), ReplacementTransform(caption_shift_r2, caption_scale_2), run_time=1.5)
        self.play(emote.scale, 2, run_time=1.6)

        self.wait(0.4)
        self.play(Write(tex_annotation), FadeOut(caption_scale_2), run_time=4)

        self.wait(5)

class Emote_bounce_around(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        emote = Emote_new(height=3.2, plot_depth=-1, color=BLACK).shift(UP * 1.234) #.set_opacity(0.12)
        emote.emote_02.remove_updater(emote.update_emote)
        self.emote_velocity = (RIGHT * 2 + UP * 1.25) * 2.4e-2
        self.rotate_speed = 2.5 * DEGREES

        def update_emote(l, dt):
            l.shift(self.emote_velocity)
            l.rotate(self.rotate_speed, about_point=l.center_dot.get_center())
            self.emote_velocity += (RIGHT * 2 + UP * 1.25) * 2.8e-5 * np.sign(self.emote_velocity)

            if abs(l.get_center()[1]) > (FRAME_HEIGHT - l.get_height())/2:
                self.emote_velocity *= DR # or we can use self.emote_velocity[1] *= -1
                self.rotate_speed *= -1
                l.shake_on()
            if abs(l.get_center()[0]) > (FRAME_WIDTH - l.get_width())/2:
                self.emote_velocity *= UL # or we can use self.emote_velocity[0] *= -1
                self.rotate_speed *= -1
                l.shake_on()
            else:
                l.emote_02.set_opacity(l.emote_02.get_fill_opacity() - 0.02 if l.emote_02.get_fill_opacity() > 0 else 0)

        emote.add_updater(update_emote)
        self.add(emote)

        self.wait(24)

