# from widcardw
#
#
# 这个Border写的太草了...
# CtrlT是会自动更新的, 只要传入一个物件, 就可以像TrackedPath一样用
# 但是我感觉不是特别好, 还不如用下面那个NoneUpdate的, 加个lambda become岂不美哉
# 或许对于作业4有点帮助吧
# 还有, 不许吐槽我为什么不用for循环, 我本来就只会硬刚
# 说不定今后有时间再加一个center_point呢

from manimlib.imports import *
class CtrlT(VGroup):
    CONFIG = {"buff": SMALL_BUFF, "black_bg": False,
              "add_corner": True}

    def __init__(self, obj, **kwargs):
        VGroup.__init__(self, **kwargs)
        if not self.black_bg:
            border = Rectangle(width=4, height=2).add_updater(
                lambda b: b.become(Rectangle(width=obj.get_width()+2*self.buff, height=obj.get_height()+2*self.buff,
                                             stroke_width=1, stroke_color="#000000").move_to(obj.get_center())))
            corner_group = VGroup()
            if self.add_corner:
                dot_0 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#ffffff", stroke_width=1,
                        stroke_color="#000000").move_to(border.get_vertices()[0])
                ))
                dot_1 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#ffffff", stroke_width=1,
                        stroke_color="#000000").move_to(border.get_vertices()[1])
                ))
                dot_2 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#ffffff", stroke_width=1,
                        stroke_color="#000000").move_to(border.get_vertices()[2])
                ))
                dot_3 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#ffffff", stroke_width=1,
                        stroke_color="#000000").move_to(border.get_vertices()[3])
                ))
                corner_group.add(dot_0, dot_1, dot_2, dot_3)
        else:
            border = Rectangle(width=obj.get_width()+2*self.buff, height=obj.get_height()+2*self.buff,
                               stroke_color="#ffffff", stroke_width=1).add_updater(
                lambda b: b.move_to(obj.get_center())
            )
            corner_group = VGroup()
            if self.add_corner:
                dot_0 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#000000", stroke_width=1,
                        stroke_color="#ffffff").move_to(border.get_vertices()[0])
                ))
                dot_1 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#000000", stroke_width=1,
                        stroke_color="#ffffff").move_to(border.get_vertices()[1])
                ))
                dot_2 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#000000", stroke_width=1,
                        stroke_color="#ffffff").move_to(border.get_vertices()[2])
                ))
                dot_3 = Dot().add_updater(lambda d: d.become(
                    Dot(color="#000000", stroke_width=1,
                        stroke_color="#ffffff").move_to(border.get_vertices()[3])
                ))
                corner_group.add(dot_0, dot_1, dot_2, dot_3)
        self.add(border, corner_group)


class BorderNoneUpdate(VGroup):
    CONFIG = {"buff": SMALL_BUFF, "black_bg": False,
              "add_corner": True}

    def __init__(self, obj, **kwargs):
        VGroup.__init__(self, **kwargs)
        if not self.black_bg:
            border = Rectangle(width=obj.get_width()+2*self.buff, height=obj.get_height()+2*self.buff,
                               stroke_width=1, stroke_color="#000000").move_to(obj.get_center())
            corner_group = VGroup()
            if self.add_corner:
                dot_0 = Dot(color="#ffffff", stroke_width=1,
                            stroke_color="#000000").move_to(border.get_vertices()[0])
                dot_1 = Dot(color="#ffffff", stroke_width=1,
                            stroke_color="#000000").move_to(border.get_vertices()[1])
                dot_2 = Dot(color="#ffffff", stroke_width=1,
                            stroke_color="#000000").move_to(border.get_vertices()[2])
                dot_3 = Dot(color="#ffffff", stroke_width=1,
                            stroke_color="#000000").move_to(border.get_vertices()[3])
                corner_group.add(dot_0, dot_1, dot_2, dot_3)
        else:
            border = Rectangle(width=obj.get_width()+2*self.buff, height=obj.get_height()+2*self.buff,
                               stroke_width=1, stroke_color="#ffffff").move_to(obj.get_center())
            corner_group = VGroup()
            if self.add_corner:
                dot_0 = Dot(color="#000000", stroke_width=1,
                            stroke_color="#ffffff").move_to(border.get_vertices()[0])
                dot_1 = Dot(color="#000000", stroke_width=1,
                            stroke_color="#ffffff").move_to(border.get_vertices()[1])
                dot_2 = Dot(color="#000000", stroke_width=1,
                            stroke_color="#ffffff").move_to(border.get_vertices()[2])
                dot_3 = Dot(color="#000000", stroke_width=1,
                            stroke_color="#ffffff").move_to(border.get_vertices()[3])
                corner_group.add(dot_0, dot_1, dot_2, dot_3)
        self.add(border, corner_group)

