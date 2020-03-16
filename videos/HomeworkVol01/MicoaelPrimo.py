from manimlib.imports import *

class StartingScene(Scene):

    def construct(_):
        
        e = Text("Manim homework by mp",font="Consolas",color=BLUE)
        _.play(Write(e),run_time=3)
        _.wait()
        _.play(Uncreate(e))
        A =  Dot().move_to(np.array([0-2,0,0]))
        B =  Dot().move_to(np.array([9/10-2,12/10,0]))
        C =  Dot().move_to(np.array([5/2-2,0,0]))
        D = B.copy().shift(9/10*UP+6/5*LEFT)
        E = A.copy().shift(9/10*UP+6/5*LEFT)
        F = B.copy().shift(8/5*UP+6/5*RIGHT)
        G = C.copy().shift(8/5*UP+6/5*RIGHT)
        H = A.copy().shift(5/2*DOWN)
        I = C.copy().shift(5/2*DOWN)
        lab = VGroup()
        labtxt = [TextMobject("A").next_to(A).scale(0.5),
                 TextMobject("B").next_to(B).scale(0.5),
                 TextMobject("C").next_to(C).scale(0.5),
                 TextMobject("D").next_to(D).scale(0.5),
                 TextMobject("E").next_to(E).scale(0.5),
                 TextMobject("F").next_to(F).scale(0.5),
                 TextMobject("G").next_to(G).scale(0.5),
                 TextMobject("H").next_to(H).scale(0.5),
                 TextMobject("I").next_to(I).scale(0.5),
                ]
        for i in range(len(labtxt)):
            lab.add(labtxt[i])

        original_trangle = Polygon(A.get_center(),B.get_center(),C.get_center(),color=ORANGE,fill_color = ORANGE,fill_opacity=0.5)
        rect1 = Polygon(A.get_center(),B.get_center(),D.get_center(),E.get_center(),color=GREEN,fill_color = GREEN,fill_opacity=0.5)
        rect2 = Polygon(B.get_center(),F.get_center(),G.get_center(),C.get_center(),color=GREEN,fill_color = GREEN,fill_opacity=0.5)
        rect3 = Polygon(A.get_center(),C.get_center(),I.get_center(),H.get_center(),color=GREEN,fill_color = GREEN,fill_opacity=0.5)
        tran1 = Polygon(D.get_center(),F.get_center(),B.get_center(),color=YELLOW,fill_color = YELLOW,fill_opacity=0.5)
        tran2 = Polygon(E.get_center(),A.get_center(),H.get_center(),color=YELLOW,fill_color = YELLOW,fill_opacity=0.5)
        tran3 = Polygon(C.get_center(),G.get_center(),I.get_center(),color=YELLOW,fill_color = YELLOW,fill_opacity=0.5)
        def getc1(obj):
            obj.move_to(tran1.get_center())
        def getc2(obj):
            obj.move_to(tran2.get_center())
        def getc3(obj):
            obj.move_to(tran3.get_center())
        S1 = TexMobject("S1").add_updater(getc1)
        S2 = TexMobject("S2").add_updater(getc2)
        S3 = TexMobject("S3").add_updater(getc3)
        trans = VGroup(tran1,tran2,tran3,S1,S2,S3)
#        _.add(A,B,C,D,E,F,G,H,I,lab,original_trangle,rect1,rect2,rect3,tran1,tran2,tran3,S1,S2,S3)
        _.play(ShowCreation(original_trangle))
        _.wait()
        _.play(ShowCreation(rect1),ShowCreation(rect2),ShowCreation(rect3))
        _.wait()
        _.play(ShowCreation(tran1),ShowCreation(tran2),ShowCreation(tran3)
               ,Write(S1),Write(S2),Write(S3) ,)
        _.wait()
        _.play(FadeOut(rect1),FadeOut(rect2),FadeOut(rect3))
        _.wait()
        _.play(Rotate(tran1,PI/2,about_point = B.get_center()),
               Rotate(tran2,PI/2,about_point = A.get_center()),
               Rotate(tran3,PI/2,about_point = C.get_center()) )
        _.play(Transform(tran1,original_trangle))
        _.play(Transform(tran2,original_trangle))
        _.play(Transform(tran3,original_trangle))
        S1.clear_updaters()
        S2.clear_updaters()
        S3.clear_updaters()
        _.play(S1.shift,2*UP+1.5*LEFT)
        _.play(S2.shift,2*UP)
        _.play(S3.shift,2*UP+1.5*RIGHT)
        eq = TextMobject("=").next_to(S1)
        eq2 = TextMobject("=").next_to(S2)
        _.play(Write(eq),Write(eq2))
        
