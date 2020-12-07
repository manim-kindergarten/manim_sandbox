# from @pdcxs
# This is a scene that plot parabola
# Demos can be bound in
# https://github.com/pdcxs/ManimProjects/tree/master/Parabola

from manimlib.imports import *

class Parabola(Scene):
    CONFIG = {
        'focus': 2,
        'y_max': 10,
        'x_min': -8,
        'color': WHITE
    }

    def adjust_x_range(self):
        self.y_min = -self.y_max
        self.x_max = 2 * self.y_max / FRAME_HEIGHT * FRAME_WIDTH + self.x_min
        self.func = lambda y: y ** 2 / (4 * self.focus)

    def get_graph(self, color=WHITE):
        f = self.focus
        func = self.func

        def parameterized_function(alpha):
            y = interpolate(self.y_max, self.y_min, alpha)
            x = func(y)
            return self.coords_to_point(x, y)
        
        self.graph = ParametricFunction(
            parameterized_function,
            color = color
        )
        return self.graph

    @staticmethod
    def get_horizontal():
        return Line(FRAME_X_RADIUS * LEFT, FRAME_X_RADIUS * RIGHT)

    def value_to_point(self, y):
        x = y ** 2 / (4 * self.focus)
        return self.coords_to_point(x, y)

    def get_focus(self):
        return self.coords_to_point(self.focus, 0)

    def get_directrix(self):
        f = self.coords_to_point(-self.focus, 0)
        return Line(
            f + FRAME_Y_RADIUS * UP,
            f + FRAME_Y_RADIUS * DOWN)

    @staticmethod
    def map(val, from_min, from_max, to_min, to_max):
        return (val - from_min) / (from_max - from_min) * (to_max - to_min) + to_min

    def coords_to_point(self, x, y):
        to_x = self.map(x, self.x_min, self.x_max,
            -FRAME_X_RADIUS, FRAME_X_RADIUS)
        to_y = self.map(y, self.y_min, self.y_max,
            -FRAME_Y_RADIUS, FRAME_Y_RADIUS)
        return to_x * RIGHT + to_y * UP

    def point_to_coords(self, point):
        pos = point.get_center()
        x = pos[0]
        y = pos[1]
        to_x = self.map(x, -FRAME_X_RADIUS,
            FRAME_X_RADIUS,
            self.x_min,
            self.x_max)
        to_y = self.map(y, -FRAME_Y_RADIUS,
            FRAME_Y_RADIUS,
            self.y_min,
            self.y_max)
        return [to_x, to_y]

    def get_opposite_y(self, y):
        f = self.focus
        return -4 * f * f / y

    def get_opposite(self, point):
        pos = self.point_to_coords(point)
        [x, y] = pos
        opp_y = self.get_opposite_y(y)
        opp_x = self.func(opp_y)
        return self.coords_to_point(opp_x, opp_y)

    def chord_to_directrix(self, p1, p2):
        # p1 on left, p2 on right
        if (p1.get_center()[0] > p2.get_center()[0]):
            p1, p2 = p2, p1
        pos1 = p1.get_center()
        pos2 = p2.get_center()
        vec = pos1 - pos2
        if vec[0] == 0:
            return self.coords_to_point(-self.focus, 0)
        vec /= vec[0]
        dest_x = self.coords_to_point(-self.focus, 0)[0]
        fac = dest_x - pos1[0]
        return pos1 + vec * fac

    @staticmethod
    def right(point1, point2):
        pos1 = point1.get_center()
        pos2 = point2.get_center()
        if pos1[0] > pos2[0]:
            return pos1
        return pos2

    def get_tangent_to_directrix(self, point):
        [x, y] = self.point_to_coords(point)
        d = y / (2 * self.focus)
        dx = -self.focus - x
        dy = dx / d
        return self.coords_to_point(
            -self.focus,
            y + dy
        )

    def add_tangent_line_updater(self, line, point):
        line.add_updater(lambda l:\
            l.put_start_and_end_on(
                point.get_center(),
                self.get_tangent_to_directrix(point)
            ))

    def add_tangent_extent_updater(self, line, point):
        def updater(l):
            l.put_start_and_end_on(LEFT * FRAME_WIDTH, RIGHT * FRAME_WIDTH)
            pos1 = point.get_center()
            pos2 = self.get_tangent_to_directrix(point)
            vec = pos2 - pos1
            ang = math.atan2(vec[1], vec[0])
            l.set_angle(ang)
            l.move_to(pos1)
        line.add_updater(lambda l:\
            updater(l))

    def add_directrix_point_updater(self, p, d):
        d.add_updater(lambda m:\
            m.move_to(self.coords_to_point(
                -self.focus, 0
            ) + p.get_center()[1] * UP))
        
    def get_normal_to_directrix(self, point):
        [x, y] = self.point_to_coords(point)
        if y == 0:
            return self.coords_to_point(-self.focus, 0)
        d = -y / (2 * self.focus)
        dx = -self.focus - x
        dy = dx * d
        return self.coords_to_point(
            -self.focus,
            y + dy
        )

    def add_normal_updater(self, line, point):
        def updater(l):
            l.put_start_and_end_on(LEFT * FRAME_WIDTH, RIGHT * FRAME_WIDTH)
            pos1 = point.get_center()
            pos2 = self.get_normal_to_directrix(point)
            vec = pos2 - pos1
            ang = math.atan2(vec[1], vec[0])
            l.set_angle(ang)
            l.move_to(pos1)
        line.add_updater(lambda l:\
            updater(l))
