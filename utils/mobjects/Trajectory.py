# @ widcardw
# 基于 TracedPath 的轨迹类，能够自动减淡轨迹的尾部

from manimlib import VMobject, TracedPath, Scene, Dot, Rotating, get_norm
from manimlib.constants import *


class Trajectory(TracedPath):
    """
    基类
    """
    CONFIG = {
        "stroke_width": [0, 6],
        "stroke_color": WHITE,
        "stroke_opacity": [0, 1],
        "min_distance_to_new_point": 0.1,
    }

    def __init__(self, traced_point_func, **kwargs):
        super().__init__(traced_point_func, **kwargs)
        self.traced_point_func = traced_point_func

    def pop_points(self):
        self.data["points"] = np.delete(self.data["points"], [0, 1, 2], 0)
        self.refresh_bounding_box()
        return self


class TrajectoryOnLength(Trajectory):
    """
    固定长度的轨迹
    接受一个物件的函数，调用这个函数可以得到坐标
    例如 dot.get_center, 注意不加括号
    """
    CONFIG = {
        "life_length": 40
    }

    def __init__(self, traced_point_func, **kwargs):
        super().__init__(traced_point_func, **kwargs)
        self.add_updater(lambda m: m.update_path())

    def update_path(self):
        super(TrajectoryOnLength, self).update_path()
        if len(self.get_points()) / self.n_points_per_curve > self.life_length:
            self.pop_points()


class TrajectoryOnTime(Trajectory):
    """
    根据时间长度变化的轨迹
    接受参数: 1.能够生成点坐标的函数, 2.场景
    之所以要接受场景，是因为涉及到了控制时间
    life_time = 开始消亡的时间点 - 该对象诞生时间点
    fade_ratio 用于控制消亡速度
      - 为什么会有这个？因为我暂时想不出什么好办法来控制它消亡的速度了
      - 取值为正整数，取值越小，消亡越快
      - 消亡速度与“帧率”有关
    """
    CONFIG = {
        "life_time": 5,
        "fade_ratio": 5
    }

    def __init__(self, traced_point_func, scene: Scene, **kwargs):
        assert scene
        self.count = 0
        super().__init__(traced_point_func, **kwargs)
        self.scene = scene
        self.birth_time = scene.time
        self.add_updater(lambda m: m.update_path())

    def update_path(self):
        super(TrajectoryOnTime, self).update_path()
        self.count += 1
        if self.count % self.fade_ratio == 0 and (self.scene.time - self.birth_time > self.life_time):
            self.pop_points()


# 使用例，基于时间消亡的轨迹
class TestTrajectory(Scene):

    def construct(self):
        d = Dot(RIGHT * 2)
        t = TrajectoryOnTime(d.get_center, scene=self, life_time=2)
        self.add(d, t)
        self.play(Rotating(d, TAU, about_point=ORIGIN, run_time=5))
        self.wait(2)


# 使用例，基于长度消亡的轨迹
class TestTrajectory2(Scene):

    def construct(self):
        d = Dot(RIGHT * 2)
        t = TrajectoryOnLength(d.get_center)
        self.add(d, t)
        self.play(Rotating(d, TAU, about_point=ORIGIN, run_time=5))
        self.wait(2)
