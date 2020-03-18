# from @鹤翔万里

from manimlib.imports import *
from manim_sandbox.utils.mobjects.MyBoxes import MyBox, MyBoxes

class PeriodicTable(VGroup):
    CONFIG = {
        'center': ORIGIN,
        'bottom_size': (0.45, 0.6),
        'box_height': 0.4,
        'gap': 0,
        'fill_color': BLUE,
        'shade_in_3d': False
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.id_to_pos = [
            0, 144, 161,
            126, 127, 138, 139, 140, 141, 142, 143,
            108, 109, 120, 121, 122, 123, 124, 125,
            *list(range(90, 108)),
            *list(range(72, 90)),
            54, 55,
            *list(range(20, 35)),
            *list(range(57, 72)),
            36, 37,
            *list(range(2, 17)),
            *list(range(39, 54))
        ]
        self.create_boxes()
        self.mask_array = np.zeros((9, 18))
        self.colors = color_gradient([BLUE_D, YELLOW, RED, RED_D], 110)
    
    def create_boxes(self):
        pos = MyBoxes(resolution=(9, 18), bottom_size=self.bottom_size, gap=0.15, box_height=0.4)
        boxes = VGroup()
        for i in range(0, 119):
            box = MyBox(pos=pos[self.id_to_pos[i]].get_center(), bottom_size=self.bottom_size,
                        box_height=self.box_height, fill_color=self.fill_color)
            box.reset_color()
            boxes.add(box)
        boxes[0].set_fill(opacity=0)
        self.add(boxes)
    
    def add_label(self):
        self.id_to_label = [
            "0", "H", "He",
            "Li", "Be", "B", "C", "N", "O", "F", "Ne",
            "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
            "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
            "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
            "Cs", "Ba",
            "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
            "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
            "Fr", "Ra",
            "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
            "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
        ]
        self.label_to_id = {}
        for i, label in enumerate(self.id_to_label):
            self.label_to_id[label] = i
        labels = VGroup()
        for i in range(0, 119):
            label = TextMobject(self.id_to_label[i], color=BLACK, background_stroke_width=0)
            label.scale(0.5).move_to(self[0][i][1].get_center()).set_shade_in_3d(z_index_as_group=True).shift(OUT * 1e-3)
            labels.add(label)
        labels[0].set_fill(opacity=0)
        for i in [43, 61, *list(range(84, 119))]:
            labels[i].set_color(RED)
        self.add(labels)
        return self
    
    def set_block_color(self):
        colors = [PURPLE_E, PURPLE, PINK, ORANGE, YELLOW, GOLD, BLUE, GREEN_B, GREEN]
        self.id_to_color_id = [
            0, 0, 2,
            0, 1, 4, 4, 4, 4, 3, 2,
            0, 1, 5, 4, 4, 4, 3, 2,
            0, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 4, 4, 3, 2,
            0, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 4, 3, 2,
            0, 1,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 3, 2,
            0, 1,
            8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 3, 2
        ]
        for i in range(0, 119):
            self[0][i].set_color(colors[self.id_to_color_id[i]]).reset_color()
        return self
    
    def set_height_by_array(self, h):
        for i in range(1, 119):
            if h[i] == 0.25:
                self[0][i].update_top_and_bottom(0.1, 0)
            else:
                self[0][i].update_top_and_bottom(h[i], 0)
