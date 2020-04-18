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

    def valid_boundary_check(self):
        for boundary in self.boundary:
            assert (boundary >= 0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.valid_boundary_check()

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

    def hit_upper_bound(self, *args, **kwargs):
        pass

    def hit_lower_bound(self, *args, **kwargs):
        pass

    def hit_right_bound(self, *args, **kwargs):
        pass

    def hit_left_bound(self, *args, **kwargs):
        pass


class FreeFallEngine(AbstractFreeFallEngine):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def uniform(self, vx, t):
        return vx * t

    def accelerate(self, vy, t):
        return vy * t + self.gravity / 2 * (t ** 2)

    def hit_lower_bound(self, instance):
        return instance.get_bottom()[1] < -self.boundary[1]

    def out_left_bound(self, instance):
        return instance.get_right()[0] < -self.boundary[0]

    def out_right_bound(self, instance):
        return instance.get_left()[0] > self.boundary[0]

    def approximation_points(self, _instance, vx, vy):
        assert (isinstance(_instance, Mobject))
        points = []
        instance = _instance.copy()
        while True:
            if self.out_right_bound(instance) or self.out_left_bound(instance):
                return points
            if self.hit_lower_bound(instance):
                vy *= -self.lost_ratio
                instance.shift(np.array([0, - self.boundary[1] - instance.get_bottom()[1], 0]))
            else:
                instance.shift(np.array([self.uniform(vx, self.tick), -self.accelerate(vy, self.tick), 0]))
                vy += self.gravity * self.tick
                points.append(copy.deepcopy(instance.get_center()))


class ThreeDFreeFallEngine(AbstractFreeFallEngine):
    pass
