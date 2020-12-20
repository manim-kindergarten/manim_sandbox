# from @cigar666

"""

1. 在以前的代码的基础上改写的，有的地方不是很棒，比如后面的移动方块可以用for循环统一表示的

2. 里面的公式使用了MyText类，但在表示和'\\sum'相关的公式时有bug，
    解决方法是在MyText类中加入可以和debugTex配合使用的基于下标的替换方式

"""

from manimlib.imports import *
from manim_sandbox.utils.imports import *

class Sum_of_cubes_new(ThreeDScene):

    CONFIG = {
        'camera_init': {
            'phi': 52.5 * DEGREES,
            'gamma': 0,
            'theta': -45 * DEGREES,
        },
        'camera_config': {
            'should_apply_shading': False
        },
    }

    def construct(self):
        self.set_camera_orientation(**self.camera_init)

        color_list = [[GREEN_E, MAROON, GREEN_A, TEAL_D],
                      [MAROON, BLUE_D, GOLD_D, PURPLE_A],
                      [GREEN_A, GOLD_D, RED, YELLOW_D],
                      [TEAL_D, PURPLE_A, YELLOW_D, PINK]]

        shift_list = [0, 1.5, 1.5 + 2.5, 1.5 + 2.5 + 3.5]

        size = 0.5
        cube_config = {
            # 'reset_color': False,
            'cube_size': size,
            'gap': 0,
            'fill_opacity': 0.85,
            'stroke_color': WHITE,
            'stroke_width': 1.2,
        }

        cube_config_02 = {
            # 'reset_color': False,
            'cube_size': size,
            'gap': 0,
            'fill_opacity': 0.2,
            'stroke_color': WHITE,
            'stroke_width': 0.6,
        }

        group_all = VGroup()
        for j in range(4):
            for i in range(4):
                rect_ij = Cube_array(resolution=(4 - j, i + 1, 1), fill_color=color_list[4 - 1 - j][i], **cube_config)\
                    .outer_faces.shift((shift_list[4 - 1 - j] * UP + shift_list[i] * RIGHT) * size)
                group_all.add(rect_ij)

        s = 0.98
        # square_01 = self.l_shape_mn((1, 1), 4, scale_factor=0.9, color=LIGHT_GREY, stroke_opacity=1).set_shade_in_3d()
        # square_02 = self.l_shape_mn((3, 3), 4, scale_factor=0.9, color=LIGHT_GREY, stroke_opacity=1).set_shade_in_3d()
        # square_03 = self.l_shape_mn((6., 6.), 4, scale_factor=0.9, color=LIGHT_GREY, stroke_opacity=1).set_shade_in_3d()
        # square_04 = self.rect_mn_2d((10., 10.), 4, scale_factor=0.9, color=LIGHT_GREY, stroke_opacity=1).set_shade_in_3d()

        # group_square = VGroup(square_01, square_02, square_03, square_04).set_shade_in_3d()
        s02 = 1.1
        group_all_02 = VGroup()
        for j in range(4):
            for i in range(4):
                rect_ij = Cube_array(resolution=(4 - j, i + 1, 1), fill_color=color_list[4 - 1 - j][i], **cube_config_02)\
                    .scale(s02).outer_faces.shift((shift_list[4 - 1 - j] * UP + shift_list[i] * RIGHT) * size * (1 + s))
                group_all_02.add(rect_ij)

        group_all.shift((LEFT + DOWN) * 2.25 + (LEFT + UP) * 0.8).shift(np.array([0, 0, 1.2])).scale(1.5)
        # group_square.shift((LEFT + DOWN) * 3.5 + (LEFT + UP) * 0.8 + np.array([0, 0, -0.25]))
        group_all_02.shift((LEFT + DOWN) * 4. + (LEFT + UP) * 0.8)
        group_01, group_02, group_03, group_04 = VGroup(), VGroup(), VGroup(), VGroup()
        group_01.add(group_all_02[12])
        group_02.add(group_all_02[8], group_all_02[9], group_all_02[13])
        group_03.add(group_all_02[4], group_all_02[5], group_all_02[6], group_all_02[10], group_all_02[14])
        group_04.add(group_all_02[0], group_all_02[1], group_all_02[2], group_all_02[3], group_all_02[7], group_all_02[11], group_all_02[15])


        for i in range(16):
            self.play(FadeIn(group_all[i]), run_time=0.12)
            self.play(ApplyMethod(group_all[i].shift, np.array([0, 0, -1.2])), run_time=0.3)
            self.wait(0.08)
        self.wait(0.5)
        brace_01 = Brace(group_all, DOWN)
        tex_01 = brace_01.get_tex('1+2+\\cdots+n')
        brace_02 = Brace(group_all, RIGHT)
        tex_02 = brace_02.get_tex('1+2+\\cdots+n').rotate(PI/2).next_to(brace_02, RIGHT * 0.5)
        tex_group = VGroup(brace_01, brace_02, tex_01, tex_02).align_to(group_all, IN)
        self.play(FadeIn(tex_group), run_time=0.9)

        color_dict = {'^2': BLUE, '^3': PINK, '+': ORANGE, '(': RED, ')': RED}
        tex_sum_01 = MyText('(', '1', '+', '2', '+', '\\cdots', '+', 'n', ')', '^2', default_font='思源黑体 Bold').set_height(1.25).shift(UP * 1)
        tex_sum_01.set_color_by_tex_to_color_map(color_dict)
        bg_01 = SurroundingRectangle(tex_sum_01, stroke_color=YELLOW, fill_color=BLACK, fill_opacity=0.8, plot_depth=-1)
        replace_dict = {'1': '1', '2': '2', '^2': '2', 'n': 'n', '+': ' + ', '\\cdots': '...'}
        tex_sum_new_01 = tex_sum_01.get_new_font_texs(replace_dict)
        t_01 = VGroup(bg_01.scale(1.1), tex_sum_new_01,)
        self.add_fixed_in_frame_mobjects(t_01)
        self.play(FadeIn(bg_01), Write(tex_sum_new_01), run_time=2.)
        self.wait(1.8)
        self.play(FadeOut(tex_group), FadeOut(t_01), run_time=0.9)
        # self.play(ApplyMethod(group_all.scale, 0.8), run_time=0.8)
        self.wait(0.5)

        self.play(ReplacementTransform(group_all, group_all_02), run_time=1.5)
        self.wait(0.5)

        opac = 0.15
        ### 2 ** 2 anim
        a = group_02[0].copy()
        self.add(a)
        group_02[0].set_fill(color_list[0][1], opac)
        self.play(ApplyMethod(a.shift, OUT * size * s02), run_time=0.6)
        self.play(a.align_to, group_02[1], LEFT, run_time=0.6)
        self.wait(0.8)

        a = group_02[2].copy()
        self.add(a)
        group_02[2].set_fill(color_list[0][1], opac)
        self.play(ApplyMethod(a.shift, OUT * size * s02), run_time=0.64)
        self.play(Rotating(a, radians=PI/2, run_time=1.25))
        self.wait(0.1)
        self.play(a.align_to, group_02[1], RIGHT, run_time=0.25)
        self.play(a.align_to, group_02[1], UP, run_time=0.8)
        self.wait(1.)

        ### 3 ** 3 anim

        # move right
        a = group_03[1].copy()
        self.add(a)
        group_03[1].set_fill(color_list[2][1], opac)
        self.play(ApplyMethod(a.shift, OUT * size * s02), run_time=0.64)
        self.play(a.align_to, group_03[2], LEFT, run_time=1)
        self.wait(0.8)

        a = group_03[0].copy()
        self.add(a)
        group_03[0].set_fill(color_list[0][2], opac)
        self.play(ApplyMethod(a.shift, 2 * OUT * size * s02), run_time=0.8)
        self.play(a.align_to, group_03[2], LEFT, run_time=1.2)
        self.wait(0.8)

        # move up

        a = group_03[4].copy()
        self.add(a)
        group_03[4].set_fill(color_list[2][0], opac)
        self.play(ApplyMethod(a.shift, OUT * size* s02), run_time=0.64)
        self.play(Rotating(a, radians=PI/2, run_time=1.25))
        self.wait(0.1)
        self.play(a.align_to, group_03[2], RIGHT, run_time=0.3)
        self.play(a.align_to, group_03[2], UP, run_time=1.4)
        self.wait(0.8)

        a = group_03[3].copy()
        self.add(a)
        group_03[3].set_fill(color_list[2][1], opac)
        self.play(ApplyMethod(a.shift, 2 * OUT * size * s02), run_time=0.8)
        self.play(Rotating(a, radians=PI/2, run_time=1.25))
        self.wait(0.1)
        self.play(a.align_to, group_03[2], RIGHT, run_time=0.25)
        self.play(a.align_to, group_03[2], UP, run_time=1.)
        self.wait(1.)

        ### 4 ** 4 anim
        # move right

        a = group_04[2].copy()
        self.add(a)
        group_04[2].set_fill(color_list[3][2], opac)
        self.play(ApplyMethod(a.shift, OUT * size * s02), run_time=0.64)
        self.play(a.align_to, group_04[3], LEFT, run_time=0.9)
        self.wait(0.8)

        a = group_04[1].copy()
        self.add(a)
        group_04[1].set_fill(color_list[3][1], opac)
        self.play(ApplyMethod(a.shift, 2 * OUT * size * s02), run_time=0.8)
        self.play(a.align_to, group_04[3], LEFT, run_time=1.25)
        self.wait(0.8)

        a = group_04[0].copy()
        self.add(a)
        group_04[0].set_fill(color_list[3][0], opac)
        self.play(ApplyMethod(a.shift, 3 * OUT * size * s02), run_time=0.9)
        self.play(a.align_to, group_04[3], LEFT, run_time=1.75)
        self.wait(0.8)

        # move up

        a = group_04[6].copy()
        self.add(a)
        group_04[6].set_fill(color_list[3][0], opac)
        self.play(ApplyMethod(a.shift, OUT * size * s02), run_time=0.64)
        self.play(Rotating(a, radians=PI/2, run_time=1.25))
        self.wait(0.1)
        self.play(a.align_to, group_04[3], RIGHT, run_time=0.36)
        self.play(a.align_to, group_04[3], UP, run_time=2)
        self.wait(0.8)

        a = group_04[5].copy()
        self.add(a)
        group_04[5].set_fill(color_list[3][1], opac)
        self.play(ApplyMethod(a.shift, 2 * OUT * size * s02), run_time=0.8)
        self.play(Rotating(a, radians=PI/2, run_time=1.25))
        self.wait(0.1)
        self.play(a.align_to, group_04[3], RIGHT, run_time=0.3)
        self.play(a.align_to, group_04[3], UP, run_time=1.8)
        self.wait(0.8)

        a = group_04[4].copy()
        self.add(a)
        group_04[4].set_fill(color_list[3][2], opac)
        self.play(ApplyMethod(a.shift, 3 * OUT * size * s02), run_time=0.9)
        self.play(Rotating(a, radians=PI/2, run_time=1.25))
        self.wait(0.1)
        self.play(a.align_to, group_04[3], RIGHT, run_time=0.25)
        self.play(a.align_to, group_04[3], UP, run_time=1.6)
        self.wait()

        tex_sum_02 = MyText('1', '^3', '+', '2', '^3', '+', '\\cdots', '+', 'n', '^3', default_font='思源黑体 Bold').set_height(1.25).shift(DOWN * 1.25)
        tex_sum_02.set_color_by_tex_to_color_map(color_dict)
        replace_dict = {'1': '1', '2': '2', '^3': '3', 'n': 'n', '+': ' + ', '\\cdots': '...'}
        bg_02 = SurroundingRectangle(tex_sum_02, stroke_color=YELLOW, fill_color=BLACK, fill_opacity=0.8, plot_depth=-1)
        tex_sum_new_02 = tex_sum_02.get_new_font_texs(replace_dict)

        t_02 = VGroup(bg_02.scale(1.1), tex_sum_new_02,)
        self.add_fixed_in_frame_mobjects(t_02)
        self.play(FadeIn(bg_02), Write(tex_sum_new_02), run_time=2)
        self.wait(2)
        self.play(FadeOut(VGroup(*self.mobjects)), run_time=1.8)
        self.wait(0.5)
        # self.play(FadeIn(t_01.shift(UP)), FadeIn(t_02.shift(DOWN * 0.5)), run_time=1)
        # self.wait(0.4)
        #
        # equation = MyText('\\sum', '_{i=1}', '^n', 'i', '^3', '\\quad=\\quad', '(', '\\sum', '_{i=1}', '^n', 'i', ')', '^2', default_font='思源黑体 Bold').set_height(1.5)
        # replace_dict = {'1': '1', '2': '2', '^3': '3', '^n': 'n', '^2': '2', '\\quad=\\quad': ' = ', '_{i=1}': 'i=1',
        #                 '\\sum': '∑', '(': '(', ')': ')'}
        # equ = equation.get_new_font_texs(replace_dict)
        # self.add_fixed_in_frame_mobjects(equ)
        #
        # self.play(Write(equ[5]))
        # self.wait(0.4)
        # self.play(ReplacementTransform(t_02, equ[0:5]), run_time=1.2)
        # self.wait(0.5)
        # self.play(ReplacementTransform(t_01, equ[6:]), run_time=1.2)
        #
        # self.wait(4)

    @staticmethod
    def l_shape_mn(mn, stroke_scale, scale_factor=1, **kwargs):
        m, n = mn[0], mn[1]
        p = np.array([[-1, -1, 0], [2 * n - 1, -1, 0], [2 * n - 1, 2 * m - 1, 0], [-1, 2 * m - 1, 0]]) * 0.5
        l01 = Line(p[1], p[2], stroke_width=1 * stroke_scale, **kwargs).scale_about_point(scale_factor, ORIGIN)
        l02 = Line(p[2], p[3], stroke_width=1 * stroke_scale, **kwargs).scale_about_point(scale_factor, ORIGIN)
        return VGroup(l01, l02)

    @staticmethod
    def rect_mn_2d(mn, stroke_scale, scale_factor=1, **kwargs):
        m, n = mn[0], mn[1]
        p = np.array([[-1, -1, 0], [2 * n - 1, -1, 0], [2 * n - 1, 2 * m - 1, 0], [-1, 2 * m - 1, 0]]) * 0.5
        rect_mn = Polygon(p[0], p[1], p[2], p[3], stroke_width=1 * stroke_scale, **kwargs).scale_about_point(scale_factor, ORIGIN)
        return rect_mn

class Equation_2d(Scene):

    def construct(self):

        color_dict = {'^2': BLUE, '^3': PINK, '+': ORANGE, '(': RED, ')': RED}
        tex_sum_01 = MyText('(', '1', '+', '2', '+', '\\cdots', '+', 'n', ')', '^2', default_font='思源黑体 Bold').set_height(1.25).shift(UP * 1)
        tex_sum_01.set_color_by_tex_to_color_map(color_dict)
        bg_01 = SurroundingRectangle(tex_sum_01, stroke_color=YELLOW, fill_color=BLACK, fill_opacity=0.8, plot_depth=-1)
        replace_dict = {'1': '1', '2': '2', '^2': '2', 'n': 'n', '+': ' + ', '\\cdots': '...'}
        tex_sum_new_01 = tex_sum_01.get_new_font_texs(replace_dict)
        t_01 = VGroup(bg_01.scale(1.1), tex_sum_new_01,)

        tex_sum_02 = MyText('1', '^3', '+', '2', '^3', '+', '\\cdots', '+', 'n', '^3', default_font='思源黑体 Bold').set_height(1.25).shift(DOWN * 1.25)
        tex_sum_02.set_color_by_tex_to_color_map(color_dict)
        replace_dict = {'1': '1', '2': '2', '^3': '3', 'n': 'n', '+': ' + ', '\\cdots': '...'}
        bg_02 = SurroundingRectangle(tex_sum_02, stroke_color=YELLOW, fill_color=BLACK, fill_opacity=0.8, plot_depth=-1)
        tex_sum_new_02 = tex_sum_02.get_new_font_texs(replace_dict)

        t_02 = VGroup(bg_02.scale(1.1), tex_sum_new_02,)

        equation = MyText('\\sum', '_{i=1}', '^{n}', 'i', '^3', '=', '(', '\\sum', '_{i=1}', '^n', 'i', ')', '^2',
                          default_font='思源黑体 Bold').set_height(2.2)
        equation.set_color_by_tex_to_color_map({
            # '\\sum': BLUE,
            # # '^{n}': RED,
            # '_{i=1}': ORANGE,
            '^3': PINK,
            '^2': BLUE,
        })
        replace_dict = {'^3': '3', '^{n}': 'n', '^2': '2', '=': '=', '_{i=1}': 'i=1',
                       '\\sum': '∑', '(': '(', ')': ')'}
        equ = equation#.get_new_font_texs(replace_dict)
        # 上面如果直接使用 方法会有bug, TODO 在MyText类中加入可以和debugTex配合使用的基于下标的替换方式
        gou = TexMobject('\\checkmark', color=GREEN).set_height(1.8).next_to(equ, RIGHT * 1.75)

        self.play(FadeIn(t_01.shift(UP)), FadeIn(t_02.shift(DOWN * 0.5)), run_time=1.6)
        self.wait(0.4)

        self.play(Write(equ[5]))
        self.wait(0.4)
        self.play(ReplacementTransform(t_02, equ[0:5]), run_time=1.6)
        self.wait(0.5)
        self.play(ReplacementTransform(t_01, equ[6:]), run_time=1.6)
        self.wait(0.25)
        self.play(ShowCreationThenFadeAround(SurroundingRectangle(equ).scale(1.05)), run_time=1.5)
        self.wait(0.2)
        self.play(Write(gou), run_time=1.5)

        self.wait(3)
