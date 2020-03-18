# from @cigar666

"""
注：
1.这个类用来创建一个轮廓形状产生的阴影（有边缘的模糊效果）
2.这个类尚不完善，对圆形、接近圆的椭圆和多边形等效果还凑合，对于其他形状可能和预期的阴影效果不一样
3.本质上是一个渐变效果，所以通过改动CONFIG或其他参数可以用来表示其他类似渐变效果
"""
from manimlib.imports import *

class Shadow_around(VGroup):

    CONFIG = {
        'shadow_color': DARK_GRAY,
        'shadow_opacity': 0.6,
        'blur_width': 0.25,
        'layer_num': 40,
        'scale_factor': 1,
        'shadow_out': True,
        'show_basic_shape': True,
        'plot_depth': -1,
        'rate_func': lambda t: t ** 0.5,
    }

    def __init__(self, mob_or_points, **kwargs):
        VGroup.__init__(self, **kwargs)

        if type(mob_or_points) == list:
            self.shape = Polygon(*mob_or_points, stroke_width=0, plot_depth=-1)
        else:
            self.shape = mob_or_points.set_stroke(width=0)

        self.shape.set_fill(color=self.shadow_color, opacity=self.shadow_opacity * (1 if self.show_basic_shape else 0)).scale(self.scale_factor)
        self.blur_outline = VGroup()
        s = (self.shape.get_height() + self.shape.get_width())/2
        if self.blur_width > 1e-4:
            for i in range(self.layer_num):
                layer_i = self.shape.copy().set_stroke(color=self.shadow_color, width=51 * self.blur_width/self.layer_num, opacity=self.shadow_opacity * (1-self.rate_func(i/self.layer_num))).\
                    set_fill(opacity=0).scale((s + (1 if self.shadow_out else -1) * self.blur_width/self.layer_num * (i+0.5))/ s).set_plot_depth(-2)
                self.blur_outline.add(layer_i)
        self.add(self.shape, self.blur_outline)

class Test_Shadow(Scene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
    }
    def construct(xgnb): # 'xgnb' can be replaced by 'self'
        num=8
        colors = color_gradient([RED, PINK, BLUE, GREEN, YELLOW, ORANGE], num)
        s = 0.6
        circles = VGroup(*[Circle(radius=s * (i+0.6)) for i in range(num * 2)])
        shadows_out = VGroup(*[Shadow_around(circles[i*2], blur_width=0.5 * s, shadow_color=BLACK, layer_num=50, show_basic_shape=False, shadow_out=True) for i in range(num)], plot_depth=1)
        shadows_in = VGroup(*[Shadow_around(circles[i*2+1], blur_width=0.5 * s, shadow_color=BLACK, layer_num=50, show_basic_shape=False, shadow_out=False) for i in range(num-1)], plot_depth=1)
        annulus_group = VGroup(*[Annulus(inner_radius=s * (2 * i - 1 + 0.6), outer_radius=s * (2 * i + 0.6), fill_color=colors[i], fill_opacity=1, stroke_width=0, plot_depth=-5) for i in range(1, num)])
        circle = Circle(radius=0.6 * s, stroke_width=0, fill_color=colors[0], fill_opacity=1, plot_depth=1)

        xgnb.add(shadows_out, shadows_in, annulus_group, circle)
        xgnb.wait(5)

class Test_Shadow_02(Scene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
    }
    def construct(xgnb): # 'xgnb' can be replaced by 'self'
        num = 2
        s = 0.9
        circles = VGroup(*[Circle(radius=s * (i+0.6)) for i in range(num * 2)])
        shadows_out = VGroup(*[Shadow_around(circles[i], blur_width=0.54 * s, shadow_color=BLACK, layer_num=50, show_basic_shape=False, shadow_out=True) for i in range(num)], plot_depth=1)
        shadows_in = VGroup(*[Shadow_around(circles[i+num], blur_width=0.54 * s, shadow_color=BLACK, layer_num=50, show_basic_shape=False, shadow_out=False) for i in range(num)], plot_depth=1)
        xgnb.add(shadows_out, shadows_in)
        xgnb.wait(5)
