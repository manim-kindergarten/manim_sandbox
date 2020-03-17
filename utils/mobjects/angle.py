# from @pdcxs

from manimlib.imports import *

# Usage: Angle(p1, p2, p3)
# p1, p2, p3 should be in counterclock order
# p2 is the vertex of the angle
# is_right: make the angle always be a right angle
# not_right: the angle is always NOT a right angle
# if is_right and not_right are both false, the angle
# will be drawed according to the value

class Angle(Arc):
    CONFIG = {
        "radius": 0.5,
        "color": WHITE,
        "show_edge": False,
        "is_right": False,
        "not_right": False,
    }
    def __init__(self, p1, p2, p3, **kwargs):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.arc_center = p2.get_center()
        Arc.__init__(self,
            start_angle=self.get_start_angle(),
            angle = self.get_angle(),
            **kwargs)

    def get_start(self):
        pos1 = self.p1.get_center()
        pos2 = self.p2.get_center()
        vec = pos1 - pos2
        return pos2 + normalize(vec) * self.radius
    
    def get_end(self):
        pos3 = self.p3.get_center()
        pos2 = self.p2.get_center()
        vec = pos3 - pos2
        return pos2 + normalize(vec) * self.radius

    def get_start_angle(self):
        pos1 = self.p1.get_center()
        pos2 = self.p2.get_center()
        vec = pos1 - pos2
        x = vec[0]
        y = vec[1]

        return math.atan2(y, x)

    def get_angle(self):
        pos1 = self.p3.get_center()
        pos2 = self.p2.get_center()
        vec = pos1 - pos2
        x = vec[0]
        y = vec[1]

        angle = math.atan2(y, x) -\
            self.get_start_angle()
        
        if angle < 0:
            angle += TAU
        
        return angle

    def make_angle_dynamic(self):
        self.add_updater(lambda m: m.generate_points())

    def get_label_loc(self, buff=SMALL_BUFF):
        s_angle = self.get_start_angle()
        e_angle = self.get_angle()
        angle = s_angle + e_angle / 2

        x = np.cos(angle) * (self.radius + buff) * RIGHT
        y = np.sin(angle) * (self.radius + buff) * UP

        return x + y + self.p2.get_center()

    def add_label(self, label, buff=SMALL_BUFF):
        label.add_updater(lambda m:\
            m.move_to(self.get_label_loc(buff)))

    def generate_points(self):
        o = self.p2.get_center()
        if self.is_right or\
        (not self.not_right and\
            abs(self.get_angle() - PI/2) < 1e-6):
            self.clear_points()
            vec = self.get_end() - o
            if self.show_edge:
                self.append_points([o])
                self.add_line_to(self.get_start())
            self.append_points([self.get_start()])
            self.add_line_to(self.get_start() + vec)
            self.append_points([self.get_start() + vec])
            self.add_line_to(self.get_end())
            self.append_points([self.get_end()])
            if self.show_edge:
                self.add_line_to(o)
                self.append_points([o])
        else:
            arc = Arc(
                radius = self.radius,
                start_angle = self.get_start_angle(),
                angle = self.get_angle(),
                arc_center = o
            )
            self.clear_points()
            self.append_points(arc.points)
            if (self.show_edge):
                self.add_line_to(o)
                self.append_points([o])
                self.add_line_to(arc.points[0])
