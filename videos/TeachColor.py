# from @鹤翔万里
# manim教程第三期 - 颜色的表示及相关函数

from manimlib.imports import *
from manim_sandbox.utils.imports import *
from manim_projects.tony_useful.imports import *


class ColorText(Text):
    CONFIG = {
        "size": 0.4,
        "font": "Consolas",
        "t2c": {
            '"': YELLOW_E,
            'np': BLACK,
            'array': BLUE_D,
            '~': WHITE
        },
        "color": DARK_GRAY,
    }
    def __init__(self, color, name=None, **kwargs):
        if name:
            Text.__init__(self, name, color=color, **kwargs)
        else:
            if isinstance(color, str):
                Text.__init__(self, '"' + color + '"', color=color, **kwargs)
            elif color[0] > 1 or color[1] > 1 or color[2] > 1:
                name = 'np.array([{},~{},~{}])'.format(
                    str(int(color[0])).rjust(3, "~"), 
                    str(int(color[1])).rjust(3, "~"), 
                    str(int(color[2])).rjust(3, "~")
                )
                Text.__init__(self, name, color=rgb_to_color(color/255), **kwargs)
                self[10:name.index(",")].set_color(RED)
                self[name.index(",")+2:name.index(",", name.index(",")+1)].set_color(GREEN)
                self[name.index(",", name.index(",")+1)+2:-2].set_color(BLUE)
                self.set_color_by_t2c({"~": WHITE})
            else:
                name = 'np.array([{:.1f},~{:.1f},~{:.1f}])'.format(color[0], color[1], color[2])
                Text.__init__(self, name, **kwargs)
                self[10:name.index(",")].set_color(RED)
                self[name.index(",")+2:name.index(",", name.index(",")+1)].set_color(GREEN)
                self[name.index(",", name.index(",")+1)+2:-2].set_color(BLUE)
                self.set_color_by_t2c({"~": WHITE})


class TestColor(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        color = VGroup(
            ColorText(RED_C, "RED_C"),
            ColorText("#66CCFF"),
            ColorText(np.array([255, 165, 0])),
        ).arrange(DOWN)
        test = Text("test", font="Consolas").set_color(rgb_to_color(np.array([255/255, 165/255, 0])))
        self.add(color)    


class CodeLine(Text):
    CONFIG = {
        't2c': {
            'x': average_color(BLUE, PINK),
            'y': average_color(BLUE, PINK),
            'z': average_color(BLUE, PINK),
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'IN': ORANGE,
            'OUT': ORANGE,
            'ORIGIN': ORANGE,
            'DL': ORANGE,
            'DR': ORANGE,
            'UL': ORANGE,
            'UR': ORANGE,
            'TOP': ORANGE,
            'BOTTOM': ORANGE,
            'LEFT_SIDE': ORANGE,
            'RIGHT_SIDE': ORANGE,
            'manim': GOLD,
            'constants.py': GOLD,
            'manimlib/utils/color.py': GOLD,
            '#': GOLD,
            '_C': BLUE,
            'BLUE_C': BLUE,
            'BLUE': BLUE,
            'GREEN': GREEN,
            'YELLOW': YELLOW,
            'RED': RED,
            'RGB': PURPLE,
            'RGBA': PURPLE,
            'rgb': PURPLE,
            'int_rgb': PURPLE,
            'hex': PURPLE,
            'Color': GREEN,
            'FRAME_HEIGHT': BLUE_D,
            'FRAME_WIDTH': BLUE_D,
            'PIXEL_HEIGHT': RED_B,
            'PIXEL_WIDTH': RED_B,
            'np': BLACK,
            'array': BLUE_D,
            'ndarray': BLUE,
            'FadeIn': average_color(RED, ORANGE),
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'arrange': BLUE_D,
            'VGroup': BLUE_D,
            'VMobject': BLUE_D,
            'ImageMobject': BLUE_D,
            'Mobject': BLUE_D,
            'list': BLUE_D,
            'append': BLUE_D,
            'remove': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'GREY_BROWN': GREY_BROWN,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'add_to_back': BLUE_D,
            'vector': ORANGE,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            'aligned_edge': RED,
            'center': RED,
            'radius': RED,
            ">>>": RED,
            'coor_mask': RED,
            'point_or_mobject': RED,
            'python': GOLD,
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'True': average_color(BLUE, PINK),
            '2D': RED_B,
            '3D': RED_B,
            'self': PINK,
            'mob': RED_D,
            'mob1': RED_D,
            'mob2': RED_D,
            'mob3': RED_D,
            'mob0': RED_D,
            "~": "#EBEBEB",
            "vg2": DARK_GRAY,
            'hex_to_rgb': BLUE_D,
            'rgb_to_hex': BLUE_D,
            'color_to_rgb': BLUE_D,
            'rgb_to_color': BLUE_D,
            'color_to_int_rgb': BLUE_D,
            'get_hex_l': BLUE_D,
            'invert_color': BLUE_D,
            'interpolate_color': BLUE_D,
            'average_color': BLUE_D,
            'color_gradient': BLUE_D,
            'random_color': BLUE_D,
            'alpha': GOLD,
            '#6cf': "#66CCFF",
            '#66CCFF': "#66CCFF",
            '#930': "#993300",
            '#9da288': "#9da288",
            'style': PURPLE,
            'stroke': BLUE_D,
            'fill': BLUE_D,
            'background_stroke': BLUE_D,
            'opacity': BLUE_D,
            'set_color': BLUE_D,
            'set_fill': BLUE_D,
            'set_background_stroke': BLUE_D,
            "stroke_color": ORANGE,
            "stroke_opacity": ORANGE,
            "fill_color": ORANGE,
            "fill_opacity": ORANGE,
            "background_stroke_color": ORANGE,
            "background_stroke_opacity": ORANGE,
            "set_color_by_gradient": BLUE_D,
            "set_colors_by_radial_gradient": BLUE_D,
            "outer_color": RED,
            "set_sheen_direction": BLUE_D,
            "set_sheen": BLUE_D,
            "sheen": BLUE_D,
        },
        'font': 'Consolas',
        'size': 0.36,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }
    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class DecimalNumberText(VMobject):
    CONFIG = {
        "num_decimal_places": 2,
        "include_sign": False,
        "group_with_commas": True,
        "digit_to_digit_buff": 0.05,
        "show_ellipsis": False,
        "unit": None,  # Aligned to bottom unless it starts with "^"
        "include_background_rectangle": False,
        "edge_to_fix": LEFT,
        "text_config": {
            "font": "Consolas",
            "size": 0.4,
            "color": GOLD,
        }
    }

    def __init__(self, number=0, **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.initial_config = kwargs

        if isinstance(number, complex):
            formatter = self.get_complex_formatter()
        else:
            formatter = self.get_formatter()
        num_string = formatter.format(number)

        rounded_num = np.round(number, self.num_decimal_places)
        if num_string.startswith("-") and rounded_num == 0:
            if self.include_sign:
                num_string = "+" + num_string[1:]
            else:
                num_string = num_string[1:]

        self.add(*[
            Text(char, **kwargs, **self.text_config)
            for char in num_string
        ])

        # Add non-numerical bits
        if self.show_ellipsis:
            self.add(Text("...", **self.text_config))

        if num_string.startswith("-"):
            minus = self.submobjects[0]
            minus.next_to(
                self.submobjects[1], LEFT,
                buff=self.digit_to_digit_buff
            )

        if self.unit is not None:
            self.unit_sign = Text(self.unit, color=self.color, **self.text_config)
            self.add(self.unit_sign)

        self.arrange(
            buff=self.digit_to_digit_buff,
            aligned_edge=DOWN
        )

        # Handle alignment of parts that should be aligned
        # to the bottom
        for i, c in enumerate(num_string):
            if c == "-" and len(num_string) > i + 1:
                self[i].align_to(self[i + 1], UP)
                self[i].shift(self[i+1].get_height() * DOWN / 2)
            elif c == ",":
                self[i].shift(self[i].get_height() * DOWN / 2)
        if self.unit and self.unit.startswith("^"):
            self.unit_sign.align_to(self, UP)
        #
        if self.include_background_rectangle:
            self.add_background_rectangle()

    def get_formatter(self, **kwargs):
        """
        Configuration is based first off instance attributes,
        but overwritten by any kew word argument.  Relevant
        key words:
        - include_sign
        - group_with_commas
        - num_decimal_places
        - field_name (e.g. 0 or 0.real)
        """
        config = dict([
            (attr, getattr(self, attr))
            for attr in [
                "include_sign",
                "group_with_commas",
                "num_decimal_places",
            ]
        ])
        config.update(kwargs)
        return "".join([
            "{",
            config.get("field_name", ""),
            ":",
            "+" if config["include_sign"] else "",
            "," if config["group_with_commas"] else "",
            ".", str(config["num_decimal_places"]), "f",
            "}",
        ])

    def get_complex_formatter(self, **kwargs):
        return "".join([
            self.get_formatter(field_name="0.real"),
            self.get_formatter(field_name="0.imag", include_sign=True),
            "i"
        ])

    def set_value(self, number, **config):
        full_config = dict(self.CONFIG)
        full_config.update(self.initial_config)
        full_config.update(config)
        new_decimal = DecimalNumberText(number, **full_config)
        # Make sure last digit has constant height
        new_decimal.scale(
            self[-1].get_height() / new_decimal[-1].get_height()
        )
        new_decimal.move_to(self, self.edge_to_fix)
        new_decimal.match_style(self)

        old_family = self.get_family()
        self.submobjects = new_decimal.submobjects
        for mob in old_family:
            # Dumb hack...due to how scene handles families
            # of animated mobjects
            mob.points[:] = 0
        self.number = number
        return self

    def get_value(self):
        return self.number

    def increment_value(self, delta_t=1):
        self.set_value(self.get_value() + delta_t)


class TestDecimalNumberText(Scene):
    def construct(self):
        decimal = DecimalNumberText(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()



class Scene_(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }


class OpeningScene(Scene_):
    def construct(self):
        t2c = {"manim": average_color(PINK, RED),
               "颜色": ORANGE}
        text_color = DARK_GRAY

        font = "PangMenZhengDao"
        text_1 = Text("大家好!", font=font, color=text_color, size=1, t2c=t2c).to_edge(UP * 2, buff=1)
        text_2 = Text("欢迎来到manim视频教程", font=font,
                      color=text_color, size=1, t2c=t2c).to_edge(UP * 3.2, buff=1)
        text_3 = Text("这一期我们将学习manim中", font=font, color=text_color, size=1, t2c=t2c).to_edge(UP * 1.8, buff=1)
        text_4 = Text("颜色的表示和相关方法", font=font, color=text_color, size=1, t2c=t2c).to_edge(UP * 3., buff=1)
        text_34, text_12 = VGroup(text_3, text_4), VGroup(text_1, text_2)


        methods = [['Color', 'constants', 'hex', 'RGB'],
                   ['color_to_rgb', 'rgb_to_color', 'rgb_to_hex', 'hex_to_rgb'],
                   ['invert_color, ', 'color_gradient, ', 'average_color, ', 'random_color,'],
                   ['set_color, ', 'set_color_by_gradient, ', 'set_sheen']]
        m_group_1 = VGroup(*[Text(tex + ', ', size=0.42, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[0]]).arrange(RIGHT)
        m_group_2 = VGroup(*[Text(tex + ', ', size=0.42, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[1]]).arrange(RIGHT)
        m_group_3 = VGroup(*[Text(tex, size=0.42, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[2]]).arrange(RIGHT)
        m_group_4 = VGroup(*[Text(tex, size=0.42, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[3]]).arrange(RIGHT)
        m_group = VGroup(m_group_1, m_group_2, m_group_3, m_group_4).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        methodes_group = VGroup(*m_group_1, *m_group_2, *m_group_3, *m_group_4).next_to(text_34, DOWN, buff=0.5)

        # self.add(picture)
        self.wait(0.5)
        self.play(Write(text_1))
        self.wait(0.5)
        self.play(WriteRandom(text_2), run_time=1.5)
        self.wait(1.8)
        self.play(ReplacementTransform(text_12, text_34), run_time=1.2)
        self.wait(1.2)
        self.play(FadeInRandom(methodes_group), run_time=2.4)
        self.wait(2.6)
        self.play(FadeOutRandom(methodes_group), FadeOutRandom(text_3),
                  FadeOutRandom(text_4), run_time=1.8)
        self.wait(1)


class ExpressAColor(Scene_):
    def start(self):
        t2c = {"manim": GOLD,
               "颜色": ORANGE}
        title = VGroup(
            Text("Chapter Ⅰ.", font="Monaco for Powerline", color=BLUE_D, size=0.5, t2c=t2c),
            Text("manim中颜色的表示", font="Source Han Sans CN Bold", color=DARK_GRAY, size=0.5, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "在manim中,颜色使用RGB模式",
            "可以用定义的常量、十六进制和RGB数组来表示",
            "constants.py中定义了这54种颜色常量,可以直接使用",
            "以_C结尾的也可以省去_C,例如BLUE_C也可写作BLUE",
            "所有的GRAY也可写作GREY(GREY_BROWN除外)",
            "也可以使用十六进制来表示颜色",
            "具体为一个字符串,以#开头,后接六位十六进制颜色(hex)",
            "也可以使用一个ndarray来表示RGB颜色",
            "并使用相应方法转化为hex或Color(后面会讲)",
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        
        colors = VGroup(
            VGroup(
                *[
                    VGroup(
                        *[
                            ColorText(color, name) for name, color in list(COLOR_MAP.items())[i:i + 5]
                        ]
                    ).arrange(DOWN, aligned_edge=LEFT)
                    for i in range(3, 43, 5)
                ]
            ).arrange(RIGHT),
            VGroup(
                VGroup(
                    *[
                        ColorText(color, name) for name, color in list(COLOR_MAP.items())[:3]
                    ]
                ).arrange(DOWN, aligned_edge=LEFT),
                VGroup(
                    *[
                        ColorText(color, name) for name, color in list(COLOR_MAP.items())[43:46]
                    ]
                ).arrange(DOWN, aligned_edge=LEFT),
                VGroup(
                    *[
                        ColorText(color, name) for name, color in list(COLOR_MAP.items())[47:52:2]
                    ]
                ).arrange(DOWN, aligned_edge=LEFT),
                VGroup(
                    *[
                        ColorText(color, name) for name, color in list(COLOR_MAP.items())[53:56]
                    ]
                ).arrange(DOWN, aligned_edge=LEFT),
                VGroup(
                    *[
                        ColorText(color, name) for name, color in list(COLOR_MAP.items())[-2:]
                    ]
                ).arrange(DOWN, aligned_edge=LEFT),
            ).arrange(RIGHT)
        ).arrange(DOWN, buff=0.5)
        colors[1][1][0].add_background_rectangle(buff=0.1)
        withoutc = VGroup(
            ColorText(BLUE, "BLUE").move_to(colors[0][0][2], aligned_edge=LEFT),
            ColorText(TEAL, "TEAL").move_to(colors[0][1][2], aligned_edge=LEFT),
            ColorText(GREEN, "GREEN").move_to(colors[0][2][2], aligned_edge=LEFT),
            ColorText(YELLOW, "YELLOW").move_to(colors[0][3][2], aligned_edge=LEFT),
            ColorText(GOLD, "GOLD").move_to(colors[0][4][2], aligned_edge=LEFT),
            ColorText(RED, "RED").move_to(colors[0][5][2], aligned_edge=LEFT),
            ColorText(MAROON, "MAROON").move_to(colors[0][6][2], aligned_edge=LEFT),
            ColorText(PURPLE, "PURPLE").move_to(colors[0][7][2], aligned_edge=LEFT),
        )
        recs = VGroup(
            *[
                SurroundingRectangle(colors[0][i][2], color=GOLD)
                for i in range(8)
            ]
        )
        grey = VGroup(
            ColorText(LIGHT_GREY, "LIGHT_GREY").move_to(colors[1][1][2]),
            ColorText(GREY, "GREY").move_to(colors[1][2][0]),
            ColorText(DARK_GREY, "DARK_GREY").move_to(colors[1][2][1]),
            ColorText(DARKER_GREY, "DARKER_GREY").move_to(colors[1][2][2]),
        )
        recs2 = VGroup(
            SurroundingRectangle(colors[1][1][2], color=GOLD),
            SurroundingRectangle(colors[1][2][0], color=GOLD),
            SurroundingRectangle(colors[1][2][1], color=GOLD),
            SurroundingRectangle(colors[1][2][2], color=GOLD),
        )

        self.play(Write(caps[0]))
        self.wait(3)
        self.play(Transform(caps[0], caps[1]))
        self.wait(3)
        self.play(Transform(caps[0], caps[2]))
        self.wait()
        self.play(Write(colors[0]))
        self.play(Write(colors[1]))
        self.wait(4)
        self.play(Transform(caps[0], caps[3]))
        self.wait(2)
        self.play(ShowCreation(recs, lag_ratio=0.8))
        self.play(
            *[
                Transform(colors[0][i][2], withoutc[i])
                for i in range(8)
            ]
        )
        self.play(FadeOut(recs))
        self.wait(2)
        self.play(Transform(caps[0], caps[4]))
        self.wait(2)
        self.play(ShowCreation(recs2, lag_ratio=0.8))
        self.play(
            Transform(colors[1][1][2], grey[0]),
            Transform(colors[1][2][0], grey[1]),
            Transform(colors[1][2][1], grey[2]),
            Transform(colors[1][2][2], grey[3]),
        )
        self.play(FadeOut(recs2))
        self.wait(3)
        self.play(Transform(caps[0], caps[5]))
        self.wait(2)
        self.play(FadeOut(colors))
        self.play(Transform(caps[0], caps[6]))
        hex_color = VGroup(
            ColorText("#66CCFF", size=0.55),
            ColorText("#00FFCC", size=0.55),
            ColorText("#EE0000", size=0.55),
        ).arrange(DOWN)
        self.play(
            *[
                FadeIn(VGroup(color[:2], color[-1]))
                for color in hex_color
            ]
        )
        self.wait()
        self.play(
            *[
                Write(color[2:-1])
                for color in hex_color
            ]
        )
        self.wait(2)
        self.play(Transform(caps[0], caps[7]))
        self.wait()
        rgb = VGroup(
            ColorText(hex_to_rgb("#66CCFF") * 255, size=0.55),
            ColorText(hex_to_rgb("#00FFCC") * 255, size=0.55),
            ColorText(hex_to_rgb("#EE0000") * 255, size=0.55)
        ).arrange(DOWN)
        self.play(
            *[
                Transform(hex_color[i], rgb[i])
                for i in range(3)
            ]
        )
        self.wait(3)
        self.play(Transform(caps[0], caps[8]))
        self.wait(3)
        self.play(
            FadeOut(caps[0]), FadeOut(hex_color)
        )


class ConvertColor(Scene_):
    def start(self):
        t2c = {"manim": GOLD,
               "颜色": ORANGE}
        title = VGroup(
            Text("Chapter II.", font="Monaco for Powerline", color=BLUE_D, size=0.5, t2c=t2c),
            Text("颜色表示方法的相互转换", font="Source Han Sans CN Bold", color=DARK_GRAY, size=0.5, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "manimlib/utils/color.py中包含一些转换颜色表示方法的函数",
            "首先再次明确manim中颜色的表示",
            "manim表示颜色有hex,rgb,int_rgb,Color类四种",
            "rgb与int_rgb的区别是前者RGB值为0至1,后者为0至255",
            "Color类是最终的颜色,一切表示方法都将转化为Color类",
            "hex与rgb相互转换可以使用hex_to_rgb和rgb_to_hex函数",
            "rgb和int_rgb之间互相转换使用乘/除255就可以解决",
            "rgb和Color转换可以使用rgb_to_color和color_to_rgb函数",
            "另外还有color_to_int_rgb函数将Color转换为int_rgb",
            "hex和Color没有必要相互转换",
            "但是在manim中,可以放入set_color等方法的仅有hex和Color",
            "使用rgb或者int_rgb时需要先转换为hex或者Color"
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        func_list = [
            "hex_to_rgb", "rgb_to_hex",
            "color_to_rgb", "rgb_to_color",
            "color_to_int_rgb"
        ]
        path = CodeLine("manimlib/utils/color.py")
        func = VGroup(
            *[
                CodeLine(each) for each in func_list
            ]
        ).arrange(DOWN)
        first = VGroup(path, func).arrange(RIGHT)
        path.save_state()

        self.play(Write(caps[0]))
        path.center()
        self.play(Write(path))
        self.play(path.restore, FadeInFromDown(func))
        self.wait(2)
        self.play(FadeOut(first), Transform(caps[0], caps[1]))
        self.wait(3)
        self.play(Transform(caps[0], caps[2]))

        color_type = VGroup(
            CodeLine("hex", size=0.5),
            CodeLine("rgb", size=0.5),
            CodeLine("int_rgb", size=0.5),
            CodeLine("Color", size=0.55)
        ).arrange(DOWN, buff=1.5)
        color_type[-1].next_to(color_type[1], RIGHT, buff=4)
        color_type.center()
        dar1 = DoubleArrow(color_type[1].get_bottom(), color_type[2].get_top(), color=ORANGE)
        dars = VGroup(
            *[Arrow(mob.get_right(), color_type[-1].get_left()).set_color([PURPLE, GREEN]).set_sheen_direction(RIGHT)
            for mob in color_type[:-1]]
        )
        for each in dars:
            each.tip.set_color(GREEN)
        times255 = CodeLine("×255").add_background_rectangle(color=WHITE).move_to(dar1)

        self.play(Write(color_type[:-1]))
        self.play(Write(color_type[-1]))
        self.wait(2)
        self.play(Transform(caps[0], caps[3]))
        self.play(Write(dar1))
        self.play(Write(times255))
        self.wait(2)
        self.play(Transform(caps[0], caps[4]))
        self.play(Write(dars))
        self.wait(4)

        self.play(Transform(caps[0], caps[5]), FadeOut(VGroup(color_type, dar1, dars, times255)))
        convert_hex_and_rgb = VGroup(
            CodeLine("hex"),
            TexMobject("\\Longleftrightarrow", color=ORANGE, background_stroke_width=0),
            CodeLine("rgb")
        ).arrange(RIGHT).scale(1.4).to_corner(UL, buff=1)
        code1 = VGroup(
            VGroup(
                CodeLine("hex_to_rgb(", size=0.4),
                ColorText("#66CCFF"),
                CodeLine(")", size=0.4),
            ).arrange(RIGHT),
            VGroup(
                CodeLine("~~~~", size=0.4).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText(hex_to_rgb("#66CCFF"))
            ).arrange(RIGHT),
            VGroup(
                CodeLine("rgb_to_hex(", size=0.4),
                ColorText(hex_to_rgb("#66CCFF")),
                CodeLine(")", size=0.4),
            ).arrange(RIGHT),
            VGroup(
                CodeLine("~~~~", size=0.4).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText("#66CCFF")
            ).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT)
        code1[:2].shift(UP*0.5)
        code1[2:].shift(DOWN*0.5)
        bg = Rectangle(stroke_width=1, fill_color="#EBEBEB", plot_depth=-10, stroke_color=DARK_GRAY, fill_opacity=1)
        bg.surround(code1, buff=0.5)
        self.play(Write(convert_hex_and_rgb), FadeInFromDown(bg))
        self.play(Write(code1[0][0][:-1]), Write(code1[2][0][:-1]))
        self.wait(2)
        self.play(Write(VGroup(code1[0][0][-1], code1[0][1:])))
        self.play(Write(code1[1]))
        self.wait()
        self.play(Write(VGroup(code1[2][0][-1], code1[2][1:])))
        self.play(Write(code1[3]))
        self.wait(5)
        self.play(
            Transform(caps[0], caps[6]),
            FadeOut(VGroup(bg, code1, convert_hex_and_rgb))    
        )
        convert_rgb_and_int = VGroup(
            CodeLine("rgb"),
            TexMobject("\\rightleftharpoons", color=ORANGE, background_stroke_width=0).set_width(1.6, True),
            CodeLine("int_rgb")
        ).arrange(RIGHT, buff=0.25).scale(1.4)
        times255.remove(times255.background_rectangle).next_to(convert_rgb_and_int[1], UP)
        divide255 = CodeLine("÷255").next_to(convert_rgb_and_int[1], DOWN)
        self.play(Write(convert_rgb_and_int[0]), Write(convert_rgb_and_int[-1]))
        self.play(Write(convert_rgb_and_int[1]))
        self.wait()
        self.play(Write(times255))
        self.play(Write(divide255))
        self.wait(2)
        self.play(
            Transform(caps[0], caps[7]),
            FadeOut(VGroup(convert_rgb_and_int, times255, divide255))
        )
        self.wait()

        convert_rgb_and_color = VGroup(
            CodeLine("rgb"),
            TexMobject("\\Longleftrightarrow", color=ORANGE, background_stroke_width=0),
            CodeLine("Color")
        ).arrange(RIGHT).scale(1.4).to_corner(UL, buff=0.6)
        code2 = VGroup(
            VGroup(
                CodeLine("rgb_to_color(", size=0.35),
                ColorText(hex_to_rgb("#66CCFF"), size=0.35),
                CodeLine(")", size=0.35),
            ).arrange(RIGHT),
            VGroup(
                CodeLine("~~~~", size=0.35).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                CodeLine("<Color #6cf>", size=0.35)
            ).arrange(RIGHT),
            CodeLine("color = Color(\"#66CCFF\")"),
            VGroup(
                CodeLine("color_to_rgb(", size=0.35),
                CodeLine("color", size=0.35),
                CodeLine(")", size=0.35),
            ).arrange(RIGHT),
            VGroup(
                CodeLine("~~~~", size=0.35).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText(hex_to_rgb("#66CCFF"), size=0.35)
            ).arrange(RIGHT),
            CodeLine("color_to_int_rgb( color )", size=0.35),
            VGroup(
                CodeLine("~~~~", size=0.35).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText(hex_to_rgb("#66CCFF")*255, size=0.35)
            ).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT)
        code2[:2].shift(UP*0.5)
        code2[2:].shift(DOWN*0.2)
        bg2 = Rectangle(stroke_width=1, fill_color="#EBEBEB", plot_depth=-10, stroke_color=DARK_GRAY, fill_opacity=1)
        bg2.surround(code2, buff=0.5).set_height(4.8, True)
        self.play(Write(convert_rgb_and_color), FadeInFromDown(bg2))
        self.play(Write(code2[0][0][:-1]), Write(code2[3][0][:-1]))
        self.wait(2)
        self.play(Write(VGroup(code2[0][0][-1], code2[0][1:])))
        self.play(Write(code2[1]))
        self.wait()
        self.play(Write(code2[2]))
        self.play(Write(VGroup(code2[3][0][-1], code2[3][1:])))
        self.play(Write(code2[4]))
        self.wait(2)
        self.play(Transform(caps[0], caps[8]))
        self.play(Write(code2[5]))
        self.play(Write(code2[6]))
        self.wait(3)

        self.play(Transform(caps[0], caps[9]))

        self.wait(3)
        self.play(FadeOut(VGroup(bg2, code2, convert_rgb_and_color)))
        self.wait()
        dar2 = DoubleArrow(color_type[0].get_bottom(), color_type[1].get_top(), color=ORANGE)
        self.play(Transform(caps[0], caps[10]), FadeIn(VGroup(color_type, dars, dar1, dar2)))
        self.wait()
        recs = VGroup(
            SurroundingRectangle(color_type[0]),
            SurroundingRectangle(color_type[3]),
        )
        self.play(Write(recs))
        self.wait(2)
        self.play(Transform(caps[0], caps[11]))
        self.wait(4)
        self.play(FadeOut(VGroup(*self.mobjects)))


class ColorOperations(Scene_):
    def start(self):
        t2c = {"manim": GOLD,
               "颜色": ORANGE}
        title = VGroup(
            Text("Chapter III.", font="Monaco for Powerline", color=BLUE_D, size=0.5, t2c=t2c),
            Text("颜色的运算函数", font="Source Han Sans CN Bold", color=DARK_GRAY, size=0.5, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "首先第一个函数，invert_color，用来对颜色反色",
            "输入一个hex或者Color，返回反色的Color类",
            "第二个函数，interpolate_color，在两个颜色之间用alpha比例插值",
            "也是输入hex或者Color，返回插值结果的Color类，alpha为0到1之间的数",
            "（为了方便，这里显示的结果是将Color转换为hex后的）",
            "第三个函数，average_color，传入多个颜色，返回其平均颜色",
            "第四个函数，color_gradient，传入多个参考颜色列表，和需要的长度n",
            "返回长度为n的颜色梯度序列（还是为了方便，这里显示hex）",
            "第五个函数，random_color，随机返回constants.py中定义的一个颜色"
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        func_title = [
            "invert_color(color)",
            "interpolate_color(color1,~color2,~alpha)",
            "average_color(*colors)",
            "color_gradient(reference_colors,~length_of_output)",
            "random_color()"
        ]
        t2c = {
            'colors': ORANGE,
            'color1': ORANGE,
            'color2': ORANGE,
            'reference_colors': ORANGE,
            'length_of_output': ORANGE,
            'invert_color': BLUE_D,
            'interpolate_color': BLUE_D,
            'average_color': BLUE_D,
            'color_gradient': BLUE_D,
            'random_color': BLUE_D,
            'alpha': GOLD,
            '~': WHITE,
        }
        funcs = VGroup(
            *[
                CodeLine(func, size=0.5, t2c=t2c).to_corner(UL, buff=0.7)
                for func in func_title
            ]
        )
        funcs[0][-6:-1].set_color(ORANGE)
        funcs[3].scale(0.85, about_edge=LEFT)

        self.play(Write(caps[0]))
        self.play(Write(funcs[0]))
        code1 = VGroup(
            VGroup(
                CodeLine("invert_color(", size=0.4),
                ColorText("#66CCFF"),
                CodeLine(")", size=0.4),
            ).arrange(RIGHT),
            VGroup(
                CodeLine("~~~~", size=0.4).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                CodeLine("<Color #930>", size=0.4)
            ).arrange(RIGHT),
            VGroup(
                CodeLine("color_to_rgb(invert_color(", size=0.4),
                VGroup(
                    CodeLine("~~~~rgb_to_hex("),
                    ColorText(hex_to_rgb("#66CCFF")),
                    CodeLine(")))", size=0.4),
                ).arrange(RIGHT)
            ).arrange(DOWN, aligned_edge=LEFT),
            VGroup(
                CodeLine("~~~~~~~~~~", size=0.4).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText(color_to_rgb(invert_color("#66CCFF")))
            ).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT)
        code1[:2].shift(UP*0.5)
        code1[2:].shift(DOWN*0.5)
        bg = Rectangle(stroke_width=1, fill_color="#EBEBEB", plot_depth=-10, stroke_color=DARK_GRAY, fill_opacity=1)
        bg.surround(code1, buff=0.5)
        self.play(FadeInFromDown(bg))
        self.play(Write(code1[0][0][:-1]))
        self.wait(2)
        self.play(Transform(caps[0], caps[1]))
        self.wait()
        self.play(Write(VGroup(code1[0][0][-1], code1[0][1:])))
        self.play(Write(code1[1]))
        self.wait(2)
        self.play(Write(code1[2]))
        self.wait()
        self.play(Write(code1[3]))
        self.wait()
        self.play(
            ShowCreationThenDestructionAround(VGroup(code1[2][1][1], code1[3][2]))
        )
        self.wait(2)
        self.play(Transform(caps[0], caps[2]), Transform(funcs[0], funcs[1]))
        
        alpha = ValueTracker(0)
        code2 = VGroup(
            VGroup(
                CodeLine("interpolate_color(BLUE, GREEN, ", size=0.4),
                DecimalNumberText(0),
                CodeLine(")", size=0.4)
            ).arrange(RIGHT),
            VGroup(
                CodeLine("~~~~", size=0.4).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText(
                    interpolate_color(BLUE, GREEN, alpha.get_value()).get_hex_l()
                )
            ).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT)
        bg2 = BackgroundRectangle(code2, fill_color="#EBEBEB", fill_opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=DARK_GRAY, buff=0.4)

        self.play(Transform(bg, bg2), FadeOut(code1))
        self.wait(3)
        self.play(Transform(caps[0], caps[3]))
        self.play(Write(code2[0]))
        self.wait(3)
        self.play(Transform(caps[0], caps[4]), Write(code2[1]))
        self.wait()
        code2[0][1].add_updater(
            lambda m: m.set_value(alpha.get_value())
        )
        code2[1][2].add_updater(
            lambda m: m.become(
                ColorText(
                    interpolate_color(BLUE, GREEN, alpha.get_value()).get_hex_l()
                ).move_to(code2[1][2])
            )
        )
        self.play(
            alpha.increment_value, 1, run_time=3, rate_func=linear
        )
        self.wait(0.5)
        self.play(
            alpha.increment_value, -1, run_time=2, rate_func=linear
        )
        code2[0][1].clear_updaters()
        code2[1][2].clear_updaters()
        self.wait(3)
        
        self.play(Transform(caps[0], caps[5]), Transform(funcs[0], funcs[2]))
        code3 = VGroup(
            CodeLine("average_color(BLUE, GREEN, RED)", size=0.4),
            VGroup(
                CodeLine("~~~~", size=0.4).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                CodeLine("<Color #9da288>", size=0.4)
            ).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT)
        bg3 = BackgroundRectangle(code3, fill_color="#EBEBEB", fill_opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=DARK_GRAY, buff=0.5)
        self.play(Transform(bg, bg3), FadeOut(code2))
        self.wait(3)
        self.play(Write(code3[0]))
        self.wait(1)
        self.play(Write(code3[1]))
        self.wait(3)
        
        self.play(Transform(caps[0], caps[6]), Transform(funcs[0], funcs[3]))
        ans = VGroup(
            VGroup(
                ColorText("#58C4DD"), CodeLine(", ", size=0.4),
                ColorText("#63C3BF"), CodeLine(", ", size=0.4),
                ColorText("#6DC2A2"), CodeLine(", ", size=0.4),
            ).arrange(RIGHT, aligned_edge=DOWN),
            VGroup(
                ColorText("#78C284"), CodeLine(", ", size=0.4),
                ColorText("#83C167"), CodeLine(", ", size=0.4),
                ColorText("#A1A962"), CodeLine(", ", size=0.4),
            ).arrange(RIGHT, aligned_edge=DOWN),
            VGroup(
                ColorText("#BF915E"), CodeLine(", ", size=0.4),
                ColorText("#DE7A59"), CodeLine(", ", size=0.4),
                ColorText("#FC6255"), CodeLine("~]", size=0.4)
            ).arrange(RIGHT, aligned_edge=DOWN),
        ).arrange(DOWN, aligned_edge=LEFT)
        code4 = VGroup(
            CodeLine("color_gradient([BLUE, GREEN, RED], 9)", size=0.4),
            VGroup(
                CodeLine("~~~~", size=0.4).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                CodeLine("[", size=0.4),
                ans
            ).arrange(RIGHT, aligned_edge=UP),
        ).arrange(DOWN, aligned_edge=LEFT)
        bg4 = BackgroundRectangle(code4, fill_color="#EBEBEB", fill_opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=DARK_GRAY, buff=0.5)
        self.play(Transform(bg, bg4), FadeOut(code3))
        self.wait(2)
        self.play(Write(code4[0]))
        self.wait()
        self.play(Transform(caps[0], caps[7]), Write(code4[1]))
        self.wait(5)

        self.play(Transform(caps[0], caps[8]), Transform(funcs[0], funcs[4]))
        code5 = VGroup(
            CodeLine("random_color()", size=0.4),
            VGroup(
                CodeLine("~~~~", size=0.4).set_color("#EBEBEB"),
                TexMobject("\\rightarrow", background_stroke_width=0, color=BLACK),
                ColorText(random_color())
            ).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT)
        bg5 = BackgroundRectangle(code5, fill_color="#EBEBEB", fill_opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=DARK_GRAY, buff=0.5)
        self.play(Transform(bg, bg5), FadeOut(code4))
        self.wait(3)
        self.play(Write(code5[0]))
        self.wait(1)
        self.play(Write(code5[1]))
        self.wait(1)
        # def random_updater(obj):
        #     new_color = random_color()
        #     obj.become(ColorText(new_color).move_to(code5[1][2]))
        fps = 30
        for color in COLOR_MAP.values():
            code5[1][2].become(ColorText(color).move_to(code5[1][2]))
            self.wait(1 / fps)
        for color in COLOR_MAP.values():
            code5[1][2].become(ColorText(color).move_to(code5[1][2]))
            self.wait(1 / fps)
        # code5[1][2].remove_updater(random_updater)
        self.wait(4)
        self.play(
            FadeOut(VGroup(caps[0], funcs[0], bg, code5))
        )
        self.wait()


class SetColors(Scene_):
    def start(self):
        t2c = {"manim": GOLD,
               "颜色": ORANGE}
        title = VGroup(
            Text("Chapter IV.", font="Monaco for Powerline", color=BLUE_D, size=0.5, t2c=t2c),
            Text("物体颜色的设置", font="Source Han Sans CN Bold", color=DARK_GRAY, size=0.5, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "由于Mobject一般不使用颜色,所以这里只介绍VMobject及子类的上色方法",
            "VMobject涉及颜色有关的style有stroke、fill和background_stroke",
            "而且manim中使用RGBA格式,所以还有opacity不透明度这一设置",
            "所以也就有了这六个style",
            "那么我们先来看一下set_color方法",
            "set_color会将stroke和fill均设为给出的颜色,并保持opacity不变",
            "set_stroke方法可以更改线条的颜色和不透明度",
            "set_fill方法可以更改填充的颜色和不透明度",
            "set_background_stroke方法可以更改背景线条的颜色和不透明度"
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        styles = VGroup(
            VGroup(
                CodeLine("stroke", size=0.45),
                CodeLine("stroke_color", size=0.35),
                CodeLine("stroke_opacity", size=0.35),
            ).arrange(DOWN),
            VGroup(
                CodeLine("fill", size=0.45),
                CodeLine("fill_color", size=0.35),
                CodeLine("fill_opacity", size=0.35),
            ).arrange(DOWN),
            VGroup(
                CodeLine("background_stroke", size=0.45),
                CodeLine("background_stroke_color", size=0.35),
                CodeLine("background_stroke_opacity", size=0.35),
            ).arrange(DOWN)
        ).arrange(RIGHT, buff=0.5)
        styles[0][0].shift(UP*0.7)
        styles[1][0].shift(UP*0.7)
        styles[2][0].shift(UP*0.7)

        rec = Square(side_length=3, fill_opacity=0.5, color=BLUE).shift(LEFT*3)
        rec_bg = SurroundingRectangle(rec, fill_color=DARKER_GRAY, fill_opacity=0, buff=1, stroke_width=0)
        code = [
            ">>> rec.set_color(GREEN)",
            ">>> rec.set_stroke(color=RED,",
            "~~~~~~~~width=15, opacity=0.4)",
            ">>> rec.set_fill(color=ORANGE,",
            "~~~~~~~~opacity=0.9)",
            ">>> rec.set_background_stroke(",
            "~~~~~~~~color=WHITE,",
            "~~~~~~~~width=10,",
            "~~~~~~~~opacity=1",
            "~~~~)"
        ]
        t2c2 = {
            "color": ORANGE,
            "set_color": BLUE_D,
            "set_stroke": BLUE_D,
            "set_fill": BLUE_D,
            "set_background_stroke": BLUE_D,
            "GREEN": GREEN,
            "RED": RED,
            "WHITE": BLACK,
            "opacity": ORANGE,
            "ORANGE": ORANGE,
            "width": ORANGE,
            "10": average_color(BLUE, PINK),
            "0.2": average_color(BLUE, PINK),
            "0.9": average_color(BLUE, PINK),
            "1": average_color(BLUE, PINK),
        }
        codes = VGroup(
            *[
                CodeLine(code_, t2c=t2c2) for code_ in code
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes.next_to(ORIGIN, aligned_edge=LEFT, buff=0.5).shift(UP*0.5)
        codes[0][8:17].set_color(BLUE_D)
        bg = SurroundingRectangle(codes, stroke_width=1, stroke_color=DARK_GRAY, fill_color="#EBEBEB", fill_opacity=1, buff=0.2)
        
        self.play(Write(caps[0]))
        self.wait(3)
        self.play(Transform(caps[0], caps[1]))
        self.wait(1)
        self.play(
            Write(styles[0][0]),
            Write(styles[1][0]),
            Write(styles[2][0]),
        )
        self.wait()
        self.play(Transform(caps[0], caps[2]))
        self.wait(3)
        self.play(
            Transform(caps[0], caps[3]),
            Write(styles[0][1:]),
            Write(styles[1][1:]),
            Write(styles[2][1:]),
        )
        self.wait(4)
        self.play(Transform(caps[0], caps[4]), FadeOut(styles))
        self.wait(1)
        self.add(rec_bg)
        self.play(ShowCreation(rec), FadeInFromDown(bg))
        self.wait()
        self.play(Transform(caps[0], caps[5]))
        self.wait()
        self.play(Write(codes[0]))
        self.play(rec.set_color, GREEN)
        self.wait(4)
        self.play(Transform(caps[0], caps[6]))
        self.wait()
        self.play(Write(codes[1]))
        self.play(Write(codes[2]))
        self.play(rec.set_stroke, RED, 15, 0.4)
        self.wait(4)
        self.play(Transform(caps[0], caps[7]))
        self.wait()
        self.play(Write(codes[3]))
        self.play(Write(codes[4]))
        self.play(rec.set_fill, ORANGE, 0.9)
        self.wait(4)
        self.play(Transform(caps[0], caps[8]))
        self.wait()
        self.play(Write(codes[5]), Write(codes[-1]))
        self.wait()
        self.play(Write(codes[6:9]))
        self.play(rec_bg.set_fill, {"opacity": 1})
        self.wait()
        self.play(rec.set_background_stroke, {"color": WHITE, "width": 10, "opacity": 1})
        self.wait(5)
        self.play(FadeOut(VGroup(bg, codes, rec_bg, rec, caps[0])))


class SubmobjectSetColor(Scene_):
    def start(self):
        t2c = {"manim": GOLD,
               "颜色": ORANGE}
        title = VGroup(
            Text("Chapter V.", font="Monaco for Powerline", color=BLUE_D, size=0.5, t2c=t2c),
            Text("给子物体上颜色", font="Source Han Sans CN Bold", color=DARK_GRAY, size=0.5, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "给一个VGroup的所有子物体上色",
            "可以使用前述三个方法如set_color将所有物体上为同一颜色",
            "使用set_color_by_gradient方法可以从首至尾上为梯度颜色",
            "使用set_colors_by_radial_gradient方法根据距离半径上梯度颜色",
            "传入的参数为center(默认物体中心),梯度达到的最远半径radius,和内外颜色",
            "距离center超过radius的子物体都会上为outer_color的颜色"
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        vg = VGroup(
            *[
                VGroup(
                    *[
                        Square(side_length=0.5, color=GRAY, fill_opacity=1) for i in range(7)
                    ]
                ).arrange(RIGHT)
                for _ in range(7)
            ]
        ).arrange(DOWN).shift(LEFT*4)
        code = [
            ">>> vg.set_color(BLUE_B)",
            ">>> vg.set_color_by_gradient(",
            "~~~~~~~~GREEN, RED, BLUE)",
            ">>> vg.set_colors_by_radial_gradient(",
            "~~~~~~~~# center=vg.get_center(),",
            "~~~~~~~~radius=2.7,",
            "~~~~~~~~inner_color=BLUE,",
            "~~~~~~~~outer_color=PINK",
            "~~~~)"
        ]
        t2c2 = {
            "set_color": BLUE_D,
            "set_color_by_gradient": BLUE_D,
            "set_colors_by_radial_gradient": BLUE_D,
            "BLUE_B": BLUE_B,
            "GREEN": GREEN,
            "RED": RED,
            "BLUE": BLUE,
            "radius": ORANGE,
            "inner_color": ORANGE,
            "outer_color": ORANGE,
            "# center=vg.get_center(),": GREEN,
            "3": average_color(BLUE, PINK),
            "PINK": PINK,
        }
        codes = VGroup(
            *[
                CodeLine(code_, t2c=t2c2, size=0.34) for code_ in code
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes.next_to(ORIGIN, aligned_edge=LEFT, buff=-0.5)
        bg = SurroundingRectangle(codes, stroke_width=1, stroke_color=DARK_GRAY, fill_color="#EBEBEB", fill_opacity=1, buff=0.2)

        self.play(Write(caps[0]))
        self.play(ShowCreation(vg, lag_ratio=0.8), run_time=2.5)
        self.play(FadeInFromDown(bg))
        self.wait(1.5)
        self.play(Transform(caps[0], caps[1]))
        self.wait()
        self.play(Write(codes[0]))
        self.wait(2)
        self.play(vg.set_color, BLUE_B)
        self.wait(3)
        self.play(Transform(caps[0], caps[2]))
        self.wait()
        self.play(Write(codes[1]))
        self.play(Write(codes[2]))
        self.wait(2)
        self.play(vg.set_color_by_gradient, GREEN, RED, BLUE, lag_ratio=0.8, run_time=2.5, rate_func=linear)
        self.wait(4)
        self.play(Transform(caps[0], caps[3]))
        self.wait()
        self.play(Write(codes[3]))
        self.play(Write(codes[-1]))
        self.wait(2)
        self.play(Transform(caps[0], caps[4]))
        self.wait()
        self.play(Write(codes[4:-1]))
        self.wait(2)
        circle = Circle(radius=2.7, color=DARK_GRAY).shift(LEFT*4)
        dc = DashedVMobject(circle, num_dashes=40)
        self.play(vg.set_colors_by_radial_gradient, None, 2.7, BLUE, PINK)
        self.wait()
        self.play(Transform(caps[0], caps[5]))
        self.play(ShowCreation(dc))
        self.wait(6)
        self.play(FadeOut(VGroup(vg, dc, caps[0], bg, codes)))


class SheenAndGradientColor(Scene_):
    def start(self):
        t2c = {"manim": GOLD,
               "光泽": GOLD,
               "颜色": ORANGE}
        title = VGroup(
            Text("Chapter VI.", font="Monaco for Powerline", color=BLUE_D, size=0.5, t2c=t2c),
            Text("光泽与渐变颜色", font="Source Han Sans CN Bold", color=DARK_GRAY, size=0.5, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "manim中,可以使用set_sheen来给物体增加光泽(本质上是将RGB加上一个数)",
            "传入factor表示光泽的尺度、direction表示光泽变化的方向",
            "或者仅仅使用set_sheen_direction来改变sheen的方向",
            "达到渐变色的效果,可以向set_color中传入一个列表表示渐变的颜色",
            "再用set_sheen_direction来改变渐变色的渐变方向",
        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        factor = ValueTracker(0.5)
        codes = VGroup(
            VGroup(
                CodeLine(">>> rec.set_sheen("),
                DecimalNumberText(factor.get_value(), text_config={"size": 0.36, "color": RED}),
                CodeLine(", RIGHT)")
            ).arrange(RIGHT, buff=0.15),
            CodeLine(">>> rec.set_sheen_direction(UL)"),
            CodeLine(">>> rec.set_sheen_direction(DR)"),
            CodeLine(">>> rec.set_color([BLUE, RED, GREEN])"),
            CodeLine(">>> rec.set_sheen_direction(RIGHT)"),
            CodeLine("~~~~"),
            CodeLine("~~~~"),
            CodeLine("~~~~"),
            CodeLine("~~~~"),
            CodeLine("~~~~"),
            CodeLine("~~~~"),
            CodeLine("~~~~"),
        ).arrange(DOWN, aligned_edge=LEFT)
        codes.next_to(ORIGIN, aligned_edge=LEFT, buff=-1)
        bg = SurroundingRectangle(codes, stroke_width=1, stroke_color=DARK_GRAY, fill_color="#EBEBEB", fill_opacity=1, buff=0.2)

        rec = Square(side_length=3, fill_opacity=1, color=BLUE_D).shift(LEFT*4)
        arrow = Arrow(ORIGIN, RIGHT, color=ORANGE).set_width(rec.get_width()).next_to(rec, UP)
        # self.add(rec, bg)

        self.play(Write(caps[0]))
        self.wait()
        self.play(ShowCreation(rec), FadeInFromDown(bg))
        self.wait(3)
        self.play(Transform(caps[0], caps[1]))
        self.play(Write(codes[0]))
        self.play(rec.set_sheen, 0.5, RIGHT)
        self.wait()
        self.play(Write(arrow))
        self.wait()
        codes[0][1].add_updater(lambda m: m.set_value(factor.get_value()))
        rec.add_updater(
            lambda m: m.become(
                Square(side_length=3, fill_opacity=1, color=BLUE_D).shift(LEFT*4).set_sheen(factor.get_value(), RIGHT)
            )
        )
        self.play(factor.increment_value, 2, rate_func=linear, run_time=3)
        self.play(factor.increment_value, -2.5, rate_func=linear, run_time=3)
        self.wait()
        self.play(factor.increment_value, 0.5, rate_func=linear, run_time=2)
        codes[0][1].clear_updaters()
        rec.clear_updaters()
        self.wait(3)
        self.play(Transform(caps[0], caps[2]), FadeOut(arrow))
        self.wait()
        self.play(Write(codes[1]))
        corners = rec.get_vertices()
        arrow2 = Arrow(corners[2], corners[0], color=ORANGE)
        arrow3 = Arrow(corners[0], corners[2], color=ORANGE)
        self.play(Write(arrow2))
        self.play(rec.set_sheen_direction, UL)
        self.wait(3)
        self.play(Write(codes[2]))
        self.play(rec.set_sheen_direction, DR, Transform(arrow2, arrow3))
        self.wait(3)
        self.play(Transform(caps[0], caps[3]))
        self.wait(2)
        self.play(Write(codes[3]))
        self.play(rec.set_color, [BLUE, RED, GREEN])
        self.wait(3)
        self.play(Transform(caps[0], caps[4]))
        self.wait(2)
        self.play(Write(codes[4]))
        self.play(rec.set_sheen_direction, RIGHT, Transform(arrow2, arrow))
        self.wait(5)
        self.play(FadeOut(Group(*self.mobjects)))


class DownProgressBar(Scene_):
    def construct(self):
        methods_dict = {
            '颜色的表示': '0022', 
            '颜色表示法的转换': '0125', 
            '颜色的运算函数': '0305',
            '给物体设置颜色': '0443', 
            '子物体的梯度上色': '0600', 
            '光泽和渐变色': '0701',
            ' ': '0810'
        }
        total_time = '0822'
        func_time = lambda t: int(t[0:2]) * 60 + int(t[2:])
        func_loc = lambda t: func_time(t)/func_time(total_time) * FRAME_WIDTH * RIGHT + FRAME_WIDTH * LEFT / 2
        p_list = [FRAME_WIDTH * LEFT / 2]
        for v in methods_dict.values():
            p_list.append(func_loc(v))
        p_list.append(func_loc(total_time))

        colors = color_gradient([BLUE, PINK, RED, ORANGE, GREEN], len(methods_dict)+1)

        lines = VGroup(*[Line(p_list[i], p_list[i+1]-0.02*RIGHT, color=colors[i], stroke_width=20) for i in range(len(methods_dict)+1)])
        lines.to_edge(DOWN * 0.22, buff=1)
        texts = VGroup(*[Text(t, color=WHITE, font='思源黑体 CN Bold', size=0.14) for t in methods_dict.keys()], plot_depth=1)
        text = Text('空降', color=WHITE, font='庞门正道标题体', size=0.22).to_edge(DOWN * 0.132, buff=1).to_edge(LEFT, buff=0.4)
        text[1].shift(RIGHT*0.03)
        text[0].shift(LEFT*0.01)
        for i in range(len(methods_dict)):
            texts[i].move_to(lines[i+1])

        self.add(lines, texts, text)


class VideoCover(Scene):
    def construct(self):
        background = Polygon(
            LEFT_SIDE * 2 + BOTTOM, BOTTOM, LEFT_SIDE / 2 + TOP, LEFT_SIDE * 2 + TOP,
            fill_opacity=0.7, fill_color=BLACK, stroke_width=0
        ).shift(RIGHT)
        text = VGroup(
            Text("manim教程", font="庞门正道标题体", color=BLUE).scale(0.9),
            Text("第三讲", font="庞门正道标题体", color=BLUE).scale(1.1),
            Text("颜色的表示和设置", font="庞门正道标题体", color=ORANGE).scale(1.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        text[2].shift(DOWN*0.4)
        text.center().to_edge(LEFT, buff=0.8).shift(UP*0.5)
        text2 = VGroup(
            Text("manim教程", font="庞门正道标题体", color=BLUE).scale(0.9).set_stroke(width=12, opacity=0.4),
            Text("第三讲", font="庞门正道标题体", color=BLUE).scale(1.1).set_stroke(width=12, opacity=0.4),
            Text("颜色的表示和设置", font="庞门正道标题体", color=ORANGE).scale(1.5).set_stroke(width=13, opacity=0.4)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        text2[2].shift(DOWN*0.4)
        text2.center().to_edge(LEFT, buff=0.8).shift(UP*0.5)
        self.add(background, text2, text)


class VideoCover1(Scene):
    def construct(self):
        background = Polygon(
            LEFT_SIDE * 2 + BOTTOM, BOTTOM, LEFT_SIDE / 2 + TOP, LEFT_SIDE * 2 + TOP,
            fill_opacity=0.7, fill_color=BLACK, stroke_width=0
        ).shift(RIGHT)
        text = VGroup(
            Text("manim教程", font="庞门正道标题体", color=BLUE).scale(0.9),
            Text("第一讲", font="庞门正道标题体", color=BLUE).scale(1.1),
            Text("物体的位置与变换", font="庞门正道标题体", color=ORANGE).scale(1.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        text[2].shift(DOWN*0.4)
        text.center().to_edge(LEFT, buff=0.8).shift(UP*0.5)
        text2 = VGroup(
            Text("manim教程", font="庞门正道标题体", color=BLUE).scale(0.9).set_stroke(width=12, opacity=0.4),
            Text("第一讲", font="庞门正道标题体", color=BLUE).scale(1.1).set_stroke(width=12, opacity=0.4),
            Text("物体的位置与变换", font="庞门正道标题体", color=ORANGE).scale(1.5).set_stroke(width=13, opacity=0.4)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        text2[2].shift(DOWN*0.4)
        text2.center().to_edge(LEFT, buff=0.8).shift(UP*0.5)
        self.add(background, text2, text)



