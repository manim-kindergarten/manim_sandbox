from manimlib.constants import *
from manimlib.mobject.geometry import Circle
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.svg.tex_mobject import TexText
from manimlib.mobject.svg.brace import Brace
from manimlib.utils.config_ops import digest_config


class Tree_Diagram(VGroup):
    CONFIG = {
        "style": None,
        "branch_color": GREY,
        "branch_opacity": 1,
        "branch_stroke_width": 3,  # for specified style
        "branch_buff": 0.1,  # for specified style
        "branch_h_buff": 0.5,
        "item_v_buff": 0.3,
        "item_scale": 0.7,
    }

    def __init__(self, tree_dict, **kwargs):
        digest_config(self, kwargs)
        self.tree_dict = tree_dict
        VGroup.__init__(self, **kwargs)

        if self.style == None:
            self.add(self.recursive_generate_brace_style(tree_dict)[1])

        else:
            self.add(*self.recursive_generate_line_style(tree_dict)[1])

    def get_lowest_vgroup(self, set):
        return VGroup(*[TexText(i).scale(self.item_scale) for i in set]).arrange(DOWN, buff=self.item_v_buff, aligned_edge=LEFT)

    def recursive_generate_brace_style(self, tree_dict):
        
        if len(tree_dict) == 0:
            return VGroup(Circle(radius=0))
        # TODO better way to handle empty set

        elif isinstance(tree_dict, set):
            a = self.get_lowest_vgroup(tree_dict)
            return VGroup(Brace(a, LEFT, buff=self.branch_buff/2).set_style(fill_color=self.branch_color, fill_opacity=self.branch_opacity), a)

        else:
            vg = VGroup()
            
            for i in tree_dict:
                a = self.recursive_generate_brace_style(tree_dict[i])
                
                if i == "~":
                    b = VGroup(Circle(radius=0).next_to(
                        a[0], LEFT, buff=self.branch_buff/2), a)
                # TODO better way to handle "~"

                else:
                    b = VGroup(TexText(i).scale(self.item_scale).next_to(
                        a[0], LEFT, buff=self.branch_buff/2), a)
                vg.add(b)

            vg.arrange(DOWN, buff=self.item_v_buff, aligned_edge=LEFT)
            to_be_braced = VGroup(*[i[0] for i in vg])

            return VGroup(Brace(to_be_braced, LEFT, buff=self.branch_buff/2).set_style(fill_color=self.branch_color, fill_opacity=self.branch_opacity), vg)

    def recursive_generate_line_style(self, tree_dict):

        if len(tree_dict) == 0:
            return VGroup(Circle(radius=0)).set_opacity(0)
        # TODO better way to handle empty set

        elif isinstance(tree_dict, set):
            a = self.get_lowest_vgroup(tree_dict)
            return VGroup(
                VGroup(
                    *[self.style(a.get_left() + self.branch_h_buff*5/6*LEFT, i.get_left() + self.branch_h_buff*1/6*LEFT, buff=0.1) for i in a]
                ).set_style(stroke_color=self.branch_color, stroke_opacity=self.branch_opacity), a)

        else:
            vg = VGroup()

            for i in tree_dict:
                a = self.recursive_generate_line_style(tree_dict[i])

                if len(a) == 1:
                    coord = a.get_center()

                else:
                    coord = a[0][0].get_start() - 0.1*a[0][0].get_vector()

                if i == "~":
                    b = VGroup(Circle(radius=0).next_to(
                        coord, LEFT, buff=self.branch_h_buff/6), a)
                # TODO better way to handle "~"
                
                else:
                    b = VGroup(TexText(i).scale(self.item_scale).next_to(
                        coord, LEFT, buff=self.branch_h_buff/6), a)
                vg.add(b)
            vg.arrange(DOWN, buff=self.item_v_buff, aligned_edge=LEFT)
            to_be_braced = VGroup(*[i[0] for i in vg])

            return VGroup(
                VGroup(
                    *[self.style(to_be_braced.get_left() + self.branch_h_buff*5/6*LEFT, i.get_left() + self.branch_h_buff*1/6*LEFT, buff=0.1) for i in to_be_braced]
                ).set_style(stroke_color=self.branch_color, stroke_opacity=self.branch_opacity), vg)
