##@有一种悲伤叫颓废
from manimlib.imports import *
import math


class ShiftAndMoveto(Scene):
    CONFIG = {
        'camera_config': {'background_color': WHITE},
    }

    def mob_moveto(self, mob, pos, run_time=1, start_stroke=10, fade_width=0.05, fade_opacity=0.01):
        vec = pos-mob.get_center()
        dist = get_distance(pos, mob.get_center())
        n = int(dist/0.1)
        for i in range(n):
            path = Line(mob.get_center(),mob.get_center()+vec/n, stroke_width=start_stroke, stroke_opacity=1 ,stroke_color='#FFA500')\
                .add_updater(lambda p,dt:p.set_stroke(width=p.get_stroke_width()-fade_width, opacity=p.get_stroke_opacity()-fade_opacity))
            self.add(path)
            self.play(
                mob.shift, vec/n, 
                rate_func=linear, 
                run_time=run_time/n, 
                )

    def construct(self):
        numberplane = NumberPlane().set_stroke(opacity=0.5)
        self.add(numberplane)

        axes = ThreeDAxes(
            color=BLACK, 
            x_min=-FRAME_X_RADIUS, x_max=FRAME_X_RADIUS,
            y_min=-FRAME_Y_RADIUS, y_max=FRAME_Y_RADIUS,
            number_line_config={"color": BLACK}
            ).set_stroke(width=2)
        self.add(axes)
        

        captions = [
            "shift函数是指对一个mobject进行位移",
            "Vector=[-2,+2,0]",
            "Vector=[-2,-2,0]",
            "Vector=[+2,-2,0]",
            "Vector=[+2,+2,0]",
            "mob.shift([-2,+2,0])",
            "mob.shift([-2,-2,0])",
            "mob.shift([+2,-2,0])",
            "mob.shift([+2,+2,0])",
            "这个例子的轨迹是正方形",
            "轨迹是圆形呢？",
            "显然用颓废法(微分位移)，在圆上取多个点即可",
            "用颓废法，可以用shift实现任意轨迹的运动",
            "move_to函数的功能是对mobject的位置进行设定",
            "mob.move_to(point_or_mobject=[1,-2,0])",
            "mob.move_to(point_or_mobject=[2,2,0],aligned_edge=UP)",
            "mob.move_to(point_or_mobject=[2,2,0],coor_mask=[1,0,0])",
        ]
        text = [
            Text(i, font="Source Han Sans Bold", color=BLACK, plot_depth=2).scale(1/3).to_edge(DOWN)\
                for i in captions
            ]
        text[0][0:5].set_color('#FFA500')
        text[0][12:19].set_color('#7A7A7A')
        text[0][21:23].set_color('#EE0000')
        [text[1+i][0:6].set_color('#F08080') for i in range(4)]
        [text[1+i][8:-1].set_color('#7A7A7A') for i in range(4)]
        text[13][0:7].set_color('#FFA500')
        text[13][14:21].set_color('#7A7A7A')
        text[14][4:11].set_color('#FFA500')
        text[14][12:28].set_color('#7A7A7A')
        text[15][4:11].set_color('#FFA500')
        text[15][12:28].set_color('#7A7A7A')
        text[15][37:49].set_color('#7A7A7A')
        text[16][4:11].set_color('#FFA500')
        text[16][12:28].set_color('#7A7A7A')
        text[16][37:46].set_color('#7A7A7A')

        n = 4
        arrow = VGroup(
            *[
                Arrow(
                    [2*np.cos(i*TAU/n),2*np.sin(i*TAU/n),0],
                    [2*np.cos((i+1)%n*TAU/n),2*np.sin((i+1)%n*TAU/n),0],
                    max_tip_length_to_length_ratio=0.3/2/np.sqrt(2),
                    color='#7A378B',
                    buff=0,
                    ) for i in range(n)
            ])

        [text[i+1].next_to([UR,UL,DL,DR][i],[UR,UL,DL,DR][i],buff=0) for i in range(4)]
        
        textbg = [
            BackgroundRectangle(i,color=WHITE,plot_depth=1)\
                for i in text
        ]
        
        self.play(ShowCreation(textbg[0]),ShowCreation(text[0]))
        self.wait()

        text2 = VGroup(
            Text("mob.shift(*vectors)", font="Source Han Sans Bold", color=BLACK, plot_depth=2),
            Text("vectors是一个位移起点到终点的向量", font="Source Han Sans Bold", color=BLACK, plot_depth=2),
            plot_depth=2,
            ).scale(1/3).arrange(DOWN,aligned_edge=LEFT)
        text2bg = BackgroundRectangle(text2,plot_depth=1).set_fill(color='#8F8F8F',opacity=0.3)
        text2g = Group(text2,text2bg)
        text2[0][4:9].set_color('#FFA500')
        text2[0][11:18].set_color('#EE0000')
        text2[1][0:7].set_color('#EE0000')
        self.play(FadeInFromDown(text2g))
        self.wait(2)
        self.play(FadeOutAndShiftDown(text2g))
        
        self.play(ShowCreation(arrow))

        self.add(*textbg[1:5])
        self.play(*[Write(text[1+i]) for i in range(4)],run_time=2)
        self.wait(2)
        

        mob = VGroup(
            Dot(color='#EE7AE9', plot_depth=2).scale(1.6),
            Dot(color='#EE7AE9', plot_depth=1, fill_opacity=0.5).scale(2.5)
            ).move_to(RIGHT*2)
        
        self.play(ShowCreation(mob))

        
        n = 4
        text_old, textbg_old = text[0], textbg[0]
        for i in range(n):
            self.play(
                FadeOut(text[1+i]),
                FadeOut(textbg[1+i]),
                FadeOut(text_old),
                FadeOut(textbg_old),
                FadeOut((Dot(UR*5),text[4+i][11:18])[i!=0]),
                ReplacementTransform(arrow[i],text[5+i][11:18]),
                ReplacementTransform(text_old,VGroup(text[5+i][0:11],text[5+i][18:],plot_depth=2)),
                ReplacementTransform(textbg_old,textbg[5+i]),
                )
            text_old, textbg_old = VGroup(text[5+i][0:11],text[5+i][18:],plot_depth=2), textbg[5+i]
            self.wait()
            self.mob_moveto(mob,[2*np.cos((i+1)*TAU/n),2*np.sin((i+1)*TAU/n),0],run_time=4/n)
            
        
        
        for i in range(3):
            self.play(
                ReplacementTransform(text[8+i],text[9+i]),
                ReplacementTransform(textbg[8+i],textbg[9+i]),
                )
            self.wait(2)
        n=60
        for i in range(n):
            self.mob_moveto(mob,[2*np.cos((i+1)*TAU/n),2*np.sin((i+1)*TAU/n),0],run_time=4/n)
        

        self.play(
                ReplacementTransform(text[11],text[12]),
                ReplacementTransform(textbg[11],textbg[12]),
                )
        
        
        svgmob = SVGMobject(r"C:\Users\Administrator\Desktop\HomeworkVol04\投币.svg",color=BLACK)\
            .scale(2.5).set_fill(opacity=0)
        #self.add(svgmob)
        
        path = svgmob.family_members_with_points()[0]
        path = VMobject()
        for sp in svgmob.family_members_with_points():
            path.append_points(sp.points)

        mob.move_to(path.point_from_proportion(0))

        n=300
        for i in range(n):
            self.mob_moveto(
                mob,
                path.point_from_proportion((i+1)%n/n),
                run_time=6/n,
                start_stroke=6,
                fade_width=0.01,
                fade_opacity=0.001,
                )
        self.wait()

        
        self.play(
            ReplacementTransform(text[12],text[13]),
            ReplacementTransform(textbg[12],textbg[13]),
            )
        self.wait()

        text3 = VGroup(
            Text("mob.move_to(point_or_mobject,aligned_edge,coor_mask)", font="Source Han Sans Bold", color=BLACK, plot_depth=2),
            Text("point_or_mobject是一个坐标或物体", font="Source Han Sans Bold", color=BLACK, plot_depth=2),
            Text("aligned_edge指与point_or_mobject对齐的边，默认为ORIGIN", font="Source Han Sans Bold", color=BLACK, plot_depth=2),
            Text("coor_mask定义了基的长度，默认为[i,j,k]=[1,1,1]", font="Source Han Sans Bold", color=BLACK, plot_depth=2),
            Text("当某个分量为0，point_or_mobject的对应分量不起作用", font="Source Han Sans Bold", color=BLACK, plot_depth=2),
            plot_depth=2,
            ).scale(1/3).arrange(DOWN,aligned_edge=LEFT)
        text3bg = BackgroundRectangle(text3,plot_depth=1).set_fill(color='#8F8F8F',opacity=0.3)
        text3g = Group(text3,text3bg)
        text3[0][4:11].set_color('#FFA500')
        text3[0][12:28].set_color('#EE0000')
        text3[0][29:41].set_color('#EE0000')
        text3[0][42:51].set_color('#EE0000')
        text3[1][0:16].set_color('#EE0000')
        text3[2][0:12].set_color('#EE0000')
        text3[2][14:30].set_color('#EE0000')
        text3[3][0:9].set_color('#EE0000')
        text3[4][8:24].set_color('#EE0000')
        self.play(FadeInFromDown(text3g))
        self.wait(7)
        self.play(FadeOutAndShiftDown(text3g))
        self.wait()
        

        self.play(
            ReplacementTransform(text[13],text[14]),
            ReplacementTransform(textbg[13],textbg[14]),
            )
        self.wait()
        
        dot = Dot([1,-2,0],color='#A0522D')
        self.play(ShowCreation(dot))
        self.wait()
        self.mob_moveto(mob,[1,-2,0],run_time=2)
        self.wait()
        self.play(
            ReplacementTransform(text[14],text[15]),
            ReplacementTransform(textbg[14],textbg[15]),
            )
        self.wait()
        
        dot2 = Dot([2,2,0],color='#A0522D')
        self.play(ShowCreation(dot2))
        self.wait()
        self.mob_moveto(mob,[2,2-BackgroundRectangle(mob).get_height()/2,0],run_time=2)
        self.wait()

        self.play(
            ReplacementTransform(text[15],text[16]),
            ReplacementTransform(textbg[15],textbg[16]),
            )
        self.wait()

        dot3 = Dot([2,0,0],color='#A0522D')
        self.play(ShowCreation(dot3))
        self.wait()
        self.mob_moveto(mob,[2,0,0],run_time=2)

        self.wait(3)
