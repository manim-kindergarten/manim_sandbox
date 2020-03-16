# from @cigar666

from manimlib.imports import *

class MyBox(Cube):

    CONFIG = {
        'pos': ORIGIN,
        'box_height': 2,
        'bottom_size': [1, 1],
        'fill_opacity': 1,
    }

    def __init__(self, **kwargs):
        Cube.__init__(self, **kwargs)
        self.box_size = np.array([self.bottom_size[0], self.bottom_size[1], self.box_height])
        self.scale(self.box_size/2)
        # self.move_to(self.pos + self.box_height * OUT/2)
        self.move_to(self.pos)
        self.reset_color()

    def update_height(self, new_height):
        self.scale(np.array([1, 1, new_height/self.box_height])) #.shift(OUT * (new_height - self.height)/2)
        self.box_height = new_height

    def update_top_and_bottom(self, top, bottom):
        new_height = abs(top-bottom)
        old_center = self.get_center()
        self.update_height(new_height)
        self.shift(((top+bottom)/2 - old_center[-1]) * OUT)

    def update_top(self, top):
        bottom = self.get_center()[-1] - self.box_height/2
        self.update_top_and_bottom(top, bottom)

    def update_bottom(self, bottom):
        top = self.get_center()[-1] + self.box_height/2
        self.update_top_and_bottom(top, bottom)

    def reset_color(self):
        colors = color_gradient([WHITE, self.get_color(), BLACK], 11)
        self[0].set_fill(color=colors[8])
        self[1].set_fill(color=colors[3])
        self[2].set_fill(color=colors[8])
        self[3].set_fill(color=colors[2])
        self[4].set_fill(color=colors[5])
        self[5].set_fill(color=colors[7])

class MyBoxes(VGroup):

    CONFIG = {
        'center': ORIGIN,
        'bottom_size': [0.25, 0.25],
        'box_height': 2,
        'gap': 0,
        'fill_color': BLUE,
        'resolution': (20, 20),
    }

    def __init__(self, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.create_boxes(self.resolution)
        self.mask_array = np.zeros(self.resolution)
        self.colors = color_gradient([BLUE_D, YELLOW, RED, RED_D], 110)

    def create_boxes(self, resolution=(20, 20)):
        a, b = self.bottom_size[0] + self.gap, self.bottom_size[1] + self.gap
        m, n = resolution[0], resolution[1]
        for i in range(m):
            for j in range(n):
                box_ij = MyBox(pos=a * (j - n/2 + 1/2) * RIGHT + b * (i - m/2 + 1/2) * UP, bottom_size=self.bottom_size,
                               box_height=self.box_height, fill_color=self.fill_color)
                box_ij.reset_color()
                self.add(box_ij)

    def update_height_by_2darray(self, arr_2d):
        m, n = self.resolution[0], self.resolution[1]
        if len(arr_2d)>=m and len(arr_2d[0])>=n:
            for i in range(m):
                for j in range(n):
                    self[i*n+j].update_height(arr_2d[i, j])

    def update_height_by_func(self, func, s=1):
        for box in self:
            center = box.get_center()
            box.update_height(func(center[0], center[1]) * s)

    def update_top_and_bottom_by_2darray(self, arr_top, arr_bottom):
        m, n = self.resolution[0], self.resolution[1]
        if len(arr_top)>=m and len(arr_top[0])>=n and len(arr_bottom)>=m and len(arr_bottom[0])>=n:
            for i in range(m):
                for j in range(n):
                    self[i*n+j].update_top_and_bottom(arr_top[i, j], arr_bottom[i, j])

    def update_top_and_bottom_by_func(self, func_top, func_bottom, s=1):
        for box in self:
            center = box.get_center()
            box.update_top_and_bottom(func_top(center[0], center[1]) * s, func_bottom(center[0], center[1]) * s)

    def update_top_by_func(self, func_top, s=1):
        for box in self:
            center = box.get_center()
            box.update_top(func_top(center[0], center[1]) * s)

    def update_bottom_by_func(self, func_bottom, s=1):
        for box in self:
            center = box.get_center()
            box.update_top(func_bottom(center[0], center[1]) * s)

    def update_color_by_func(self, func):

        a, b = self.bottom_size[0] + self.gap, self.bottom_size[1] + self.gap
        m, n = self.resolution[0], self.resolution[1]
        x, y = np.linspace(-a * n/2, a * n/2, n), np.linspace(-b * m/2, b * m/2, m)
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)
        z_min, z_max = Z.min(), Z.max()
        # print(z_min, z_max)

        for box in self:
            center = box.get_center() + box.box_height/2 * OUT
            # print(int((func(center[0], center[1]) - z_min)/(z_max-z_min) * 100))
            box.set_color(self.colors[int((func(center[0], center[1]) - z_min)/(z_max-z_min) * 100)])
            box.reset_color()

    def update_color_by_2darray(self, top_array):
        Z = top_array
        m, n = self.resolution[0], self.resolution[1]
        z_min, z_max = Z.min(), Z.max()
        if len(Z) >= m and len(Z) >= n:
            for i in range(m):
                for j in range(n):
                    self[i*n+j].set_color(self.colors[int((Z[i, j] - z_min)/(z_max-z_min) * 100)])
                    self[i*n+j].reset_color()

    def set_mask_array(self, mask):
        self.mask_array = mask

    def divide_by_height(self, h_min=1e-4):
        self.high_boxes, self.short_boxes = VGroup(), VGroup()
        for box in self:
            if box.get_depth() < h_min:
                self.short_boxes.add(box)
            else:
                self.high_boxes.add(box)
        return self.high_boxes, self.short_boxes

    def get_high_boxes(self, h=1e-2):
        return self.divide_by_height(h_min=h)[0]

    def get_short_boxes(self, h=1e-2):
        return self.divide_by_height(h_min=h)[1]

    def apply_mask(self):

        m, n = self.resolution[0], self.resolution[1]
        for i in range(m):
            for j in range(n):
                if self.mask_array[i, j] == 1.: # if self.mask_array[i, j]:
                    self[i*n+j].set_fill(opacity=0)

    def set_mask_by_min_height(self, min_height):

        pass

## test MyBoxes ##

class Test_boxes(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        }
    def construct(self):

        self.set_camera_to_default_position()

        boxes = MyBoxes(fill_color=GRAY, resolution=(24, 24), bottom_size=(0.3, 0.3), gap=0.1)
        # func_01 = lambda x, y: np.sin(x ** 2 / 2.1 + y ** 2 / 2.1 + 5 * DEGREES) * 1.8 + 2.
        R = lambda x, y: np.sqrt(x ** 2 * 4 + y ** 2 * 4) + 1e-8
        func_02 = lambda u, v: 8 * np.sin(R(u, v))/R(u, v) * 0.45 - 0.2
        boxes.update_top_by_func(func_02)
        boxes.update_color_by_func(func_02)

        mask = np.zeros((24, 24))
        for i in range(24):
            for j in range(24):
                if np.sqrt((i - 11.5) ** 2 + (j - 11.5) ** 2) > 9:
                    mask[i, j] = 1

        boxes.set_mask_array(mask)
        boxes.apply_mask()

        self.add(boxes)
        self.wait(2)

class ThreeD_heart_colorful(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 64 * DEGREES,
            "theta": 30 * DEGREES,
            "distance": 100,
            },
        'camera_config': {'background_color': BLUE_A},
        }
    def construct(self):

        self.set_camera_to_default_position()
        heart_func = lambda x, y, z: (x ** 2 + 9/4 * z ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3 - 9/80 * z ** 2 * y ** 3
        m, n = 50, 50
        x, y = np.linspace(-1.6, 1.6, n+1), np.linspace(-1.6, 1.6, m+1)

        def dichotomy(func, min=0, max=3, err=1e-4):
            if func(min) * func(max) > 0:
                return 0
            else:
                while max - min > err:
                    mid = (max + min)/2
                    if func(min) * func(mid) <= 0:
                        max = mid
                    else:
                        min = mid
                return (max + min)/2
        z = np.zeros((m+1, n+1))
        for i in range(m+1):
            for j in range(n+1):
                z[i, j] = dichotomy(lambda z: heart_func(x[j], y[i], z)) * 2
        z *= 2.5
        print(z)
        heart_by_boxes = MyBoxes(fill_color=average_color(RED, PINK), resolution=(m+1, n+1), bottom_size=(0.15, 0.15), gap=0)
        heart_by_boxes.update_height_by_2darray(z)
        heart_by_boxes.update_color_by_func(lambda x, y: np.sin((x ** 2 + y ** 2)/12))
        heart = heart_by_boxes.get_high_boxes()
        heart.rotate(PI/2)
        heart.rotate(PI/2, axis=UP)
        heart.scale(1.5).shift(OUT * 0.4)

        text = Text('@bilibili cigar666', font='思源黑体 Bold', color=PINK).set_height(0.6).shift(DOWN * 5.)

        self.camera.add_fixed_in_frame_mobjects(text)
        self.add(heart, text)
        self.play(Rotating(heart, run_time=6))
        # self.wait()

