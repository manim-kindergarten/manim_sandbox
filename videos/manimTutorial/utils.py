from manimlib.imports import *
from manim_sandbox.utils.imports import *


class CodeLine(Text):
    CONFIG = {
        't2c': {
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
            'FRAME_HEIGHT': BLUE_D,
            'FRAME_WIDTH': BLUE_D,
            'PIXEL_HEIGHT': RED_B,
            'PIXEL_WIDTH': RED_B,

            'manim': GOLD,
            'python': GOLD,

            'BLUE_C': BLUE,
            'BLUE': BLUE,
            'GREEN': GREEN,
            'YELLOW': YELLOW,
            'RED': RED,
            'GREY_BROWN': GREY_BROWN,

            'np': BLACK,
            'array': BLUE_D,
            'ndarray': BLUE,

            'move_to': BLUE_D,
            'shift': BLUE_D,
            'arrange': BLUE_D,
            'append': BLUE_D,
            'remove': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'add_to_back': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            'set_color': BLUE_D,
            'set_fill': BLUE_D,
            'set_background_stroke': BLUE_D,

            'VGroup': BLUE_D,
            'VMobject': BLUE_D,
            'ImageMobject': BLUE_D,
            'Mobject': BLUE_D,
            'list': BLUE_D,
            
            'self': PINK,
            'play': BLUE_D,
            ">>>": RED,
            'mob': RED_D,
            'mob1': RED_D,
            'mob2': RED_D,
            'mob3': RED_D,
            'mob0': RED_D,

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
            'False': average_color(BLUE, PINK),

            '2D': RED_B,
            '3D': RED_B,

            '~': "#EBEBEB"
        },
        'font': 'Consolas',
        'size': 0.72,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }
    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class CodeLines(VGroup):
    def __init__(self, *text, buff=0.2, **kwargs):
        VGroup.__init__(self)
        for each in text:
            self.add(CodeLine(each, **kwargs))
        self.arrange(DOWN, aligned_edge=LEFT, buff=buff)


class CodeBackground(BackgroundRectangle):
    CONFIG = {
        "fill_color": "#EBEBEB",
        "fill_opacity": 1,
        "stroke_width": 1,
        "stroke_opacity": 1,
        "stroke_color": DARK_GRAY,
        "buff": 0.5
    }


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
        new_decimal.scale(
            self[-1].get_height() / new_decimal[-1].get_height()
        )
        new_decimal.move_to(self, self.edge_to_fix)
        new_decimal.match_style(self)

        old_family = self.get_family()
        self.submobjects = new_decimal.submobjects
        for mob in old_family:
            mob.points[:] = 0
        self.number = number
        return self

    def get_value(self):
        return self.number

    def increment_value(self, delta_t=1):
        self.set_value(self.get_value() + delta_t)


class Scene_(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        },
        "fade_all": True,
    }
    
    def setup(self):
        self.caps_cnt = 1

    def next_caps(self):
        self.play(Transform(self.caps[0], self.caps[self.caps_cnt]))
        self.wait()
        self.caps_cnt += 1

    def tear_down(self):
        if self.fade_all:
            self.play(FadeOut(Group(*self.mobjects)))

