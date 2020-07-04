# from @RY-Givenchy

#
# Copyright: 2020 niedong
# Physics engine design
#
# Originally written for my solitaire video
#

from manimlib.imports import *


class PhysicsEngine(Container):
    CONFIG = {
        "boundary": [FRAME_X_RADIUS, FRAME_Y_RADIUS, 0],
        "tick": 1 / DEFAULT_FRAME_RATE
    }

    def validate(self):
        for boundary in self.boundary:
            assert (boundary >= 0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.validate()

    def approximation_points(self, *args, **kwargs):
        pass


class AbstractFreeFallEngine(PhysicsEngine):
    CONFIG = {
        "gravity": 9.8,
        "lost_ratio": 0.75
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def uniform(self, *args, **kwargs):
        pass

    def accelerate(self, *args, **kwargs):
        pass

    def hit_up(self, *args, **kwargs):
        pass

    def hit_down(self, *args, **kwargs):
        pass

    def hit_left(self, *args, **kwargs):
        pass

    def hit_right(self, *args, **kwargs):
        pass


class FreeFallEngine(AbstractFreeFallEngine):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def uniform(self, vx, t):
        return vx * t

    def accelerate(self, vy, t):
        return vy * t + self.gravity / 2 * (t ** 2)

    def get_dim(self, instance):
        return -self.boundary[1] - instance.get_bottom()[1]

    def hit_down(self, instance):
        return self.get_dim(instance) > 0

    def out_left(self, instance):
        return instance.get_right()[0] < -self.boundary[0]

    def within_left(self, instance):
        return not self.out_left(instance)

    def out_right(self, instance):
        return instance.get_left()[0] > self.boundary[0]

    def within_right(self, instance):
        return not self.out_right(instance)

    def within_x(self, instance):
        return self.within_left(instance) and self.within_right(instance)

    def approximation_points(self, instance, vx, vy):
        assert (isinstance(instance, Mobject))
        ins = instance.copy()
        while self.within_x(ins):
            if self.hit_down(ins):
                vy *= -self.lost_ratio
                ins.shift(np.array([0, self.get_dim(ins), 0]))
            else:
                ins.shift(np.array([self.uniform(vx, self.tick), -self.accelerate(vy, self.tick), 0]))
                vy += self.gravity * self.tick
            yield copy.deepcopy(ins.get_center())


class ThreeDFreeFallEngine(AbstractFreeFallEngine):
    pass
