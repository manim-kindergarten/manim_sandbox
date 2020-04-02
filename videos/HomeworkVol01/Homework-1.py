#from @PeterSardine
from manimlib.imports import *

class Main(Scene):
    def construct(self):
        title = Text(r'Manim Homework I').shift(UP)\
            .set_color(ORANGE).set_opacity(0.5)
        signature = Text(r'by  PeterSardine').next_to(title, DOWN).scale(0.5)\
            .set_color(ORANGE).set_opacity(0.5)
        beginning = VGroup(title, signature)

        self.play(Write(title), rate_func=smooth)
        self.play(Write(signature), rate_func=smooth)
        self.wait(2)

        triangle = Polygon(
            np.array([-1,-1,0]),
            np.array([1.2,0.5,0]),
            np.array([-0.5,1,0])
            )
        
        self.play(ReplacementTransform(beginning, triangle))
        self.wait(1)

        squares = VGroup()
        points = []
        for pair in adjacent_pairs(triangle.get_vertices()):
            from_point, to_point = pair
            mid = (from_point+to_point)/2
            center = mid + rotate(from_point-mid, np.pi/2)
            points.extend([
                rotate(to_point-from_point, -np.pi/2) + from_point,
                rotate(to_point-from_point, -np.pi/2) + to_point,
            ])
            squares.add(Square(
                side_length = np.linalg.norm(to_point-from_point),
                color=BLUE,
                fill_opacity=0.5
            ).move_to(center).rotate(np.arctan((to_point[1]-from_point[1])/(to_point[0]-from_point[0])))
            )

        self.play(ShowCreation(squares))
        self.wait(1)

        triangles = VGroup()
        for i in range(3):
            triangles.add(
                Polygon(triangle.get_vertices()[i], points[2*i-1], points[2*i],\
                    color=RED, fill_opacity=0.5)
            )
        labels = VGroup()
        labels.add(TexMobject('S_{1}', color=WHITE))
        labels.add(*[
            TexMobject('S_%d'%i, color=WHITE)
            for i in range(3)
        ])
        labels.add_updater(
            lambda m:[m[i+1].move_to(triangles[i].get_center())for i in range(3)]
        )
        self.play(ShowCreation(triangles))
        self.play(Write(labels))
        self.play(*[Rotate(triangles[i], np.pi/2, about_point=triangle.get_vertices()[i])for i in range(3)],\
            FadeOut(squares))

        labels.suspend_updating()
        eq = TexMobject('S_0=S_1=S_2=S_3', color= WHITE)
        for i in triangles:
            self.play(ReplacementTransform(i, triangle))
        self.play(ReplacementTransform(labels, eq))
        self.play(eq.shift, UP*1.5)
        self.wait(2)

            
            