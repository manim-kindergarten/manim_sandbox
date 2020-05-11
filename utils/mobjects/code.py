# from @鹤翔万里

from manimlib.imports import *

class Code(Text):
    CONFIG = {
        'font'         : 'Monaco for Powerline',
        'size'         : 1,
        'color'        : WHITE,
        'stroke_color' : WHITE,
        'stroke_weight': 0,
    }

    def __init__(self, *text, **config):
        res_text = ''
        for each_text in text:
            res_text += each_text + '\n'
        super(Code, self).__init__(res_text, **config)
        self.set_stroke(self.stroke_color, self.stroke_weight)

class LinedCode(Text):
    CONFIG = {
        'font'         : 'Consolas',
        'size'         : 1,
        'color'        : WHITE,
        'stroke_color' : WHITE,
        'stroke_weight': 0,
        'ln_color'     : GRAY,
    }

    def __init__(self, *text, **config):
        digest_config(self, config)
        res_text = ''
        i = 1
        for each_text in text:
            res_text += str(i) + '  ' + each_text + '\n'
            self.t2c['{}  '.format(i)] = self.ln_color
            i = i + 1
        super(LinedCode, self).__init__(res_text, **config)
        self.set_stroke(self.stroke_color, self.stroke_weight)