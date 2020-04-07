#author: @pdcxs

# This is an L-System Scene

from manimlib.imports import *

class LSystem(Scene):
    CONFIG = {
        'rules': {'F':'F+F--F+F'},
        'length': 1,
        'start_loc': ORIGIN,
        'angle': PI/3,
        'start_rot': 0,
        'iteration': 1,
        'initial': 'F',
        'actions': {},
        'locations': [],
        'rotations': [],
        'graphs': [],
        'expression': '',
        'step_time': 1,
        'animation': None,
        'weight': 1,
    }

    def setup(self):
        self.actions['F'] = self.draw_forward
        self.actions['+'] = self.rotate_forward
        self.actions['-'] = self.rotate_backward
        self.actions['['] = self.push
        self.actions[']'] = self.pop
        self.cur_loc = self.start_loc
        self.cur_rot = self.start_rot
        self.expression = self.initial
        self.animation = lambda x: \
            self.play(ShowCreation(x),\
                run_time=self.step_time)

    def draw_forward(self):
        o = self.cur_loc
        l = self.length
        a = self.cur_rot

        e = o + \
            l * np.cos(a) * RIGHT + \
            l * np.sin(a) * UP
        self.cur_loc = e
        g = Line(o, e)
        g.stroke_width = self.weight

        self.animation(g)

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
            print(f'generating iteration {i+1}')
            new_exp = ''
            for e in self.expression:
                new_exp += self.rules.get(e, e)
            self.expression = new_exp
            print(f'iteration {i+1} is finished')
    
    def draw(self):
        for e in self.expression:
            act = self.actions.get(e, None)
            if act is not None:
                act()
        
class Koch(LSystem):
    CONFIG = {
        'iteration': 3,
        'start_loc': (FRAME_X_RADIUS - 0.3) * LEFT + DOWN,
        'step_time': 0.1,
        'length': 0.5
    }

    def construct(self):
        self.generate()
        self.draw()
        self.wait()

class Levy(LSystem):
    CONFIG = {
        'iteration': 9,
        'start_loc': 2.5 * LEFT + 2 * DOWN,
        'length': 0.2,
        'step_time': 0.1,
        'angle': PI/4,
        'rules': {
            'F': '+F--F+'
        }
    }

    def construct(self):
        self.generate()
        # self.animation = lambda x: self.add(x)
        self.draw()
        self.wait()

class Tree(LSystem):
    CONFIG = {
        'iteration': 6,
        'start_loc': 3.5 * DOWN + 3 * LEFT,
        'angle': 25 * DEGREES,
        'rules': {
            'X': 'F+[[X]-X]-F[-FX]+X',
            'F': 'FF'
        },
        'initial': 'X',
        'length': 0.1,
        'step_time': 0.1,
        'start_rot': 75 * DEGREES
    }

    def construct(self):
        self.generate()
        # self.animation = lambda x: self.add(x)
        self.draw()
        self.wait()

