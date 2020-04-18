# from @鹤翔万里

from manimlib.mobject.svg.text_mobject import Text
from manimlib.utils.color import *
from manimlib.constants import *

class ColorText(Text):
    CONFIG = {
        "size": 0.4,
        "font": "Consolas",
        "t2c": {
            '"': YELLOW_E,
            'np': BLACK,
            'array': BLUE_D,
        },
        "color": DARK_GRAY,
    }
    def __init__(self, color, name=None, **kwargs):
        if name:
            Text.__init__(self, name, color=color, **kwargs)
        else:
            if isinstance(color, str):
                Text.__init__(self, '"' + color + '"', color=color, **kwargs)
            else:
                name = 'np.array([{}, {}, {}])'.format(
                    str(int(color[0])).rjust(3), 
                    str(int(color[1])).rjust(3), 
                    str(int(color[2])).rjust(3)
                )
                Text.__init__(self, name, color=rgb_to_color(color/255), **kwargs)
                self[10:name.index(",")].set_color(RED)
                self[name.index(",")+2:name.index(",", name.index(",")+1)].set_color(GREEN)
                self[name.index(",", name.index(",")+1)+2:-2].set_color(BLUE)
