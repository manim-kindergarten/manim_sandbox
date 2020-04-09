# from @cigar666
from manimlib.imports import *

class VideoProgressBar(VGroup):

    CONFIG = {
        'methods_dict': {
            '序言': '0025',
            'shift+move_to': '0210',
            'scale': '0402',
            'rotate': '0504',
            'flip': '0712',
            'stretch': '0901',
            'to_corner': '1014',
            'align_to': '1129',
            'next_to': '1227',
            'set_width+set_height': '1500',
            ' ': '1659'},
        'total_time': '1724',
        'text_font': "思源黑体 Bold",
        'color_list': [BLUE, PINK, RED, ORANGE, GREEN],
        'bar_width': 20,
        'text_size': 0.15,
    }

    def __init__(self, **kwargs):

        VGroup.__init__(self, **kwargs)

        func_time = lambda t: int(t[0:2]) * 60 + int(t[2:])
        func_loc = lambda t: func_time(t)/func_time(self.total_time) * FRAME_WIDTH * RIGHT + FRAME_WIDTH * LEFT / 2

        p_list = [FRAME_WIDTH * LEFT / 2]
        for v in self.methods_dict.values():
            p_list.append(func_loc(v))
        p_list.append(func_loc(self.total_time))

        self.colors = color_gradient(self.color_list, len(self.methods_dict)+1)

        self.lines = VGroup(*[Line(p_list[i], p_list[i+1]-0.02*RIGHT, color=self.colors[i], stroke_width=self.bar_width) for i in range(len(self.methods_dict)+1)])
        self.lines.to_edge(DOWN * 0.22, buff=1)
        self.texts = VGroup(*[Text(t, color=WHITE, font=self.text_font, size=self.text_size) for t in self.methods_dict.keys()], plot_depth=1)

        for i in range(len(self.methods_dict)):
            self.texts[i].move_to(self.lines[i+1])

        self.add(self.lines, self.texts)

## to be tested ##


