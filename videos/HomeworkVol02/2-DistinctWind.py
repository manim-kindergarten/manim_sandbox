# from @DistinctWind

from manimlib.imports import *
from numpy import *
class BeginScene(Scene) :
    def construct(self) :
        title = Text("Manim Homework Vol.2", font='微软雅黑', stroke_width=0)
        author = Text("Made by @DistinctWind", font='微软雅黑', stroke_width=0).scale(0.5)
        title.move_to(UP*0.5)
        author.move_to(DOWN*0.5)
        self.play(Write(title))
        self.play(Write(author))
        self.wait(2)
        
        title_and_author = VGroup(title, author)
        main = Text("自然数立方和公式证明", font='微软雅黑', stroke_width=0)
        self.play(
            FadeOut(title_and_author)
        )
        self.play(
            Write(main),
            run_time=2
        )
        self.wait(2)
        self.play(FadeOutAndShift(main))
        self.wait(2)

class main(Scene) :
    @staticmethod
    def Build_numbers() :
        lines = []
        for line_num in range(1, 4) :
            line = []
            mystr = lambda x: 'n' if x==1 else str(x)+'n'
            for col_num in range(1, 4) :
                line.append(TexMobject(str(line_num*col_num)))
            line.append(TexMobject('\\cdots'))
            line.append(TexMobject(mystr(line_num)))
            lines.append(line)
        lines.append([TexMobject('\\vdots'), TexMobject('\\vdots'), TexMobject('\\vdots'), TexMobject('\\ddots'), TexMobject('\\vdots')])
        lines.append([TexMobject('n'), TexMobject('2n'), TexMobject('3n'), TexMobject('\\cdots'), TexMobject('n^2')])
        return lines
    
    def construct(self) :
        formala_text = Text('自然数立方和公式', font='微软雅黑', stroke_width=0).scale(0.7)
        equal = TexMobject('=')
        formala_left = TexMobject('(1+2+\\dots +n)^2').next_to(equal, LEFT, buff=0.5).set_color(YELLOW)
        formala_right = TexMobject('1^3+2^3+3^3+\\dots +n^3').next_to(equal, RIGHT, buff=0.5).set_color(BLUE)
        formala_text.to_edge(UL)
        self.play(Write(formala_text))
        self.play(
            Write(formala_left),
            Write(formala_right),
            Write(equal)
        )
        self.wait(3)
        self.play(
            FadeOut(formala_text),
            FadeOut(formala_left),
            FadeOut(formala_right), 
            FadeOut(equal)
        )
        self.wait()

        lines = self.Build_numbers()
        lines_group_list = [VGroup(*lines[0]).arrange(buff=1).to_edge(UP)]
        for line_num in range(1, 5) :
            for col_num in range(5) :
                lines[line_num][col_num].move_to(lines[line_num-1][col_num].get_center()+DOWN)
            lines_group_list.append(VGroup(*lines[line_num]))
        lines_group = VGroup(*lines_group_list)

        col_group_list = []
        for col_num in range(5) :
            col_list = []
            for line_num in range(5) :
                col_list.append(lines[line_num][col_num])
            col_group_list.append(VGroup(*col_list))
        col_group = VGroup(*col_group_list)

        all = lines_group
        all.move_to(ORIGIN)
        for line in range(5) :
            self.play(Write(lines_group_list[line]))
        self.wait(2)

        rec1=SurroundingRectangle(all)
        self.play(ShowCreation(rec1))
        aim = Text("求和", font="微软雅黑", stroke_width=0).scale(0.5).next_to(all, DOWN, buff=0.5)
        self.play(ReplacementTransform(rec1, aim))
        self.wait(2)
        self.play(
            FadeOut(aim),
            ApplyMethod(all.to_corner, UL)
        )
        self.wait()

        line_rec_list = []
        line_sum_list = []
        mystr = lambda x: '(1+2+\\cdots +n)' if x==1 else str(x)+'(1+2+\\cdots +n)'
        for line_num in range(3) :
            rec = SurroundingRectangle(lines_group_list[line_num])
            s = TexMobject(mystr(line_num+1)).move_to(rec.get_center()+RIGHT*6.5).set_color(YELLOW)
            line_rec_list.append(rec1)
            line_sum_list.append(s)
            self.play(ShowCreation(rec))
            self.wait()
            self.play(ReplacementTransform(rec, s))
            self.wait()
        #lines[3]
        rec = SurroundingRectangle(lines_group_list[3])
        s = TexMobject('\\vdots').move_to(rec.get_center()+RIGHT*6.5).set_color(YELLOW)
        line_rec_list.append(rec)
        line_sum_list.append(s)
        self.play(ShowCreation(rec))
        self.wait()
        self.play(ReplacementTransform(rec, s))
        self.wait()
        #lines[4]
        rec = SurroundingRectangle(lines_group_list[4])
        s = TexMobject('n(1+2+\\cdots +n)').move_to(rec.get_center()+RIGHT*6.5).set_color(YELLOW)
        line_rec_list.append(rec)
        line_sum_list.append(s)
        self.play(ShowCreation(rec))
        self.wait()
        self.play(ReplacementTransform(rec, s))
        self.wait()

        all_rec = SurroundingRectangle(VGroup(*line_sum_list))
        self.play(ShowCreation(all_rec))
        formala = TexMobject('(1+2+\\cdots +n)+2(1+2+\\cdots +n)+3(1+2+\\cdots +n)+\\cdots+n(1+2+\\cdots +n)').scale(0.7).to_edge(DOWN).shift(UP*0.5).set_color(YELLOW)
        self.play(ReplacementTransform(all_rec, formala))
        self.wait(3)
        formala.target = TexMobject('(1+2+\\cdots +n)(1+2+\\cdots +n)').to_edge(DOWN).shift(UP*0.5).set_color(YELLOW)
        self.play(MoveToTarget(formala))
        self.wait(2)
        formala.target = TexMobject('(\\sum^n_{i=1} i)(\\sum^n_{i=1} i)').to_edge(DOWN).shift(UP*0.5).set_color(YELLOW)
        self.play(MoveToTarget(formala))
        self.wait()
        formala.target = TexMobject('(\\sum^n_{i=1} i)^2').to_edge(DOWN).shift(UP*0.5).set_color(YELLOW)
        self.play(MoveToTarget(formala))
        self.wait(2)
        self.play(ApplyMethod(formala.to_corner, DL))
        self.wait()
        self.play(
            *[FadeOut(x) for x in line_sum_list]
        )
        self.wait()

        polygon_list = [SurroundingRectangle(lines_group_list[0][0], buff=0.3).set_color(BLUE)]
        judge = lambda x: 0.2 if x==4 else 0.3
        for i in range(1, 5) :
            polygon_list.append(
                Polygon(
                    lines[i][0].get_corner(UL)+UL*0.3,
                    lines[i][0].get_corner(DL)+DL*0.3,
                    lines[i][i].get_corner(DR)+DR*judge(i),
                    lines[0][i].get_corner(UR)+UR*0.3,
                    lines[0][i].get_corner(UL)+UL*0.3,
                    lines[i][i].get_corner(UL)+UL*judge(i),
                    lines[i][0].get_corner(UL)+UL*0.3,
                )
            )
        
        cor_sum_list = [
            TexMobject('1').next_to(lines[0][4], buff=4.25).set_color(BLUE),
            TexMobject('2\\times 2(1)+2^2'),
            TexMobject('2\\times 3(1+2)+3^2'),
            TexMobject('\\vdots'),
            TexMobject('2\\times n\\left[ 1+2+\\cdots +(n-1) \\right] +n^2'),
        ]
        for i in range(1, 5):
            cor_sum_list[i].move_to(cor_sum_list[i-1].get_center()+DOWN).set_color(BLUE)
        for i, f, pol in zip(range(5), cor_sum_list, polygon_list) :
            self.play(ShowCreation(pol))
            self.wait()
            self.play(ReplacementTransform(pol, f))
            self.wait()
        c = cor_sum_list[4]
        c_target_list = [
            TexMobject('2\\times n \\dfrac{\\left[1+(n-1) \\right] (n-1)}{2}+n^2'),
            TexMobject('2\\times n \\dfrac{n(n-1)}{2}+n^2'),
            TexMobject('n^2(n-1)+n^2'),
            TexMobject('n^3-n^2+n^2'),
            TexMobject('n^3'),
        ]
        for item in c_target_list :
            item.move_to(c.get_center()).set_color(BLUE)
        self.wait()
        for t in c_target_list :
            c.target = t
            self.play(MoveToTarget(c))
            self.wait(2)
        cor_sum_target_list = [
            TexMobject(str(x)+'^3').move_to(cor_sum_list[x-1].get_center()).set_color(BLUE) for x in range(1,4)
        ]
        for i, t in zip(range(3), cor_sum_target_list) :
            cor_sum_list[i].target = t
        self.wait()
        self.play(
            *[MoveToTarget(x) for x in [cor_sum_list[y] for y in range(3)] ]
        )
        self.wait()
        
        s = SurroundingRectangle(
            VGroup(
                *list(cor_sum_list)
            )
        ).set_color(BLUE)
        self.play(ShowCreation(s))

        r_formala = TexMobject('1^3+2^3+3^3+\\cdots +n^3').to_edge(DOWN).shift(UP*0.5).set_color(BLUE)
        r_formala.target=TexMobject('\\sum^n_{i=1}i^3').to_edge(DOWN).shift(UP*0.5).set_color(BLUE)
        self.wait(2)
        self.play(ReplacementTransform(s, r_formala))
        self.wait(2)
        self.play(MoveToTarget(r_formala))

        equal.next_to(formala, RIGHT, buff=0.5)
        r_formala.target = r_formala.copy().next_to(equal, buff=0.5).set_color(BLUE)
        self.play(
            FadeIn(equal),
            MoveToTarget(r_formala)
        )
        self.wait(2)
        formala_group = VGroup(formala, equal, r_formala)

        self.play(
            ApplyMethod(formala_group.move_to, ORIGIN),
            FadeOut(all),
            *[FadeOut(f) for f in cor_sum_list]
        )
        self.wait(2)
        formala.target = TexMobject('(1+2+3+\\cdots +n)^2').next_to(equal, LEFT, buff=0.5).set_color(YELLOW)
        r_formala.target = TexMobject('1^3+2^3+3^3+\\cdots +n^3').next_to(equal, RIGHT ,buff=0.5).set_color(BLUE)
        self.play(
            MoveToTarget(formala),
            MoveToTarget(r_formala)
        )
        self.wait()
        qed = TexMobject('QED').next_to(equal, DOWN, buff=1.5).scale(1.25)
        qed.set_color_by_gradient(YELLOW, WHITE, BLUE)
        self.play(FadeInFrom(qed, UP))
        self.wait(3)
