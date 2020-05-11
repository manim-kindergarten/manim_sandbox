# from @cigar666 & @鹤翔万里
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
        'text_size': 0.30,
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


class LeftProgressBar(Scene):
    '''
    用于导出制作左侧进度条上文字的场景
    目前细节需要微调
    推荐导出5120x2880像素，带透明度的pbg图像
    '''
    CONFIG = {
        'methods_dict': {
            '序言': '0025', 
            'shift': '0210', 
            'move_to': '0300',
            'scale': '0402',
            'rotate': '0504', 
            'flip': '0712', 
            'stretch': '0901',
            'to_corner': '1014', 
            'align_to': '1129',
            'next_to': '1227', 
            'set_width\nset_height': '1500',
        },
        'total_time': '1706',
        'text_font': "Consolas",
        'text_scale_factor': 0.7,
    }

    def construct(self):
        func_time = lambda t: int(t[0:2]) * 60 + int(t[2:])
        func_loc  = lambda t: func_time(t) / func_time(total_time) * FRAME_HEIGHT * UP + FRAME_HEIGHT * DOWN / 2
        p_list = [FRAME_HEIGHT * DOWN / 2]
        for v in methods_dict.values():
            p_list.append(func_loc(v))
        p_list.append(func_loc(total_time))
        print(p_list)

        texts = VGroup(
            *[
                Text(text, color=WHITE, font=self.text_font, size=0.4, background_stroke_color=WHITE).scale(self.text_scale_factor)
                for text in methods_dict.keys()
            ]
        )
        texts[-1].become(
            VGroup(
                Text('set_width', color=WHITE, font=self.text_font, size=0.4, background_stroke_color=WHITE).scale(self.text_scale_factor),
                Text('set_height', color=WHITE, font=self.text_font, size=0.4, background_stroke_color=WHITE).scale(self.text_scale_factor)
            ).arrange(DOWN, buff=0.04)
        )
        times = VGroup(
            *[
                Text("{}:{}".format(time[:2], time[2:]), color=WHITE, font=self.text_font, size=0.4, background_stroke_color=WHITE).scale(0.55)
                for time in methods_dict.values()
            ]
        )
        
        for i in range(len(methods_dict)):
            times[i].next_to(texts[i], DOWN, buff=0.05)
            texts[i].add(times[i])
            texts[i].move_to(p_list[i + 1])

        self.add(texts)


## to be tested ##


