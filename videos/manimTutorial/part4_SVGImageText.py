# from @鹤翔万里
# manim教程第四期 - SVG、图片与文字

from manimlib.imports import *
from manim_sandbox.utils.imports import *
from manim_projects.tony_useful.imports import *

class CodeLine(Text):
    CONFIG = {
        't2c': {
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'IN': ORANGE,
            'OUT': ORANGE,
            'ORIGIN': ORANGE,
            'DL': ORANGE,
            'DR': ORANGE,
            'UL': ORANGE,
            'UR': ORANGE,
            'manim': GOLD,
            'constants.py': GOLD,
            '#': GOLD,
            '_C': BLUE,
            'BLUE_C': BLUE,
            'BLUE': BLUE,
            'GREEN': GREEN,
            'YELLOW': YELLOW,
            'RED': RED,
            'np': BLACK,
            'array': BLUE_D,
            'ndarray': BLUE,
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'arrange': BLUE_D,
            'VGroup': BLUE_D,
            'VMobject': BLUE_D,
            'ImageMobject': BLUE_D,
            'TextMobject': BLUE_D,
            'TexMobject': BLUE_D,
            'Mobject': BLUE_D,
            'list': BLUE_D,
            'append': BLUE_D,
            'remove': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'GREY_BROWN': GREY_BROWN,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'add_to_back': BLUE_D,
            'vector': ORANGE,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            'aligned_edge': RED,
            'center': RED,
            'radius': RED,
            ">>>": RED,
            'coor_mask': RED,
            'point_or_mobject': RED,
            'python': GOLD,
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'True': average_color(BLUE, PINK),
            '2D': RED_B,
            '3D': RED_B,
            'self': PINK,
            'mob': RED_D,
            'style': PURPLE,
            'stroke': BLUE_D,
            'fill': BLUE_D,
            'background_stroke': BLUE_D,
            'opacity': BLUE_D,
            'set_color': BLUE_D,
            'set_fill': BLUE_D,
            'set_background_stroke': BLUE_D,
            "SVG": GREEN,
            "图片": GREEN,
            "assets": PINK,
            "assets/": PINK,
            "raster_images": PINK,
            "raster_images/": PINK,
            "svg_images": PINK,
            "svg_images/": PINK,
            "sounds": PINK,
            "sounds/": PINK,
            "manim.py": GOLD,
            "manimlib": GOLD,
            "~": "#EBEBEB",
            'ImageMobject': BLUE_D,
            "SVGMobject": BLUE_D,
            "stroke_width": ORANGE,
            "color": ORANGE,
            "background_stroke_color": ORANGE,
            "coin.svg": GOLD_D,
            "up.png": GOLD_D,
            "height": ORANGE,
            "invert": ORANGE,
            "Uncreate": BLUE_D,
            "Write": BLUE_D,
            "Transform": BLUE_D,
            "FadeOut": BLUE_D,
            "img": RED_D,
            "square": RED_D,
            "LaTeX": GOLD,
            "xelatex": GOLD,
            "Text": BLUE_D,
            "Text ": GOLD_D,
            "\\": PURPLE,
            "ab": GOLD_D,
            "cde": GOLD_D,
            "text2": DARK_GRAY,
            "text3": DARK_GRAY,
            "text4": DARK_GRAY,
            "妈咪叔": BLUE_D,
            "www.latexlive.com": PURPLE,
            "debugTeX": BLUE_D,
            "\\\\sum^n_{i=1}i^3=?": GOLD_D,
            "$": GOLD_D,
            "\\\\text{": GOLD_D,
            "bcd": GOLD_D,
            "a bbcde\\n\\tfghi": GOLD_D,
            "\\n": PURPLE,
            "\\t": PURPLE,
            "t2c": ORANGE,
            "font": ORANGE,
            "Consolas": GOLD_D,
        },
        'font': 'Consolas',
        'size': 0.72,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }
    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class CodeLines(VGroup):
    def __init__(self, *text, **kwargs):
        VGroup.__init__(self)
        for each in text:
            self.add(CodeLine(each, **kwargs))
        self.arrange(DOWN, aligned_edge=LEFT)


class SVGCode(CodeLine):
    CONFIG = {
        "t2c": {
            "x": BLUE_D,
            "y": BLUE_D,
            "cx": BLUE_D,
            "cy": BLUE_D,
            "r": BLUE_D,
            "rx": BLUE_D,
            "ry": BLUE_D,
            "points": BLUE_D,
            "d": BLUE_D,
            "width": BLUE_D,
            "height": BLUE_D,
            '"': GOLD_D,
            "xml": RED_D,
            "svg": RED_D,
            "path": RED_D,
            "rect": RED_D,
            "polygon": RED_D,
            "polyline": RED_D,
            "circle": RED_D,
            "ellipse": RED_D,
            "text": RED_D,
            "image": RED_D,
        },
        "size": 0.6
    }


class LaTeXCode(CodeLine):
    CONFIG = {
        "t2c": {
            "preview": ORANGE,
            "standalone": BLUE_D,
            "usepackage": RED_D,
            "begin": GREEN_D,
            "end": GREEN_D,
            "document": ORANGE,
            "align*": ORANGE,
            "~": "#EBEBEB",
            "documentclass": RED_D,
            "\\": DARK_GRAY,
        },
        "size": 0.6
    }


class CodeBackground(BackgroundRectangle):
    CONFIG = {
        "fill_color": "#EBEBEB",
        "fill_opacity": 1,
        "stroke_width": 1,
        "stroke_opacity": 1,
        "stroke_color": DARK_GRAY,
        "buff": 0.5
    }


class Scene_(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }
    def setup(self):
        self.caps_cnt = 1
    def next_caps(self):
        self.play(Transform(self.caps[0], self.caps[self.caps_cnt]))
        self.wait()
        self.caps_cnt += 1
    # def tear_down(self):
    #     self.play(FadeOut(Group(*self.mobjects)))


class OpeningScene(Scene_):
    def construct(self):
        t2c = {
            "manim": average_color(PINK, RED),
            "SVG": BLUE,
            "图片": average_color(BLUE, GREEN),
            "文字": GREEN,
        }
        text_color = DARK_GRAY

        font = "庞门正道标题体"
        text_1 = Text("大家好!", font=font, color=text_color, size=2, t2c=t2c).to_edge(UP * 2, buff=1)
        text_2 = Text("欢迎来到manim视频教程", font=font,
                      color=text_color, size=2, t2c=t2c).to_edge(UP * 3.2, buff=1)
        text_3 = Text("这一期我们将学习manim中", font=font, color=text_color, size=2, t2c=t2c).to_edge(UP * 1.8, buff=1)
        text_4 = Text("SVG、图片和文字的用法", font=font, color=text_color, size=2, t2c=t2c).to_edge(UP * 3., buff=1)
        text_34, text_12 = VGroup(text_3, text_4), VGroup(text_1, text_2)


        methods = [
            ["SVGMobject", "ImageMobject"],
            ["TextMobject", "TexMobject", "Text"],
            ["LaTeX, ", "cairo"]
        ]
        m_group_1 = VGroup(*[Text(tex + ', ', size=0.9, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[0]]).arrange(RIGHT)
        m_group_2 = VGroup(*[Text(tex + ', ', size=0.9, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[1]]).arrange(RIGHT)
        m_group_3 = VGroup(*[Text(tex, size=0.9, font='Consolas', stroke_width=2, color=BLUE_D) for tex in methods[2]]).arrange(RIGHT)
        m_group = VGroup(m_group_1, m_group_2, m_group_3).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        methodes_group = VGroup(*m_group_1, *m_group_2, *m_group_3).next_to(text_34, DOWN, buff=0.7)

        # self.add(picture)
        self.wait(0.5)
        self.play(Write(text_1))
        self.wait(0.5)
        self.play(WriteRandom(text_2), run_time=1.5)
        self.wait(1.8)
        self.play(ReplacementTransform(text_12, text_34), run_time=1.2)
        self.wait(1.2)
        self.play(FadeInRandom(methodes_group), run_time=2.4)
        self.wait(2.6)
        self.play(FadeOutRandom(methodes_group), FadeOutRandom(text_3),
                  FadeOutRandom(text_4), run_time=1.8)
        self.wait(1)


class AssetsDir(Scene_):
    def start(self):
        t2c = {
            "manim": GOLD,
            "SVG": BLUE,
            "图片": average_color(BLUE, GREEN),
            "文字": GREEN,
        }
        title = VGroup(
            Text("Chapter Ⅰ.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("素材文件夹", font="思源黑体 CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "在manim中使用外部图片或SVG文件时，可以直接使用绝对路径定位文件",
            "也可以放在与manim.py、manimlib同级的文件夹内，使用相对路径",
            "但更推荐的方法是放在素材目录(assets/)中",
            "assets/目录并不自带，所以要自己在manim.py的同级目录中创建文件夹",
            "assets/文件夹下还要创建三个子文件夹，分别是",
            "raster_images/、svg_images/、sounds/(一般不用)",
            "把需要使用的图片素材放到assets/raster_images/中",
            "需要使用的SVG素材放到assets/svg_images/中",
            "这样之后，仅仅使用文件名(后缀名可省略)manim就可以自动定位到对应文件",
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        self.wait()

        self.play(Write(self.caps[0]))
        absdir = VGroup(
            CodeLine("\"D:\\\\...\\\\manim\\\\picture.png\"", size=0.8).set_color(DARK_GRAY),
            CodeLine("\"/home/.../manim/picture.png\"", size=0.8).set_color(DARK_GRAY)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(UP)
        for each in absdir:
            each[1:-1].set_color(GOLD_D)
        self.wait()
        self.play(Write(absdir))
        self.wait(2)

        self.next_caps()
        tree = CodeLines(
            "manim",
            "├── manim.py",
            "├── manimlib",
            "│   └── ... ",
            "├── picture.png",
            "└── svg_file.png",
        ).arrange(DOWN, aligned_edge=LEFT, buff=0).shift(UP*0.7)
        tree[0].next_to(tree[1].get_left(), UP, buff=0.35)
        self.play(Write(tree[0]))
        self.play(FadeInFromDown(tree[1:]))
        self.wait(3)

        self.next_caps()
        self.wait(3)
        self.next_caps()
        self.play(tree.shift, LEFT*3)
        tree2 = CodeLines(
            "manim",
            "├── manim.py",
            "├── manimlib",
            "│   └── ... ",
            "└── assets",
            "~   ├── raster_images",
            "~   │   └── picture.png",
            "~   ├── svg_images",
            "~   │   └── svg_file.svg",
            "~   └── sounds"
        ).arrange(DOWN, aligned_edge=LEFT, buff=0).shift(RIGHT*3)
        tree2[0].next_to(tree2[1].get_left(), UP, buff=0.35)
        tree2[5:].shift(DOWN*0.1)
        self.wait()
        self.play(TransformFromCopy(tree, tree2[:5]))
        self.wait(2)

        self.next_caps()
        self.wait(2)
        self.next_caps()
        self.play(
            FadeInFromDown(
                VGroup(tree2[5], tree2[6][4], tree2[7], tree2[8][4], tree2[9])
            )
        )
        self.wait(2)
        self.next_caps()
        self.play(Write(tree2[6][8:]))
        self.wait(2)
        self.next_caps()
        self.play(Write(tree2[8][8:]))
        self.wait(2)
        self.next_caps()
        self.wait(4)


class UseSVG(Scene_):
    def start(self):
        t2c = {
            "manim": GOLD,
            "SVG": BLUE,
            "图片": average_color(BLUE, GREEN),
            "文字": GREEN,
        }
        title = VGroup(
            Text("Chapter ⅠI.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("manim中插入SVG", font="思源黑体 CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "manim中插入SVG图片直接使用SVGMobject即可",
            "传入的唯一参数为一个字符串，指向SVG文件(具体写法见上一部分)",
            "关键字参数有stroke_width(路径粗细)等和VMobject共有的属性",
            "由于SVGMobject是VMobject的子类，所以可以使用所有动画效果",
            "另外，SVGMobject能够处理的和显示有关的SVG元素只有如下几个:",
            "path, rect, circle, ellipse, polygon, polyline",
            "而其余的元素(例如image和text)都会省略，所以制作SVG时需要注意",
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        codes = VGroup(
            CodeLine(">>> mob = SVGMobject(", size=0.8),
            CodeLine('~~~~~~~~"coin.svg",', size=0.8),
            CodeLine("~~~~~~~~color=BLUE,", size=0.8),
            VGroup(
                CodeLine("~~~~~~~~stroke_width=", size=0.8),
                DecimalNumberText(0)
            ).arrange(RIGHT),
            CodeLine("~~~~)", size=0.8),
            CodeLine(">>> self.play(Uncreate(mob))", size=0.8),
            VGroup(*[
                CodeLine("~", size=0.8) for _ in range(4)
            ]).arrange(DOWN)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=0.8)
        codebg = CodeBackground(codes)
        mob = SVGMobject("coin.svg", color=BLUE, stroke_width=0)
        mob.scale(1.5).shift(LEFT*3.5)
        self.wait()
        self.play(Write(self.caps[0]))
        self.wait()
        self.play(FadeInFromDown(codebg))
        self.play(Write(VGroup(codes[0], codes[4])))
        self.wait(2)
        self.next_caps()
        self.play(Write(codes[1]))
        self.wait(3)
        self.next_caps()
        self.play(Write(VGroup(codes[2], codes[3])))
        self.play(FadeIn(mob))
        self.wait()

        sw = ValueTracker(0)
        codes[3][1].add_updater(lambda m: m.set_value(sw.get_value()))
        mob.add_updater(lambda m: m.set_stroke(width=sw.get_value()))
        self.play(sw.increment_value, 10, run_time=3, rate_func=linear)
        self.play(sw.increment_value, -5, run_time=1.5, rate_func=linear)
        codes[3][1].clear_updaters()
        mob.clear_updaters()
        self.wait(3)

        self.next_caps()
        self.play(Write(codes[5]))
        self.wait()
        self.play(Uncreate(mob))
        self.wait(2)
        self.play(FadeOut(codes))
        self.next_caps()
        svg = VGroup(
            SVGCode("<?xml ...>\n..."),
            SVGCode("<svg ...>"),
            SVGCode('<path d="........." ... />'),
            SVGCode('<rect width="..." height="..." x="..." y="..." ... />'),
            SVGCode('<circle cx="..." cy="..." r="..." ... />'),
            SVGCode('<ellipse cx="..." cy="..." rx="..." ry="..." ... />'),
            SVGCode('<polygon points="... ..." ... />'),
            SVGCode('<polyline points="... ..." ... />'),
            SVGCode('<image ... />'),
            SVGCode('<text x="..." y="..." ... > ... </text>'),
            SVGCode('</svg>')
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP*0.4)
        svgbg = CodeBackground(svg)
        check = VGroup(
            TexMobject("\\checkmark", color=GREEN, background_stroke_color=GREEN).scale(0.7).next_to(svg[2], LEFT, buff=0.1),
            TexMobject("\\checkmark", color=GREEN, background_stroke_color=GREEN).scale(0.7).next_to(svg[3], LEFT, buff=0.1),
            TexMobject("\\checkmark", color=GREEN, background_stroke_color=GREEN).scale(0.7).next_to(svg[4], LEFT, buff=0.1),
            TexMobject("\\checkmark", color=GREEN, background_stroke_color=GREEN).scale(0.7).next_to(svg[5], LEFT, buff=0.1),
            TexMobject("\\checkmark", color=GREEN, background_stroke_color=GREEN).scale(0.7).next_to(svg[6], LEFT, buff=0.1),
            TexMobject("\\checkmark", color=GREEN, background_stroke_color=GREEN).scale(0.7).next_to(svg[7], LEFT, buff=0.1),
            TexMobject("\\times", color=RED, background_stroke_color=RED, background_stroke_width=2.5).scale(0.7).next_to(svg[8], LEFT, buff=0.15),
            TexMobject("\\times", color=RED, background_stroke_color=RED, background_stroke_width=2.5).scale(0.7).next_to(svg[9], LEFT, buff=0.15)
        )
        self.play(ReplacementTransform(codebg, svgbg))
        self.play(FadeIn(svg))
        self.wait()
        self.next_caps()
        for each in check[:-2]:
            self.play(Write(each))
        self.wait(2)
        self.next_caps()
        for each in check[-2:]:
            self.play(Write(each))
        self.wait(3)


class UseImage(Scene_):
    def start(self):
        t2c = {
            "manim": GOLD,
            "SVG": BLUE,
            "图片": average_color(BLUE, GREEN),
            "文字": GREEN,
        }
        title = VGroup(
            Text("Chapter ⅠII.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("manim中插入图片", font="思源黑体 CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "在manim中插入图片，需要使用ImageMobject",
            "与SVGMobject类似，传入一个参数表示图片文件名(jpg,png,gif均可)",
            "height表示插入图片的高度(默认为2)，invert表示是否反色(默认False)",
            "ImageMobject不是VMobject的子类，所以有很多动画无法使用",
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        self.wait()
        self.play(Write(self.caps[0]))
        self.wait()
        codes = CodeLines(
            '>>> img = ImageMobject(',
            '~~~~~~~~"up.png",',
            '~~~~~~~~height=3,',
            '~~~~~~~~invert=True',
            '~~~~)',
            '>>> self.play(Uncreate(img))',
            '>>> self.play(Transform(img, square))',
            '>>> self.play(FadeOut(img))',
            '~',
        ).to_edge(RIGHT, buff=0.7)
        codebg = CodeBackground(codes)
        img = ImageMobject("Tony.png", height=2).shift(LEFT*4)
        img2 = ImageMobject("Tony.png", height=3, invert=True).shift(LEFT*4)
        self.play(FadeInFromDown(codebg))
        self.play(Write(VGroup(codes[0], codes[4])))
        self.wait(2)
        self.next_caps()
        self.play(Write(codes[1]))
        self.play(FadeIn(img))
        self.wait(3)
        self.next_caps()
        self.play(Write(codes[2]))
        self.wait()
        self.play(img.scale, 1.5)
        self.wait(2)
        self.play(Write(codes[3]))
        self.wait()
        self.play(Transform(img, img2))
        self.wait(3)
        self.next_caps()
        self.play(Write(codes[5]))
        self.wait()
        self.play(Write(Cross(codes[5][4:], plot_depth=10)))
        self.wait(2)
        self.play(Write(codes[6]))
        self.wait()
        self.play(Write(Cross(codes[6][4:], plot_depth=10)))
        self.wait(2)
        self.play(Write(codes[7]))
        self.wait()
        self.play(FadeOut(img))
        self.wait(3)


class UseTextMobject(Scene_):
    def start(self):
        t2c = {
            "manim": GOLD,
            "SVG": BLUE,
            "图片": average_color(BLUE, GREEN),
            "文字": GREEN,
        }
        title = VGroup(
            Text("Chapter IV.", font="Monaco for Powerline", color=BLUE_D, size=1, t2c=t2c),
            Text("manim中使用文字", font="思源黑体 CN Bold", color=DARK_GRAY, size=1, t2c=t2c),
        ).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(FadeOutAndShiftDown(title))
    def construct(self):
        self.start()
        captions = [
            "在manim中使用文字，可以使用TextMobject（利用LaTeX编译转换出SVG）",
            "传入一个字符串，来表示显示的文字（会套入模板中使用xelatex编译）",
            "其他属性和VMobject的均相同，也可以使用所有动画效果",
            "注意：其中需要使用LaTeX命令的\\都需要替换为\\\\转义，或在字符串前加'r'",
            "一个TextMobject中也可以传入多个字符串，会单独编译，连在一起显示",
            "一个TextMobject包含一个或多个子物体，指向传入的每个字符串",
            "而下一级的子物体，就是这个字符串里的每条路径了(一般是字符)",
            "所以可以通过两级下标来访问到每个字符"
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        self.caps[3][-2].set_color(BLUE_D)
        codes = VGroup(
            CodeLine(">>> text = TextMobject(", size=0.68),
            VGroup(
                CodeLine('~~~~~~~~"Text ', size=0.68),
                Text("文字", color=GOLD_D, size=0.6, font="思源黑体 CN Regular"),
                CodeLine('",', size=0.68),
            ).arrange(RIGHT, buff=0.05, aligned_edge=UP),
            CodeLine("~~~~~~~~color=BLUE,", size=0.68),
            CodeLine("~~~~~~~~background_stroke_color=RED", size=0.68),
            CodeLine("~~~~)", size=0.68),
            CodeLine(">>> self.play(Uncreate(text))", size=0.68),
            CodeLine(">>> text2 = TextMobject(", size=0.68),
            VGroup(
                CodeLine('~~~~~~~~"\\\\LaTeX\\\\\\\\', size=0.68),
                Text("换行", color=GOLD_D, size=0.6, font="思源黑体 CN Regular"),
                CodeLine('")', size=0.68),
            ).arrange(RIGHT, buff=0.05, aligned_edge=UP),
            CodeLine(">>> text3 = TextMobject(", size=0.68),
            CodeLine('~~~~~~~~r"\\LaTeX")', size=0.68),
            CodeLine(">>> text4 = TextMobject(", size=0.68),
            CodeLine('~~~~~~~~"ab", "cde")', size=0.68)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(RIGHT, buff=0.8).shift(UP*0.2)
        codes[9][8].set_color(BLUE_D)
        codebg = CodeBackground(codes, buff=0.38)

        text = TextMobject("Text文字", color=BLACK).scale(1.5).shift(LEFT*3.5)
        text2 = TextMobject("\\LaTeX\\\\换行", color=BLACK).scale(1.5)
        text3 = TextMobject("\\LaTeX", color=BLACK).scale(1.5)
        text4 = TextMobject("ab", "cde", color=BLACK).scale(1.5)
        VGroup(text2, text3, text4).arrange(DOWN, buff=0.4).move_to(LEFT*3.5)

        self.wait()
        self.play(Write(self.caps[0]))
        self.play(FadeInFromDown(codebg))
        self.wait()
        self.play(Write(VGroup(codes[0], codes[4])))
        self.wait(2)
        self.next_caps()
        self.play(Write(codes[1]))
        self.wait()
        self.play(Write(text))
        self.wait(3)
        self.next_caps()
        self.play(Write(codes[2]))
        self.wait()
        self.play(text.set_color, BLUE)
        self.wait(2)
        self.play(Write(codes[3]))
        self.wait()
        self.play(text.set_background_stroke, {"color": RED})
        self.wait(2)
        self.play(Write(codes[5]))
        self.wait()
        self.play(Uncreate(text))
        self.wait(3)
        self.next_caps()
        self.play(Write(VGroup(codes[6], codes[7])))
        self.wait()
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(VGroup(codes[8], codes[9])))
        self.wait()
        self.play(Write(text3))
        self.wait(3)
        self.next_caps()
        self.play(Write(VGroup(codes[10], codes[11])))
        self.wait()
        self.play(Write(text4))
        self.wait(4.5)
        self.next_caps()
        self.play(FadeOut(codes), FadeOut(codebg), FadeOut(text2), FadeOut(text3), FadeOut(text4))

        title = CodeLine('text = TextMobject("ab", "cde")', size=1).to_edge(UP)
        level1 = VGroup(
            CodeLine('text:', size=0.7),
            TextMobject("ab", "cde", color=BLACK),
        ).arrange(RIGHT).next_to(title, DOWN, buff=0.8)
        level2 = VGroup(
            VGroup(
                CodeLine('text[0]:', size=0.7),
                level1[1][0].copy()
            ).arrange(RIGHT),
            VGroup(
                CodeLine('text[1]:', size=0.7),
                level1[1][1].copy()
            ).arrange(RIGHT)
        ).arrange(RIGHT, buff=2).next_to(level1, DOWN, buff=0.9)
        level3 = VGroup(
            VGroup(
                level2[0][1][0].copy(),
                CodeLine('text[0][0]', size=0.6),
            ).arrange(DOWN, buff=0.5),
            VGroup(
                level2[0][1][1].copy(),
                CodeLine('text[0][1]', size=0.6),
            ).arrange(DOWN, buff=0.5),
            VGroup(
                level2[1][1][0].copy(),
                CodeLine('text[1][0]', size=0.6),
            ).arrange(DOWN, buff=0.5),
            VGroup(
                level2[1][1][1].copy(),
                CodeLine('text[1][1]', size=0.6),
            ).arrange(DOWN, buff=0.5),
            VGroup(
                level2[1][1][2].copy(),
                CodeLine('text[1][2]', size=0.6),
            ).arrange(DOWN, buff=0.5),
        ).arrange(RIGHT, buff=0.8, aligned_edge=DOWN).next_to(level2, DOWN, buff=0.9)
        level1bg = CodeBackground(level1, buff=0.15).round_corners(0.2)
        level2bg = VGroup()
        for each in level2:
            level2bg.add(CodeBackground(each, buff=0.15).round_corners(0.2))
        level3bg = VGroup()
        base = CodeBackground(level3[1][0], buff=0.2).round_corners(0.2)
        for each in level3:
            level3bg.add(base.copy().move_to(each[0], coor_mask=np.array([1, 0, 1])))
        lines12 = VGroup(
            Line(level1bg.get_bottom(), level2bg[0].get_top(), color=DARK_GRAY, stroke_width=3),
            Line(level1bg.get_bottom(), level2bg[1].get_top(), color=DARK_GRAY, stroke_width=3),
        )
        lines23 = VGroup(
            Line(level2bg[0].get_bottom(), level3bg[0].get_top(), color=DARK_GRAY, stroke_width=3),
            Line(level2bg[0].get_bottom(), level3bg[1].get_top(), color=DARK_GRAY, stroke_width=3),
            Line(level2bg[1].get_bottom(), level3bg[2].get_top(), color=DARK_GRAY, stroke_width=3),
            Line(level2bg[1].get_bottom(), level3bg[3].get_top(), color=DARK_GRAY, stroke_width=3),
            Line(level2bg[1].get_bottom(), level3bg[4].get_top(), color=DARK_GRAY, stroke_width=3),
        )

        self.play(Write(title))
        self.wait()
        self.play(FadeInFromDown(level1bg))
        self.play(Write(level1))
        self.wait(3)
        self.play(
            *[Write(line) for line in lines12],
            FadeInFrom(level2bg, UP)
        )
        self.wait(2.5)
        self.play(
            Write(level2[0][0]),
            Write(level2[1][0]),
        )
        self.play(
            TransformFromCopy(level1[1][0], level2[0][1]),
            TransformFromCopy(level1[1][1], level2[1][1]),
            run_time=2
        )
        self.wait(3)
        self.next_caps()
        self.play(
            *[Write(line) for line in lines23],
            FadeInFrom(level3bg, UP)
        )
        self.wait(2.5)
        self.play(
            TransformFromCopy(level2[0][1][0], level3[0][0]),
            TransformFromCopy(level2[0][1][1], level3[1][0]),
            TransformFromCopy(level2[1][1][0], level3[2][0]),
            TransformFromCopy(level2[1][1][1], level3[3][0]),
            TransformFromCopy(level2[1][1][2], level3[4][0]),
            run_time=2.5
        )
        self.wait(3)
        self.next_caps()
        self.play(
            AnimationGroup(
                *[FadeInFromDown(level3[i][1], lag_ratio=0.05) for i in range(5)],
                lag_ratio=0.4
            )
        )
        self.wait(7)


class UseTexMobject(Scene_):
    def construct(self):
        captions = [
            "书写公式常使用TexMobject，即LaTeX的align*环境",
            "使用LaTeX的数学公式语法编写公式，结构也和TextMobject类似",
            "而TextMobject和TexMobject的区别在于：",
            "TextMobject直接将内容写在LaTeX的document中\n"
            "      而TexMobject使用了LaTeX的align*公式环境",
            "所以对于文字和公式，上面这两种写法是等价的",
            "关于LaTeX公式的预览和教程，可以尝试妈咪叔维护的www.latexlive.com",
            "可以对实时预览公式，并且含有一些基础的公式教程"
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        codes = VGroup(
            CodeLine(">>> tex = TexMobject("),
            CodeLine(r'~~~~~~~~"\\sum^n_{i=1}i^3=?"'),
            CodeLine("~~~~).scale(2)"),
            CodeLine(">>> debugTeX(self, tex[0])"),
            CodeLine("~~~~#↑自定义的显示子物体下标的函数", font="思源黑体 CN Regular", size=0.6),
            CodeLine("~~~~# 在manim_sandbox中有定义", font="思源黑体 CN Regular", size=0.6),
            CodeLine("~"),
            CodeLine("~"),
            CodeLine("~"),
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=0.7)
        tex = TexMobject("\\sum^n_{i=1}i^3=?", color=BLACK).scale(2).shift(LEFT*3.5)
        codes[4][4:].set_color(GREEN)
        codes[5][4:].set_color(GREEN)
        codebg = CodeBackground(codes)
        self.wait()
        self.play(Write(self.caps[0]))
        self.wait()
        self.play(FadeInFromDown(codebg))
        self.play(Write(VGroup(codes[0], codes[2][:5])))
        self.wait(3)
        self.next_caps()
        self.play(Write(codes[1]))
        self.play(Write(codes[2][5:]))
        self.wait()
        self.play(Write(tex))
        self.wait(3)
        self.play(Write(codes[3]))
        self.play(Write(VGroup(codes[4], codes[5])))
        self.wait()
        index = VGroup()
        for i, j in enumerate(tex[0]):
            index.add(Text(str(i), font="Consolas", size=0.8, color=RED).move_to(j))
            self.play(FadeInFromLarge(index[-1]), run_time=0.5)
        self.wait(5)
        self.next_caps()
        self.play(FadeOut(VGroup(codes, codebg, tex, index)))
        self.wait()
        self.next_caps()
        text_temp = VGroup(
            LaTeXCode("\\documentclass[preview]{standalone}"),
            LaTeXCode("~"),
            LaTeXCode("\\usepackage{...}"),
            LaTeXCode("..."),
            LaTeXCode("\\usepackage{...}"),
            LaTeXCode("~"),
            LaTeXCode("\\begin{document}"),
            LaTeXCode("~"),
            LaTeXCode("~"),
            LaTeXCode("TextMobject"),
            LaTeXCode("~"),
            LaTeXCode("~"),
            LaTeXCode("\\end{document}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        tex_temp = VGroup(
            LaTeXCode("\\documentclass[preview]{standalone}"),
            LaTeXCode("~"),
            LaTeXCode("\\usepackage{...}"),
            LaTeXCode("..."),
            LaTeXCode("\\usepackage{...}"),
            LaTeXCode("~"),
            LaTeXCode("\\begin{document}"),
            LaTeXCode("~"),
            LaTeXCode("\\begin{align*}"),
            LaTeXCode("TexMobject"),
            LaTeXCode("\\end{align*}"),
            LaTeXCode("~"),
            LaTeXCode("\\end{document}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        VGroup(text_temp, tex_temp).arrange(RIGHT, aligned_edge=UP, buff=1.5).shift(UP*0.3)
        texbg = CodeBackground(tex_temp)
        textbg = texbg.copy().move_to(text_temp, coor_mask=np.array([1, 0, 1]))
        # self.add(textbg, text_temp, texbg, tex_temp)
        self.play(FadeInFromDown(textbg))
        self.play(Write(VGroup(text_temp[:7], text_temp[-1])))
        self.wait(2)
        self.play(Write(text_temp[9]))
        self.wait(3)
        self.play(FadeInFrom(texbg, LEFT))
        self.play(
            TransformFromCopy(text_temp[:7], tex_temp[:7]),
            TransformFromCopy(text_temp[-1], tex_temp[-1]),
            run_time=2
        )
        self.wait()
        self.play(Write(VGroup(tex_temp[8], tex_temp[10])))
        self.wait(2)
        self.play(Write(tex_temp[9]))
        self.wait(5)

        equal = VGroup(
            VGroup(
                CodeLine('TextMobject("', size=0.68),
                Text("文字", color=GOLD_D, size=0.6, font="思源黑体 CN Regular"),
                CodeLine('$', size=0.68),
                Text("公式", color=GOLD_D, size=0.6, font="思源黑体 CN Regular"),
                CodeLine('$")', size=0.68)
            ).arrange(RIGHT, aligned_edge=UP, buff=0.05),
            TexMobject("\\Longleftrightarrow", color=ORANGE, background_stroke_color=ORANGE).scale(0.7),
            VGroup(
                CodeLine('TexMobject("\\\\text{', size=0.68),
                Text("文字", color=GOLD_D, size=0.6, font="思源黑体 CN Regular"),
                CodeLine('}', size=0.68, color=GOLD_D),
                Text("公式", color=GOLD_D, size=0.6, font="思源黑体 CN Regular"),
                CodeLine('")', size=0.68)
            ).arrange(RIGHT, aligned_edge=UP, buff=0.05),
        ).arrange(RIGHT, buff=0.3)
        self.play(FadeOut(VGroup(texbg, textbg, tex_temp, text_temp)))
        self.wait()
        self.play(Write(equal))
        self.next_caps()
        self.wait(4)
        
        img = ImageMobject("latexlive.png", height=8)
        rects = VGroup(*[Rectangle() for x in range(2)])
        rects.set_stroke(width=0)
        rects.set_fill(GREY, 0.5)

        rects.set_height(2.2, stretch=True)
        rects.set_width(7.4, stretch=True)

        rects[0].move_to(DOWN*0.1)

        rects[1].set_height(1.5, stretch=True)
        rects[1].set_width(3, stretch=True)
        rects[1].move_to(DOWN*2.75)

        inv_rects = VGroup()
        for rect in rects:
            fsr = FullScreenFadeRectangle()
            fsr.append_points(rect.points[::-1])
            inv_rects.add(fsr)

        inv_rects.set_fill(BLACK, 0.7)
        url = TextMobject("www.latexlive.com", color=BLUE, plot_depth=10).scale(1.5).to_corner(UL)
        self.play(FadeOut(equal))
        self.next_caps()
        self.play(FadeIn(img), FadeIn(url))
        self.wait(2)
        self.next_caps()
        self.wait()
        self.play(FadeOut(self.caps[0]))
        self.play(VFadeIn(inv_rects[0]))
        self.wait(2)
        self.play(Transform(inv_rects[0], inv_rects[1]))
        self.wait(2)
        self.play(VFadeOut(inv_rects[0]))
        self.wait(3)
        img2 = ImageMobject("latexhelp.png", height=8)
        url2 = TextMobject("www.latexlive.com/help", color=BLUE, plot_depth=10).scale(1.5).to_corner(UL)
        self.play(
            Transform(img, img2),
            Transform(url, url2)
        )
        self.wait(3)


class UseText(Scene_):
    def construct(self):
        captions = [
            "如果只使用文字，或者想自定义字体的话，可以使用Text(需要最新版manim)",
            "只能传入一个字符串，支持\\t\\n等，还要传入想要使用的字体名称",
            "还可以传入一个t2c字典来实现自动上色",
            "Text类是SVGMobject的子类，所以有其全部属性，和动画效果",
            "一个Text的子物体就是他的每个字符，空格\\n也包括在内，\\t算为4空格",
            "有关Text的更多用法，可以查看这个官方中文文档"
        ]
        self.caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.64).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        codes = CodeLines(
            ">>> text = Text(",
            '~~~~~~~~"a bbcde\\n\\tfghi",',
            '~~~~~~~~color=BLACK,',
            '~~~~~~~~font="Consolas",',
            '~~~~~~~~t2c={"bcd": BLUE},',
            '~~~~).scale(2)',
            '>>> self.play(Write(text))',
            '>>> debugTeX(self, text)',
        ).to_edge(RIGHT, buff=1)
        codebg = CodeBackground(codes)
        text = Text("a bbcde\n\tfghi", color=BLACK, font="Consolas").scale(2).shift(LEFT*3.5)
        self.wait()
        self.play(Write(self.caps[0]))
        self.wait()
        self.play(FadeInFromDown(codebg))
        self.play(Write(VGroup(codes[0], codes[5][:5])))
        self.wait(2)
        self.next_caps()
        self.play(Write(VGroup(codes[1:3], codes[5][5:])))
        self.wait()
        self.play(Write(codes[3]))
        self.wait()
        self.play(Write(text))
        self.wait(3)
        self.next_caps()
        self.play(Write(codes[4]))
        self.wait()
        self.play(text[3:6].set_color, BLUE)
        self.wait(3)
        self.next_caps()
        self.play(Write(codes[6]))
        self.wait()
        self.play(Write(text))
        self.wait(3)
        self.next_caps()
        comment = Text("注：目前版本非显示字符在前一个显示字符的位置上,可能后续会改变", font="思源黑体 CN Bold", \
            size=0.6, t2c={"目前版本": RED}, color=DARK_GRAY).to_edge(UP)
        self.add(comment)
        self.play(Write(codes[7]))
        self.wait()
        index = VGroup()
        for i, j in enumerate(text):
            index.add(Text(str(i), font="Consolas", size=0.8, color=RED).move_to(j))
            self.play(FadeInFromLarge(index[-1]), run_time=0.5)
        self.wait(5)
        img = ImageMobject("TextDoc.png", height=8)
        url = Text("github.com/manim-kindergarten/manim_sandbox/wiki/text_mobject-文字对象", \
            color=BLUE_D, background_stroke_width=1, font="思源宋体 CN", size=0.6).shift(UP*2.5)
        self.next_caps()
        bg = BackgroundRectangle(self.caps[0], color=WHITE, fill_opacity=0.9, plot_depth=1.5, buff=0.05)
        self.play(FadeOut(VGroup(index, text, codes, codebg)), FadeIn(img), FadeIn(bg))
        self.play(Write(url))
        self.wait(7)


class DownProgressBar(Scene_):
    def construct(self):
        methods_dict = {
            '素材文件夹': '0022', 
            'SVGMobject': '0123', 
            'ImageMobject': '0230',
            'TextMobject': '0330', 
            'TexMobject': '0525', 
            'Text': '0703',
            ' ': '0815'
        }
        total_time = '0828'
        func_time = lambda t: int(t[0:2]) * 60 + int(t[2:])
        func_loc = lambda t: func_time(t)/func_time(total_time) * FRAME_WIDTH * RIGHT + FRAME_WIDTH * LEFT / 2
        p_list = [FRAME_WIDTH * LEFT / 2]
        for v in methods_dict.values():
            p_list.append(func_loc(v))
        p_list.append(func_loc(total_time))

        colors = color_gradient([BLUE, PINK, RED, ORANGE, GREEN], len(methods_dict)+1)

        lines = VGroup(*[Line(p_list[i], p_list[i+1]-0.02*RIGHT, color=colors[i], stroke_width=20) for i in range(len(methods_dict)+1)])
        lines.to_edge(DOWN * 0.22, buff=1)
        texts = VGroup(*[Text(t, color=WHITE, font='思源黑体 CN Bold', size=0.28) for t in methods_dict.keys()], plot_depth=1)
        text = Text('空降', color=WHITE, font='庞门正道标题体', size=0.44).to_edge(DOWN * 0.132, buff=1).to_edge(LEFT, buff=0.4)
        text[1].shift(RIGHT*0.03)
        text[0].shift(LEFT*0.01)
        for i in range(len(methods_dict)):
            texts[i].move_to(lines[i+1])

        self.add(lines, texts, text)


class VideoCover(Scene):
    def construct(self):
        background = Polygon(
            LEFT_SIDE * 2 + BOTTOM, BOTTOM, LEFT_SIDE / 2 + TOP, LEFT_SIDE * 2 + TOP,
            fill_opacity=0.7, fill_color=BLACK, stroke_width=0
        ).shift(RIGHT)
        text = VGroup(
            Text("manim教程", font="庞门正道标题体", color=BLUE, size=2).scale(0.9),
            Text("第四讲", font="庞门正道标题体", color=BLUE, size=2).scale(1.1),
            Text("SVG、图片与文字", font="庞门正道标题体", color=ORANGE, size=2).scale(1.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        text[2].shift(DOWN*0.4)
        text.center().to_edge(LEFT, buff=0.8).shift(UP*0.5)
        text2 = VGroup(
            Text("manim教程", font="庞门正道标题体", color=BLUE, size=2).scale(0.9).set_stroke(width=12, opacity=0.4),
            Text("第四讲", font="庞门正道标题体", color=BLUE, size=2).scale(1.1).set_stroke(width=12, opacity=0.4),
            Text("SVG、图片与文字", font="庞门正道标题体", color=ORANGE, size=2).scale(1.5).set_stroke(width=13, opacity=0.4)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        text2[2].shift(DOWN*0.4)
        text2.center().to_edge(LEFT, buff=0.8).shift(UP*0.5)
        self.add(background, text2, text)


class PreView(Scene_):
    def construct(self):
        title = VGroup(
            Text("SVG?", font="思源黑体 CN Heavy", color=BLUE, size=2.7),
            Text("图片?", font="思源黑体 CN Heavy", color=average_color(BLUE, GREEN), size=2.7),
            Text("文字?", font="思源黑体 CN Heavy", color=GREEN, size=2.7),
        ).arrange(RIGHT, buff=0.7).to_edge(UP)

        content = VGroup(
            CodeLine("SVGMobject()", size=2),
            CodeLine("ImageMobject()", size=2),
            CodeLine("TextMobject()", size=2),
            CodeLine("TexMobject()", size=2),
            CodeLine("Text()", size=2),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(title, DOWN)
        
        self.add(title)
        self.wait()
        self.play(TransformFromCopy(title[0], content[0]))
        self.play(TransformFromCopy(title[1], content[1]))
        self.play(TransformFromCopy(title[2], content[2:]))
        self.wait(2)
        self.clear()

        title = CodeLine('text = TextMobject("ab", "cde")', size=1).to_edge(UP)
        level1 = VGroup(
            CodeLine('text:', size=0.7),
            TextMobject("ab", "cde", color=BLACK),
        ).arrange(RIGHT).next_to(title, DOWN, buff=1.5)

        level2 = VGroup(
            VGroup(
                CodeLine('text[0]:', size=0.7),
                level1[1][0].copy()
            ).arrange(RIGHT),
            VGroup(
                CodeLine('text[1]:', size=0.7),
                level1[1][1].copy()
            ).arrange(RIGHT)
        ).arrange(RIGHT, buff=2).next_to(level1, DOWN, buff=0.9)

        level3 = VGroup(
            VGroup(
                level2[0][1][0].copy(),
                CodeLine('text[0][0]', size=0.6),
            ).arrange(DOWN, buff=0.5),
            VGroup(
                level2[0][1][1].copy(),
                CodeLine('text[0][1]', size=0.6),
            ).arrange(DOWN, buff=0.5),
            VGroup(
                level2[1][1][0].copy(),
                CodeLine('text[1][0]', size=0.6),
            ).arrange(DOWN, buff=0.5),
            VGroup(
                level2[1][1][1].copy(),
                CodeLine('text[1][1]', size=0.6),
            ).arrange(DOWN, buff=0.5),
            VGroup(
                level2[1][1][2].copy(),
                CodeLine('text[1][2]', size=0.6),
            ).arrange(DOWN, buff=0.5),
        ).arrange(RIGHT, buff=0.8, aligned_edge=DOWN).next_to(level2, DOWN, buff=0.9)

        level1bg = CodeBackground(level1, buff=0.15).round_corners(0.2)
        level2bg = VGroup()
        for each in level2:
            level2bg.add(CodeBackground(each, buff=0.15).round_corners(0.2))

        level3bg = VGroup()
        base = CodeBackground(level3[1][0], buff=0.2).round_corners(0.2)
        for each in level3:
            level3bg.add(base.copy().move_to(each[0], coor_mask=np.array([1, 0, 1])))

        lines12 = VGroup(
            Line(level1bg.get_bottom(), level2bg[0].get_top(), color=DARK_GRAY, stroke_width=3),
            Line(level1bg.get_bottom(), level2bg[1].get_top(), color=DARK_GRAY, stroke_width=3),
        )

        lines23 = VGroup(
            Line(level2bg[0].get_bottom(), level3bg[0].get_top(), color=DARK_GRAY, stroke_width=3),
            Line(level2bg[0].get_bottom(), level3bg[1].get_top(), color=DARK_GRAY, stroke_width=3),
            Line(level2bg[1].get_bottom(), level3bg[2].get_top(), color=DARK_GRAY, stroke_width=3),
            Line(level2bg[1].get_bottom(), level3bg[3].get_top(), color=DARK_GRAY, stroke_width=3),
            Line(level2bg[1].get_bottom(), level3bg[4].get_top(), color=DARK_GRAY, stroke_width=3),
        )

        self.add(title)

        self.play(FadeInFromDown(level1bg))
        self.play(Write(level1))

        self.play(
            *[Write(line) for line in lines12],
            FadeInFrom(level2bg, UP)
        )
        self.play(
            Write(level2[0][0]),
            Write(level2[1][0]),
        )
        self.play(
            TransformFromCopy(level1[1][0], level2[0][1]),
            TransformFromCopy(level1[1][1], level2[1][1]),
            run_time=1
        )

        self.play(
            *[Write(line) for line in lines23],
            FadeInFrom(level3bg, UP)
        )
        self.play(
            TransformFromCopy(level2[0][1][0], level3[0][0]),
            TransformFromCopy(level2[0][1][1], level3[1][0]),
            TransformFromCopy(level2[1][1][0], level3[2][0]),
            TransformFromCopy(level2[1][1][1], level3[3][0]),
            TransformFromCopy(level2[1][1][2], level3[4][0]),
            run_time=1
        )

        self.play(
            AnimationGroup(
                *[FadeInFromDown(level3[i][1], lag_ratio=0.02) for i in range(5)],
                lag_ratio=0.2
            )
        )
        self.wait(2)


