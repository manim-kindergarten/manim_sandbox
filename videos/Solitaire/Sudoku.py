from manimlib.imports import *

color_map = [RED, ORANGE, YELLOW, GREEN, BLUE, TEAL, PURPLE, PINK, WHITE]
diff_str = ['Easy', 'Medium', 'Hard', 'Very hard']
diff_color = [GREEN, BLUE, PURPLE, RED]


class Plot1v2(GraphScene):
    CONFIG = {
        "y_max": 4,
        "y_min": 0,
        "x_max": 4,
        "x_min": 0,
        "x_axis_width": 8,
        "y_axis_height": 4,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_axis_label": "$n$",
        "y_axis_label": "$d$",
        "axes_color": MAROON,
        "graph_origin": np.array((-4, -3, 0))
    }

    def construct(self):
        nums = [32, 30, 27, 24]
        diff_textstr = VGroup(*[TextMobject(strdiff) for strdiff in diff_str]).arrange(RIGHT * 2)
        decimals = VGroup(*[DecimalNumber(num, num_decimal_places=0) for num in nums])
        for i in range(len(decimals)):
            decimals[i].next_to(diff_textstr[i], DOWN * 2)
        group = VGroup(diff_textstr, decimals).center()
        anim_diff = [
            Write(diff_textstr[i].set_color(diff_color[i]))
            for i in range(len(diff_textstr))
        ]
        anim_deci = [
            Write(decimals[i].set_color(diff_color[i]))
            for i in range(len(decimals))
        ]
        self.play(*anim_diff, *anim_deci, run_time=2)
        self.wait()
        self.play(group.shift, UP * 3)
        self.wait()
        dots = VGroup(*[
            Dot(np.array([-4 + (i + 0.375) * 2, 1 / (i + 0.375) - 3, 0])).set_color(diff_color[3 - i])
            for i in range(0, 4)
        ])
        self.setup_axes(animate=True)
        anim = [
            Transform(VGroup(diff_textstr[i], decimals[i]).copy(), dots[3 - i])
            for i in range(len(decimals))
        ]
        self.play(*anim)
        self.wait()
        graph = self.get_graph(lambda x: 1 / x,
                               color=TEAL,
                               x_min=0.25,
                               x_max=4,
                               )
        self.play(
            ShowCreation(graph),
            run_time=2
        )


class Box:
    def __init__(self, val=0, width=0.5):
        self.width = width
        self.square = Square().set_width(width)
        if val != 0:
            text = TextMobject(str(val)).scale(self.width / 0.5)
            text.move_to(self.square.get_center())
            self.text = text
            self.group = VGroup(self.square, self.text)
        else:
            self.text = None
            self.group = VGroup(self.square)

    def add_number(self, val):
        if val != 0:
            text = TextMobject(str(val)).scale(self.width / 0.5)
            text.set_color(color_map[val - 1])
            text.move_to(self.square.get_center())
            self.text = text
            self.group = VGroup(self.square, self.text)
            return self.text


class SudokuBoard:
    def __init__(self, width=0.8):
        self.box = [[Box(width=width) for j in range(9)] for i in range(9)]
        self.board = VGroup(*[
            VGroup(*[
                self.box[i][j].group for j in range(9)
            ]).arrange(RIGHT * 0.0000001) for i in range(9)
        ]).arrange(DOWN * 0.0000001)
        line_color = MAROON
        self.square = VGroup(*[
            VGroup(*[
                self.box[i][j].square for j in range(9)
            ]) for i in range(9)
        ])
        h_lines = VGroup(*[
            Line(self.board[i][0].get_critical_point(LEFT + DOWN),
                 self.board[i][8].get_critical_point(RIGHT + DOWN)).set_color(line_color)
            for i in range(2, 8, 3)
        ])
        self.h_lines = h_lines
        v_lines = VGroup(*[
            Line(self.board[0][j].get_critical_point(RIGHT + UP),
                 self.board[8][j].get_critical_point(RIGHT + DOWN)).set_color(line_color)
            for j in range(2, 8, 3)
        ])
        self.v_lines = v_lines
        frame_color = MAROON
        h_frame_lines = VGroup(*[
            Line(self.board[0][0].get_critical_point(LEFT + UP),
                 self.board[0][8].get_critical_point(RIGHT + UP)).set_color(frame_color),
            Line(self.board[8][0].get_critical_point(LEFT + DOWN),
                 self.board[8][8].get_critical_point(RIGHT + DOWN)).set_color(frame_color)
        ])
        self.h_frame_lines = h_frame_lines
        v_frame_lines = VGroup(*[
            Line(self.board[0][0].get_critical_point(LEFT + UP),
                 self.board[8][0].get_critical_point(LEFT + DOWN)).set_color(frame_color),
            Line(self.board[0][8].get_critical_point(RIGHT + UP),
                 self.board[8][8].get_critical_point(RIGHT + DOWN)).set_color(frame_color)
        ])
        self.v_frame_lines = v_frame_lines
        self.count = 0
        self.group = VGroup(self.board, h_lines, v_lines, h_frame_lines, v_frame_lines)


    def load(self, path):
        file = open(path, "r")
        buff = file.read()
        list_buff = list(buff)
        while ' ' in list_buff:
            list_buff.remove(' ')
        while '\n' in list_buff:
            list_buff.remove('\n')
        while '\0' in list_buff:
            list_buff.remove('\0')
        assert (len(list_buff) == 81)
        for i in range(0, 9):
            for j in range(0, 9):
                num = ord(list_buff[i * 9 + j]) - ord('0')
                if num != 0:
                    self.count += 1
                self.box[i][j].add_number(num)
        file.close()
        self.board = VGroup(*[
            VGroup(*[
                self.box[i][j].group for j in range(9)
            ]).arrange(RIGHT * 0.0000001) for i in range(9)
        ]).arrange(DOWN * 0.0000001)
        self.group = VGroup(self.board, self.h_lines, self.v_lines, self.h_frame_lines, self.v_frame_lines)
        return self

    def text_count(self):
        return DecimalNumber(self.count, include_sign=False, unit=None, num_decimal_places=0). \
            scale(self.box[0][0].width / 0.5).next_to(self.group, RIGHT * 2)
        # r eturn TextMobject(str(self.count)).scale(self.box[0][0].width / 0.5).next_to(self.group, RIGHT * 2)

    def row_rec(self, i):
        rec = Rectangle().set_height(self.box[0][0].group.get_height(), stretch=True)
        rec.set_width(self.box[0][0].group.get_height() * 9, stretch=True)
        rec.move_to(self.box[i][4].group.get_center())
        rec.set_color(RED).set_opacity(0.4)
        return rec

    def column_rec(self, j):
        rec = Rectangle().set_width(self.box[0][0].group.get_height(), stretch=True)
        rec.set_height(self.box[0][0].group.get_height() * 9, stretch=True)
        rec.move_to(self.box[4][j].group.get_center())
        rec.set_color(GREEN).set_opacity(0.4)
        return rec

    def square_rec(self, i, j):
        sq = Square().set_width(self.box[0][0].group.get_width() * 3)
        sq_i = int(i / 3)
        sq_j = int(j / 3)
        sq.move_to(self.box[sq_i * 3 + 1][sq_j * 3 + 1].group.get_center())
        sq.set_color(BLUE).set_opacity(0.4)
        return sq

    def choose_number(self, i, j):
        return self.box[i][j].text

    def cross_line(self, i, j, color=RED):
        line_1 = Line(self.box[i][j].square.get_critical_point(LEFT + UP),
                      self.box[i][j].square.get_critical_point(RIGHT + DOWN)).set_color(color)
        line_2 = Line(self.box[i][j].square.get_critical_point(RIGHT + UP),
                      self.box[i][j].square.get_critical_point(LEFT + DOWN)).set_color(color)
        return VGroup(line_1, line_2)


class Sudoku(Plot1v2):
    def construct(self):
        start = SudokuBoard(width=0.7)
        start.load('puzzle\\easy\\1')
        text = start.text_count().set_color(diff_color[0])
        diff_scale = 1
        diff = TextMobject('Easy').scale(diff_scale).next_to(start.group, LEFT * 2).set_color(diff_color[0])
        self.play(ShowCreation(start.group), run_time=4, lag_ratio=0.05)
        self.wait(8)
        start.box[1][0].text = TexMobject("\\checkmark").scale(start.box[0][0].width / 0.5). \
            move_to(start.box[1][0].group.get_center()).set_color(GREY)
        self.play(Write(start.box[1][0].text))
        self.wait(4)
        recs = [start.row_rec(1), start.column_rec(0), start.square_rec(1, 0)]
        for rec in recs:
            self.play(ShowCreation(rec))
            self.wait(0.5)
        self.wait()
        self.play(FadeOut(VGroup(*recs)))
        self.wait()
        self.play(FadeOut(start.box[1][0].text))
        start.box[1][0].text = TextMobject("3").scale(start.box[0][0].width / 0.5). \
            move_to(start.box[1][0].group.get_center()).set_color(color_map[3 - 1])
        self.play(Write(start.box[1][0].text))
        self.wait(2)
        trap_coord_list = [[4, 1], [7, 5], [0, 6]]
        square_list = []
        for trap_coord in trap_coord_list:
            s = Square().set_width(start.box[0][0].width). \
                move_to(start.box[trap_coord[0]][trap_coord[1]].square.get_center()). \
                set_color(color_map[3 - 1]).set_opacity(0.4)
            square_list.append(s)
        self.play(start.box[1][0].text.shift, np.array([start.box[0][0].width, 0, 0]),
                  ShowCreation(square_list[0]))
        self.wait()
        self.play(FadeOut(square_list[0]),
                  start.box[1][0].text.shift, np.array([start.box[0][0].width * 4, 0, 0]),
                  ShowCreation(square_list[1]))
        self.wait()
        self.play(FadeOut(square_list[1]),
                  start.box[1][0].text.shift, np.array([start.box[0][0].width, 0, 0]),
                  ShowCreation(square_list[2]))
        self.wait()
        self.play(start.box[1][0].text.shift, np.array([-start.box[0][0].width * 6, 0, 0]),
                  FadeOut(square_list[2]))
        self.wait()
        self.play(FadeOut(start.box[1][0].text))
        self.wait(4)
        net_addr = TextMobject("www.sudokukingdom.com").scale(0.9). \
            to_edge(LEFT, buff=1)
        trans_group = start.group.copy().to_edge(RIGHT, buff=1)
        self.play(start.group.move_to, trans_group.get_center(),
                  Write(net_addr))
        self.wait(2)
        self.play(FadeOut(net_addr), start.group.center)
        self.wait(2)
        self.play(Write(diff))
        self.play(Write(text))
        self.wait(2)
        paths = [
            [
                'puzzle\\easy\\2'
            ],
            [
                'puzzle\\medium\\1',
                'puzzle\\medium\\2'
            ],
            [
                'puzzle\\hard\\1',
                'puzzle\\hard\\2'
            ],
            [
                'puzzle\\veryhard\\1',
                'puzzle\\veryhard\\2'
            ]
        ]
        for i in range(len(paths)):
            if i == 0:
                end = 1
            else:
                end = 2
            for j in range(end):
                s = SudokuBoard(width=0.7).load(paths[i][j])
                text_diff = TextMobject(diff_str[i]).scale(diff_scale).next_to(s.group, LEFT * 2). \
                    set_color(diff_color[i])
                self.play(
                    Transform(start.group, s.group),
                    Transform(diff, text_diff),
                    Transform(text, s.text_count().set_color(diff_color[i]))
                )
                self.wait(2)
        self.clear()

        super().construct()

        self.wait(6)
        self.clear()

        start = SudokuBoard(0.7).load(paths[-1][-2])
        text = start.text_count().set_color(diff_color[-1])
        text.add_updater(lambda n: n.set_value(start.count))
        diff_scale = 1
        diff = TextMobject('Very hard').scale(diff_scale).next_to(start.group, LEFT * 2).set_color(diff_color[-1])
        self.play(ShowCreation(start.group), run_time=2, lag_ratio=0.05)
        self.play(Write(diff))
        self.play(Write(text))
        ex_count = start.count
        self.wait(8)
        for i in range(9):
            for j in range(9):
                if start.box[i][j].text is not None:
                    self.play(FadeOutAndShift(start.box[i][j].text, RIGHT), run_time=2 / ex_count)
                    start.count -= 1
        self.wait()
        que_diff = TextMobject("???").scale(diff_scale).next_to(start.group, LEFT * 2)
        self.play(Transform(diff, que_diff),
                  text.set_color, WHITE)
        self.wait(4)
        super_easy_diff = TextMobject("Medium").scale(diff_scale). \
            next_to(start.group, LEFT * 2).set_color(diff_color[1])
        self.play(Transform(diff, super_easy_diff),
                  FadeOut(text))
        self.wait(8)
        empty_solve = SudokuBoard(width=0.7).load('C:\\Users\\niedo\\Desktop\\sudoku_vid_prepare\\solve_empty')
        expect_nums = [9, 8, 7]
        expect_texts = [
            TextMobject(str(expect_nums[i])).scale(empty_solve.box[0][0].width / 0.5).move_to(
                empty_solve.box[1][3 + i].square.get_center()).set_color(color_map[expect_nums[i] - 1])
            for i in range(len(expect_nums))
        ]
        for i in range(9):
            for j in range(9):
                if i <= 2:
                    self.play(Write(empty_solve.box[i][j].text), run_time=1 / 9)
                else:
                    self.play(Write(empty_solve.box[i][j].text), run_time=2 / (81 - 3 * 9))
                if i == 0 and j == 8:
                    self.wait(2)
                if i == 1 and j == 2:
                    self.wait(2)
                    for expect_text in expect_texts:
                        self.play(Write(expect_text), run_time=1)
                    self.wait(4)
                    red_cross_lines = [
                        empty_solve.cross_line(1, 3 + i)
                        for i in range(3)
                    ]
                    self.play(Write(VGroup(*red_cross_lines)), run_time=1)
                    self.play(FadeOut(VGroup(*red_cross_lines, *expect_texts)))
                    self.wait()
                if i == 1 and j == 5:
                    self.wait()
            if i <= 2:
                self.wait()
        self.wait(8)
        self.clear()
        start = SudokuBoard(0.7).load(paths[-1][-2])
        diff = TextMobject('Very hard').scale(diff_scale).next_to(start.group, UP).set_color(diff_color[-1])
        VGroup(start.group, diff).center()
        self.play(ShowCreation(start.group), Write(diff),
                  run_time=2, lag_ratio=0.05)
        self.wait()
        self.play(VGroup(start.group, diff).to_edge, LEFT)
        self.wait()
        nums = [[9, 8, 0, 0, 5, 7, 6, 2, 1], [0, 6, 5, 9]]
        step_count = 0
        step_list = []
        num_list = []
        scale_fac = 1
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                format_string = "Step %d: i = %d, j = %d, num: " % (step_count + 1, i, j), "%d" % (nums[i][j])
                if nums[i][j] != 0:
                    if step_count == 0:
                        step_str = TextMobject(*format_string).scale(scale_fac). \
                            to_edge(RIGHT).to_edge(UP, 0.7)
                    else:
                        step_str = TextMobject(*format_string).scale(scale_fac).next_to(step_list[-1], DOWN). \
                            align_to(step_list[-1], LEFT)
                    step_list.append(step_str)
                    write_number = start.box[i][j].add_number(nums[i][j])
                    num_list.append(write_number)
                    self.play(Write(step_str),
                              Write(write_number), run_time=1)
                    self.wait(0.5)
                    step_count += 1
        start.box[1][4].text = TexMobject("\\checkmark").scale(start.box[0][0].width / 0.5). \
            move_to(start.box[1][4].group.get_center()).set_color(GREY)
        self.play(Write(start.box[1][4].text))
        self.wait(2)
        trap_list = [
            [7, 4], [1, 0], [4, 4], [1, 7], [1, 2], [5, 4], [3, 4], [2, 5], [1, 3]
        ]
        trap_square = [
            Square().set_width(start.box[0][0].width).set_color(color_map[i]). \
                move_to(start.box[trap_list[i][0]][trap_list[i][1]].square.get_center()).set_opacity(0.4)
            for i in range(len(trap_list))
        ]
        self.play(ShowCreation(VGroup(*trap_square)))
        self.wait(6)
        num_list.reverse()
        step_list.reverse()
        self.play(FadeOut(VGroup(*trap_square)))
        for i in range(len(num_list)):
            self.play(FadeOutAndShift(num_list[i], LEFT),
                      FadeOutAndShift(step_list[i], UP),
                      run_time=1 / len(num_list))
        self.play(VGroup(start.group, diff, start.box[1][4].text).center)
        self.wait(2)
        em_trap_list = [[7, 4], [1, 0], [4, 4], [1, 7], [0, 0], [5, 4], [3, 4], [2, 5], [0, 0]]
        em_trap_group_list = []
        for i in range(len(em_trap_list)):
            if em_trap_list[i][0] != 0 or em_trap_list[i][1] != 0:
                s = Square().set_width(start.box[0][0].width).set_color(color_map[i]) \
                    .move_to(start.box[em_trap_list[i][0]][em_trap_list[i][1]].square.get_center()).set_opacity(0.4)
                em_trap_group_list.append(s)
        self.play(ShowCreation(VGroup(*em_trap_group_list)))
        self.wait(4)
        num_list.reverse()
        shift_len = start.box[0][0].square.get_center()[0] - num_list[0].get_center()[0]
        for num in num_list:
            num.shift(np.array([shift_len, 0, 0]))
        for num in num_list:
            self.play(Write(num), run_time=1 / len(num_list))
        s_1 = Square().set_width(start.box[0][0].width).set_color(color_map[5 - 1]). \
            set_opacity(0.4).move_to(start.box[1][2].square.get_center())
        s_2 = Square().set_width(start.box[0][0].width).set_color(color_map[9 - 1]). \
            set_opacity(0.4).move_to(start.box[1][3].square.get_center())
        self.wait()
        self.play(ShowCreation(VGroup(s_1, s_2)))
        self.wait(10)
        self.play(FadeOut(VGroup(*em_trap_group_list, s_1, s_2, start.box[1][4].text)))
        num_list.reverse()
        for num in num_list:
            self.play(FadeOutAndShift(num, LEFT), run_time=1 / len(num_list))
        self.wait(6)
        square_rec = start.square_rec(4, 8)
        self.play(ShowCreation(square_rec))
        self.wait(2)
        self.play(FadeOut(square_rec))
        row_rec = start.row_rec(5).set_color(GREEN).set_opacity(0.4)
        column_rec = start.column_rec(7)
        self.play(ShowCreation(row_rec))
        self.wait()
        self.play(ShowCreation(column_rec))
        self.wait(4)
        sq_1 = Square().set_width(start.box[0][0].width) \
            .set_color(color_map[4 - 1]).set_opacity(0.4).move_to(start.box[3][6].square.get_center())
        sq_2 = Square().set_width(start.box[0][0].width) \
            .set_color(color_map[4 - 1]).set_opacity(0.4).move_to(start.box[3][8].square.get_center())
        sq_group = VGroup(sq_1, sq_2)
        num_1 = start.box[3][6].add_number(4)
        num_2 = start.box[3][8].add_number(4)
        num_group = VGroup(num_1, num_2)
        self.play(ShowCreation(sq_group), ShowCreation(num_group))
        self.play(FadeIn(sq_1), FadeIn(sq_2), FadeIn(num_1), FadeIn(num_2), run_time=0.2)
        self.play(FadeOut(sq_1), FadeOut(sq_2), FadeOut(num_1), FadeOut(num_2), run_time=0.2)
        self.play(FadeIn(sq_1), FadeIn(sq_2), FadeIn(num_1), FadeIn(num_2), run_time=0.2)
        self.wait(3)
        self.play(Transform(VGroup(sq_group, num_group), start.row_rec(3).set_color(GREEN).set_opacity(0.4)))
        self.wait(3)
        square_rec = start.square_rec(4, 4)
        self.play(ShowCreation(square_rec))
        self.wait()
        self.play(FadeOut(square_rec))
        self.play(ShowCreation(start.column_rec(3)))
        self.wait(2)
        self.play(Write(start.box[4][5].add_number(4)))
        self.wait(3)
        self.clear()

        VGroup(start.group, diff, start.box[1][4].text).to_edge(LEFT)
        self.play(ShowCreation(start.group), Write(diff),
                  run_time=2, lag_ratio=0.05)
        num_list.reverse()
        step_list.reverse()
        for num in num_list:
            num.shift(np.array([-shift_len, 0, 0]))
        for i in range(len(num_list)):
            self.play(Write(num_list[i]),
                      Write(step_list[i]),
                      run_time=1 / len(num_list))
        self.play(Write(start.box[1][4].text))
        self.wait(4)
        self.play(FadeOut(num_list[-1]))
        new_num = start.box[1][3].add_number(1)
        self.play(Write(new_num))
        self.wait(2)
        copy_1 = deepcopy(start.box[1][3].text)
        trans_text = TextMobject("Step 10: i = 1, j = 3, num: ", "1"). \
            scale(scale_fac).move_to(step_list[-1].get_center())
        trans_text[-1].set_color(color_map[1 - 1])
        self.play(Transform(copy_1, trans_text[-1].copy()),
                  Transform(step_list[-1][-1], trans_text[-1].copy()), run_time=1)
        self.wait(10)
        num_list[-1] = copy_1
        num_list.reverse()
        step_list.reverse()
        self.play(FadeOut(start.box[1][4].text),
                  FadeOut(new_num),
                  run_time=1 / (len(step_list)))
        for i in range(len(step_list)):
            self.play(FadeOutAndShift(step_list[i], UP),
                      FadeOutAndShift(num_list[i], LEFT),
                      run_time=1 / (len(step_list)))
        self.play(VGroup(start.group, diff).center)
        step = TextMobject("Step:").next_to(VGroup(start.group, diff), RIGHT)
        each_step_folder = 'C:\\Users\\niedo\\Desktop\\sudoku_vid_prepare\\test\\.sudoku-step\\'
        val = 0
        deci = DecimalNumber(val, num_decimal_places=0, include_sign=False).next_to(step, RIGHT)
        deci.add_updater(lambda n: n.set_value(val))
        self.play(Write(VGroup(step, deci)))
        self.wait(2)
        while val <= 1274:
            load_step = SudokuBoard(width=0.7).load(each_step_folder + str(val + 1))
            load_step.group.move_to(start.group.get_center())
            self.play(Transform(start.group, load_step.group), run_time=2 / 1275)
            val += 1
        self.wait(2)
        self.clear()

        easy = SudokuBoard(width=0.7).load('C:\\Users\\niedo\\myapp\\puzzle\\easy\\1')
        easy_diff = TextMobject("Easy").scale(diff_scale).next_to(easy.group, UP).set_color(diff_color[0])
        VGroup(easy.group, easy_diff).center()
        self.play(ShowCreation(easy.group), Write(easy_diff),
                  run_time=2, lag_ratio=0.05)
        step = TextMobject("Step:").next_to(VGroup(easy.group, easy_diff), RIGHT)
        each_step_folder = 'C:\\Users\\niedo\\Desktop\\sudoku_vid_prepare\\easy1\\.sudoku-step\\'
        val = 0
        deci = DecimalNumber(val, num_decimal_places=0, include_sign=False).next_to(step, RIGHT)
        deci.add_updater(lambda n: n.set_value(val))
        self.play(Write(VGroup(step, deci)))
        self.wait(2)
        while val <= 165:
            load_step = SudokuBoard(width=0.7).load(each_step_folder + str(val + 1))
            load_step.group.move_to(start.group.get_center())
            self.play(Transform(easy.group, load_step.group), run_time=2 / 166)
            val += 1
        self.wait(2)
        self.clear()

        empty = SudokuBoard(width=0.7).load('C:\\Users\\niedo\\myapp\\puzzle\\empty')
        empty_diff = TextMobject("Empty").scale(diff_scale).next_to(empty.group, UP).set_color(TEAL)
        VGroup(empty.group, empty_diff).center()
        self.play(ShowCreation(empty.group), Write(empty_diff),
                  run_time=2, lag_ratio=0.05)
        step = TextMobject("Step:").next_to(VGroup(empty.group, empty_diff), RIGHT)
        each_step_folder = 'C:\\Users\\niedo\\Desktop\\sudoku_vid_prepare\\emptystep\\.sudoku-step\\'
        val = 0
        deci = DecimalNumber(val, num_decimal_places=0, include_sign=False).next_to(step, RIGHT)
        deci.add_updater(lambda n: n.set_value(val))
        self.play(Write(VGroup(step, deci)))
        self.wait(2)
        while val <= 390:
            load_step = SudokuBoard(width=0.7).load(each_step_folder + str(val + 1))
            load_step.group.move_to(start.group.get_center())
            self.play(Transform(empty.group, load_step.group), run_time=2 / 391)
            val += 1
        self.wait(6)
        self.wait()
        self.clear()


class SudokuP2(Scene):
    def construct(self):
        s_l = SudokuBoard().load("C:\\Users\\niedo\\source\\repos\\2017\\project\\sudoku_vid\\puzzle\\empty")
        s_r = SudokuBoard().load("C:\\Users\\niedo\\source\\repos\\2017\\project\\sudoku_vid\\puzzle\\empty")
        s_r.group.scale(0.8).next_to(s_l.group.scale(0.8), RIGHT * 4)
        step_1 = TextMobject("Step:").scale(0.8).next_to(s_l.group, DOWN)
        step_2 = TextMobject("Step:").scale(0.8).next_to(s_r.group, DOWN)
        val = 0
        val_1 = DecimalNumber(val, num_decimal_places=0).scale(0.8).next_to(step_1, RIGHT)
        val_1.add_updater(lambda n: n.set_value(val))
        val_2 = DecimalNumber(val, num_decimal_places=0).scale(0.8).next_to(step_2, RIGHT)
        val_2.add_updater(lambda n: n.set_value(val))
        group = VGroup(s_l.group, s_r.group, step_1, step_2, val_1, val_2).center()
        self.play(ShowCreation(s_l.group), ShowCreation(s_r.group), lag_ratio=0.05, run_time=2)
        self.play(Write(VGroup(step_1, val_1)), Write(VGroup(step_2, val_2)), run_time=1)
        self.wait(10)
        l_str = "C:\\Users\\niedo\\Desktop\\sudoku\\empty\\rev\\"
        r_str = "C:\\Users\\niedo\\Desktop\\sudoku\\empty\\norev\\"
        while val < 391:
            val += 1
            t_s_l = SudokuBoard().load(l_str + str(val))
            t_s_r = SudokuBoard().load(r_str + str(val))
            t_s_l.group.scale(0.8).move_to(s_l.group.get_center())
            t_s_r.group.scale(0.8).move_to(s_r.group.get_center())
            self.play(Transform(s_l.group, t_s_l.group), Transform(s_r.group, t_s_r.group), run_time=1 / 60)
        self.wait(10)
        s_l_n = SudokuBoard().load(l_str + str(val))
        s_r_n = SudokuBoard().load(r_str + str(val))
        s_r_n.group.scale(0.8).next_to(s_l_n.group.scale(0.8), RIGHT * 4)
        VGroup(s_l_n.group, s_r_n.group).center()
        s_l_text = VGroup(*[
            VGroup(*[
                s_l_n.box[i][j].text for j in range(9)
            ]) for i in range(9)
        ])
        s_r_text = VGroup(*[
            VGroup(*[
                s_r_n.box[i][j].text for j in range(9)
            ]) for i in range(9)
        ])
        self.play(s_l.group.move_to, s_l_text.get_center(),
                  s_r.group.move_to, s_r_text.get_center(),
                  FadeOut(VGroup(step_1, val_1, step_2, val_2)), run_time=1)
        self.play(FadeOut(VGroup(s_l.square, s_r.square)), run_time=1)
        self.play(FadeOut(VGroup(s_l.h_lines, s_l.h_frame_lines, s_l.v_lines,
                                 s_l.v_frame_lines, s_r.h_lines, s_r.h_frame_lines, s_r.v_lines,
                                 s_r.v_frame_lines)), run_time=1)
        self.wait(4)


class SudokuP2_2(Scene):
    def construct(self):
        l_str = "C:\\Users\\niedo\\Desktop\\sudoku\\empty\\rev\\"
        r_str = "C:\\Users\\niedo\\Desktop\\sudoku\\empty\\norev\\"
        val = 391
        s_l = SudokuBoard().load(l_str + str(val))
        s_r = SudokuBoard().load(r_str + str(val))
        s_r.group.scale(0.8).next_to(s_l.group.scale(0.8), RIGHT * 4)
        VGroup(s_l.group, s_r.group).center()
        s_l_text = VGroup(*[
            VGroup(*[
                s_l.box[i][j].text for j in range(9)
            ]) for i in range(9)
        ])
        s_r_text = VGroup(*[
            VGroup(*[
                s_r.box[i][j].text for j in range(9)
            ]) for i in range(9)
        ])
        self.add(s_l_text, s_r_text)
        anim_list_l = []
        for i in range(9):
            for j in range(1, 9):
                anim = ApplyMethod(s_l.box[i][j].text.shift,
                                   np.array([-j * s_l.box[0][0].square.get_width() * 0.45, 0, 0]))
                anim_list_l.append(anim)
        anim_list_r = []
        for i in range(9):
            for j in range(1, 9):
                anim = ApplyMethod(s_r.box[i][j].text.shift,
                                   np.array([-j * s_r.box[0][0].square.get_width() * 0.45, 0, 0]))
                anim_list_r.append(anim)
        self.play(*anim_list_l, *anim_list_r, run_time=1, lag_ratio=0.05)
        self.play(VGroup(s_l_text, s_r_text).center)
        self.wait(20)
        eq = TexMobject("\\geq", "Solution", "\\geq").scale(0.9)
        self.play(Write(eq[1]))
        self.wait(20)
        max_text = TextMobject("Max").scale(0.9).set_color(RED).next_to(s_l_text, UP)
        min_text = TextMobject("Min").scale(0.9).set_color(BLUE).next_to(s_r_text, UP)
        self.play(Write(max_text))
        self.wait(10)
        self.play(Write(min_text))
        self.wait(10)
        self.play(Write(eq[0]))
        self.play(Write(eq[-1]))
        self.wait(10)


class SudokuP2_3(Scene):
    def construct(self):
        s = SudokuBoard().load("C:\\Users\\niedo\\source\\repos\\2017\\project\\sudoku_vid\\puzzle\\easy\\1")
        s.group.scale(0.8)
        s_g_copy = s.group.copy()
        copy_align_group = s.group.copy()
        copy_r_align_group = s_g_copy.copy()
        copy_r_align_group.next_to(copy_align_group, RIGHT * 4)
        VGroup(copy_align_group, copy_r_align_group).center()
        self.play(ShowCreation(s.group), run_time=2, lag_ratio=0.05)
        self.wait(10)
        self.play(s.group.move_to, copy_align_group.get_center(),
                  s_g_copy.move_to, copy_r_align_group.get_center(), run_time=1)
        copy_s_g = s.group.copy()
        val = 0
        step_1 = TextMobject("Step:").scale(0.8).next_to(s.group, DOWN)
        step_2 = TextMobject("Step:").scale(0.8).next_to(s_g_copy, DOWN)
        val = 0
        val_1 = DecimalNumber(val, num_decimal_places=0).scale(0.8).next_to(step_1, RIGHT)
        val_1.add_updater(lambda n: n.set_value(val))
        val_2 = DecimalNumber(val, num_decimal_places=0).scale(0.8).next_to(step_2, RIGHT)
        upd = lambda n: n.set_value(val)
        val_2.add_updater(upd)
        max_text = TextMobject("Max").scale(0.9).set_color(RED).next_to(s.group, UP)
        min_text = TextMobject("Min").scale(0.9).set_color(BLUE).next_to(s_g_copy, UP)
        self.play(Write(max_text), Write(min_text), run_time=1)
        dis = abs(s.group.get_center()[0] - s_g_copy.get_center()[0]) - 1
        self.play(Write(VGroup(step_1, val_1)), Write(VGroup(step_2, val_2)), run_time=1)
        self.wait(10)
        l_str = "C:\\Users\\niedo\\Desktop\\sudoku\\easy\\rev\\"
        r_str = "C:\\Users\\niedo\\Desktop\\sudoku\\easy\\norev\\"
        while val < 161:
            val += 1
            t_s_l = SudokuBoard().load(l_str + str(val))
            t_s_r = SudokuBoard().load(r_str + str(val))
            t_s_l.group.scale(0.8).move_to(s.group.get_center())
            t_s_r.group.scale(0.8).move_to(s_g_copy.get_center())
            self.play(Transform(s.group, t_s_l.group), Transform(s_g_copy, t_s_r.group), run_time=1 / 60)
        val_2.remove_updater(upd)
        while val < 166:
            t_s_l = SudokuBoard().load(l_str + str(val))
            t_s_l.group.scale(0.8).move_to(s.group.get_center())
            self.play(Transform(s.group, t_s_l.group), run_time=1 / 60)
            val += 1
        t_s_l = SudokuBoard().load(l_str + str(val))
        t_s_l.group.scale(0.8).move_to(s.group.get_center())
        self.play(Transform(s.group, t_s_l.group), run_time=1 / 60)
        self.wait(10)
        self.play(s.group.move_to, s_g_copy.get_center(), FadeOut(VGroup(step_1, step_2, val_1, val_2)),
                  max_text.shift, np.array([dis, 0, 0]),
                  ApplyMethod(min_text.shift, RIGHT), run_time=1)
        eq = TexMobject("=").scale(0.9).next_to(s_g_copy, UP)
        self.play(Write(eq))
        self.wait(2)
        original = TextMobject("Original").scale(0.9).next_to(copy_s_g, UP)
        self.play(FadeInFrom(copy_s_g, LEFT), run_time=1)
        self.play(Write(original))
        self.wait(10)
        self.play(FadeOut(VGroup(original, copy_s_g)),
                  VGroup(s.group, s_g_copy, max_text, min_text, eq).center, run_time=1)
        self.wait(10)


class SudokuP2_4(Scene):
    def construct(self):
        s = SudokuBoard().load("C:\\Users\\niedo\\Desktop\\sudoku\\easy\\norev\\161")
        s.group.scale(0.8)
        max_text = TextMobject("Max").scale(0.9).set_color(RED).next_to(s.group, UP).shift(LEFT)
        min_text = TextMobject("Min").scale(0.9).set_color(BLUE).next_to(s.group, UP).shift(RIGHT)
        eq = TexMobject("=").scale(0.9).next_to(s.group, UP)
        group = VGroup(s.group, max_text, min_text, eq).center()
        self.add(group)
        s_text = VGroup(*[
            VGroup(*[
                s.box[i][j].text for j in range(9)
            ]) for i in range(9)
        ])
        self.play(FadeOut(s.square), run_time=1)
        self.play(FadeOut(VGroup(s.h_lines, s.h_frame_lines, s.v_lines, s.v_frame_lines)), run_time=1)
        anim_list = []
        for i in range(9):
            for j in range(1, 9):
                anim = ApplyMethod(s.box[i][j].text.shift,
                                   np.array([-j * s.box[0][0].square.get_width() * 0.45, 0, 0]))
                anim_list.append(anim)
        self.play(*anim_list, run_time=1)
        text_copy = s_text.copy().center()
        eq_1 = TextMobject("Max", " = ", "Min").scale(0.9).next_to(text_copy, UP)
        eq_1[0].set_color(RED)
        eq_1[2].set_color(BLUE)
        VGroup(text_copy, eq_1).center()
        self.play(s_text.move_to, text_copy.get_center(),
                  max_text.move_to, eq_1[0].get_center(),
                  eq.move_to, eq_1[1].get_center(),
                  min_text.move_to, eq_1[2].get_center(), run_time=1)
        group = VGroup(s_text, max_text, eq, min_text)
        self.wait(20)
        d = 4
        scale_n = 1
        leq_l = TexMobject("\\textless").scale(scale_n).next_to(group, LEFT * d)
        leq_r = TexMobject("\\textless").scale(scale_n).next_to(group, RIGHT * d)
        solution = TexMobject("S").scale(scale_n).next_to(leq_r, RIGHT * d)
        self.play(Write(solution))
        self.play(Write(leq_r))
        self.wait(10)
        self.play(solution.next_to, leq_l, LEFT * d, FadeOut(leq_r), run_time=1)
        self.play(Write(leq_l))
        self.wait(10)
        self.play(solution.next_to, leq_r, RIGHT * d, FadeOut(leq_l), run_time=1)
        self.play(Write(leq_r))
        self.wait(15)
        copy_max_text = max_text.copy().move_to(np.array([solution.get_center()[0], eq.get_center()[1], 0]))
        dum_max_text = max_text.copy()
        dum_min_text = min_text.copy()
        self.play(max_text.move_to, copy_max_text.get_center(), FadeOut(eq), min_text.move_to, eq.get_center(),
                  solution.set_color, RED)
        self.wait(10)
        self.play(max_text.move_to, dum_max_text.get_center(), FadeIn(eq), min_text.move_to, dum_min_text.get_center())
        self.play(solution.next_to, leq_l, LEFT * d, solution.set_color, WHITE, FadeOut(leq_r))
        self.play(Write(leq_l))
        self.wait(10)
        copy_min_text = min_text.copy().move_to(np.array([solution.get_center()[0], eq.get_center()[1], 0]))
        self.play(min_text.move_to, copy_min_text.get_center(), FadeOut(eq), max_text.move_to, eq.get_center(),
                  solution.set_color, BLUE)
        self.wait(10)
        self.play(min_text.move_to, dum_min_text.get_center(), FadeOut(leq_l), FadeOut(solution),
                  FadeIn(eq), max_text.move_to, dum_max_text.get_center(), run_time=1)
        self.wait(10)


class SudokuExtra(Scene):
    def construct(self):
        path = "C:\\Users\\niedo\\Desktop\\sudoku_vid_prepare\\"
        s_rev = SudokuBoard().load(path+"rev")
        s_rev.group.scale(0.8)
        s_norev = SudokuBoard().load(path+"norev")
        s_norev.group.scale(0.8).next_to(s_rev.group, RIGHT * 4)
        hard_text = TextMobject("Max").scale(0.9).next_to(s_rev.group, UP).set_color(RED)
        hard_text_r = TextMobject("Min").scale(0.9).next_to(s_norev.group, UP).set_color(BLUE)
        ans = 1
        ans_text = TextMobject("Ans:").scale(0.9).next_to(s_rev.group, DOWN)
        ans_deci = DecimalNumber(ans, num_decimal_places=0).scale(0.9).next_to(ans_text, RIGHT)
        ans_deci.add_updater(lambda n: n.set_value(ans))
        VGroup(ans_text, ans_deci).next_to(s_rev.group, DOWN)
        VGroup(s_rev.group, s_norev.group, hard_text, hard_text_r, ans_text, ans_deci).center()
        self.play(ShowCreation(s_rev.group), ShowCreation(s_norev.group), run_time=2, lag_ratio=0.05)
        self.play(Write(hard_text), Write(hard_text_r), Write(VGroup(ans_text, ans_deci)), run_time=1)
        self.wait()
        self.play(FadeOut(hard_text))
        self.wait(2)
        while ans < 141:
            ans += 1
            s = SudokuBoard().load(path+"veryhard1\\"+str(ans))
            s.group.scale(0.8).move_to(s_rev.group.get_center())
            self.play(Transform(s_rev.group, s.group), run_time=1/60)
        self.wait(2)
        dis = abs(s_rev.group.get_center()[0])
        self.play(VGroup(s_rev.group, ans_text, ans_deci).shift, np.array([dis, 0, 0]),
                  VGroup(s_norev.group, hard_text_r).shift, np.array([-dis, 0, 0]), run_time=1)
        self.wait(20)
