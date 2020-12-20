# from @cigar666
# 这是我在旋轮线那期视频写的相关的齿轮类和场景

from manimlib.imports import *

class Gear_outline(VMobject):
    CONFIG = {
        'arc_segments': 4,
        'curve_segments': 6,
    }

    def __init__(self, pitch_circle_radius=2, tooth_hight=0.5, tooth_num=17, **kwargs):

        VMobject.__init__(self, **kwargs)
        self.pitch_circle_radius = pitch_circle_radius
        self.tooth_hight = tooth_hight
        self.tooth_num = tooth_num

        self.rb = self.pitch_circle_radius - self.tooth_hight/2
        self.pitch = self.pitch_circle_radius * 2 * PI / self.tooth_num
        theta_pitch = np.tan(np.arccos(self.rb/self.pitch_circle_radius)) - np.arccos(self.rb/self.pitch_circle_radius)
        theta_top = np.tan(np.arccos(self.rb/(self.rb + self.tooth_hight))) - np.arccos(self.rb/(self.rb + self.tooth_hight))
        alpha_max = np.arccos(self.rb/(self.rb + self.tooth_hight))

        alphas = np.linspace(0, alpha_max, self.curve_segments)
        curve01_radius = self.rb/np.cos(alphas)
        curve01_thetas = np.tan(alphas) - alphas - theta_pitch - TAU/self.tooth_num/2/2
        arc_top_thetas = np.linspace(theta_top - theta_pitch - TAU/self.tooth_num/2/2, -(theta_top - theta_pitch - TAU/self.tooth_num/2/2), self.arc_segments)
        curve02_radius = self.rb/np.cos(alphas)
        curve02_thetas = -curve01_thetas
        arc_bottom_thetas = np.linspace(theta_pitch + TAU/self.tooth_num/2/2, -(theta_pitch + TAU/self.tooth_num/2/2) + TAU/self.tooth_num, self.arc_segments)
        arc_top_radius = np.array([(self.rb + self.tooth_hight) for i in range(self.arc_segments)])
        arc_bottom_radius = np.array([self.rb for i in range(self.arc_segments)])
        part_01_thetas = np.concatenate((curve01_thetas, arc_top_thetas[1:-1], curve02_thetas[::-1], arc_bottom_thetas[1:-1]), axis=0)
        part_01_radius = np.concatenate((curve01_radius, arc_top_radius[1:-1], curve02_radius[::-1], arc_bottom_radius[1:-1]), axis=0)

        all_part_thetas = part_01_thetas
        all_part_radius = part_01_radius
        for i in range(1, self.tooth_num):
            all_part_thetas = np.concatenate((all_part_thetas, part_01_thetas + i * TAU/self.tooth_num), axis=0)
            all_part_radius = np.concatenate((all_part_radius, part_01_radius), axis=0)


        vertices = self.polar2xyz(all_part_radius, all_part_thetas)

        self.set_points_as_corners(
            [*vertices, vertices[0]]
        )

    @staticmethod
    def polar2xyz(r, theta):
        if type(theta) == np.ndarray:
            if type(r) == np.ndarray:

                return np.concatenate((np.cos(theta).reshape(-1, 1), np.sin(theta).reshape(-1, 1), theta.reshape(-1, 1) * 0), axis=1) * r.reshape(-1, 1)
            else:
                return np.concatenate((np.cos(theta).reshape(-1, 1), np.sin(theta).reshape(-1, 1), theta.reshape(-1, 1) * 0), axis=1) * r
        else:
            return np.array([np.cos(theta), np.sin(theta), 0]) * r

    def get_vertices(self):
        return self.get_start_anchors()

    def round_corners(self, radius=0.01):
        vertices = self.get_vertices()
        arcs = []
        for v1, v2, v3 in adjacent_n_tuples(vertices, 3):
            vect1 = v2 - v1
            vect2 = v3 - v2
            unit_vect1 = normalize(vect1)
            unit_vect2 = normalize(vect2)
            angle = angle_between_vectors(vect1, vect2)
            # Negative radius gives concave curves
            angle *= np.sign(radius)
            # Distance between vertex and start of the arc
            cut_off_length = radius * np.tan(angle / 2)
            # Determines counterclockwise vs. clockwise
            sign = np.sign(np.cross(vect1, vect2)[2])
            arc = ArcBetweenPoints(
                v2 - unit_vect1 * cut_off_length,
                v2 + unit_vect2 * cut_off_length,
                angle=sign * angle
            )
            arcs.append(arc)

        self.clear_points()
        # To ensure that we loop through starting with last
        arcs = [arcs[-1], *arcs[:-1]]
        for arc1, arc2 in adjacent_pairs(arcs):
            self.append_points(arc1.points)
            line = Line(arc1.get_end(), arc2.get_start())
            # Make sure anchors are evenly distributed
            len_ratio = line.get_length() / arc1.get_arc_length()
            line.insert_n_curves(
                int(arc1.get_num_curves() * len_ratio)
            )
            self.append_points(line.get_points())
        return self

class Show_gear(Scene):

    def construct(self):

        gear = Gear_outline(pitch_circle_radius=3.6, tooth_hight=0.25, tooth_num=67, color=BLUE, stroke_width=2.5) # .round_corners()

        gear_02 = Gear_outline(pitch_circle_radius=3.6 * 49/67, tooth_hight=0.25, tooth_num=49, color=YELLOW, stroke_width=2.5).shift(RIGHT * (3.6 - 3.6 * 49/67))

        w1 = TAU/360 * 5
        R = np.array([[np.cos(-w1), -np.sin(-w1), 0],
                      [np.sin(-w1), np.cos(-w1), 0],
                      [0, 0, 1]])

        def gear_updater(gear, dt):
            loc = gear.get_center()
            loc_new = np.dot(loc, R)
            gear.move_to(loc_new)
            gear.rotate(-w1*67/49+w1, about_point=gear.get_center())
            return gear

        self.play(ShowCreation(gear), run_time=1.2)
        self.wait(0.25)
        self.play(ShowCreation(gear_02), run_time=1.2)
        gear_02.add_updater(gear_updater)
        self.wait(5)
        gear_02.remove_updater(gear_updater)

        # time=10
        # dt=1/15
        # n = int(time/dt)
        # for i in range(n):
        #     loc = gear_02.get_center()
        #     loc_new = np.dot(loc, R)
        #     gear_02.move_to(loc_new)
        #     gear_02.rotate(-w1*67/49 + w1, about_point=gear_02.get_center())
        #     # gear.rotate(-w1)
        #     self.wait(dt)

        self.wait(4)

class Spirograph(VGroup):

    CONFIG = {
        'radius_outer': 3.8,
        'radius_big': 3.5,
        'gear_color': [BLUE, YELLOW],
        'tooth_num_big': 59,
        'tooth_num_small': 29,
        'center_loc': LEFT * 3.,

        # 'dt': 1/25,
        'speed': TAU/360 * 2,
        'hole_radius': 0.09,
    }

    def __init__(self, **kwargs):

        VMobject.__init__(self, **kwargs)

        self.pitch = self.radius_big * 2 * PI / self.tooth_num_big
        self.tooth_hight = self.pitch * 0.6

        self.outer_circle = Circle(radius=self.radius_outer, fill_color=self.gear_color[0], fill_opacity=0.54, stroke_color=self.gear_color[0], stroke_width=2.25)
        self.outline_big = Gear_outline(pitch_circle_radius=self.radius_big, tooth_num=self.tooth_num_big, tooth_hight=self.tooth_hight,
                                        stroke_width=2.25, fill_opacity=1, fill_color=BLACK, stroke_color=self.gear_color[0])
        self.gear_big = VGroup(self.outer_circle, self.outline_big).move_to(self.center_loc)
        self.radius_small = self.pitch * self.tooth_num_small / 2 / PI
        self.outline_small = Gear_outline(pitch_circle_radius=self.radius_small, tooth_num=self.tooth_num_small, tooth_hight=self.tooth_hight,
                                          stroke_width=2.25, stroke_color=self.gear_color[1], fill_color=self.gear_color[1],
                                          fill_opacity=0.32).move_to(self.center_loc).shift(RIGHT * (self.radius_big-self.radius_small-0.01))

        self.hole_group = VGroup() # the tiny holes on the small gear
        # self.add_hole(ORIGIN)
        self.small_gear = VGroup(self.outline_small, self.hole_group)

        self.curves_group = VGroup() # put in the curves we wanna draw
        self.add(self.gear_big, self.small_gear, self.curves_group)

        self.small_gear_speed = -self.speed * self.tooth_num_big/self.tooth_num_small + self.speed

    def add_hole(self, loc, scale=1):

        hole = Circle(radius=self.hole_radius, color=self.gear_color[1], fill_color=BLACK, fill_opacity=1, stroke_width=1.8).scale(scale).move_to(self.outline_small.get_center() + loc)
        self.hole_group.add(hole)

    def add_hole_by_spiral(self, hole_num=13, min_radius=0.25, angle=PI * 3, delta_r=0.4):

        a, b = min_radius, np.log((self.radius_small-delta_r)/min_radius)/3/PI
        spiral_polar_r = lambda theta: a * np.exp(b * theta)
        theta = 0
        for i in range(hole_num):
            r = spiral_polar_r(theta)
            self.add_hole(r * (np.cos(theta) * RIGHT + np.sin(theta) * UP))
            theta += angle/(hole_num-1) * (1 + (5.5 - i) * 0.1)

    def add_hole_by_line(self, hole_num=7, delta_r=0.4):
        n = hole_num
        x = np.linspace(-(self.radius_small - delta_r), self.radius_small - delta_r, hole_num)

        for i in range(hole_num):
            self.add_hole(x[i] * RIGHT)

class Spirograph_test(Scene):

    def construct(self):

        self.temp_dot = []

        self.color_list = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PINK, RED], 320)

        self.color_pointer = 0

        spirograph = Spirograph()
        spirograph.add_hole_by_spiral()

        self.add(spirograph)
        self.wait(0.5)
        spirograph.add_updater(self.update_small_gear)

        self.wait(90)

    def update_small_gear(self, spirograph, dt=1/60):
        w1 = spirograph.speed
        R = np.array([[np.cos(-w1), -np.sin(-w1), 0],
                      [np.sin(-w1), np.cos(-w1), 0],
                      [0, 0, 1]])
        loc = spirograph.outline_small.get_center()
        loc_new = np.dot(loc-spirograph.center_loc, R) + spirograph.center_loc
        spirograph.small_gear.shift(loc_new-spirograph.outline_small.get_center())
        spirograph.small_gear.rotate(spirograph.small_gear_speed, about_point=spirograph.outline_small.get_center())

        self.temp_dot.append(spirograph.hole_group[-1].get_center())
        if len(self.temp_dot) > 2:
            self.temp_dot.remove(self.temp_dot[0])
        if len(self.temp_dot) == 2:
            spirograph.curves_group.add(Line(self.temp_dot[-1], self.temp_dot[-2], stroke_width=2.4, color=self.color_list[int(self.color_pointer/20)%len(self.color_list)]))
        # self.add(Dot(spirograph.hole_group[-1].get_center()).scale(0.4).set_color(self.color_list[int(self.color_pointer/8)%len(self.color_list)]))
        self.color_pointer += 1

class SpirographScene(Scene):

    CONFIG = {
        'total_hight': 7.5,
        'tooth_num_big': 72,
        'tooth_num_small': 48,
        'ratio_str': '3/2',
        'gear_color': [BLUE, YELLOW],
        'spirograph_loc': LEFT * 2.75,
        'rotate_speed': TAU/360 * 0.75,
        'run_time': 12,
        'dt': 1/60,
        'curve_stroke': 3.2,
    }

    def construct(self):

        self.temp_dot = []
        self.color_list = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PINK, RED], 320)
        self.color_pointer = 0

        self.spirograph = Spirograph(radius_outer=self.total_hight/2, radius_big=self.total_hight/2-0.32, center_loc=self.spirograph_loc,
                                tooth_num_big=self.tooth_num_big, tooth_num_small=self.tooth_num_small, speed=self.rotate_speed,
                                gear_color=self.gear_color)

        self.add_holes()
        self.add(self.spirograph)
        self.wait(0.4)
        self.add_parameter_info()
        self.start_draw()

    def add_holes(self):
        self.spirograph.hole_radius = 0.064
        self.spirograph.add_hole_by_line(hole_num=12, delta_r=0.275)

    def start_draw(self):
        self.spirograph.add_updater(self.draw_all_hole)
        self.wait(self.run_time)


    def draw_last_hole(self, spirograph, dt=1/60):
        dt=self.dt
        w1 = spirograph.speed
        R = np.array([[np.cos(-w1), -np.sin(-w1), 0],
                      [np.sin(-w1), np.cos(-w1), 0],
                      [0, 0, 1]])
        loc = spirograph.outline_small.get_center()
        loc_new = np.dot(loc-spirograph.center_loc, R) + spirograph.center_loc
        spirograph.small_gear.shift(loc_new-spirograph.outline_small.get_center())
        spirograph.small_gear.rotate(spirograph.small_gear_speed, about_point=spirograph.outline_small.get_center())

        self.temp_dot.append(spirograph.hole_group[-1].get_center())
        if len(self.temp_dot) > 2:
            self.temp_dot.remove(self.temp_dot[0])
        if len(self.temp_dot) == 2:
            spirograph.curves_group.add(Line(self.temp_dot[-1], self.temp_dot[-2], stroke_width=self.curve_stroke, color=self.color_list[int(self.color_pointer/20)%len(self.color_list)]))
        # self.add(Dot(spirograph.hole_group[-1].get_center()).scale(0.4).set_color(self.color_list[int(self.color_pointer/8)%len(self.color_list)]))
        self.color_pointer += 1

    def draw_all_hole(self, spirograph, dt=1/60):
        dt=self.dt
        w1 = spirograph.speed
        R = np.array([[np.cos(-w1), -np.sin(-w1), 0],
                      [np.sin(-w1), np.cos(-w1), 0],
                      [0, 0, 1]])
        loc = spirograph.outline_small.get_center()
        loc_new = np.dot(loc-spirograph.center_loc, R) + spirograph.center_loc
        spirograph.small_gear.shift(loc_new-spirograph.outline_small.get_center())
        spirograph.small_gear.rotate(spirograph.small_gear_speed, about_point=spirograph.outline_small.get_center())

        if self.temp_dot == []:
            self.temp_dot = [[] for i in range(len(spirograph.hole_group))]

        n = len(spirograph.hole_group)
        for i in range(n):
            self.temp_dot[i].append(spirograph.hole_group[i].get_center())
            if len(self.temp_dot[i]) > 2:
                self.temp_dot[i].remove(self.temp_dot[i][0])
            if len(self.temp_dot[i]) == 2:
                spirograph.curves_group.add(Line(self.temp_dot[i][-1], self.temp_dot[i][-2], stroke_width=self.curve_stroke, color=self.color_list[int(i/n * len(self.color_list))]))

        #         spirograph.curves_group.add(Line(self.temp_dot[i][-1], self.temp_dot[i][-2], stroke_width=2.4, color=self.color_list[int(self.color_pointer/20)%len(self.color_list)]))
        # self.color_pointer += 1

    def add_parameter_info(self):

        text_big_num = Text('定轮齿数：', font='新蒂小丸子体', color=self.gear_color[0]).scale(1.28).to_corner(UP * 2 + LEFT * 18)
        text_small_num = Text('动轮齿数：', font='新蒂小丸子体', color=self.gear_color[1]).scale(1.28).to_corner(UP * 4.5 + LEFT * 18)
        text_ratio = Text('齿数比：', font='新蒂小丸子体', color=average_color(*self.gear_color)).scale(1.28).to_corner(UP * 7 + LEFT * 18)
        big_num = Text('%d' % self.tooth_num_big, font='Comic Sans MS', color=self.gear_color[0]).scale(1.28).next_to(text_big_num, RIGHT * 1.5)
        small_num = Text('%d' % self.tooth_num_small, font='Comic Sans MS', color=self.gear_color[1]).scale(1.28).next_to(text_small_num, RIGHT * 1.5).align_to(big_num, LEFT)
        ratio = Text(self.ratio_str, font='Comic Sans MS', color=average_color(*self.gear_color)).scale(1.28).next_to(text_ratio, RIGHT * 1.5)
        self.add(text_big_num, text_small_num)
        self.wait(0.2)
        self.play(FadeIn(big_num))
        self.play(FadeIn(small_num))
        self.wait(0.2)
        self.play(FadeIn(text_ratio), FadeIn(ratio), run_time=1.25)
        self.wait(0.5)

class Spirograph_72_48(SpirographScene):

    CONFIG = {
        'tooth_num_big': 72,
        'tooth_num_small': 48,
        'rotate_speed': TAU/360 * 0.5,
        'run_time': 16,
    }

    def add_holes(self):
        self.spirograph.hole_radius = 0.072
        self.spirograph.add_hole_by_line(hole_num=12, delta_r=0.275)

    def start_draw(self):
        self.spirograph.add_updater(self.draw_all_hole)
        self.wait(self.run_time)
