# from @cigar666
# 曼德勃罗集
# Warning: 这个代码实现的不好，不要轻易尝试

from manimlib.imports import *
from datetime import *

class Mandelbrot(Scene):
    def construct(self):
        st_t = datetime.now()
        scale = 2
        iter_func = lambda z, c: z ** 2 + c
        iter_num = 128
        colors = color_gradient(['#182AFF', WHITE, BLACK], iter_num + 1)
        def get_color(c):
            z = complex(0, 0)
            num = 0
            while abs(z) < 2 and num < iter_num:
                z = iter_func(z, c)
                num += 1
            return colors[num]
        x_pn , y_pn = 1440, 1440
        sp = Square(stroke_width=0, fill_color=RED, fill_opacity=1).scale(4 * scale / y_pn / 2 * 1.12)
        for i in range(int(y_pn / 2) + 1):
            for j in range(x_pn):
                lij = (-x_pn / 2 + j) / x_pn * 4 * scale * RIGHT + \
                      (-y_pn / 2 + i) / y_pn * 4 * scale * UP
                c = complex(*(lij[:2] / scale)) / 1.6 - 0.6
                self.add(sp.copy().set_fill(color=get_color(c)).move_to(lij))
                self.add(sp.copy().set_fill(color=get_color(c)).move_to(lij * np.array([1, -1, 0])))
                if j == 1:
                    print('i = %d, j = %d\t' %(i, j), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        ed_t = datetime.now()
        tot_t = (ed_t - st_t).total_seconds()
        print('Total time : %d s' %tot_t)

        self.wait()