# from @cigar666
from manimlib.imports import *

class BaseTree(VGroup):

    CONFIG = {
        'base_branch': (DOWN * 3, DOWN),
        'derived_branch': [(DOWN, LEFT), (DOWN, RIGHT)],
        'layer_num': 8,
    }

    def __init__(self, mob=None, change_stroke=True, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.origin_mob = mob if mob!=None else Line(self.base_branch[0], self.base_branch[1], stroke_width=20)
        self.create_tree(change_stroke=change_stroke)

    def create_tree(self, change_stroke=True):
        old_points = self.base_branch
        self.add(self.origin_mob.copy())
        for i in range(self.layer_num):
            layer_i = VGroup()
            for new_points in self.derived_branch:
                layer_i.add(self.generate_new_branch(self[-1], old_points, new_points))
            if change_stroke:
                layer_i.set_stroke(width=self.origin_mob.get_stroke_width() * 1.35 ** (-i) + 0.5)
            self.add(layer_i)
        return self

    @staticmethod
    def generate_new_branch(mob, old_points, new_points):
        old_vect, new_vect = old_points[1] - old_points[0], new_points[1] - new_points[0]
        old_angle, new_angle = np.angle(complex(*old_vect[:2])), np.angle(complex(*new_vect[:2]))
        mob_new = mob.copy().shift(new_points[0] - old_points[0])\
            .rotate(new_angle-old_angle, about_point=new_points[0])\
            .scale(abs(complex(*new_vect[:2]))/(abs(complex(*old_vect[:2]))+1e-6), about_point=new_points[0])
        # if change_stroke:
        #     mob_new.set_stroke(width=mob_new.get_stroke_width() * np.sqrt(abs(complex(*new_vect[:2]))/(abs(complex(*old_vect[:2]))+1e-6)))
        return mob_new

class Test_BaseTree(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        layer_num=11
        colors = color_gradient([RED, GREEN, BLUE], layer_num+1)
        # tree = BaseTree(layer_num=layer_num, base_branch=(DOWN * 3.25, DOWN * 1), derived_branch=[(DOWN, LEFT + UP * 0.2), (DOWN, DOWN * 1.25 + 0.9 * LEFT), (DOWN, RIGHT * 1.25)])
        # for i in range(layer_num+1):
        #     tree[i].set_stroke(color=colors[i])

        text = Text('？', font='思源黑体 Bold').set_height(2.25).move_to(2.25 * DOWN)
        tree_text = BaseTree(text, layer_num=layer_num, base_branch=(DOWN * 3.2, DOWN * 1), derived_branch=[(DOWN + RIGHT * 0.06, LEFT * 1 + UP * 0.3), (DOWN + LEFT * 0.06, DOWN * 0.1 + RIGHT * 1.25)])
        for i in range(layer_num+1):
            tree_text[i].set_color(colors[i])
        tree_text.set_height(7.2).move_to(ORIGIN)

        # text_xgnb = Text('XGNB', font='庞门正道标题体').rotate(PI/2).set_height(2).move_to(2.1*DOWN)
        # tree_xgnb = BaseTree(text_xgnb, layer_num=layer_num, base_branch=(DOWN * 3.1, DOWN * 1), derived_branch=[(DOWN, LEFT - UL * 0.2), (DOWN, RIGHT + UR * 0.2)])
        # for i in range(layer_num+1):
        #     tree_xgnb[i].set_color(colors[i])

        self.add(tree_text)
        self.wait()

class PythagoreanTree(BaseTree):

    CONFIG = {
        'layer_num': 8,
        'colors': [RED, YELLOW, BLUE],
        'total_hight': 6.4,
    }

    def __init__(self, abc=(3, 4, 5), change_stroke=False, **kwargs):

        digest_config(self, kwargs)
        # a、b、c为三边长，c为水平的斜边，其实不是直角三角形也可以
        colors = color_gradient(self.colors, self.layer_num)
        a, b, c = abc[0], abc[1], abc[2]
        S_ABC = np.sqrt(sum(abc)*(sum(abc)-2*a)*(sum(abc)-2*b)*(sum(abc)-2*c))/4
        h = S_ABC * 2 / c
        angle_B = np.arcsin(h/a)
        angle_A = np.arcsin(h/b)
        point_C = np.array([c/2 - a * np.cos(angle_B),h,0])
        point_A, point_B = LEFT * c/2, RIGHT * c/2
        vect_AC, vect_BC = point_C - point_A, point_C - point_B
        mid_AC, mid_BC = (point_C + point_A) / 2, (point_C + point_B) / 2
        mob = Square(stroke_width=0).set_height(c).shift(DOWN * c * 0.5)
        BaseTree.__init__(self, mob, base_branch=(DOWN * c, ORIGIN), derived_branch=[(mid_AC, mid_AC + complex_to_R3(R3_to_complex(vect_AC)*1j)), (mid_BC, mid_BC + complex_to_R3(R3_to_complex(vect_BC)/1j))])

        colors = color_gradient(self.colors, self.layer_num+1)
        for i in range(self.layer_num+1):
            self[i].set_fill(colors[i], 1)
        self.set_height(self.total_hight).move_to(ORIGIN)

class XGNB_Tree(BaseTree):

    CONFIG = {
        'layer_num': 8,
        'colors': [RED, YELLOW, BLUE],
        'total_hight': 6.4,
    }

    def __init__(self, abc=(3, 4, 5), **kwargs):

        digest_config(self, kwargs)
        # a、b、c为三边长，c为水平的斜边，其实不是直角三角形也可以
        colors = color_gradient(self.colors, self.layer_num)
        a, b, c = abc[0], abc[1], abc[2]
        S_ABC = np.sqrt(sum(abc)*(sum(abc)-2*a)*(sum(abc)-2*b)*(sum(abc)-2*c))/4
        h = S_ABC * 2 / c
        angle_B = np.arcsin(h/a)
        angle_A = np.arcsin(h/b)
        point_C = np.array([c/2 - a * np.cos(angle_B),h,0])
        point_A, point_B = LEFT * c/2, RIGHT * c/2
        vect_AC, vect_BC = point_C - point_A, point_C - point_B
        mid_AC, mid_BC = (point_C + point_A) / 2, (point_C + point_B) / 2
        mob = Square(stroke_width=0).set_height(c).shift(DOWN * c * 0.5)
        text_1 = Text('XG', font='庞门正道标题体')
        text_2 = Text('NB', font='庞门正道标题体')
        xgnb = VGroup(text_1, text_2).arrange(DOWN, buff=0.01).set_height(c*0.9).move_to(mob)

        BaseTree.__init__(self, xgnb, base_branch=(DOWN * c, ORIGIN), derived_branch=[(mid_AC, mid_AC + complex_to_R3(R3_to_complex(vect_AC)*1j)), (mid_BC, mid_BC + complex_to_R3(R3_to_complex(vect_BC)/1j))])

        colors = color_gradient(self.colors, self.layer_num+1)
        for i in range(self.layer_num+1):
            self[i].set_fill(colors[i], 1)
        self.set_height(self.total_hight).move_to(ORIGIN)

class Test_PythagoreanTree(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        self.add(PythagoreanTree(layer_num=11))
        self.wait(4)

class ArcTree(BaseTree):

    CONFIG = {
        'arc_angle': PI/4,
        'base_branch': (DOWN * 2.4, ORIGIN),
        'stroke_width': 25,
        'derived_branch': [(ORIGIN,  UL * 1.25), (ORIGIN, UR * 1.1)],
        'layer_num': 8,
        'colors': [RED, YELLOW, BLUE],
        'total_hight': 6.4,
    }

    def __init__(self, **kwargs):

        digest_config(self, kwargs)
        arc = ArcBetweenPoints(self.base_branch[0], self.base_branch[1], angle=self.arc_angle, stroke_width=self.stroke_width)

        BaseTree.__init__(self, arc)
        colors = color_gradient(self.colors, self.layer_num+1)
        for i in range(self.layer_num+1):
            self[i].set_stroke(color=colors[i], opacity=1)
        self.set_height(self.total_hight).move_to(ORIGIN)

class Test_ArcTree(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        self.add(ArcTree(layer_num=12))
        self.wait(4)

class Sierpinski_carpet(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        r = 1
        A, B, C = complex_to_R3(r * np.exp(-PI/6 * 1j)), complex_to_R3(r * np.exp(PI/2 * 1j)), complex_to_R3(r * np.exp(-5 * PI/6 * 1j))
        mid_AB, mid_BC, mid_AC = (A+B)/2, (B+C)/2, (A+C)/2,
        mob = Square(stroke_width=0, fill_color=WHITE, fill_opacity=1).set_height(2)
        bg = Square(stroke_width=0, fill_color=BLUE, fill_opacity=1, plot_depth=-1).set_height(6)
        base_branch = (DOWN, UP)
        derived_branch = [(2 * UL + DOWN/3, 2 * UL + UP/3), (UP * 2 + DOWN/3, UP * 2 + UP/3), (2 * UR + DOWN/3, 2 * UR + UP/3),
                          (2 * LEFT + DOWN/3, 2 * LEFT + UP/3), (2 * RIGHT + DOWN/3, 2 * RIGHT + UP/3),
                          (2 * DL + DOWN/3, 2 * DL + UP/3), (DOWN * 2 + DOWN/3, DOWN * 2 + UP/3), (2 * DR + DOWN/3, 2 * DR + UP/3)]

        mobs = BaseTree(mob, base_branch=base_branch, derived_branch=derived_branch, layer_num=5)
        sierpinski_carpet = VGroup(mobs, bg).set_height(7.5)

        self.add(*sierpinski_carpet)

        self.wait(4)

class DandelionTree(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        layer_num=6
        colors = color_gradient([RED, GREEN, BLUE], layer_num+1)
        mob = Line(DOWN * 3, ORIGIN, stroke_width=20)
        tree = BaseTree(mob, layer_num=layer_num, base_branch=(DOWN * 3., ORIGIN), derived_branch=[(ORIGIN, complex_to_R3(1.6 * np.exp((-15+30 * i) * DEGREES * 1j))) for i in range(8)])
        for i in range(layer_num+1):
            tree[i].set_stroke(color=colors[i], width=20 * 0.4 ** i)
        tree.set_height(7.2).move_to(ORIGIN)

        self.add(tree)
        self.wait()

class Tiling(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        layer_num = 3
        colors = color_gradient([YELLOW, RED, BLUE], layer_num+1)
        mob = Polygon(ORIGIN, np.array([3/4, np.sqrt(3)/4, 0]), np.array([1/2, np.sqrt(3)/2, 0]), UP * np.sqrt(3)/2, stroke_width=0).scale(0.9)
        mobs = VGroup(mob, mob.copy().flip(about_point=ORIGIN))
        tree = BaseTree(mob, layer_num=layer_num, base_branch=(ORIGIN, np.array([1/2, np.sqrt(3)/2, 0])), derived_branch=[(np.sqrt(3)/2 * UP, np.sqrt(3)/2 * UP + np.array([1/2, 1/2/np.sqrt(3), 0])),
                                                                                                                          #(np.sqrt(3)/2 * UP, np.sqrt(3)/2 * UP + UP/np.sqrt(3)),
                                                                                                                          (np.array([1/2, np.sqrt(3)/2, 0]), np.array([1/2, np.sqrt(3)/2, 0]) * (1 + 1/3)),
                                                                                                                          (np.array([3/4, np.sqrt(3)/4, 0]), np.array([3/4, np.sqrt(3)/4, 0]) + UP/np.sqrt(3))])
        tree_02 = BaseTree(mobs, layer_num=layer_num, base_branch=(ORIGIN, np.sqrt(3)/2 * UP), derived_branch=[(np.sqrt(3)/2 * UP, np.sqrt(3)/2 * UP + UP * np.sqrt(3)/4 + RIGHT * 1/4),
                                                                                                            (np.sqrt(3)/2 * UP, np.sqrt(3)/2 * UP + UP * np.sqrt(3)/4 + LEFT * 1/4),
                                                                                                            ], change_stroke=False)
        # tree_02 = BaseTree(mob, layer_num=layer_num, base_branch=(ORIGIN, np.array([1/2, np.sqrt(3)/2, 0])), derived_branch=[(np.array([1/2, np.sqrt(3)/2, 0]), np.array([1/2, np.sqrt(3)/2, 0]) * (1 + 1/3))], change_stroke=False)

        for i in range(layer_num+1):
            tree[i].set_fill(color=colors[i], opacity=1)
            tree_02[i].set_fill(color=colors[i], opacity=1)

        trees = VGroup(*([tree.copy().rotate(PI/3 * i, about_point=ORIGIN) for i in range(6)] + [tree_02.copy().rotate(PI/3 * i, about_point=ORIGIN) for i in range(6)]))
        trees.set_height(7.2).move_to(ORIGIN)

        self.add(trees)
        self.wait()

class BinaryTree_(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        layer_num=16
        colors = color_gradient([RED, GREEN, BLUE], layer_num+1)
        mob = Line(DOWN * 2, ORIGIN, stroke_width=8)
        # tree = BaseTree(layer_num=layer_num, base_branch=(DOWN * 2., ORIGIN), derived_branch=[(ORIGIN, complex_to_R3(1.36 * np.exp(0 * 1j))), (ORIGIN, complex_to_R3(1.36 * np.exp(PI * 1j)))])
        # tree = BaseTree(layer_num=layer_num, base_branch=(DOWN * 2., ORIGIN), derived_branch=[(ORIGIN, complex_to_R3(0.6 * np.exp(0 * DEGREES * 1j))), (ORIGIN, complex_to_R3(1.75 * np.exp(120 * DEGREES * 1j)))])

        tree = BaseTree(mob, layer_num=layer_num, base_branch=(DOWN * 2., ORIGIN), derived_branch=[(ORIGIN, complex_to_R3(1 * np.exp(0 * DEGREES * 1j))), (ORIGIN, complex_to_R3(1.5 * np.exp(102.5 * DEGREES * 1j)))])

        for i in range(layer_num+1):
            tree[i].set_stroke(color=colors[i], width=5*(0.85)**i)
        tree.set_height(7.2).move_to(ORIGIN)

        self.add(tree)
        self.wait()

class Koch_Snowflake(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        layer_num=7
        colors = color_gradient([RED, GREEN, BLUE], layer_num+1)
        # mob = Line(LEFT * 3.08, RIGHT * 3.08, stroke_width=12)
        # tree = BaseTree(mob, layer_num=layer_num, base_branch=(LEFT * 3, RIGHT * 3), derived_branch=[(LEFT * 3, LEFT), (LEFT, UP * np.sqrt(3)), (UP * np.sqrt(3), RIGHT), (RIGHT, RIGHT * 3)])

        # mob = Line(LEFT * (1.05+np.sqrt(10)), RIGHT * (1.05+np.sqrt(10)), stroke_width=16)
        # tree = BaseTree(mob, layer_num=layer_num, base_branch=(LEFT * (1+np.sqrt(10)), RIGHT * (1+np.sqrt(10))),
        #                 derived_branch=[(LEFT * (1+np.sqrt(10)), LEFT), (LEFT, UP * 3), (UP * 3, RIGHT), (RIGHT, RIGHT * (1+np.sqrt(10)))])

        h = 6
        mob = Line(LEFT * (1.05+np.sqrt(1+h**2)), RIGHT * (1.05+np.sqrt(1+h**2)), stroke_width=16)
        tree = BaseTree(mob, layer_num=layer_num, base_branch=(LEFT * (1+np.sqrt(1+h**2)), RIGHT * (1+np.sqrt(1+h**2))),
                        derived_branch=[(LEFT * (1+np.sqrt(1+h**2)), LEFT), (LEFT, UP * h), (UP * h, RIGHT), (RIGHT, RIGHT * (1+np.sqrt(1+h**2)))])


        for i in range(layer_num+1):
            tree[i].set_stroke(color=colors[i], width=16 * 0.65 ** i)
        tree.set_width(12).move_to(ORIGIN)

        snowflake =VGroup(*tree[-1].get_family()).set_color_by_gradient(ORANGE, RED, PINK)

        self.add(snowflake)
        self.wait()

class Dragon_Curve_Arc(Scene):

    # CONFIG = {
    #     'camera_config': {
    #         'background_color': WHITE,
    #     }
    # }

    def construct(self):

        layer_num=10
        colors_01 = [WHITE, PINK]
        colors_02 = [ORANGE, GREEN_B]

        mob = Line(LEFT * 2.06, RIGHT * 2.06, stroke_width=16)
        tree = BaseTree(mob, layer_num=layer_num, base_branch=(LEFT * 2., RIGHT * 2.),
                        derived_branch=[(LEFT * 2., UP * 2.), (RIGHT * 2., UP * 2.)])
        tree_02 = tree.copy().rotate(PI, about_point=ORIGIN)

        double_dragon = VGroup(VGroup(*tree[-1].get_family()).set_color_by_gradient(*colors_01), VGroup(*tree_02[-1].get_family()).set_color_by_gradient(*colors_02)).flip()
        double_dragon.set_height(7.5).move_to(ORIGIN).set_stroke(width=2)
        self.add(double_dragon)

        # double_draon = VGroup(tree.set_color_by_gradient(*colors_01), tree_02.set_color_by_gradient(*colors_02)).flip()
        # double_draon.set_height(7.2).move_to(ORIGIN)
        # self.play(ShowCreation(tree[0]), ShowCreation(tree_02[0]), run_time=1.2)
        # self.wait()
        # for i in range(0, layer_num):
        #     self.play(ReplacementTransform(tree[i], tree[i+1]), ReplacementTransform(tree_02[i], tree_02[i+1]))
        #     self.wait(2)

        self.wait(2)

class Dragon_Curve_Arc(Scene):

    # CONFIG = {
    #     'camera_config': {
    #         'background_color': WHITE,
    #     }
    # }

    def construct(self):

        layer_num=10
        colors_01 = [WHITE, PINK]
        colors_02 = [ORANGE, GREEN_B]

        # mob = Line(LEFT * 2.06, RIGHT * 2.06, stroke_width=16)
        mob_arc = ArcBetweenPoints(LEFT * 2.0, RIGHT * 2.0, stroke_width=16)
        tree = BaseTree(mob_arc, layer_num=layer_num, base_branch=(LEFT * 2., RIGHT * 2.),
                        derived_branch=[(LEFT * 2., UP * 2.), (RIGHT * 2., UP * 2.)])
        tree_02 = tree.copy().rotate(PI, about_point=ORIGIN)

        double_dragon = VGroup(VGroup(*tree[-1].get_family()).set_color_by_gradient(*colors_01), VGroup(*tree_02[-1].get_family()).set_color_by_gradient(*colors_02)).flip()
        double_dragon.set_height(7.5).move_to(ORIGIN).set_stroke(width=2)
        self.add(double_dragon)

        # double_draon = VGroup(tree.set_color_by_gradient(*colors_01), tree_02.set_color_by_gradient(*colors_02)).flip()
        # double_draon.set_height(7.2).move_to(ORIGIN)
        # self.play(ShowCreation(tree[0]), ShowCreation(tree_02[0]), run_time=1.2)
        # self.wait()
        # for i in range(0, layer_num):
        #     self.play(ReplacementTransform(tree[i], tree[i+1]), ReplacementTransform(tree_02[i], tree_02[i+1]))
        #     self.wait(2)

        self.wait(2)

# fractal anim #

class DandelionTree_Anim(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        layer_num = 6
        colors = color_gradient([RED, GREEN, BLUE], layer_num+1)
        mob = Line(DOWN * 3, ORIGIN, stroke_width=20)
        tree = BaseTree(mob, layer_num=layer_num, base_branch=(DOWN * 3., ORIGIN), derived_branch=[(ORIGIN, complex_to_R3(1.6 * np.exp((-15+30 * i) * DEGREES * 1j))) for i in range(8)])
        for i in range(layer_num+1):
            tree[i].set_stroke(color=colors[i], width=20 * 0.4 ** i)
        tree.set_height(7.2).move_to(ORIGIN)

        self.play(ShowCreation(tree[0]), rate_func=linear, run_time=1.2)
        self.wait(1.)
        for i in range(layer_num):
            # self.play(ShowCreation(tree[i]), rate_func=linear, run_time=0.8 + i ** 0.4 * 0.8)
            self.play(TransformFromCopy(tree[i], tree[i+1]), rate_func=linear, run_time=1 + i ** 0.5 * 0.25)
            self.wait(0.5)

        self.wait(3)

class Koch_Snowflake_Anim(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        layer_num = 8
        colors = color_gradient([RED, GREEN, BLUE], layer_num+1)
        # mob = Line(LEFT * 3.08, RIGHT * 3.08, stroke_width=12)
        # tree = BaseTree(mob, layer_num=layer_num, base_branch=(LEFT * 3, RIGHT * 3), derived_branch=[(LEFT * 3, LEFT), (LEFT, UP * np.sqrt(3)), (UP * np.sqrt(3), RIGHT), (RIGHT, RIGHT * 3)])

        # mob = Line(LEFT * (1.05+np.sqrt(10)), RIGHT * (1.05+np.sqrt(10)), stroke_width=16)
        # tree = BaseTree(mob, layer_num=layer_num, base_branch=(LEFT * (1+np.sqrt(10)), RIGHT * (1+np.sqrt(10))),
        #                 derived_branch=[(LEFT * (1+np.sqrt(10)), LEFT), (LEFT, UP * 3), (UP * 3, RIGHT), (RIGHT, RIGHT * (1+np.sqrt(10)))])

        h = 6
        mob = Line(LEFT * (1.05+np.sqrt(1+h**2)), RIGHT * (1.05+np.sqrt(1+h**2)), stroke_width=16)
        tree = BaseTree(mob, layer_num=layer_num, base_branch=(LEFT * (1+np.sqrt(1+h**2)), RIGHT * (1+np.sqrt(1+h**2))),
                        derived_branch=[(LEFT * (1+np.sqrt(1+h**2)), LEFT), (LEFT, UP * h), (UP * h, RIGHT), (RIGHT, RIGHT * (1+np.sqrt(1+h**2)))])

        for i in range(layer_num+1):
            tree[i].set_stroke(color=colors[i], width=16 * 0.65 ** i)
        tree.set_width(12).move_to(ORIGIN)

        for i in range(layer_num+1):
            tree[i].set_color_by_gradient(ORANGE, RED, PINK)

        self.play(ShowCreation(tree[0]), rate_func=linear, run_time=1.8)
        self.wait(1.2)
        for i in range(layer_num):
            self.play(ReplacementTransform(tree[i], tree[i+1]), rate_func=linear, run_time=1 + i ** 0.5 * 0.4)
            self.wait(0.55 + i ** 0.25 * 0.25)

        self.wait(3)

class PythagoreanTree_Anim(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        layer_num = 15
        tree = PythagoreanTree(layer_num=layer_num, total_hight=7.2)
        self.play(FadeIn(tree[0]), rate_func=linear, run_time=1.6)
        self.wait(1.)
        for i in range(layer_num):
            self.play(TransformFromCopy(tree[i], tree[i+1]), rate_func=linear, run_time=0.6 + i ** 0.5 * 0.25)
            self.wait(0.25 + i ** 0.25 * 0.25)

        self.wait(3)
