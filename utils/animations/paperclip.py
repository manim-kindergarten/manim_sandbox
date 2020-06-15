# from @鹤翔万里

"""
这里面的Animation是对回形针PaperClip几个动效的拙劣模仿
"""

from manimlib.constants import RED, LEFT, RIGHT, DOWN, UP, FRAME_WIDTH

from manimlib.mobject.mobject import Mobject
from manimlib.mobject.geometry import Rectangle, Line
from manimlib.mobject.shape_matchers import SurroundingRectangle
from manimlib.mobject.types.vectorized_mobject import VGroup

from manimlib.animation.animation import Animation
from manimlib.animation.composition import AnimationGroup
from manimlib.animation.transform import Restore, MoveToTarget
from manimlib.animation.creation import ShowCreation, Uncreate

from manimlib.utils.space_ops import get_norm
from manimlib.utils.config_ops import digest_config
from manimlib.utils.bezier import interpolate
from manimlib.utils.rate_functions import *


class PassingRectangle(Animation):
    """一个矩形从 ``mobject`` 的左边生成滑到右边结束"""
    CONFIG = {
        "rate_func": smooth,
        "buff": 0.05,
        "rec_rate": rush_into,
        "remover": True,
        "rectangle_config": {
            "color": RED,
            "fill_opacity": 0.6,
            "stroke_width": 0,
        },
    }

    def __init__(self, mobject, **kwargs):
        assert(isinstance(mobject, Mobject))
        digest_config(self, kwargs)
        self.mob_left = mobject.get_left() + self.buff * LEFT
        self.mob_right = mobject.get_right() + self.buff * RIGHT
        self.height = mobject.get_height() + 2 * self.buff
        self.width = mobject.get_width() + 2 * self.buff
        self.left = self.mob_left
        self.right = self.mob_right
        self.mobject = Rectangle(
            width=get_norm(self.right-self.left),
            height=self.height,
            **self.rectangle_config,
        ).move_to((self.left + self.right) / 2)
    
    def interpolate_mobject(self, alpha):
        alpha_left = self.rec_rate(alpha)
        alpha_right = 1 - self.rec_rate(1 - alpha)
        self.left = interpolate(self.mob_left, self.mob_right, alpha_left)
        self.right = interpolate(self.mob_left, self.mob_right, alpha_right)
        self.mobject.become(
            Rectangle(
                width=get_norm(self.right-self.left),
                height=self.height,
                **self.rectangle_config,
            ).move_to((self.left + self.right) / 2)
        )


class PassingRectangleWithBound(AnimationGroup):
    """``PassingRectangle`` 和 ``LaggedCreation``"""
    def __init__(self, mob, rec, **kwargs):
        AnimationGroup.__init__(
            self,
            PassingRectangle(mob, **kwargs),
            LaggedCreation(rec, **kwargs),
            lag_ratio=0.1,
            run_time=1.5
        )


class LaggedCreation(Animation):
    """起点和终点不同的Creation，只对Rectangle效果好"""
    CONFIG = {
        "lag_ratio": 1,
        "start_ratio": 1 / 6,
    }

    def interpolate_submobject(self, submob, start_submob, alpha):
        a, b = self.get_bounds(alpha)
        submob.pointwise_become_partial(
            start_submob, a, b
        )
        if b > 1:
            left_part = submob.copy().pointwise_become_partial(
                start_submob, 0, b - 1
            )
            submob.append_points(left_part.get_points())

    def get_bounds(self, alpha):
        ratio = self.start_ratio
        a = interpolate((1 - ratio) / 4, 1 / 2 + ratio / 4, alpha)
        b = interpolate((1 - ratio) / 4, 3 / 2 + ratio / 4, alpha)
        return (a, b)


class HighLightWithLines(AnimationGroup):
    """突出显示，并且上下边有直线"""
    CONFIG = {
        "color": RED,
        "rec_opacity": 0.5,
        "buff": 0.05
    }

    def __init__(self, mobject, **kwargs):
        assert(isinstance(mobject, Mobject))
        digest_config(self, kwargs)
        if not hasattr(mobject, "lines"):
            self.generate_lines(mobject)
        if not hasattr(mobject, "rectangle"):
            self.generate_rec(mobject)
        mobject.rectangle.save_state()
        mobject.rectangle.set_width(0, stretch=True, about_edge=LEFT)
        AnimationGroup.__init__(
            self,
            ShowCreation(mobject.lines, lag_ratio=0),
            Restore(mobject.rectangle),
            **kwargs
        )
    
    def generate_lines(self, mobject):
        line_up = Line(color=self.color, stroke_width=2).set_width(FRAME_WIDTH)
        line_up.next_to(mobject, UP, buff=self.buff, coor_mask=np.array([0, 1, 0]))
        line_down = Line(color=self.color, stroke_width=2).set_width(FRAME_WIDTH)
        line_down.next_to(mobject, DOWN, buff=self.buff, coor_mask=np.array([0, 1, 0]))
        mobject.lines = VGroup(line_up, line_down)
    
    def generate_rec(self, mobject):
        rectangle = SurroundingRectangle(
            mobject,
            color=self.color,
            fill_opacity=self.rec_opacity,
            stroke_width=0,
            buff=self.buff,
        )
        mobject.rectangle = rectangle


class UnHighLightWithLines(AnimationGroup):
    """``HighLightWithLines`` 的逆操作"""
    def __init__(self, mobject, **kwargs):
        assert(isinstance(mobject, Mobject))
        digest_config(self, kwargs)
        if not hasattr(mobject, "lines"):
            raise AttributeError("mobject must has lines attribute")
        if not hasattr(mobject, "rectangle"):
            raise AttributeError("mobject must has rectangle attribute")
        mobject.rectangle.generate_target()
        mobject.rectangle.target.set_width(0, stretch=True, about_edge=LEFT)
        AnimationGroup.__init__(
            self,
            Uncreate(mobject.lines, lag_ratio=0),
            MoveToTarget(mobject.rectangle),
            **kwargs
        )
        del mobject.lines, mobject.rectangle
