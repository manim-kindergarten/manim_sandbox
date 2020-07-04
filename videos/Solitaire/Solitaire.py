# from @RY-Givenchy

#
# Copyright: 2020 niedong
# Solitaire random waterfall design
#
# See the original video at:
# https://www.bilibili.com/video/BV12a4y1x78t
#

from Card import *
from FreeFallEngine import *
from raw_frame_scene import *


def add_boundary(value, boundary):
    assert (boundary > 0)
    if 0 < value < boundary:
        value += boundary
    elif -boundary < value <= 0:
        value -= boundary
    return value


def rand(a, b, boundary=None):
    if boundary is None:
        return random.uniform(a, b)
    return add_boundary(random.uniform(a, b), boundary)


SOLITAIRE_CONSTANT = {
    "SPADE": 0, "HEART": 1, "CLUB": 2, "DIAMOND": 3,
    "ACE": 1, "TWO": 2, "THREE": 3, "FOUR": 4,
    "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8,
    "NINE": 9, "TEN": 10, "JACK": 11, "QUEEN": 12, "KING": 13,
}


class SolitaireScene(RawFrameScene):
    POINT = (None, Ace, Two, Three, Four, Five, Six,
             Seven, Eight, Nine, Ten, Jack, Queen, King)

    CONFIG = {
        "camera_config": {
            "background_color": GREEN
        },
        **SOLITAIRE_CONSTANT,
    }

    def point_constructor(self, point):
        return self.POINT[point]

    def deck_of_cards(self, sign):
        cards = []
        for i in range(self.ACE, self.KING + 1):
            cards.append(self.point_constructor(i)(sign))
        return Group(*cards)

    def four_deck_of_cards(self, corner_pos=RIGHT + UP):
        return Group(*[
            self.deck_of_cards(sign)
            for sign in range(self.SPADE, self.DIAMOND + 1)
        ]).arrange(RIGHT * 2).to_corner(corner_pos)

    def trace_move(self, obj, position):
        obj.move_to(position)
        return self.capture(obj.copy())

    def setup_engine(self, _name, **kwargs):
        setattr(self, _name, FreeFallEngine(**kwargs))
        return self

    def refresh_seed(self):
        random.seed()
        return self

    def setup(self):
        super().setup()
        self.setup_engine("engine")
        self.refresh_seed()
        return self

    def random_waterfall(self, card, vx, vy):
        for position in self.engine.approximation_points(card, vx, vy):
            self.trace_move(card, position)
        return self

    def init_background(self, *captured):
        background = Group(*captured)
        self.trace_move(background, background.get_center())

    def construct(self):
        cards = self.four_deck_of_cards()
        self.init_background(cards)
        for point in range(self.ACE, self.KING + 1):
            for sign in range(self.SPADE, self.DIAMOND + 1):
                self.random_waterfall(cards[sign][-point], rand(-3, 1.5, 1.5), rand(-4, 0))
        self.wait(4)


class SolitaireDemoScene(SolitaireScene):
    INIT_VX = -2

    def get_one_demo_card(self, corner_pos=RIGHT + UP):
        return self.point_constructor(self.JACK)(self.HEART).to_corner(corner_pos)

    def demo(self, vx, vy=0):
        card = self.get_one_demo_card()
        self.init_background(card)
        self.random_waterfall(card, vx, vy)

    def construct(self):
        self.demo(self.INIT_VX)
        self.wait(4)
