# from @cigar666

from manimlib.imports import *

class Sun(VGroup):
    CONFIG = {
        'colors': [RED_B, ORANGE, WHITE],
        # 'opacity_func': lambda t: 1.1 - t ** 0.24 if t < 0.1 else 1 - 0.95 * t ** 0.18 - 0.05 * t ** 0.05,
        # 'opacity_func': lambda t: 1000 * (1 - t ** 0.00012) if t < 0.1 else 0.75 * (1 - t ** 0.21),
        # 'opacity_func': lambda t: 1250 * (1 - abs(t-0.006) ** 0.0001) if t < 0.12 else 0.72 * (1 - t ** 0.2),
        'opacity_func': lambda t: 1500 * (1 - abs(t-0.009) ** 0.0001),
        'radius': 4,
        'layer_num': 80,
        # 'rate_func': smooth,
        'rate_func': lambda t: t ** 2,
    }
    def __init__(self, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.color_list = color_gradient(self.colors, self.layer_num)
        self.add(Dot(color=average_color(self.colors[0], WHITE), plot_depth=4).set_height(0.015 * self.radius))
        for i in range(self.layer_num):
            # self.add(Arc(radius= self.radius/self.layer_num * (0.5 + i), angle=TAU, color=self.color_list[i],
            #              stroke_width=100 * self.radius/self.layer_num,
            #              stroke_opacity=self.opacity_func(i/self.layer_num), plot_depth=5))
            self.add(Arc(radius=self.radius * self.rate_func((0.5 + i)/self.layer_num), angle=TAU, color=self.color_list[i],
                         stroke_width=101 * (self.rate_func((i + 1)/self.layer_num) - self.rate_func(i/self.layer_num)) * self.radius,
                         stroke_opacity=self.opacity_func(self.rate_func(i/self.layer_num)), plot_depth=5))

class Three_Body(VGroup):

    CONFIG = {
        'mass': np.array([0.98, 1.025, 1]) * 1.2,
        'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.75,
        'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 0.8,
        'p_pos': np.array([2, -np.sqrt(3)+1, 0]) * 1.,
        'p_velocity':np.array([-1, -1.7, 0]) * 2.4,
        'plot_depth':5,
    }

    def __init__(self, *three_Mobject, **kwargs):

        VGroup.__init__(self, **kwargs)

        self.sun_01 = three_Mobject[0].move_to(self.pos[0])
        self.sun_02 = three_Mobject[1].move_to(self.pos[1])
        self.sun_03 = three_Mobject[2].move_to(self.pos[2])
        if len(three_Mobject) > 3:
            self.planet = three_Mobject[3].move_to(self.p_pos)
        self.add(self.sun_01, self.sun_02, self.sun_03)
        if len(three_Mobject) > 3:
            self.planet = three_Mobject[3].move_to(self.p_pos)
            self.add(self.planet)

    @staticmethod
    def get_force(x1, x2, m1, m2, G=1):
        # force of obj_01 to obj_02, this vector start from obj_02 and end in obj_01
        r = np.sqrt(sum((x1 - x2) ** 2))
        return G * m1 * m2 * (x1 - x2) / (r ** 3 + 2e-3)

    def update_xyz(self, G=1, delta_t =2.5e-3):

        m1, m2, m3 = self.mass[0], self.mass[1], self.mass[2]
        x1, x2, x3 = self.pos[0], self.pos[1], self.pos[2]
        v1, v2, v3 = self.velocity[0], self.velocity[1], self.velocity[2]
        f21, f31, f32 = self.get_force(x2, x1, m2, m1, G=G), self.get_force(x3, x1, m3, m1, G=G), self.get_force(x3, x2, m3, m2, G=G)
        a1, a2, a3 = (f21 + f31) / m1, (-f21 + f32) / m2, (-f32 - f31) / m3

        xp, vp = self.p_pos, self.p_velocity
        f1, f2, f3 = self.get_force(x1, xp, m1, 1, G=G), self.get_force(x2, xp, m2, 1, G=G), self.get_force(x3, xp, m3, 1, G=G)
        a = (f1 + f2 + f3) / 1.

        self.velocity[0] += a1 * delta_t
        self.velocity[1] += a2 * delta_t
        self.velocity[2] += a3 * delta_t
        self.p_velocity += a * delta_t

        self.pos[0] += v1 * delta_t
        self.pos[1] += v2 * delta_t
        self.pos[2] += v3 * delta_t
        self.p_pos += vp *delta_t

    def reset_velocity(self):
        v1, v2, v3 = self.velocity[0], self.velocity[1], self.velocity[2]
        m1, m2, m3 = self.mass[0], self.mass[1], self.mass[2]
        momentum = v1 * m1 + v2 * m2 + v3 * m3
        v = momentum/(m1 + m2 + m3)
        v1, v2, v3 = v1 - v, v2 - v, v3 - v
        print(v1, v2, v3)
        self.p_velocity -= v
        self.velocity = np.array([v1, v2, v3])

    def update_three_body(self, tb, dt):
        self.update_xyz(G=40)
        # avervage_pos = (self.pos[0] + self.pos[1] + self.pos[2]) / 3
        # tb[0].move_to(self.pos[0] - avervage_pos)
        # tb[1].move_to(self.pos[1] - avervage_pos)
        # tb[2].move_to(self.pos[2] - avervage_pos)
        # if len(tb)>3:
        #     tb[3].move_to(self.p_pos - avervage_pos)
        tb[0].move_to(self.pos[0])
        tb[1].move_to(self.pos[1])
        tb[2].move_to(self.pos[2])
        if len(tb) > 3:
            tb[3].move_to(self.p_pos)

    def start_move(self):
        self.add_updater(self.update_three_body)

# 具体的用法见[https://github.com/cigar666/my_manim_projects/blob/master/my_projects/ThreeBody.py]
