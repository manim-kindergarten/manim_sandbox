# from @cigar666

"""

这里大部分示例为我在b站关于manim三维场景教程的一篇专栏（https://www.bilibili.com/read/cv4761465）中的代码，
专栏里有更多的文字介绍和解释，可和本示例文件中的代码配合食用

"""

from manimlib.imports import *

# demo_0: about camera orientation #
class Test_camera(ThreeDScene):

    def construct(self):

        axes = ThreeDAxes()
        cube_yellow = Cube(fill_color=YELLOW, stroke_width=2, stroke_color=WHITE)
        sphere_blue = Sphere(fill_color=BLUE, checkerboard_colors=None).shift(OUT * 2)
        cube_green = Cube(fill_color=GREEN).scale([2, 0.5, 0.5]).shift(RIGHT * 3.25)

        phi_0, theta_0 = 0, 0 # 起始角度
        phi, theta = 60 * DEGREES, -120 * DEGREES # 目标角度

        self.set_camera_orientation(phi=phi_0, theta=theta_0)
        self.add(axes, cube_yellow, sphere_blue, cube_green)
        self.wait()
        dt = 1/15
        delta_phi, delta_theta = (phi - phi_0) / 30, (theta - theta_0) / 60
        for i in range(30):
            phi_0 += delta_phi
            self.set_camera_orientation(phi=phi_0, theta=theta_0)
            self.wait(dt)
        for i in range(60):
            theta_0 += delta_theta
            self.set_camera_orientation(phi=phi_0, theta=theta_0)
            self.wait(dt)
        self.wait(2)

# demo_1: plot 3D curve by ParametricFunction
#  (almost the same as 2d curve by ParametricFunction)
class Curve_3D_test(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        r = 2 # radius
        w = 4
        circle = ParametricFunction(lambda t: r * complex_to_R3(np.exp(1j * w * t)),
                                    t_min=0, t_max=TAU * 1.5, color=RED, stroke_width=8)
        spiral_line = ParametricFunction(lambda t: r * complex_to_R3(np.exp(1j * w * t)) + OUT * t,
                                    t_min=0, t_max=TAU * 1.5, color=PINK, stroke_width=8)
        circle.shift(IN * 2.5), spiral_line.shift(IN * 2.5)

        self.add(axes, circle)
        self.wait()
        self.play(TransformFromCopy(circle, spiral_line, rate_func=there_and_back), run_time=4)
        self.wait(2)

# demo_2: draw surface by z=f(x, y)
class Surface_test_01(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes = self.get_axes()
        # create surface: z = sin(x ^ 2 + y ^ 2)
        surface = ParametricSurface(lambda u, v: np.array([u, v, np.sin(u ** 2 + v ** 2)]),
                                    u_min=-4, u_max=4, v_min=-4, v_max=4, resolution=(120, 120))
        self.add(axes, surface)
        self.wait(5)

# demo_3: draw surface by parametric function of the surface
class Surface_test_02(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes = self.get_axes()
        w = 1
        surface_01 = ParametricSurface(lambda u, v: v * complex_to_R3(np.exp(1j * w * u)),
                                       u_min=0, u_max=TAU, v_min=1, v_max=3, checkerboard_colors=None,
                                       fill_color=BLUE_B, fill_opacity=0.8, stroke_color=BLUE_A, resolution=(60, 10))
        surface_02 = ParametricSurface(lambda u, v: v * complex_to_R3(np.exp(1j * w * u)) + OUT * u/PI * 2,
                                       u_min=0, u_max=TAU, v_min=1, v_max=3, checkerboard_colors=None,
                                       fill_color=BLUE_D, fill_opacity=0.8, stroke_color=BLUE_A, resolution=(60, 10))
        self.add(axes, surface_01)
        self.wait()
        self.play(TransformFromCopy(surface_01, surface_02, rate_func=linear), run_time=5)
        self.wait(2)

# demo_4: display a surface in different styles
class Set_surface_color_test(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        ##################################################################################
        # 下面这个是我们将要绘制的曲面方程，我们将渲染默认的曲面，以及曲面的线框图及上色后的曲面 #
        # R = sqrt(x ^ 2 + y ^ 2) + eps, z = sin(R) / R * 8 - 2                          #
        ##################################################################################
        R = lambda x, y: np.sqrt(x ** 2 + y ** 2) + 1e-8
        # surface_origin 为默认的展示方式，仅更改了resolution（也就是u, v方向的分段数）
        surface_origin = ParametricSurface(lambda u, v: np.array([u, v, 8 * np.sin(R(u, v))/R(u, v) - 2]),
                                           u_min=-8, u_max=8, v_min=-8, v_max=8, resolution=(50, 50)).scale(0.5)
        # surface_frame为线框图
        surface_frame = surface_origin.copy().set_fill(color=BLUE, opacity=0)
        # colored_frame和colored_surface为上色后的曲面线框图和上色后的曲面
        r = np.linspace(1e-8, 8 * np.sqrt(2), 1000)
        z = (8 * np.sin(r)/r - 2) / 2
        z_l = max(z) - min(z)
        colors = color_gradient([BLUE_E, YELLOW, RED], 100)
        colored_frame = surface_frame.copy()
        colored_surface = surface_origin.copy()
        for ff, fs in zip(colored_frame, colored_surface):
            f_z = ff.get_center()[-1]
            ff.set_color(colors[int((f_z-min(z))/z_l * 90)])
            fs.set_color(colors[int((f_z-min(z))/z_l * 90)])
        ## 下面是几种曲面的效果展示 ##
        self.add(surface_origin)
        self.wait()
        self.play(ReplacementTransform(surface_origin, surface_frame), run_time=2)
        self.wait()
        self.play(ReplacementTransform(surface_frame, colored_frame), run_time=2)
        self.wait()
        self.play(ReplacementTransform(colored_frame, colored_surface), run_time=2)
        self.wait(2)

# demo_5: create a surface by curve rotation
class Surface_by_rotate(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes = self.get_axes()
        ## 方法一：通过旋转矩阵实现旋转 ##
        ## 注：可使用manim中有的旋转矩阵，不用自己写 ##
        curve_01 = lambda x: np.array([x, 0, x ** 2/4]) # z = x ** 2 / 4
        surface_func = lambda u, v: np.dot(curve_01(v), rotation_matrix(u, OUT).T) # 将z(v)绕z轴旋转u度得到的曲面
        surface_by_rotate_01 = ParametricSurface(surface_func, u_min=0, u_max=TAU, v_min=0, v_max=3,
                                                checkerboard_colors=None, fill_color=YELLOW_D, fill_opacity=0.8,
                                                stroke_color=WHITE, stroke_width=2.5)
        ## 方法二：通过复数 ##
        # np.exp(1j * w * u)为旋转复数，其中w控制快慢
        theta = PI / 4 # 直线夹角
        curve_02 = lambda y: np.array([1, y, y * np.tan(theta)]) # 一条直线，单叶双曲线的母线
        w = 1
        surface_func_02 = lambda u, v: complex_to_R3(complex(*curve_02(v)[0:2]) * np.exp(1j * w * u)) + curve_02(v)[-1] * OUT
        surface_by_rotate_02 = ParametricSurface(surface_func_02, u_min=0, u_max=TAU, v_min=-2, v_max=2,
                                                 checkerboard_colors=None, fill_color=BLUE, fill_opacity=0.8,
                                                stroke_color=WHITE, stroke_width=2.5)
        self.add(axes)
        self.wait()
        self.play(ShowCreation(surface_by_rotate_01))
        self.wait(2)
        self.play(ReplacementTransform(surface_by_rotate_01, surface_by_rotate_02))
        self.wait(2)

# demo_5: the animation of the generation of the surface by curve rotation
class Surface_generated_by_rotating(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -75 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        # 'camera_config': {'open_plot_depth': False}
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes = self.get_axes()
        self.var_theta = 1e-5
        theta = PI / 4 # 直线夹角
        line_func = lambda y: np.array([1, y, y * np.tan(theta)]) # 母直线方程
        line = ParametricFunction(line_func, t_min=-2, t_max=2, stroke_color=PINK, stroke_width=8, stroke_opacity=0.5)
        surface_func = lambda u, v: complex_to_R3(complex(*line_func(v)[0:2]) * np.exp(1j * u)) + line_func(v)[-1] * OUT
        surface_by_rotate = ParametricSurface(surface_func, u_min=0, u_max=self.var_theta, v_min=-2, v_max=2,)

        d_theta = 1 * DEGREES # the rotation angle in each frame
        def update_surface(s, dt):
            s.become(ParametricSurface(surface_func, u_min=0, u_max=self.var_theta, v_min=-2, v_max=2,
                                       checkerboard_colors=None, fill_color=BLUE, fill_opacity=0.8,
                                       stroke_color=WHITE, stroke_width=1.6,
                                       resolution=(1 + int(self.var_theta/DEGREES/4), 15)))
            # 此处的ParametricSurface中添加了resolution的更新，使分段数在一开始不至于过密
            self.var_theta += d_theta

        line.add_updater(lambda l, dt: l.rotate(d_theta, about_point=ORIGIN))
        surface_by_rotate.add_updater(update_surface)

        self.add(axes, line, surface_by_rotate)
        # 如果是在-pl下渲染，每秒只有15帧，所以24秒才能转一周
        self.wait(12) # -pm下只需要12秒
        surface_by_rotate.suspend_updating()
        line.suspend_updating()
        self.wait(2)

# demo_6: transform Mobius strip to a heart-shape Mobius strip
class Mobius_to_Heartshape(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 50 * DEGREES,
            "theta": -80 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):

        self.set_camera_to_default_position()
        heart_curve_func = lambda t: (16 * np.sin(t) ** 3 * RIGHT + (13 * np.cos(t) - 5 * np.cos(2 * t) - 3 * np.cos(3 * t) - np.cos(4 * t)) * UP + np.sin(t) * (1 - abs(-t/PI)) ** 2 * 8 * OUT) * 0.21

        r = 0.5
        heart_shape_mobius = ParametricSurface(lambda u, v: heart_curve_func(u) + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(-u/2) * OUT,
                                               u_min=-PI, u_max=PI, v_min=-r, v_max=r, resolution=(80, 12),
                                               checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                               stroke_width=1.5, fill_color=average_color(RED, PINK), fill_opacity=0.8)
        R = 3.6
        mobius_surface = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                           u_min=-PI/2, u_max=-PI/2 + TAU, v_min=-r, v_max=r, resolution=(80, 10),
                                           checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                           stroke_width=1.5, fill_color=BLUE, fill_opacity=0.8).rotate(PI, axis=UP)

        heart_shape_mobius.move_to(mobius_surface)

        # self.play(ShowCreation(heart_curve))
        # self.wait()

        self.add(mobius_surface)
        self.wait()
        self.play(ReplacementTransform(mobius_surface, heart_shape_mobius), run_time=4)

        self.wait(1.)

        rotate_right = lambda m, dt: m.rotate(0.25 * DEGREES, axis=RIGHT)
        rotate_up = lambda m, dt: m.rotate(0.25 * DEGREES, axis=UP)
        heart_shape_mobius.add_updater(rotate_right)
        self.wait(2.5)
        heart_shape_mobius.remove_updater(rotate_right)

        self.wait(5)

class Box_02(Cube):

    CONFIG = {
        'pos': ORIGIN,
        'box_height': 2,
        'bottom_size': [1, 1]
    }

    def __init__(self, **kwargs):
        Cube.__init__(self, **kwargs)
        self.box_size = np.array([self.bottom_size[0], self.bottom_size[1], self.box_height])
        self.scale(self.box_size/2)
        # self.move_to(self.pos + self.box_height * OUT/2)
        self.move_to(self.pos)
        self.reset_color_()

    def update_height(self, new_height):
        self.scale(np.array([1,1, new_height/self.height])) #.shift(OUT * (new_height - self.height)/2)
        self.height = new_height

    def reset_color_(self):
        colors = color_gradient([WHITE, self.get_color(), BLACK], 11)
        self[0].set_fill(color=colors[7])
        self[1].set_fill(color=colors[4])
        self[2].set_fill(color=colors[7])
        self[3].set_fill(color=colors[3])
        self[4].set_fill(color=colors[5])
        self[5].set_fill(color=colors[6])

# demo_7: the animation of waving boxes
# 注：这里的Box动画是我在MyBoxes类之前所写的，如果使用MyBoxes类会更方便地实现
# MyBoxes类见：https://github.com/manim-kindergarten/manim_sandbox/blob/master/utils/MyBoxes.py
class Wave_of_boxes_02(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 56 * DEGREES,
            "theta": -50 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': DARK_GRAY,
                          # 'open_plot_depth': False,
                          },
        }

    def construct(self):

        self.set_camera_to_default_position()

        self.var_phi = 0
        a = 0.1
        amp = 0.9 # amplitude
        self.wave_func = lambda u, v: np.array([u, v, amp + 0.0001  + amp * np.sin((u ** 2 + v ** 2)/2 + self.var_phi) * np.exp(-a * (np.sqrt(u ** 2 + v ** 2)))])
        # self.wave_func = lambda u, v: np.array([u, v, 2.1 + 2 * np.sin(u ** 2 + v ** 2)])

        self.box_bottom = [0.18, 0.18]
        self.colors = color_gradient([RED, YELLOW, GREEN_D, BLUE, PINK, RED_D], 100)

        boxes = self.create_boxes(gap=0.06)

        delta_theta = 1 * DEGREES
        def update_boxes(b, dt):
            b.become(self.create_boxes(gap=0.06))
            self.var_phi -= -delta_theta # 网上看到的牛逼写法，很有意思就用了

        boxes.add_updater(update_boxes)
        self.add(boxes)
        self.wait(16)

    def create_boxes(self, x_range=4, y_range=4, gap=0.05):
        boxes = VGroup()
        a, b = self.box_bottom[0] + gap * 2, self.box_bottom[1] + gap * 2
        m = int(y_range * 2/b)
        n = int(x_range * 2/a)
        for i in range(m):
            for j in range(n):
                xyz = a * j * RIGHT + b * i * UP + (x_range - a/2) * LEFT + (y_range - b/2) * DOWN
                box_ij = Box_02(pos=xyz, box_height=self.wave_func(xyz[0], xyz[1])[-1], color=BLUE,
                               bottom_size=self.box_bottom, fill_opacity=1,
                               fill_color=self.colors[int(np.sqrt(sum(xyz **2))/np.sqrt(x_range ** 2 + y_range ** 2) * 100)])
                boxes.add(box_ij)
        return boxes
