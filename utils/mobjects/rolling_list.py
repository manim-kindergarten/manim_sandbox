# from @widcardw
# !!!  only support manimgl  !!!
from manimlib import *


# class RollingList(VGroup):
#     """
#     已弃用, 因为很丑
#     """
#     def __init__(self, *vmobjects, arrange_style="vertical", **kwargs):
#         assert (len(vmobjects) > 1)
#         super().__init__(*vmobjects, **kwargs)
#         self.direction = arrange_style
#         self.current_index = 0
#         if arrange_style == 'vertical':
#             self.arrange(DOWN, aligned_edge=LEFT)
#         elif arrange_style == 'horizontal':
#             self.arrange(RIGHT, aligned_edge=DOWN)
#         else:
#             raise Exception('Rolling list only support vertical or horizontal style.')
#         self.set_opacity(0.4)
#         self[0].set_opacity(1)


class RollingList2(VGroup):
    """
    注意: 声明之后, 先调整到适当的位置, 再调用refresh_color方法以保证第一个项被高亮
    !!! 由于一些不可抗拒的原因(grant 没写重置 glsl code 上色方法), 只能上色一次 !!!
    transparent_ratio 是透明度的属性, 范围是 [0.0, 1.0], 注意一定要是浮点数, 值越大, 显示的范围越小
    """

    def __init__(self, *vmobjects, arrange_style="vertical", transparent_ratio=0.05, **kwargs):
        assert (len(vmobjects) > 1)
        super().__init__(*vmobjects, **kwargs)
        self.transparent_ratio = transparent_ratio
        self.direction = arrange_style
        self.current_index = 0
        if arrange_style == 'vertical':
            self.arrange(DOWN, aligned_edge=LEFT)
        elif arrange_style == 'horizontal':
            self.arrange(RIGHT, aligned_edge=DOWN)
        else:
            raise Exception('Rolling list only support vertical or horizontal style.')

    def refresh_color(self):
        top_item_y_pos = self[0].get_center()[1]
        self.set_color_by_code(f'''
                    color.a = smoothstep({self.transparent_ratio}, 1.0, 1.0/exp(abs(point.y - {top_item_y_pos})));
                ''')


class RollVerticallyTo2(Animation):
    CONFIG = {
        'rate_func': rush_from
    }

    def __init__(self, mobject: RollingList2, target_index, **kwargs):
        assert (mobject.direction == 'vertical')
        assert (0 <= target_index < len(mobject))
        super().__init__(mobject, **kwargs)
        self.target_index = target_index
        self.shift_height = self.get_shift_height()

    def get_shift_height(self):
        cuh = self.mobject[self.mobject.current_index].get_center()[1]
        tgh = self.mobject[self.target_index].get_center()[1]
        return cuh - tgh

    def begin(self):
        super().begin()

    def finish(self):
        super().finish()
        self.mobject.current_index = self.target_index

    def interpolate_submobject(self, submobject, starting_sumobject, alpha):
        submobject.move_to(starting_sumobject.get_center() + UP * self.shift_height * alpha)


#
# class RollVerticallyTo(RollVerticallyTo2):
#     # 本以为继承一下上面一个类就好了, 结果发现没法把refresh_color方法去掉...
#     # 然后这个方法里面又需要直接更改透明度, 结果还是不如重新开个类(其实 plan 1 是可以的...)
#     def begin(self):
#         super().begin()
#         self.mobject.set_opacity(0.4)
#
#     def finish(self):
#         super().finish()
#         self.mobject.set_opacity(0.4)
#         self.mobject[self.target_index].set_opacity(1)


# 使用例
class RollingScene(Scene):
    def construct(self):
        roll_list = RollingList2(
            Text("Hello world"),
            Text("I'm widcardw"),
            Text("Welcome to manimgl"),
            Text("Have a nice day")
        ).shift(DOWN)
        roll_list.refresh_color()
        self.add(roll_list)
        self.wait()
        self.play(RollVerticallyTo2(roll_list, 2))
        self.wait()
        self.play(RollVerticallyTo2(roll_list, 1))
