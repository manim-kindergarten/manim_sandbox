# from @cigar666

from manimlib.imports import *

class Trail(VGroup):

    CONFIG = {
        'max_width': 5,
        'nums': 500,
        'trail_color': BLUE_B,
        # 'rate_func': linear,
        'rate_func': lambda t: t ** 1.25,
    }

    def __init__(self, mob, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.add(mob)
        self.trail = VGroup()
        self.path_xyz = []
        self.add(self.trail)
        self.pos_old = self[0].get_center()

    def update_trail(self, trail):
        err = 1e-6
        pos_new = self[0].get_center()
        pos_old = self.pos_old
        self.pos_old = pos_new
        # if np.sqrt(sum((pos_new - pos_old) ** 2))>err:
        if sum(abs(pos_new - pos_old))>err:
            trail.add(Line(pos_old, pos_new, color=self.trail_color, plot_depth=0))

        if len(trail) > self.nums:
            trail.remove(trail[0])
            # for k in range(self.nums):
            #     trail[k].set_stroke(width=self.max_width * self.rate_func(k/self.nums),
            #                         opacity=self.rate_func(k/self.nums))
            for l in trail:
                k = trail.submobjects.index(l)
                l.set_stroke(width=self.max_width * self.rate_func(k/self.nums),
                             opacity=self.rate_func(k/self.nums))

        if len(trail) <= self.nums and len(trail) > 0:
            # for k in range(len(trail)):
            #     trail[k].set_stroke(width=self.max_width * self.rate_func(k/len(trail)),
            #                         opacity=self.rate_func(k/len(trail)))
            for l in trail:
                k = trail.submobjects.index(l)
                l.set_stroke(width=self.max_width * self.rate_func(k/len(trail)),
                             opacity=self.rate_func(k/len(trail)))

    def get_path_xyz(self, err=1e-4):
        pos_new = self[0].get_center()
        pos_old = self.pos_old
        if sum(abs(pos_new - pos_old))>err:
            self.path_xyz.append(pos_new)
        self.pos_old = pos_new
        while len(self.path_xyz) > self.nums:
            self.path_xyz.remove(self.path_xyz[0])

    def create_path(self):
        path = VGroup()
        self.get_path_xyz()
        if len(self.path_xyz) > 1:
            for i in range(len(self.path_xyz)-1):
                path.add(Line(self.path_xyz[i], self.path_xyz[i+1], stroke_color=self.trail_color,
                              stroke_opacity=self.rate_func(i/len(self.path_xyz)), plot_depth=self.rate_func(i/len(self.path_xyz)),
                              stroke_width=self.max_width * self.rate_func(i/len(self.path_xyz))))
        return path

    def update_path(self, trail):
        trail.become(self.create_path())

    def start_trace(self):
        # self.trail.add_updater(self.update_trail)
        self.trail.add_updater(self.update_path)

    def stop_trace(self):
        self.trial.remove_updater(self.update_path)

## test Trail ##

class Test_trail(Scene):

    def construct(self):

        dot = Dot(color=BLUE).shift(LEFT)
        trail = Trail(dot, trail_color=BLUE_B, max_width=4)
        trail.start_trace()

        self.add(trail)
        self.play(Rotating(dot, about_point=ORIGIN, run_time=4))

        self.wait()
