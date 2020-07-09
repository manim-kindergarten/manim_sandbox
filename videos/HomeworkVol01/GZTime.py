# from @GZTime
# homework vol 01
from manimlib.imports import *

class TriangleSquare(Scene):
    def construct(self):
        # 新建一个三角形,假设称之为三角形ABC
        triangle = Polygon(
            np.array([-1.4,-1.6,0]),
            np.array([2,0.7,0]),
            np.array([-0.7,1.5,0])
        ).scale(0.75)

        squares = []
        points = []
        ver_points = []

        # 依次取出三个点中的两个(可以理解为一条边的两个端点)
        for i in adjacent_pairs(triangle.get_vertices()):
            # 取这一边的中点坐标(i[0]和i[1]均理解为向量)
            ver = (i[0]+i[1])/2
            # squares 是将要绘制的正方形列表
            squares.append(
                Square(side_length=Line(i[0],i[1]).get_length())        # 确定边长构造三角形
                .move_to(ver + rotate(i[0]-ver,math.pi/2))              
                # move_to函数会将正方形中心对齐至某一点
                # 于是计算得到正方形中心
                .rotate(math.atan((i[1][1]-i[0][1])/(i[1][0]-i[0][0])))
                # 旋转时角度利用斜率进行计算
                .set_color(BLUE)
            )
            # 以下两个列表是添加正方形除了已知两点之外的两点
            # 通过这样方便我们记录和构造剩余的图形
            points.append(
                i[0] + rotate(i[0] - i[1],math.pi/2)
            )
            ver_points.append(
                i[1] + rotate(i[1] - i[0],math.pi/2,IN)
            )

        triangles = []
        order = 0

        for i in triangle.get_vertices():
            triangles.append(
                [Polygon(i,points[order],ver_points[(order + 2)%3])
                .set_color(YELLOW),i]
            )
            order += 1

        self.wait()
        self.play(ShowCreation(triangle))
        self.wait()
        self.play(*[ShowCreation(i) for i in squares])
        self.wait()
        self.play(*[ShowCreation(i[0]) for i in triangles])
        self.play(*[FadeOut(i) for i in squares])
        self.play(*[WiggleOutThenIn(i[0],run_time=1) for i in triangles])
        self.play(*[Rotating(
            i[0],radians=math.pi/2,
            about_point=i[1],axis=IN,
            rate_func=lambda dt: smooth(dt,inflection=7)
            ,run_time=2
            ) for i in triangles])
        self.wait()

        fill_triangle = [triangle.copy().set_fill(color=ORANGE,opacity=0.8)]
        for i in triangles:
            fill_triangle.append(i[0].copy().set_fill(color=ORANGE,opacity=0.8))

        self.play(*[FadeIn(i) for i in fill_triangle])

        texts = [TexMobject("S_1=").set_color(ORANGE).to_corner(LEFT+TOP)]
        texts.append(TexMobject("S_2=").set_color(ORANGE).next_to(texts[0]))
        texts.append(TexMobject("S_3=").set_color(ORANGE).next_to(texts[1]))
        texts.append(TexMobject("S_4").set_color(ORANGE).next_to(texts[2]))

        self.play(*[Transform(fill_triangle[i],texts[i]) for i in range(0,4)])
