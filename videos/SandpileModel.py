# from @鹤翔万里

'''
沙堆模型
---

原理在BV1W7411C7iE
运行时需要将画质调大（推荐5120x5120）
没有进行优化，计算量较大
使用PMobject来处理像素而非直接更改frame，渲染时间也很长
'''

from manimlib.imports import *
import time

class Sandpile(Scene):
    CONFIG = {
        "d": 10,
        "size": 5120 * 1.5,
        "num": 500000,
        "maxh": 4,
        "field_size": 600
        "fromtxt": None,
    }
    def construct(self):
        self.camera.set_frame_height(self.size)
        self.camera.set_frame_width(self.size)
        points = PMobject(stroke_width=self.d)
        
        if self.fromtxt is not None:
            field = np.loadtxt(self.fromtxt, dtype=int, delimiter=",")
            print("load field from file {}".format(self.fromtxt))
            center = self.field_size / 2
        else:
            field = np.zeros((self.field_size + 10, self.field_size + 10))
            center = self.field_size / 2
            field[center, center] += self.num

            iters = 0
            t0 = time.time()
            dt0 = time.time()

            while np.max(field) >= self.maxh:
                toohigh = field >= self.maxh
                field[toohigh] -= self.maxh

                field[1:,:][toohigh[:-1,:]] += self.maxh / 4
                field[:-1,:][toohigh[1:,:]] += self.maxh / 4
                field[:,1:][toohigh[:,:-1]] += self.maxh / 4
                field[:,:-1][toohigh[:,1:]] += self.maxh / 4

                field[0:1,:] = 0
                field[:,0:1] = 0

                iters += 1
                if iters % 1000 == 0:
                    dt1 = time.time()
                    print("finish {} iterations - {:.2f}s/1000it".format(iters, dt1 - dt0))
                    dt0 = time.time()

            t1 = time.time()
            print("{} iterations in {:.2f} seconds".format(iters, t1 - t0))
            np.savetxt("sand-{}.txt".format(self.num), field, fmt="%d", delimiter=",")

        t2 = time.time()
        colors = color_gradient([BLACK, GREEN, YELLOW], 4)
        for i in range(center * 2 + 3):
            dt0 = time.time()
            for j in range(center * 2 + 3):
                if field[i][j] != 0:
                    points.add_points(
                        [np.array([(-center + i) * self.d, (center - j) * self.d, 0])],
                        color = colors[int(field[i][j])]
                    )
            dt1 = time.time()
            print("finish {} in {:.2f} seconds".format(i, dt1 - dt0))
        t3 = time.time()
        if self.fromtxt is None:
            print("{} iterations in {:.2f} seconds".format(iters, t1 - t0))
        print("render in {:.2f} seconds".format(t3 - t2))
                    
        self.add(points)
