# from @有一种悲伤叫颓废

"""
注：
    1. 这是pd大大的轮子，pd大大主页(UID:10707223)：https://github.com/pdcxs/ManimProjects/blob/master/other/l_system.py
    2. 然后被我改成了VGroup形式
"""


import numpy as np
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.geometry import Line
from manimlib.constants import ORIGIN, PI, RIGHT, UP
from manimlib.utils.config_ops import digest_config
from manimlib.scene.scene import Scene



class LSystem(VGroup):
    CONFIG = {
        'rules': {'F': 'F+F--F+F'},
        'length': 1,
        'start_loc': ORIGIN,
        'angle': PI / 3,
        'start_rot': 0,
        'iteration': 1,
        'initial': 'F',
        'actions': {},
        'locations': [],
        'rotations': [],
        'graphs': [],
        'expression': '',
        'animation': None,
        'weight': 1,
    }
    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        self.kwargs = kwargs
        self.setup()
        self.tree = VGroup()
        self.generate()
        self.draw()
        VGroup.__init__(self, *self.tree)

    def setup(self):
        self.actions['F'] = self.draw_forward
        self.actions['+'] = self.rotate_forward
        self.actions['-'] = self.rotate_backward
        self.actions['['] = self.push
        self.actions[']'] = self.pop
        self.cur_loc = self.start_loc
        self.cur_rot = self.start_rot
        self.expression = self.initial

    def draw_forward(self):
        o = self.cur_loc
        l = self.length
        a = self.cur_rot

        e = o + \
            l * np.cos(a) * RIGHT + \
            l * np.sin(a) * UP
        self.cur_loc = e
        g = Line(o, e, **self.kwargs)
        self.tree.add(g)

    def rotate_forward(self):
        self.cur_rot += self.angle

    def rotate_backward(self):
        self.cur_rot -= self.angle

    def push(self):
        self.locations.append(self.cur_loc)
        self.rotations.append(self.cur_rot)

    def pop(self):
        self.cur_loc = self.locations.pop()
        self.cur_rot = self.rotations.pop()

    def generate(self):
        for i in range(self.iteration):
            #print(f'generating iteration {i + 1}')
            new_exp = ''
            for e in self.expression:
                new_exp += self.rules.get(e, e)
            self.expression = new_exp
            #print(f'iteration {i + 1} is finished')

    def draw(self):
        count = self.expression.count("F")
        #print(f'Total {count} Fs')
        for e in self.expression:
            act = self.actions.get(e, None)
            if act is not None:
                act()


class test(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": '#58B2DC',
            },
        }
    def construct(self):

        #points = [np.sin(-10+t/10)*UP/2+DOWN*3+(-10+t/10)*RIGHT for t in range(200)]
        #soil = Polygon(5*DOWN+10*LEFT, *points, 5*DOWN+10*RIGHT, fill_opacity=1, fill_color='#363B25', stroke_width=0)
        #self.add(soil)

        tree1 = LSystem(
            iteration=5, start_loc=[-7, -3.5, 0], angle=25.7 * DEGREES, color='#5B622E', stroke_width=1,
            rules={'F': 'F[+F]F[-F]F'}, initial='F', length=0.03, start_rot=75 * DEGREES,
        )
        tree2 = LSystem(
            iteration=5, start_loc=[-4, -3.5, 0], angle=20 * DEGREES, color='#F6C555', stroke_width=1,
            rules={'F': 'F[+F]F[-F][F]'}, initial='F', length=0.12, start_rot=90 * DEGREES,
        )
        tree3 = LSystem(
            iteration=4, start_loc=[-3, -3.5, 0], angle=22.5 * DEGREES, color='#855B32', stroke_width=1,
            rules={'F': 'FF-[-F+F+F]+[+F-F-F]'}, initial='F', length=0.12, start_rot=75 * DEGREES,
        )
        tree4 = LSystem(
            iteration=7, start_loc=[0, -3.5, 0], angle=20 * DEGREES, color='#E98B2A', stroke_width=1,
            rules={'X': 'F[+X]F[-X]+X', 'F': 'FF'}, initial='X', length=0.02, start_rot=60 * DEGREES,
        )
        tree5 = LSystem(
            iteration=7, start_loc=[3, -3.5, 0], angle=25.7 * DEGREES, color='#86C166', stroke_width=1,
            rules={'X': 'F[+X][-X]FX', 'F': 'FF'}, initial='X', length=0.03, start_rot=90 * DEGREES,
        )
        tree6 = LSystem(
            iteration=6, start_loc=[7, -3.5, 0], angle=22.5 * DEGREES, color='#FEDFE1', stroke_width=1,
            rules={'X': 'F-[[X]+X]+F[+FX]-X', 'F': 'FF'}, initial='X', length=0.05, start_rot=110 * DEGREES,
        )

        self.add(tree1, tree2, tree3, tree4, tree5, tree6)
        #turn_animation_into_updater(GrowFromRandom(tree1, run_time=4))
        '''
        trees = [tree1, tree2, tree3, tree4, tree5, tree6]
        for tree in trees:
            self.play(
                ShowCreation(tree), run_time=12, rate_func=linear,
            )
            self.wait()
        self.wait(5)
        self.play(FadeOutFromRandom(VGroup(*self.mobjects[1:])))
        self.wait()
        '''

