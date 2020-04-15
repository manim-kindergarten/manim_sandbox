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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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


class FreeFallEngine(AbstractFreeFallEngine):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def uniform(self, vx, t):
        return vx * t

    def accelerate(self, vy, t):
        return vy * t + self.gravity / 2 * (t ** 2)

    def approximation_points(self, instance, vx, vy):
        assert (isinstance(instance, Mobject))
        points = []
        center = instance.get_center()
        while True:
            if abs(center[0]) >= self.boundary[0] + instance.get_width() / 2:
                return points
            if center[1] - instance.get_height() / 2 < -self.boundary[1]:
                vy *= -self.lost_ratio
                center = np.array([center[0], -self.boundary[1] + instance.get_height() / 2, 0])
            else:
                center += np.array([self.uniform(vx, self.tick), -self.accelerate(vy, self.tick), 0])
                vy += self.gravity * self.tick
                points.append(copy.deepcopy(center))


class ThreeDFreeFallEngine(AbstractFreeFallEngine):
    pass
