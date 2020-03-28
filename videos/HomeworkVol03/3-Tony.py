# from @鹤翔万里

from manimlib.imports import *
from manim_sandbox.utils.imports import *

class Homework_03(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }
    def construct(self):
        circle = Circle(radius = 3, color = DARK_BLUE, plot_depth=3).flip()
        center = Dot(color=GREEN)
        A = Dot(np.array([-2, 0, 0]), color = RED)
        alpha = ValueTracker(0.0001)
        B = Dot(color=BLUE, radius=0.07, plot_depth=4)
        B.add_updater(lambda m: m.move_to(circle.point_from_proportion(alpha.get_value())))
        line1 = DashedLine(A.get_center(), B.get_center(), color=DARK_BROWN)
        line1.add_updater(lambda m: m.put_start_and_end_on(A.get_center(), B.get_center()))
        C = Dot(color=BLUE, radius=0.07, plot_depth=4)
        C.add_updater(lambda m: m.move_to(circle.point_from_proportion(alpha.get_value())).flip(axis=B.get_center()-A.get_center(), about_point=ORIGIN))
        line2 = Line(B.get_center(), C.get_center(), color=ORANGE, stroke_width=3)
        line2.add_updater(lambda m: m.put_start_and_end_on(B.get_center(), C.get_center()))

        trace = VGroup()
        self.i = 0
        def update_trace(m):
            self.i += 1
            if self.i % 4 == 0:
                m.add(line2.copy().clear_updaters())

        self.wait(3)
        self.play(ShowCreation(circle), ShowCreation(center))
        self.wait()
        self.play(ShowCreation(A))
        alpha.set_value(0.2)
        self.play(ShowCreation(B))
        self.play(alpha.increment_value, 0.6, run_time=1.5)
        self.play(alpha.increment_value, -0.6, run_time=1.6)
        self.play(ShowCreation(line1))
        self.wait()
        ra = Right_angle(corner=B.get_center(), on_the_right=False, stroke_color=BLUE)
        ra.move_corner_to(B.get_center())
        ra.change_angle_to(line1.get_angle()+PI/2)
        self.play(ShowCreation(C), ShowCreation(line2), ShowCreation(ra))
        self.wait(2)
        self.play(FadeOut(ra))
        self.play(alpha.increment_value, 0.6, run_time=1.5)
        self.play(alpha.increment_value, -0.7999, run_time=2, rate_func=linear)
        self.wait()
        self.add(trace)
        line2.set_stroke(width=2)
        self.wait(2)
        trace.add_updater(update_trace)
        alpha.set_value(0)
        anim = ApplyMethod(alpha.increment_value, 1, run_time=8, rate_func=linear)
        self.play(anim)
        self.wait(2)

        ellipse = Ellipse(width=6, height=2*np.sqrt(5), color=GREEN, plot_depth=10, run_time=2.5)
        self.play(ShowCreationThenDestruction(ellipse))
        self.wait(5)
