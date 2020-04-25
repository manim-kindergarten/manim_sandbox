# from @RY-Givenchy

#
# Copyright: 2020 niedong
# Load solitaire card from file
#

from manimlib.imports import *


class Pattern(ImageMobject):
    def __init__(self, file_name, **kwargs):
        super().__init__(file_name, **kwargs)


class Card(Pattern):
    SIGN = ["Spade", "Heart", "Club", "Diamond"]

    CONFIG = {
        "card_width": 1.25,
        "ratio": 1.396825,
    }

    def get_sign_str(self, sign):
        return self.SIGN[sign]

    def get_class_name(self):
        return self.__class__.__name__

    def get_file_name(self, sign, dim="_"):
        return self.get_sign_str(sign) + dim + self.get_class_name()

    def get_full_file_name(self, sign, folder_name, suffix):
        return os.path.join(folder_name, self.get_class_name(), self.get_file_name(sign) + suffix)

    def get_card_height(self):
        return self.card_width * self.ratio

    def __init__(self, sign, folder_name="Poker", suffix=".png", **kwargs):
        super().__init__(self.get_full_file_name(sign, folder_name, suffix), **kwargs)
        self.set_width(self.card_width, stretch=True)
        self.set_height(self.get_card_height(), stretch=True)


class Ace(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Two(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Three(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Four(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Five(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Six(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Seven(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Eight(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Nine(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Ten(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Jack(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class Queen(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)


class King(Card):
    def __init__(self, sign, **kwargs):
        super().__init__(sign, **kwargs)
