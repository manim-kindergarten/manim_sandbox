# from @cigar666

from manimlib.imports import *
from manim_sandbox.utils.mobjects.Rubik_Cube import *

class Rubik_Scene(ThreeDScene):

    CONFIG = {
        'order': 3,
        'size': 4.2,
        'camera_init': {
            'phi': 52.5 * DEGREES,
            'gamma': 0,
            'theta': -45 * DEGREES,
        },
    }

    def setup(self):

        self.set_camera_orientation(**self.camera_init)
        self.rubik = Rubik_Cube(order=self.order, size=self.size)
        self.add(self.rubik)


    def construct(self):

        pass  # To be implemented in subclasses

    def rotate_rubik_anim(self, layer, dim, quarter=1, run_time=1.5, reverse=False, **kwargs):
        theta = quarter * PI/2 * (-1 if reverse else 1)
        axis = [RIGHT, DOWN, OUT][dim-1]
        if layer != 0:
            layer_rotate = [layer] if type(layer) == int else layer
            layer_stay = []
            for i in range(1, self.order+1):
                if not i in layer_rotate:
                    layer_stay.append(i)
            if len(layer_stay) != 0:
                self.play(Rotating(self.rubik.get_layer(layer_rotate, dim=dim), radians=theta, axis=axis, run_time=run_time),
                          Rotating(self.rubik.get_layer(layer_stay, dim=dim), radians=0, axis=axis, run_time=run_time), **kwargs)
            else:
                self.play(Rotating(self.rubik.get_layer(layer_rotate, dim=dim), radians=theta, axis=axis, run_time=run_time), **kwargs)
        else:
            layer_rotate = list(range(1, self.order+1))
            self.play(Rotating(self.rubik.get_layer(layer_rotate, dim=dim), radians=theta, axis=axis, run_time=run_time), **kwargs)


class Play_rubic_order3(Rubik_Scene):

    CONFIG = {
        'order': 3,
    }

    def construct(self):

        self.wait()
        self.rotate_rubik_anim(1, 3, 1)       # U'
        self.rotate_rubik_anim(1, 1, -1)      # R
        self.rotate_rubik_anim(0, 2, 1)       # y
        self.rotate_rubik_anim(1, 3, 2)       # U'2
        self.rotate_rubik_anim(2, 1, -2)      # M'2
        self.rotate_rubik_anim([1,2], 3, -2)  # u2
        self.rotate_rubik_anim(1, 1, -1)      # L'
        self.rotate_rubik_anim([2,3], 2, 1)   # b
        self.rotate_rubik_anim(1, 3, -1)      # U
        self.wait()


class Play_rubic_order5(Rubik_Scene):

    CONFIG = {
        'order': 5,
    }

    def construct(self):

        self.wait()
        self.rotate_rubik_anim(1, 3, 1)
        self.rotate_rubik_anim(1, 1, -1)
        self.rotate_rubik_anim(0, 2, 1)
        self.rotate_rubik_anim(1, 3, 2)
        self.rotate_rubik_anim(2, 1, -2)
        self.rotate_rubik_anim([1,2], 3, -2)
        self.rotate_rubik_anim(1, 1, -1)
        self.rotate_rubik_anim([2,3], 2, 1)
        self.rotate_rubik_anim(1, 3, -1)
        self.wait()

