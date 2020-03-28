# from widcardw

from manimlib.imports import *


class Test6(Scene):
    CONFIG = {"camera_config": {"background_color": "#ffffff"}}

    def construct(self):
        circle0 = Circle(radius=1.5, stroke_color="#559944", plot_depth=-2)
        doto = Dot(ORIGIN, color="#000000")
        texto = TexMobject("O", color="#000000", background_stroke_color="#ffffff", background_stroke_width=6).next_to(
            doto, RIGHT+DOWN, buff=SMALL_BUFF)
        self.play(ShowCreation(circle0))
        self.play(Write(doto), Write(texto))
        dota = Dot(np.array([3.2, 0, 0]), color="#000000", plot_depth=1)
        texta = TexMobject("A", color="#000000").next_to(
            dota, RIGHT+DOWN, buff=SMALL_BUFF)
        self.play(Write(dota), Write(texta))
        t = ValueTracker(2)
        dotb = Dot(color="#bb3333", plot_depth=1).add_updater(lambda b: b.move_to(np.array([
            1.5*np.cos(t.get_value()), 1.5*np.sin(t.get_value()), 0
        ])))
        textb = TexMobject("B", color="#000000", background_stroke_color="#ffffff", background_stroke_width=6).add_updater(
            lambda b: b.next_to(dotb, UP+LEFT, buff=SMALL_BUFF))
        self.play(Write(dotb), Write(textb))
        self.wait(0.2)
        l_ab = DashedLine(color="#bb7755", stroke_width=1.5, plot_depth=0).add_updater(
            lambda l: l.put_start_and_end_on(dota.get_center(), dotb.get_center()))
        self.play(ShowCreation(l_ab))
        self.wait(0.2)
        self.play(t.increment_value, 1, rate_func=smooth)
        self.play(t.increment_value, -3, rate_func=smooth)
        l_b = Line(LEFT, RIGHT).add_updater(lambda l: l.become(
            Line(color="#55aaee", plot_depth=0).rotate(l_ab.get_angle()+PI/2,
                                                       about_point=l_ab.get_start())
            .move_to(l_ab.get_end()).scale(20)
        ))
        dotc = Dot(stroke_opacity=0, fill_opacity=0).add_updater(
            lambda d: d.move_to(l_b.get_start()))
        self.play(ShowCreation(l_b))
        self.add(dotc)
        anglea = Angle(dota, dotb, dotc)\
            .add_updater(lambda a: a.become(Angle(dota, dotb, dotc, color="#E65A4C")))
        self.play(ShowCreation(anglea))
        for i in range(50):
            self.play(t.increment_value, TAU/50,
                      rate_func=linear, run_time=0.12)
            l_b.clear_updaters()
            l_b.plot_depth = -1
            l_bc = l_b.copy().set_stroke(width=1.5, color="#00aaff")
            self.add(l_bc)
            l_b.add_updater(lambda l: l.become(
                Line(color="#55aaee", plot_depth=0).rotate(l_ab.get_angle()+PI/2,
                                                           about_point=l_ab.get_start())
                .move_to(l_ab.get_end()).scale(20)
            ))
            self.add(l_b)
        anglea.clear_updaters()
        l_b.clear_updaters()
        self.play(FadeOut(anglea), FadeOut(l_b))
        self.wait(3)


class Test7(Scene):
    CONFIG = {"camera_config": {"background_color": "#ffffff"}}

    def construct(self):
        t = ValueTracker(0)
        doto = Dot(DOWN*0.6, color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2).scale(0.5)
        dotp = Dot(np.array([0, -2.7, 0]), color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2).scale(0.5)
        dota = Dot(color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2).scale(0.5).add_updater(lambda d: d.move_to(np.array([
                       doto.get_center()[0]+np.cos(t.get_value()),
                       doto.get_center()[1]+np.sin(t.get_value()), 0
                   ])))
        cira = Circle().add_updater(lambda c: c.become(
            Circle(radius=get_line_long(dotp.get_center(),
                                        dota.get_center()), color="#559944").move_to(dota.get_center())
        ))
        texto = TexMobject(
            "O", color="#000000", background_stroke_color="#ffffff", background_stroke_width=6)\
            .scale(0.7).next_to(doto, DOWN+RIGHT, buff=SMALL_BUFF)
        textp = TexMobject(
            "P", color="#000000", background_stroke_color="#ffffff", background_stroke_width=6)\
            .scale(0.7).next_to(dotp, DOWN+LEFT, buff=SMALL_BUFF)
        texta = TexMobject(
            "A", color="#000000", background_stroke_color="#ffffff", background_stroke_width=6)\
            .scale(0.7).add_updater(lambda a: a.next_to(dota, DOWN+LEFT, buff=SMALL_BUFF))
        ciro = Circle(radius=1, color="#bb7755").move_to(doto.get_center())

        dotpc = Dot(color="#000000").scale(0.5).move_to(dotp.get_center())
        l_pa = DashedLine(color="#55bb33", stroke_width=1.5).add_updater(lambda l: l.put_start_and_end_on(
            dota.get_center(), dotpc.get_center()))
        self.play(ShowCreation(ciro), Write(doto), Write(texto))
        self.play(Write(dotp), Write(textp))
        self.wait(0.3)
        self.play(Write(dota), Write(texta))
        self.add(dotpc)
        self.play(ShowCreation(l_pa))
        path = TracedPath(dotpc.get_center,
                          stroke_color="#559944", stroke_width=3)
        self.add(path)
        self.play(Rotating(dotpc,  about_point=dota.get_center()),
                  run_time=1.8, rate_func=smooth)
        # self.play(ShowCreation(cira))
        l_pa.clear_updaters()
        self.remove(dotpc, path)
        self.play(FadeOut(l_pa), FadeIn(cira))
        self.play(t.increment_value, -PI/2)
        self.wait(0.3)
        for i in range(40):
            self.play(t.increment_value, TAU/40,
                      rate_func=linear, run_time=0.2)
            cira.clear_updaters()
            ciracpy = cira.copy().set_color("#9944bb").set_stroke(width=1.5)
            self.add(ciracpy)
            cira.add_updater(lambda c: c.become(
                Circle(radius=get_line_long(dotp.get_center(),
                                            dota.get_center()), color="#559944").move_to(dota.get_center())
            ))
            self.add(cira)
        #attention: get_line_long is defined by Shy_Vector
        #if it does not work, you can turn to "get_norm(...)" 
        cira.clear_updaters()
        self.play(FadeOut(cira))
        self.wait(2.5)


class Test8(Scene):
    CONFIG = {"camera_config": {"background_color": "#ffffff"}}

    def construct(self):
        doto = Dot(color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2).scale(0.7)
        dota = Dot(LEFT*1.8, color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2).scale(0.7)
        dotb = Dot(RIGHT*1.8, color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2).scale(0.7)
        texto = TexMobject("O", color="#000000", background_stroke_color="#ffffff",
                           background_stroke_width=6, plot_depth=2).scale(0.7).next_to(doto, RIGHT+DOWN, buff=SMALL_BUFF)
        texta = TexMobject("A", color="#000000", background_stroke_color="#ffffff",
                           background_stroke_width=6, plot_depth=2).scale(0.7).next_to(dota, LEFT, buff=SMALL_BUFF)
        textb = TexMobject("B", color="#000000", background_stroke_color="#ffffff",
                           background_stroke_width=6, plot_depth=2).scale(0.7).next_to(dotb, RIGHT, buff=SMALL_BUFF)
        ciro = Circle(radius=1.8, color="#559944")
        l_ab = Line(LEFT*1.8, RIGHT*1.8, color="#4488dd")
        self.play(ShowCreation(ciro), Write(doto), Write(texto))
        self.play(ShowCreation(l_ab), *[Write(obj)
                                        for obj in [dota, dotb, texta, textb]])
        self.wait(0.3)
        t = ValueTracker(1)
        dotp = Dot(color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2).scale(0.7)\
            .add_updater(lambda d: d.move_to(np.array([
                1.8*np.cos(t.get_value()), 1.8*np.sin(t.get_value()), 0
            ])))
        textp = TexMobject("P", color="#000000", background_stroke_color="#ffffff",
                           background_stroke_width=6, plot_depth=2).scale(0.7)\
            .add_updater(lambda p: p.next_to(dotp, UP+RIGHT, buff=SMALL_BUFF))
        self.play(Write(dotp), Write(textp))
        self.wait(0.2)
        cirp = Circle(radius=2).add_updater(lambda c: c.become(
            Circle(radius=abs(dotp.get_center()[1]), color="#dd7766")
            .move_to(dotp.get_center())
        ))
        self.play(ShowCreation(cirp))
        self.play(t.increment_value, 1)
        self.play(t.increment_value, -2)
        self.wait(0.2)
        for i in range(40):
            self.play(t.increment_value, TAU/40,
                      rate_func=linear, run_time=0.2)
            cirp.clear_updaters()
            cirpc = cirp.copy().set_stroke(width=1.5, color="#715582")
            self.add(cirpc)
            cirp.add_updater(lambda c: c.become(
                Circle(radius=abs(dotp.get_center()[1]), color="#dd7766")
                .move_to(dotp.get_center())))
            self.add(cirp)
        cirp.clear_updaters()
        textp.clear_updaters()
        dotp.clear_updaters()
        self.wait()
        self.play(*[FadeOut(obj)
                    for obj in [doto, dota, dotb, texta, textb, textp, textp, dotp, l_ab, ciro, texto]])
        self.wait(2)



'''

to be completed...

class Test5(Scene):
    CONFIG = {"camera_config": {"background_color": "#ffffff"}}

    def construct(self):
        dotb = Dot(LEFT*2, color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2)
        dotc = Dot(RIGHT*2, color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2)
        dota = Dot(LEFT*2+UP*1.3, color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2)
        texta = TexMobject("A", color="#000000", background_stroke_color="#ffffff",
                           background_stroke_width=6, plot_depth=2).next_to(dota, UP+LEFT, buff=SMALL_BUFF)
        textb = TexMobject("B", color="#000000", background_stroke_color="#ffffff",
                           background_stroke_width=6, plot_depth=2).next_to(dotb, LEFT+DOWN, buff=SMALL_BUFF)
        textc = TexMobject("C", color="#000000", background_stroke_color="#ffffff",
                           background_stroke_width=6, plot_depth=2).next_to(dotc, RIGHT+DOWN, buff=SMALL_BUFF)
        l_ab = Line(color="#559944")\
            .put_start_and_end_on(dota.get_center(), dotb.get_center())
        l_bc = Line(color="#559944")\
            .put_start_and_end_on(dotc.get_center(), dotb.get_center())
        self.play(*[ShowCreation(obj)
                    for obj in [l_ab, l_bc, dota, dotb, dotc]])
        self.play(*[Write(obj) for obj in [texta, textb, textc]])
        self.wait(0.3)
        t = ValueTracker(0)

        def p_pos(t):
            return np.array([0, 0, 0])
        dotp = Dot(color="#000000", background_stroke_color="#ffffff",
                   background_stroke_width=3, plot_depth=2)\
            .add_updater(lambda d: d.move_to())'''

