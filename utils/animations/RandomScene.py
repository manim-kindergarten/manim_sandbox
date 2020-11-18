# from widcardw
# 首先是贝多芬写的各种随机场景（年代好像都有点久远了），我也不太清楚有没有在之前加进来过

from manimlib.imports import *


def return_random_from_word(word):
    """
    This function receives a TextMobject, 
    obtains its length: 
        len(TextMobject("Some text"))
    and returns a random list, example:
    INPUT: word = TextMobjecT("Hello")
    length = len(word) # 4
    rango = list(range(length)) # [0,1,2,3]
    OUTPUT: [3,0,2,1] # Random list
    """
    rango = list(range(len(word)))
    random.shuffle(rango)
    return rango


def return_reverse_word(word):
    reversed_list = list(range(len(word)))
    reversed_list.reverse()
    return reversed_list


def return_ori_word(word):
    ori_word = list(range(len(word)))
    return ori_word


def return_random_direction(word):
    """
    This function returns a list of random UP or DOWN:
    [UP,UP,DOWN,UP,DOWN,DOWN,...]
    """
    return [random.choice([UP, DOWN]) for _ in range(len(word))]


def get_random_coord(r_x, r_y, step_x, step_y):
    """
    Given two ranges (a, b) and (c, d), this function returns an 
    intermediate array (x, y) such that "x" belongs to (a, c) 
    and "y" belongs to (b, d).
    """
    range_x = list(range(r_x[0], r_x[1], step_x))
    range_y = list(range(r_y[0], r_y[1], step_y))
    select_x = random.choice(range_x)
    select_y = random.choice(range_y)
    return np.array([select_x, select_y, 0])


def return_random_coords(word, r_x, r_y, step_x, step_y):
    """
    This function returns a random coordinate array, 
    given the length of a TextMobject
    """
    rango = range(len(word))
    return [word.get_center() + get_random_coord(r_x, r_y, step_x, step_y) for _ in rango]


class WriteRandom(LaggedStart):
    CONFIG = {
        "lag_ratio": 0.1,
        "run_time": 2.5,
        "anim_kwargs": {},
        "anim_type": Write
    }

    def __init__(self, text, **kwargs):
        digest_config(self, kwargs)
        super().__init__(*[
            self.anim_type(text[i], **self.anim_kwargs)
            for i in return_random_from_word(text)
        ])


class ReversedWrite(LaggedStart):
    CONFIG = {
        "lag_ratio": 0.1,
        "run_time": 2.,
        "anim_kwargs": {},
        "anim_type": Write
    }

    def __init__(self, text, **kwargs):
        digest_config(self, kwargs)
        super().__init__(*[self.anim_type(text[i], **self.anim_kwargs)
                           for i in return_reverse_word(text)])


class UnWrite(Write):
    CONFIG = {
        "anim_kwargs": {
            "rate_func": lambda t: smooth(1 - t)
        },
        "remover": True,
    }


class UnWriteRandom(WriteRandom):
    CONFIG = {
        "anim_kwargs": {
            "rate_func": lambda t: smooth(1 - t)
        },
        "remover": True,
    }


class EraseFromLeft(LaggedStart):
    CONFIG = {
        "lag_ratio": 0.1,
        "run_time": 2.,
        "anim_kwargs": {},
        "anim_type": UnWrite
    }

    def __init__(self, text, **kwargs):
        digest_config(self, kwargs)
        super().__init__(*[self.anim_type(text[i], **self.anim_kwargs)
                           for i in return_ori_word(text)])


class FadeInRandom(WriteRandom):
    CONFIG = {
        "anim_type": FadeIn
    }


class FadeOutRandom(WriteRandom):
    CONFIG = {
        "anim_type": FadeOut
    }


class GrowRandom(WriteRandom):
    CONFIG = {
        "anim_type": GrowFromCenter
    }


class UnGrowRandom(GrowRandom):
    CONFIG = {
        "anim_kwargs": {
            "rate_func": lambda t: smooth(1 - t),
        },
        "remover": True,
    }


class FadeInFromRandom(LaggedStart):
    CONFIG = {
        "lag_ratio": 0.08,
        "anim_type": FadeInFrom,
        "anim_kwargs": {}
    }

    def __init__(self, text, **kwargs):
        digest_config(self, kwargs)
        super().__init__(*[
            self.anim_type(text[i], d, **self.anim_kwargs)
            for i, d in zip(return_random_from_word(text), return_random_direction(text))
        ])


class FadeOutFromRandom(FadeInFromRandom):
    CONFIG = {
        "anim_type": FadeOutAndShiftDown
    }


class GrowFromRandom(LaggedStart):
    CONFIG = {
        "lag_ratio": 0.2,
        "anim_kwargs": {}
    }

    def __init__(self, text, r_x=[-2, 3], r_y=[-2, 3], step_x=1, step_y=1, **kwargs):
        digest_config(self, kwargs)
        super().__init__(*[
            GrowFromPoint(text[i], d, **self.anim_kwargs)
            for i, d in zip(return_random_from_word(text), return_random_coords(text, r_x, r_y, step_x, step_y))
        ])


class UnGrowFromRandom(GrowFromRandom):
    CONFIG = {
        "anim_kwargs": {
            "rate_func": lambda t: smooth(1 - t)
        },
        "remover": True
    }


# 贝多芬写的使用例
class WriteRandomScene(Scene):
    def construct(self):
        text = TextMobject("This is some text").set_width(FRAME_WIDTH - 0.5)
        self.wait(3)
        # Why text[0]?
        # answer: https://www.youtube.com/watch?v=qfifBmYTEfA
        self.play(WriteRandom(text[0]))
        self.wait()
        self.play(UnWriteRandom(text[0]))
        self.wait(3)


class FadeFromRandomScene(Scene):
    def construct(self):
        text = TextMobject("This is some text").set_width(FRAME_WIDTH - 0.5)
        # Why text[0]?
        # answer: https://www.youtube.com/watch?v=qfifBmYTEfA
        self.play(FadeInFromRandom(text[0]))
        self.wait()
        self.play(FadeOutFromRandom(text[0]))
        self.wait(3)


class GrowFromRandomScene(Scene):
    def construct(self):
        text = TextMobject("This is some text").set_width(FRAME_WIDTH - 0.5)
        # Why text[0]?
        # answer: https://www.youtube.com/watch?v=qfifBmYTEfA
        self.play(GrowFromRandom(text[0]))
        self.wait()
        self.play(UnGrowFromRandom(text[0]))
        self.wait(3)


class FadeRandomScene(Scene):
    def construct(self):
        text = TextMobject("This is some text").set_width(FRAME_WIDTH - 0.5)
        # Why text[0]?
        # answer: https://www.youtube.com/watch?v=qfifBmYTEfA
        self.play(FadeInRandom(text[0]))
        self.wait()
        self.play(FadeOutRandom(text[0]))
        self.wait(3)


class GrowRandomScene(Scene):
    def construct(self):
        text = TextMobject("This is some text").set_width(FRAME_WIDTH - 0.5)
        # Why text[0]?
        # answer: https://www.youtube.com/watch?v=qfifBmYTEfA
        self.play(GrowRandom(text[0]))
        self.wait()
        self.play(UnGrowRandom(text[0]))
        self.wait(3)


# 仿照贝多芬，用于3D场景的方法（似乎只对球的效果好一点）

# 获取每一片的运动方向
def rtn_direction(obj, scale_factor, about_point):
    direction = scale_factor * (obj.get_center() - about_point)
    return direction


class FadeInFromLargeByRandomPieces(LaggedStart):
    CONFIG = {
        "scale_factor": 1,
        "about_point": ORIGIN,
        "rate_func": running_start,
        "run_time": 2,
        "anim_type": FadeInFrom,
        "anim_kwargs": {},
        "lag_ratio": 0.012
    }

    def __init__(self, mobject, **kwargs):
        digest_config(self, kwargs)
        super().__init__(*[
            self.anim_type(mobject[i],
                           direction=rtn_direction(mobject[i],
                                                   self.scale_factor,
                                                   self.about_point),
                           run_time=np.clip(np.random.random()*self.run_time, 0.05, 1),
                           **self.anim_kwargs)
            for i in return_random_from_word(mobject)
        ])


class FadeOutAndShiftOutByRandomPieces(FadeInFromLargeByRandomPieces):
    CONFIG = {
        "scale_factor": 1,
        "about_point": ORIGIN,
        "rate_func": exponential_decay,
        "run_time": 2,
        "anim_type": FadeOutAndShift,
        "anim_kwargs": {},
        "lag_ratio": 0.012,
        "remover": True,
    }


class GrowFromCenterByRandomPieces(LaggedStart):
    CONFIG = {
        "about_point": ORIGIN,
        "rate_func": running_start,
        "run_time": 3,
        "anim_type": GrowFromPoint,
        "anim_kwargs": {},
        "lag_ratio": 0.012
    }

    def __init__(self, mobject, **kwargs):
        digest_config(self, kwargs)
        super().__init__(*[
            self.anim_type(mobject[i], point=self.about_point,
                           **self.anim_kwargs
                           )
            for i in return_random_from_word(mobject)
        ])


class ShrinkToCenterByRandomPieces(GrowFromCenterByRandomPieces):
    CONFIG = {
        "about_point": ORIGIN,
        "run_time": 3,
        "anim_type": GrowFromPoint,
        "anim_kwargs": {
            "rate_func": lambda t: 1 - t ** 2,
        },
        "lag_ratio": 0.012,
        "remover": True,
    }


# 使用例
class Example(SpecialThreeDScene):
    def construct(self):
        self.set_camera_to_default_position()
        sp = Sphere(radius=2).set_fill(opacity=0.4)
        self.play(FadeInFromLargeByRandomPieces(sp))
        self.wait()
        self.play(FadeOutAndShiftOutByRandomPieces(sp))
        self.wait()
