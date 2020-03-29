#改自widcardw
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
        cirR = ValueTracker(0).add_updater(lambda r:r.set_value(get_distance(dota,dotb)/2))
        ciro = Circle(radius=cirR.get_value(), color="#559944")
        l_ab = Line(dota, dotb, color="#4488dd").add_updater(lambda l:l.put_start_and_end_on(dota.get_center(),dotb.get_center()))
        self.play(ShowCreation(ciro), Write(doto), Write(texto))
        self.play(ShowCreation(l_ab), *[Write(obj) for obj in [dota, dotb, texta, textb]])
        
        t = ValueTracker(0.3)
        dotp = Dot(
            color="#000000", background_stroke_color="#ffffff",
            background_stroke_width=3, plot_depth=2).scale(0.7)\
                .add_updater(lambda p:p.move_to(ciro.point_from_proportion(t.get_value())))
        textp = TexMobject("P", color="#000000", background_stroke_color="#ffffff",
                           background_stroke_width=6, plot_depth=2).scale(0.7).add_updater(lambda p:p.next_to(dotp, UR, buff=SMALL_BUFF))
        self.play(Write(dotp),Write(textp))
        
        cirp = Circle().add_updater(
            lambda m:m.become(
                Circle(radius=get_distance(dotp,dota)*get_distance(dotp,dotb)/get_distance(dota,dotb), color="#559944")\
                .move_to(dotp.get_center())))
        self.play(ShowCreation(cirp))

        self.play(t.increment_value,-0.3,run_time=2)
        
        for i in range(52):
            self.play(t.increment_value, 1/52,
                      rate_func=linear, run_time=0.2)
            cirp.clear_updaters()
            cirpc = cirp.copy().set_stroke(width=1.5, color="#715582")
            self.add(cirpc)
            cirp.add_updater(lambda c: c.become(
                Circle(radius=get_distance(dotp,dota)*get_distance(dotp,dotb)/get_distance(dota,dotb), color="#dd7766")
                .move_to(dotp.get_center())))
            self.add(cirp)
        cirp.clear_updaters()
        self.wait()
        self.play(FadeOut(Group(*self.mobjects[-10:],*self.mobjects[0])))
        self.wait(2)
