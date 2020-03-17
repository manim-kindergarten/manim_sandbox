# from widcardw
# homework vol 01

from manimlib.imports import *


class scene1(Scene):
    def construct(self):
        da = Dot(np.array([-1, 1.8, 0]), plot_depth=1)
        daa = Dot().add_updater(lambda d: d.move_to(da.get_center()))
        db = Dot(np.array([-2, -0.2, 0]), plot_depth=1)
        dbb = Dot().add_updater(lambda d: d.move_to(db.get_center()))
        dc = Dot(np.array([1, -0.2, 0]), plot_depth=1)
        dcc = Dot().add_updater(lambda d: d.move_to(dc.get_center()))
        pabc = Polygon(da.get_center(), db.get_center(), dc.get_center()).add_updater(lambda p: p.become(
            Polygon(da.get_center(), db.get_center(), dc.get_center(), color="#ff9977", fill_color="#ff9977", fill_opacity=0.2)))
        ta = TexMobject("A").add_updater(lambda a: a.next_to(da, UP))
        ta.plot_depth = 1
        tb = TexMobject("B").add_updater(lambda a: a.next_to(db, LEFT))
        tb.plot_depth = 1
        tc = TexMobject("C").add_updater(lambda a: a.next_to(dc, RIGHT))
        tc.plot_depth = 1
        self.play(*[Write(obj)for obj in [da, db, dc, ta, tb, tc]])
        self.add(daa, dbb, dcc)
        '''lab = Line(opacity=0).add_updater(lambda l: l.put_start_and_end_on(
            da.get_center(), db.get_center()))
        lca = Line(opacity=0).add_updater(lambda l: l.put_start_and_end_on(
            da.get_center(), dc.get_center()))
        lbc = Line(opacity=0).add_updater(lambda l: l.put_start_and_end_on(
            dc.get_center(), db.get_center()))'''
        self.play(ShowCreation(pabc))
        self.wait(0.8)
        da_ = Dot(plot_depth=1).add_updater(lambda d: d.move_to(np.array(
            [da.get_center()[0]-da.get_center()[1]+db.get_center()[1],
             da.get_center()[1]+da.get_center()[0]-db.get_center()[0], 0])))
        db_ = Dot(plot_depth=1).add_updater(lambda d: d.move_to(np.array(
            [db.get_center()[0]-da.get_center()[1]+db.get_center()[1],
             db.get_center()[1]+da.get_center()[0]-db.get_center()[0], 0])))
        paabb = Polygon(da.get_center(), db.get_center()).add_updater(lambda p: p.become(
            Polygon(da.get_center(), db.get_center(), db_.get_center(), da_.get_center(),
                    color="#ffff88", fill_color="#ffff88", fill_opacity=0.2, plot_depth=0.6)))
        vgab = VGroup(da_, db_, paabb)
        da__ = Dot(plot_depth=1).add_updater(lambda d: d.move_to(np.array(
            [da.get_center()[0]-dc.get_center()[1]+da.get_center()[1],
             da.get_center()[1]-da.get_center()[0]+dc.get_center()[0], 0])))
        dc__ = Dot(plot_depth=1).add_updater(lambda d: d.move_to(np.array(
            [dc.get_center()[0]-dc.get_center()[1]+da.get_center()[1],
             dc.get_center()[1]-da.get_center()[0]+dc.get_center()[0], 0])))
        paacc = Polygon(da.get_center(), dc.get_center()).add_updater(lambda p: p.become(
            Polygon(da.get_center(), dc.get_center(), dc__.get_center(), da__.get_center(),
                    color="#77bbff", fill_color="#77bbff", fill_opacity=0.2, plot_depth=0.6)))
        vgac = VGroup(da__, dc__, paacc)
        db__ = Dot(plot_depth=1).add_updater(lambda d: d.move_to(np.array(
            [db.get_center()[0]-dc.get_center()[1]+db.get_center()[1],
             db.get_center()[1]-dc.get_center()[0]+db.get_center()[0], 0])))
        dc_ = Dot(plot_depth=1).add_updater(lambda d: d.move_to(np.array(
            [dc.get_center()[0]+dc.get_center()[1]-db.get_center()[1],
             dc.get_center()[1]-dc.get_center()[0]+db.get_center()[0], 0])))
        pbbcc = Polygon(db.get_center(), dc.get_center()).add_updater(lambda p: p.become(
            Polygon(db.get_center(), dc.get_center(), dc_.get_center(), db__.get_center(),
                    color="#77ffbb", fill_color="#77ffbb", fill_opacity=0.2, plot_depth=0.6)))
        vgbc = VGroup(db__, dc_, pbbcc)
        self.play(*[ShowCreation(vg) for vg in [vgab, vgac, vgbc]])
        self.wait(0.2)
        paaa = Polygon(daa.get_center(), da_.get_center()).add_updater(lambda p: p.become(
            Polygon(daa.get_center(), da_.get_center(), da__.get_center(),
                    color="#77ffbb", fill_color="#77ffbb", fill_opacity=0.2)))
        pbbb = Polygon(dbb.get_center(), db_.get_center()).add_updater(lambda p: p.become(
            Polygon(dbb.get_center(), db_.get_center(), db__.get_center(),
                    color="#77bbff", fill_color="#77bbff", fill_opacity=0.2)))
        pccc = Polygon(dcc.get_center(), dc_.get_center()).add_updater(lambda p: p.become(
            Polygon(dcc.get_center(), dc_.get_center(), dc__.get_center(),
                    color="#ffff88", fill_color="#ffff88", fill_opacity=0.2)))
        self.play(*[ShowCreation(obj)for obj in [paaa, pbbb, pccc]])
        self.play(da.shift, LEFT*1.2+DOWN*0.2,
                  dc.shift, LEFT*1.8,
                  db.shift, LEFT*2.4)
        self.wait(0.6)
        paabb.clear_updaters()
        paacc.clear_updaters()
        pbbcc.clear_updaters()
        da_.clear_updaters()
        da__.clear_updaters()
        daa.clear_updaters()
        db_.clear_updaters()
        db__.clear_updaters()
        dbb.clear_updaters()
        dc_.clear_updaters()
        dc__.clear_updaters()
        dcc.clear_updaters()
        self.play(*[FadeOut(obj) for obj in [paabb, paacc, pbbcc]])
        self.play(Rotate(da_, angle=PI/2, about_point=da.get_center()),
                  Rotate(da__, angle=PI/2, about_point=da.get_center()),
                  Rotate(db_, angle=PI/2, about_point=db.get_center()),
                  Rotate(db__, angle=PI/2, about_point=db.get_center()),
                  Rotate(dc_, angle=PI/2, about_point=dc.get_center()),
                  Rotate(dc__, angle=PI/2, about_point=dc.get_center()),
                  run_time=2)
        self.wait(0.8)
        text = TexMobject("S_{\\Delta ABC}", "=", "S_{\\text{绿}}", "=",
                          "S_{\\text{蓝}}", "=", "S_{\\text{黄}}").move_to(DOWN*3+RIGHT*1)
        text[0].set_color("#ff9977")
        text[2].set_color("#77ffbb")
        text[4].set_color("#77bbff")
        text[6].set_color("#ffff88")
        self.play(daa.move_to, dc.get_center(),
                  da__.move_to, da.get_center(),
                  runtime=4, rate_func=there_and_back_with_pause, pause_ratio=1./6)
        self.play(ReplacementTransform(pabc.copy(), text[0]), Write(
            text[1]), ReplacementTransform(paaa.copy(), text[2]))
        self.wait(0.5)
        self.play(dbb.move_to, da.get_center(),
                  db_.move_to, db.get_center(),
                  runtime=4, rate_func=there_and_back_with_pause, pause_ratio=1./6)
        self.wait(0.3)
        self.play(ReplacementTransform(pabc.copy(), text[0]), Write(
            text[3]), ReplacementTransform(pbbb.copy(), text[4]))
        self.wait(0.5)
        self.play(dcc.move_to, db.get_center(),
                  dc_.move_to, dc.get_center(),
                  runtime=4, rate_func=there_and_back_with_pause, pause_ratio=1./6)
        self.wait(0.3)
        self.play(ReplacementTransform(pabc.copy(), text[0]), Write(
            text[5]), ReplacementTransform(pccc.copy(), text[6]))
        self.wait()
