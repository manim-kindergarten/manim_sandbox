from manimlib.imports import *
class Emote_new(VGroup):
    CONFIG = {
        'file_name': r'mur.svg',
        'shake_color': average_color(YELLOW, ORANGE),
        'height': 2,
    }
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.emote = SVGMobject(self.file_name, **kwargs).set_height(self.height)
        self.emote_02 = SVGMobject(self.file_name, **kwargs).set_height(self.height)
        self.center_dot = Dot().move_to(self.emote.get_center()).shift((DOWN + RIGHT*0.4) * self.height * 0.18).set_opacity(0)
        list = [0, 1, 2, 3, 5, 6, 9]
        for i in list:
            self.emote[i].set_fill(self.shake_color, 0)
            self.emote_02[i].set_fill(self.shake_color, 0)
        self.add(self.emote_02, self.center_dot, self.emote)
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
        self.emote_02.add_updater(self.update_emote)

    def update_emote(self, mob):
        h, w, c = self.get_height(), self.get_width(), self.get_center()

        add_shake = not((h == self.attribute_list[0]) and (w == self.attribute_list[1])
                        and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]

        if add_shake:
            mob.set_opacity(1)
        else:
            mob.set_opacity(0)

    def shake_on(self):
        self.emote_02.set_opacity(1)
        return self
    def shake_off(self):
        self.emote_02.set_opacity(0)
        return self

class CodeLine(Text):   
    CONFIG = {
        't2c': {
            "stretch":"#78dcdb",
            "height":"#e28656",
            "width":"#999ce8",
            "set_height":"#7ca761",
            "set_width":"#7ca761",
            ">>>":"#e76080"
        },
        'font': 'Consolas',
        'size': 0.36,
        'color': DARK_GRAY,
        'stroke_width':0,
        'plot_depth': 2,
    }
    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)

class testa(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": "#ffffff",
            "use_plot_depth": True,
        }
    }
    def construct(self):
        #captions and codelines
        captions = [
            "这是一个mur猫",#0
            "下面我们将用set_height和set_width方法调教它",#1
            "我们使用set_height将其边长设为5",#2
            "设为3",#3
            "设为1",#4
            "再看一看",#5
            "再用同样的方法试试set_width",#6
            "设为5",#7
            "设为3",#8
            "设为1",#9
            "有没有发现什么奇怪的地方？",#10
            "按名字来说set_height是设置宽，set_width是设置长，效果不是应当不一样吗？？？",#11
            "因为在没有加入参数stretch的情况下，set_width和set_height效果和直接使用scale方法类似",#12
            "stretch？拉伸？",#13
            "加进去试试看",#14
            "可以看到，图片的高被拉伸了",#15
            "那么set_width呢？",#16
            "回顾一下",#17
            "set_width和set_height方法在没有使用stretch参数的情况下和使用scale方法效果一致",#18
            "加入stretch参数后可以对应的拉伸该对象"
        ]
        codelines = [
            ">>>img.set_height(height = 5)",#0
            ">>>img.set_height(height = 3)",#1
            ">>>img.set_height(height = 1)",#2
            ">>>img.set_width(width = 5)",#3
            ">>>img.set_width(width = 3)",#4
            ">>>img.set_width(width = 1)",#5
'''>>>img.set_height(
       height = 5,
       stretch = True
    )
''',#6
'''>>>img.set_width(
       width = 5,
       stretch = True
    )
''',#7
            ".set_height(height = 3)",#8
            ".set_width(width = 3)",#9
            ".set_height(height = 3,stretch = True)",#10
            ".set_width(width = 3,stretch = True)"#11
        ]
        captions_mob = VGroup(
            *[
                CodeLine(cap, font='思源黑体 CN Bold', size=0.32,plot_depth=5,color=DARKER_GRAY).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        codelines_mob = VGroup(
            *[
                CodeLine(codeline,size=0.29)
                for codeline in codelines
            ]
        )

        #codeline align
        for i in range(3):
            if i == 0:
                codelines_mob[i].move_to(UP * 2.9 + RIGHT * 3.8)
            else:
                codelines_mob[i].next_to(codelines_mob[i-1], DOWN).align_to(codelines_mob[i-1], LEFT)
        for i in range(3,6):
            if i == 3:
                codelines_mob[i].move_to(UP * 2.9 + RIGHT * 3.8)
            else:
                codelines_mob[i].next_to(codelines_mob[i-1], DOWN).align_to(codelines_mob[i-1], LEFT)
        for i in range(6,8):
            if i == 6:
                codelines_mob[i].move_to(UP * 2.4 + RIGHT * 3.8)
            else:
                codelines_mob[i].next_to(codelines_mob[i-1], DOWN).align_to(codelines_mob[i-1], LEFT)  


        #setup
        #code environment
        tex_bg = Rectangle(
            height = 6.2,
            width = 5.2,
            color = "#EBEBEB",
            stroke_width = 1,
            stroke_color=GRAY
            )\
            .set_opacity(1)\
            .set_plot_depth(1)\
            .to_corner(RIGHT * 1.25 + UP * 1.25)

        #image
        img = Emote_new(color=BLACK, plot_depth=1)\
            .move_to(np.array([-3.5,0,0]))\
            .save_state()\
            .move_to(ORIGIN)
        img2 = SVGMobject("mur.svg")\
            .set_color(BLACK)\
            .move_to(ORIGIN)
        img_word = CodeLine("img",color = DARKER_GRAY)\
            .move_to(ORIGIN).set_plot_depth(10)
        img_mask = SurroundingRectangle(img)\
            .set_stroke(width = 0)\
            .move_to(ORIGIN)\
            .set_opacity(0.6)\
            .set_color(WHITE).set_plot_depth(5)
        img_surround_rec = SurroundingRectangle(img)\
            .set_stroke(width = 0)\
            .set_opacity(0)\
            .add_updater(lambda r: r.become(SurroundingRectangle(img).set_stroke(width = 0).set_opacity(0)))
        side_brace_up = Brace(
            img,
            direction = UP,buff = 0.1
            )\
            .set_color(BLACK)
        side_brace_right = Brace(
            img,
            direction = RIGHT,buff = 0.1
            )\
            .set_color(BLACK)
        side_length_value_up = DecimalNumber(
            0,
            num_decimal_places=1
            )\
            .set_color(BLACK)\
            .add_updater(lambda d: d.next_to(img, UP*1.4))\
            .add_updater(lambda d: d.set_value(img.get_width()))
        side_length_value_right = DecimalNumber(
            0,
            num_decimal_places=1
            )\
            .set_color(BLACK)\
            .add_updater(lambda d: d.next_to(img, RIGHT*1.4))\
            .add_updater(lambda d: d.set_value(img.get_height()))    

        #surround rectangles
        surround_recs = []
        for code in codelines_mob:
            surround_recs.append(SurroundingRectangle(code,plot_depth = 2))

        #huge word
        stretch = CodeLine("stretch", font='思源黑体 CN Bold', size = 2,plot_depth = 4)
        set_h = CodeLine("set_height", font='思源黑体 CN Bold', size = 1,plot_depth = 4, color = "#7ca761")\
            .move_to(np.array([-3.5,0,0]))\
            .save_state()\
            .add_updater(lambda h:h.set_plot_depth(4))
        set_w = CodeLine("set_width", font='思源黑体 CN Bold', size = 1,plot_depth = 4, color = "#7ca761")\
            .move_to(np.array([3.5,0,0]))\
            .save_state()\
            .add_updater(lambda w:w.set_plot_depth(4))
        background = Rectangle(height = FRAME_HEIGHT, width = FRAME_WIDTH, color = WHITE)\
            .set_opacity(0.7)\
            .set_plot_depth(3)
        a = codelines_mob[8]\
            .next_to(set_h,UP)\
            .set_color(DARKER_GRAY)\
            .set_plot_depth(4)\
            .add_updater(lambda c: c.next_to(set_h,UP).set_plot_depth(4))
        b = codelines_mob[9]\
            .next_to(set_w,UP)\
            .set_color(DARKER_GRAY)\
            .set_plot_depth(4)\
            .add_updater(lambda c: c.next_to(set_w,UP).set_plot_depth(4))
        c = codelines_mob[10]\
            .next_to(set_h,UP)\
            .set_color(DARKER_GRAY)\
            .set_plot_depth(4)\
            .add_updater(lambda c: c.next_to(set_h,UP).set_plot_depth(4))
        d = codelines_mob[11]\
            .next_to(set_w,UP)\
            .set_color(DARKER_GRAY)\
            .set_plot_depth(4)\
            .add_updater(lambda c: c.next_to(set_w,UP))
        



        #show
        #part1 pass
        self.play(FadeInFromLarge(img2,scale_factor = 0))
        self.remove(img2)
        self.add(img)
        self.play(FadeInFrom(captions_mob[0],DOWN))
        self.wait()
        self.play(ReplacementTransform(captions_mob[0],captions_mob[1]))
        self.wait(0.75)
        self.play(ReplacementTransform(captions_mob[1],captions_mob[2]))
        self.wait(1.25)
        #set_height(part2) pass
        #2.1
        self.wait(0.25)
        side_brace_right.add_updater(lambda b: b.become(Brace(img,direction = RIGHT,buff = 0.05).set_color(BLACK)))
        self.play(GrowFromCenter(side_brace_right))
        self.play(
            AnimationGroup(
                FadeIn(tex_bg),                
                ApplyMethod(img.move_to,np.array([-3.5,0,0])),
                FadeInFrom(side_length_value_right,DOWN),
                lag_ratio = 0.4,rate_func = rush_from
                )
            )
        self.play(Write(codelines_mob[0]))
        self.play(ApplyMethod(img.set_height,5))
        #2.2 pass
        self.play(ReplacementTransform(captions_mob[2],captions_mob[3]))
        self.play(Write(codelines_mob[1]))
        self.play(ApplyMethod(img.set_height,3))
        #2.3pass
        self.play(ReplacementTransform(captions_mob[3],captions_mob[4]))
        self.play(Write(codelines_mob[2]))
        self.play(ApplyMethod(img.set_height,1))
        self.wait(1.5)
        self.play(Restore(img))

        #part3 pass
        self.play(ReplacementTransform(captions_mob[4],captions_mob[5]))
        self.wait()
        #3.1 pass
        self.play(ShowCreation(surround_recs[0]))
        self.play(Transform(surround_recs[0],img_surround_rec))
        self.remove(surround_recs[0])
        self.play(ApplyMethod(img.set_height,5))
        #3.2 pass
        self.play(ShowCreation(surround_recs[1]))
        self.play(Transform(surround_recs[1],img_surround_rec))
        self.remove(surround_recs[1])
        self.play(ApplyMethod(img.set_height,3))
        #3.3 pass
        self.play(ShowCreation(surround_recs[2]))
        self.play(Transform(surround_recs[2],img_surround_rec))
        self.remove(surround_recs[2])
        self.play(ApplyMethod(img.set_height,1))
        self.wait()
        self.play(*[Uncreate(codelines_mob[i],run_time = 0.75) for i in range(3)])
        self.play(
            AnimationGroup(
                FadeOutAndShift(captions_mob[5],DOWN),
                Restore(img),
                lag_ratio = 0.3
                )
            )
        self.wait()


        #set_width(part4)
        #4.1 pass
        side_brace_right.clear_updaters()
        side_brace_up.move_to(np.array([-3.5,img.get_corner(UL)[1]+0.2,0]))
        self.play(
            AnimationGroup(
                FadeOut(side_brace_right),
                FadeOutAndShift(side_length_value_right,LEFT)
                )
            )
        side_brace_up.add_updater(lambda b: b.become(Brace(img,direction = UP,buff = 0.05).set_color(BLACK)))
        self.play(GrowFromCenter(side_brace_up))
        self.play(FadeInFrom(side_length_value_up,DOWN))
        #4.2 pass
        self.play(ReplacementTransform(captions_mob[6],captions_mob[7]))
        self.play(Write(codelines_mob[3]))
        self.play(ApplyMethod(img.set_width,5))
        #4.3 pass
        self.play(ReplacementTransform(captions_mob[7],captions_mob[8]))
        self.play(Write(codelines_mob[4]))
        self.play(ApplyMethod(img.set_width,3))
        #4.4 pass
        self.play(ReplacementTransform(captions_mob[8],captions_mob[9]))
        self.play(Write(codelines_mob[5]))
        self.play(ApplyMethod(img.set_width,1))

        #part5
        #5.1 pass
        self.play(ReplacementTransform(captions_mob[9],captions_mob[5]))
        self.play(ShowCreation(surround_recs[3]))
        self.play(Transform(surround_recs[3],img_surround_rec))
        self.remove(surround_recs[3])
        self.play(ApplyMethod(img.set_width,5))
        #5.2 pass
        self.play(ShowCreation(surround_recs[4]))
        self.play(Transform(surround_recs[4],img_surround_rec))
        self.remove(surround_recs[4])
        self.play(ApplyMethod(img.set_width,3))
        #5.3 pass
        self.play(ShowCreation(surround_recs[5]))
        self.play(Transform(surround_recs[5],img_surround_rec))
        self.remove(surround_recs[5])
        self.play(ApplyMethod(img.set_width,1))
        self.wait()

        #stretch(part6) pass
        self.play(ReplacementTransform(captions_mob[5],captions_mob[10]))
        self.wait(1.75)
        self.play(ReplacementTransform(captions_mob[10],captions_mob[11]))
        self.wait(2)
        self.play(ReplacementTransform(captions_mob[11],captions_mob[12]))
        self.wait(2.25)
        self.play(
            AnimationGroup(
                ReplacementTransform(captions_mob[12],stretch),
                FadeIn(background)
                )
            )
        self.play(FadeInFrom(captions_mob[13],DOWN))
        self.wait(0.75)
        self.play(ReplacementTransform(captions_mob[13],captions_mob[14]))

        #stretch(part7)
        #7.1 pass
        self.play(*[Uncreate(codelines_mob[i],run_time = 0.75) for i in range(3,6)])
        self.play(
            AnimationGroup(
                FadeOutAndShift(captions_mob[14],DOWN),
                FadeOut(background),
                Transform(stretch,img_surround_rec)
                )
            )
        self.play(Restore(img))
        #7.2 pass
        self.play(Write(codelines_mob[6]))
        self.play(ApplyMethod(img.set_height,5,True))
        self.play(FadeInFrom(captions_mob[15],DOWN))
        side_brace_right.move_to(np.array([-2.3,0,0]))
        side_brace_right.add_updater(lambda b: b.become(Brace(img,direction = RIGHT,buff = 0.05).set_color(BLACK)))
        self.play(
            AnimationGroup(
                GrowFromCenter(side_brace_right),
                FadeInFrom(side_length_value_right,RIGHT),
                lag_ratio = 0.4,rate_func = rush_from
                )
            )
        self.play(Restore(img,run_time = 0.35))
        self.play(ApplyMethod(img.set_height,5,True,run_time = 0.35))
        self.play(Restore(img,run_time = 0.35))
        self.wait(0.5)
        #7.3 pass
        self.play(ReplacementTransform(captions_mob[15],captions_mob[16]))
        self.play(ShowCreation(codelines_mob[7],run_time = 0.5))
        self.play(ApplyMethod(img.set_width,5,True))
        self.wait(0.75)
        self.play(Restore(img,run_time = 0.35))
        self.play(ApplyMethod(img.set_width,5,True,run_time = 0.35))
        self.play(Restore(img,run_time = 0.35))
        self.play(*[Uncreate(codelines_mob[i]) for i in range(6,8)])
        side_brace_up.clear_updaters()
        side_brace_right.clear_updaters()
        self.remove(img)
        img2.move_to(np.array([-3.5,0,0]))
        self.add(img2)
        self.play(
            AnimationGroup(
                FadeOut(tex_bg),                
                FadeOutAndShift(img2),
                FadeOut(side_brace_up),
                FadeOut(side_length_value_up),
                FadeOut(side_brace_right),
                FadeOut(side_length_value_right),
                FadeOutAndShift(captions_mob[16],DOWN)
                )
            )

        #final part(part8)
        #8.1 pass
        self.play(FadeInFrom(captions_mob[17],DOWN))
        self.wait(0.75)
        self.play(ReplacementTransform(captions_mob[17],captions_mob[18]))
        self.play(
            AnimationGroup(
                TransformFromCopy(captions_mob[18],set_h),
                TransformFromCopy(captions_mob[18],set_w),
                lag_ratio = 0.4
                )
            )
        self.wait(0.75)
        #8.2 pas
        self.play(
            AnimationGroup(
                ShowCreation(a),
                ShowCreation(b)
                )
            )
        self.wait(0.75)
        self.play(set_h.set_height,3)
        self.play(Restore(set_h))
        self.play(set_w.set_width,3)
        self.play(Restore(set_w))
        self.wait(0.75)
        a.clear_updaters()
        b.clear_updaters()
        scale_word = VGroup(
            CodeLine(".scale(3.0)",size=0.32,color=DARKER_GRAY,plot_depth = 4).move_to(a),
            CodeLine(".scale(0.6)",size=0.32,color=DARKER_GRAY,plot_depth = 4).move_to(b)
        )
        self.play(
            ReplacementTransform(a, scale_word[0]),
            ReplacementTransform(b, scale_word[1])
        )
        self.wait(0.25)
        self.play(set_h.scale,3)
        self.play(set_w.scale,0.6)
        self.wait(0.3)
        self.play(
            AnimationGroup(
                Uncreate(scale_word),
                Restore(set_h),
                Restore(set_w)
                )
            )
        self.wait(0.75)
        self.play(ReplacementTransform(captions_mob[18],captions_mob[19]))
        self.wait(0.35)
        self.play(
            AnimationGroup(
                ShowCreation(c),
                ShowCreation(d)
                )
            )
        self.play(set_h.set_height,3,True)
        self.play(Restore(set_h))
        self.play(set_w.set_width,3,True)
        self.play(Restore(set_w))
        self.wait(2)
        self.play(
            AnimationGroup(
                Uncreate(set_h),
                Uncreate(set_w),
                FadeOutAndShift(c,DOWN),
                FadeOutAndShift(d,DOWN),
                FadeOutAndShift(captions_mob[19],DOWN)
                )
            )
        self.wait()