# from @cigar666

from manimlib.imports import *

class Cube_array(VGroup):

    CONFIG = {
        'center': ORIGIN,
        'cube_size': 0.5,
        'gap': 0,
        'fill_color': BLUE,
        'fill_opacity': 1,
        'stroke_color': WHITE,
        'stroke_width': 0,
        'resolution': (4, 4, 1),
        # 'mask_array': None,
        # 'reset_color': True,

    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.create_cubes()
        self.faces = self.get_all_faces()
        # self.classify_faces()
        self.move_to(self.center)
        self.get_outer_faces()

    def create_cubes(self):
        size, gap = self.cube_size, self.gap
        u, v, w = self.resolution[0], self.resolution[1], self.resolution[2]
        for i in range(u):
            for j in range(v):
                for k in range(w):
                    # box_ijk = MyBox(pos=(size + gap) * ((j - v/2 + 1/2) * RIGHT + (i - u/2 + 1/2) * UP + (k - w/2 + 1/2) * OUT),
                    #                 bottom_size=[size, size], box_height=size, fill_color=self.fill_color,
                    #                 opacity=self.fill_opacity, stroke_color=self.stroke_color, stroke_width=self.stroke_width)
                    box_ijk = Cube(side_length=size, fill_color=self.fill_color, opacity=self.fill_opacity,
                                   stroke_color=self.stroke_color, stroke_width=self.stroke_width)
                    box_ijk.shift((size + gap) * ((j - v/2 + 1/2) * RIGHT + (i - u/2 + 1/2) * UP + (k - w/2 + 1/2) * OUT))

                    # if self.reset_color:
                    #     box_ijk.reset_color()
                    self.add(box_ijk)

    def scale_each_cube(self, scale_factor):
        for cube in self:
            cube.scale(scale_factor)

    def rotate_each_cube(self, angle, axis=OUT, **kwargs):
        for cube in self:
            cube.rotate(angle, axis=OUT, **kwargs)

    def get_all_faces(self):
        faces = VGroup()
        for cube in self:
            faces.add(*cube)
        return faces

    def get_faces_by_range(self, max, min, dim=3):
        max, min = (min, max) if max < min else (max, min)
        faces = VGroup()
        for face in self.faces:
            if face.get_center()[dim-1] <= max and face.get_center()[dim-1] >= min:
                faces.add(face)
        return faces

    def get_top_face(self, err=1e-3):
        a = self.get_zenith()[2]
        self.top_faces = self.get_faces_by_range(a+err, a-err, dim=3)
        return self.top_faces

    def get_bottom_face(self, err=1e-3):
        a = self.get_nadir()[2]
        self.bottom_faces = self.get_faces_by_range(a+err, a-err, dim=3)
        return self.bottom_faces

    def get_front_face(self, err=1e-3):
        a = self.get_bottom()[1]
        self.front_faces = self.get_faces_by_range(a+err, a-err, dim=2)
        return self.front_faces

    def get_back_face(self, err=1e-3):
        a = self.get_top()[1]
        self.back_faces = self.get_faces_by_range(a+err, a-err, dim=2)
        return self.back_faces

    def get_left_face(self, err=1e-3):
        a = self.get_left()[0]
        self.left_faces = self.get_faces_by_range(a+err, a-err, dim=1)
        return self.left_faces

    def get_right_face(self, err=1e-3):
        a = self.get_right()[0]
        self.right_faces = self.get_faces_by_range(a+err, a-err, dim=1)
        return self.right_faces

    def classify_faces(self):

        # max_or_min = np.array([self.get_top()[1], self.get_bottom()[1], self.get_right()[0], self.get_left()[0],
        #               self.get_zenith()[2], self.get_nadir()[2]])
        max_or_min = np.array([self.get_top()[1], self.get_bottom()[1], self.get_right()[0], self.get_left()[0],
                      self.get_zenith()[2], self.get_nadir()[2]])
        print(max_or_min)
        self.outer_faces, self.inner_faces = VGroup(), VGroup()
        err = 1e-4 * self.cube_size ** 2
        for face in self.faces:
            x, y, z = face.get_center()[0], face.get_center()[1], face.get_center()[2]

            a = abs((max_or_min - x) * (max_or_min - y) * (max_or_min - z))
            print('before:', abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/self.cube_size ** 6)
            if abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/(self.cube_size/2) ** 6 < err:
                print('outer:', abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/self.cube_size ** 6)
                self.outer_faces.add(face)
            else:
                print('inner:', abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/self.cube_size ** 6)
                self.inner_faces.add(face)

            # a0 = abs(max_or_min - x)[0] * abs(max_or_min - x)[1]
            # a1 = abs(max_or_min - y)[2] * abs(max_or_min - y)[3]
            # a2 = abs(max_or_min - z)[4] * abs(max_or_min - z)[5]
            # if a0 < err or a1 < err or a2 < err:
            #     self.outer_faces.add(face)
            #     print('outer')
            # else:
            #     print('inner')
            #     self.inner_faces.add(face)
        # return self.outer_faces, self.inner_faces

    def get_outer_faces(self):
        self.outer_faces = VGroup(self.get_top_face(), self.get_bottom_face(),
                                  self.get_front_face(), self.get_back_face(),
                                  self.get_left_face(), self.get_right_face())
        return self.outer_faces

    # def get_innter_faces(self):
    #     return self.inner_faces

class Rubik_Cube(Cube_array):

    CONFIG = {
        'colors': [GREEN, BLUE_D, WHITE, YELLOW, RED_D, ORANGE],
    }

    def __init__(self, size=3, order=3, base_color=LIGHT_GREY, **kwargs):
        Cube_array.__init__(self, cube_size=size/order, resolution=(order, order, order), fill_color=base_color, fill_opacity=1, **kwargs)
        self.scale_each_cube(0.9)
        self.order = order
        self.size = size
        self.setup_color()

    def setup_color(self):
        self.top_faces.set_color(self.colors[0])
        self.bottom_faces.set_color(self.colors[1])
        self.front_faces.set_color(self.colors[2])
        self.back_faces.set_color(self.colors[3])
        self.left_faces.set_color(self.colors[4])
        self.right_faces.set_color(self.colors[5])

    def get_layer(self, layer=[1], dim=3):
        faces = VGroup()
        if type(layer) == int:
            a = self.size/2 - 0.5 * self.cube_size - (layer-1) * self.cube_size
            faces.add(self.get_faces_by_range(a + self.cube_size/2, a - self.cube_size/2, dim=dim))

        else:
            for i in layer:
                a = self.size/2 - 0.5 * self.cube_size - (i-1) * self.cube_size
                faces.add(self.get_faces_by_range(a + self.cube_size/2, a - self.cube_size/2, dim=dim))
        return faces
