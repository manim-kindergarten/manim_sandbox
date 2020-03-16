# from @cigar666

from manimlib.imports import *

class Right_angle(VGroup):
    CONFIG = {
        'size': 0.25,
        'stroke_color': WHITE,
        'stroke_width': 3.2,
        'fill_color': BLUE,
        'fill_opacity': 0.5,
        'on_the_right': True,
    }
    def __init__(self, corner=ORIGIN, angle=0, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.corner = ORIGIN
        self.angle = 0
        r = UR if self.on_the_right else UL
        self.add(Polygon(ORIGIN, RIGHT * self.size * r, UR * self.size * r, UP * self.size * r, stroke_width=0,
                         fill_color=self.fill_color, fill_opacity=self.fill_opacity),
                 Line(RIGHT * self.size * r, UR * self.size * r + UP * self.stroke_width/100/2 * 0.8, stroke_width=self.stroke_width, stroke_color=self.stroke_color),
                 Line(UR * self.size * r + RIGHT * self.stroke_width/100/2 * r * 0.8, UP * self.size * r, stroke_width=self.stroke_width, stroke_color=self.stroke_color),
                 )
        self.move_corner_to(corner)
        self.change_angle_to(angle)

    def move_corner_to(self, new_corner):
        self.shift(new_corner - self.corner)
        self.corner = new_corner
        return self

    def change_angle_to(self, new_angle):
        self.rotate(new_angle - self.angle, about_point=self.corner)
        self.angle = new_angle
        return self

## test Right_angle ##

class Test_Right_angle(Scene):

    def construct(self):

        cp = ComplexPlane().scale(2.4)

        arrow_01 = Arrow(cp.n2p(1), cp.n2p(0.5), color=BLUE, buff=0, plot_depth=1)
        arrow_02 = Arrow(cp.n2p(1), cp.n2p(1+0.5j), color=YELLOW, buff=0, plot_depth=1)
        dot = Dot(cp.n2p(1), color=GREEN, plot_depth=2)
        group_01 = VGroup(dot, arrow_01, arrow_02)
        ra = Right_angle(corner=dot.get_center(), on_the_right=False)

        # the Right_angle 'ra' will not rotate with group_01,
        # but use method 'move_corner_to' & 'change_angle_to' to adjust its position and attitude
        ra.add_updater(lambda ra: ra.move_corner_to(dot.get_center()))
        ra.add_updater(lambda ra: ra.change_angle_to(arrow_01.get_angle() + PI))

        # dash_circle = Dashed_Circle(radius=cp.n2p(1)[0], arc_config={'color': GREEN, 'stroke_width': 1.5})

        self.play(ShowCreation(cp))
        self.wait()
        self.play(ShowCreation(dot))
        self.play(ShowCreation(arrow_01), ShowCreation(arrow_02))
        self.play(ShowCreation(ra))
        self.wait()
        # self.play(ShowCreation(dash_circle))
        self.play(Rotating(group_01, about_point=ORIGIN))

        self.wait(2)
