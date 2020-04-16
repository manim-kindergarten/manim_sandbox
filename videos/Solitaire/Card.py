# from @RY-Givenchy

#
# Copyright: 2020 niedong
# Solitaire card design
#
# Please don't consider this as a perfect design
#

from manimlib.imports import *


def fill_dict(color, opacity=1):
    return {
        "color": color, "fill_color": color, "fill_opacity": opacity
    }


def close_to(*points, close_buff=0.3):
    pos = np.array([0., 0., 0.])
    for point in points:
        pos += close_buff * point
    return pos


class Pattern(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def paint(self, *materials):
        return self.add(*materials)


class Sign(Pattern):
    pass


class Handle(Pattern):
    CONFIG = {
        "handle_width": 0.025,
        "aspect_ratio": 6,
    }

    def get_rectangle(self):
        handle_height = self.handle_width * self.aspect_ratio
        rec = Rectangle(width=self.handle_width, height=handle_height, **fill_dict(BLACK))
        return rec

    def get_triangle(self, rec):
        triangle = Triangle(**fill_dict(BLACK)).set_width(self.handle_width * 2)
        triangle.move_to(rec.get_critical_point(DOWN))
        return triangle

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rectangle = self.get_rectangle()
        triangle = self.get_triangle(rectangle)
        self.paint(rectangle, triangle).center()


class Diamond(Sign):
    CONFIG = {
        "diamond_width": 0.5 / np.sqrt(2),
    }

    def get_square(self):
        square = Square(**fill_dict(RED)).set_width(self.diamond_width)
        return square.rotate(PI / 4)

    def __init__(self, width=None, **kwargs):
        super().__init__(**kwargs)
        if width is not None:
            self.diamond_width = width
        square = self.get_square()
        self.paint(square)


class Heart(Sign):
    CONFIG = {
        "heart_width": 0.5,
    }

    def get_circle_centers(self):
        dim = self.heart_width / 2 / np.sqrt(2)
        return [
            np.array([dim * i, dim, 0])
            for i in [-1, 1]
        ]

    def get_circles(self):
        centers = self.get_circle_centers()
        return VGroup(*[
            Circle(radius=self.heart_width / 2, **fill_dict(RED)).move_to(center)
            for center in centers
        ])

    def __init__(self, width=None, **kwargs):
        super().__init__(**kwargs)
        if width is not None:
            self.heart_width = width
        diamond = Diamond(diamond_width=self.heart_width)
        circles = self.get_circles()
        self.paint(VGroup(diamond, circles).set_width(self.heart_width)).center()


def get_handle(pattern):
    return Handle().move_to(pattern.get_critical_point(DOWN))


class Spade(Sign):
    CONFIG = {
        "spade_width": 0.5,
    }

    def __init__(self, width=None, **kwargs):
        super().__init__(**kwargs)
        if width is not None:
            self.spade_width = width
        heart = Heart(heart_width=self.spade_width).rotate(PI).set_color(BLACK)
        handle = get_handle(heart)
        self.paint(VGroup(heart, handle).set_width(self.spade_width)).center()


class Club(Sign):
    CONFIG = {
        "club_radius": 0.25,
        "angle": PI / 8
    }

    def get_circle_centers(self):
        axis, angle = self.club_radius, self.angle
        return [
            np.array([0, axis, 0]),
            np.array([axis * np.cos(angle), -axis * np.sin(angle), 0]),
            np.array([-axis * np.cos(angle), -axis * np.sin(angle), 0])
        ]

    def get_circles(self):
        centers = self.get_circle_centers()
        return VGroup(*[
            Circle(radius=self.club_radius, **fill_dict(BLACK)).move_to(center)
            for center in centers
        ])

    def __init__(self, diameter=None, **kwargs):
        super().__init__(**kwargs)
        if diameter is not None:
            self.club_radius = diameter / 2
        circles = self.get_circles()
        handle = get_handle(circles)
        self.paint(VGroup(circles, handle).set_width(self.club_radius * 2)).center()


def frame_lines(ins, pos_s, pos_e, width=1.5, color=BLACK):
    def fix_instance(fix_ratio=1 / 0.98):
        return ins.copy().scale(fix_ratio)

    instance = fix_instance()
    start, end = instance.get_critical_point(pos_s), instance.get_critical_point(pos_e)
    return Line(start, end, stroke_width=width).set_color(color)


class Card(Pattern):
    COLOR = (BLACK, RED, BLACK, RED)
    SIGN = (Spade, Heart, Club, Diamond)

    DEFAULT_CARD_WIDTH = 1.25

    TEXT_DICT = {
        "Ace": "A", "Two": "2", "Three": "3", "Four": "4", "Five": "5",
        "Six": "6", "Seven": "7", "Eight": "8", "Nine": "9", "Ten": "10",
        "Jack": "J", "Queen": "Q", "King": "K"
    }

    CONFIG = {
        "card_width": DEFAULT_CARD_WIDTH,
        "text_scale": 0.7,
        "sign_scale": 1.4
    }

    def sign_color(self, sign):
        return self.COLOR[sign]

    def sign_constructor(self, sign):
        return self.SIGN[sign]

    def get_card_height(self, scale_fac=1.396825):
        return self.card_width * scale_fac

    def get_ratio(self):
        return self.card_width / self.DEFAULT_CARD_WIDTH

    def get_text_from_dict(self, which):
        return self.TEXT_DICT[which]

    def paint_frame_lines(self, fill_rec):
        self.paint(frame_lines(fill_rec, LEFT + UP, RIGHT + UP))
        self.paint(frame_lines(fill_rec, RIGHT + UP, RIGHT + DOWN))
        self.paint(frame_lines(fill_rec, RIGHT + DOWN, LEFT + DOWN))
        self.paint(frame_lines(fill_rec, LEFT + DOWN, LEFT + UP))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fill_rec = Rectangle(width=self.card_width, height=self.get_card_height(), **fill_dict(WHITE))
        self.paint(fill_rec)
        self.paint_frame_lines(fill_rec)

    def get_sample(self):
        return TextMobject(self.get_text_from_dict("King")).scale(self.text_scale * self.get_ratio())

    def get_text_by_name(self, _name, color):
        text = TextMobject(self.get_text_from_dict(_name), **fill_dict(color))
        text.scale(self.text_scale * self.get_ratio()).set_stroke(color, opacity=1, background=True)
        sample = self.get_sample().next_to(self.get_critical_point(UP + LEFT), close_to(DOWN + RIGHT))
        return text.move_to(sample.get_center())

    def get_text(self, color):
        return self.get_text_by_name(self.__class__.__name__, color)

    def get_text_and_sign(self, constructor, color):
        text = self.get_text(color)
        text_sign = constructor().set_width(self.get_sample().get_width()).next_to(text, close_to(DOWN))
        return text, text_sign

    def get_sign(self, constructor):
        sign = constructor().scale(self.sign_scale * self.get_ratio())
        return sign.next_to(self.get_critical_point(RIGHT + DOWN), close_to(UP + LEFT))

    def paint_sign(self, color, constructor):
        text, text_sign = self.get_text_and_sign(constructor, color)
        sign = self.get_sign(constructor)
        self.paint(text, text_sign, sign)

    def paint_marker(self, sign):
        self.paint_sign(self.sign_color(sign), self.sign_constructor(sign))


class Ace(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Two(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Three(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Four(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Five(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Six(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Seven(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Eight(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Nine(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Ten(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Jack(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class Queen(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)


class King(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(**kwargs)
        self.paint_marker(sign)
