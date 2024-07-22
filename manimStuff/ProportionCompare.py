from manim import * 
import math
import random

class ProportionCompare(Scene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1]),
        ]

    def construct(self):
        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )
        ax.shift(RIGHT * 2.5)

        t = ValueTracker(8)

        def get_rectangle1():
            polygon1 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0, 0), (1, t.get_value() / 1.2)
                    )
                ]
            )
            polygon1.stroke_width = 1
            polygon1.set_fill(WHITE, opacity=0.9)
            polygon1.set_stroke(YELLOW_B)
            return polygon1

        polygon1 = always_redraw(get_rectangle1)

        def get_rectangle2():
            polygon2 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (2 - 1, 0), (2, (-t.get_value() +  12) / 1.8)
                    )
                ]
            )
            polygon2.stroke_width = 2
            polygon2.set_fill(BLUE_C, opacity=0.9)
            polygon2.set_stroke(YELLOW_B)
            return polygon2
        
        def get_rectangle3():
            polygon2 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (3 - 1, 0), (3, (-t.get_value() +  12) / 3)
                    )
                ]
            )
            polygon2.stroke_width = 2
            polygon2.set_fill(GREEN, opacity=0.9)
            polygon2.set_stroke(YELLOW_B)
            return polygon2

        def get_rectangle4():
            polygon2 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (4 - 1, 0), (4, (-t.get_value() +  12) / 4)
                    )
                ]
            )
            polygon2.stroke_width = 2
            polygon2.set_fill(MAROON_B, opacity=0.9)
            polygon2.set_stroke(YELLOW_B)
            return polygon2
        
        def get_rectangle5():
            polygon2 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (5 - 1, 0), (5, (-t.get_value() +  12) / 5)
                    )
                ]
            )
            polygon2.stroke_width = 2
            polygon2.set_fill(GOLD_A, opacity=0.9)
            polygon2.set_stroke(YELLOW_B)
            return polygon2

        def get_rectangle6():
            polygon2 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (6 - 1, 0), (6, (-t.get_value() +  12) / 6)
                    )
                ]
            )
            polygon2.stroke_width = 2
            polygon2.set_fill(PURPLE_E, opacity=0.9)
            polygon2.set_stroke(YELLOW_B)
            return polygon2
        
        def get_rectangle7():
            polygon2 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (7 - 1, 0), (7, (-t.get_value() +  12) / 7)
                    )
                ]
            )
            polygon2.stroke_width = 2
            polygon2.set_fill(ORANGE, opacity=0.9)
            polygon2.set_stroke(YELLOW_B)
            return polygon2
        
        def get_rectangle8():
            polygon2 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (8 - 1, 0), (8, (-t.get_value() +  12) / 8)
                    )
                ]
            )
            polygon2.stroke_width = 2
            polygon2.set_fill(DARK_GREY, opacity=0.9)
            polygon2.set_stroke(YELLOW_B)
            return polygon2
        
        def get_rectangle9():
            polygon2 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (9 - 1, 0), (9, (-t.get_value() +  12) / 9)
                    )
                ]
            )
            polygon2.stroke_width = 2
            polygon2.set_fill(DARKER_GREY, opacity=0.9)
            polygon2.set_stroke(YELLOW_B)
            return polygon2
        
        def get_rectangle10():
            polygon2 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (10 - 1, 0), (10, (-t.get_value() +  12) / 10)
                    )
                ]
            )
            polygon2.stroke_width = 2
            polygon2.set_fill(BLACK, opacity=0.9)
            polygon2.set_stroke(YELLOW_B)
            return polygon2

        polygon2 = always_redraw(get_rectangle2)
        polygon3 = always_redraw(get_rectangle3)
        polygon4 = always_redraw(get_rectangle4)
        polygon5 = always_redraw(get_rectangle5)
        polygon6 = always_redraw(get_rectangle6)
        polygon7 = always_redraw(get_rectangle7)
        polygon8 = always_redraw(get_rectangle8)
        polygon9 = always_redraw(get_rectangle9)
        polygon10 = always_redraw(get_rectangle10)

        ax.shift(LEFT * 15)
        self.add(ax)
        self.play(ax.animate(run_time=1.5).shift(RIGHT * 15))

        self.play(Create(polygon1), Create(polygon2), Create(polygon3), Create(polygon4), Create(polygon5), Create(polygon6), Create(polygon7), Create(polygon8), Create(polygon9), Create(polygon10))

        tiltAmount = 0.3
        shiftAmount = 0.35

        str1_label = Text("streaks of one").next_to(polygon1, UP).scale(0.6).rotate(PI / 2 - tiltAmount).shift(RIGHT * shiftAmount)
        str1_label.add_updater(
            lambda mobject: mobject.next_to(polygon1, UP).shift(RIGHT * shiftAmount)
        )

        str2_label = Text("streaks of two").next_to(polygon2, UP).scale(0.6).rotate(PI / 2 - tiltAmount).shift(RIGHT * shiftAmount)
        str2_label.add_updater(
            lambda mobject: mobject.next_to(polygon2, UP).shift(RIGHT * shiftAmount)
        )
        
        str3_label = Text("streaks of three").next_to(polygon3, UP).scale(0.6).rotate(PI / 2 - tiltAmount).shift(RIGHT * shiftAmount)
        str3_label.add_updater(
            lambda mobject: mobject.next_to(polygon3, UP).shift(RIGHT * shiftAmount)
        )

        str4_label = Text("streaks of four").next_to(polygon4, UP).scale(0.6).rotate(PI / 2 - tiltAmount).shift(RIGHT * shiftAmount)
        str4_label.add_updater(
            lambda mobject: mobject.next_to(polygon4, UP).shift(RIGHT * shiftAmount)
        )

        str5_label = Text("streaks of five").next_to(polygon5, UP).scale(0.6).rotate(PI / 2 - tiltAmount).shift(RIGHT * shiftAmount)
        str5_label.add_updater(
            lambda mobject: mobject.next_to(polygon5, UP).shift(RIGHT * shiftAmount)
        )

        str6_label = Text("streaks of six").next_to(polygon6, UP).scale(0.6).rotate(PI / 2 - tiltAmount).shift(RIGHT * shiftAmount)
        str6_label.add_updater(
            lambda mobject: mobject.next_to(polygon6, UP).shift(RIGHT * shiftAmount)
        )

        str7_label = Text("streaks of seven").next_to(polygon7, UP).scale(0.6).rotate(PI / 2 - tiltAmount).shift(RIGHT * shiftAmount)
        str7_label.add_updater(
            lambda mobject: mobject.next_to(polygon7, UP).shift(RIGHT * shiftAmount)
        )

        str8_label = Text("streaks of eight").next_to(polygon8, UP).scale(0.6).rotate(PI / 2 - tiltAmount).shift(RIGHT * shiftAmount)
        str8_label.add_updater(
            lambda mobject: mobject.next_to(polygon8, UP).shift(RIGHT * shiftAmount)
        )

        str9_label = Text("streaks of nine").next_to(polygon9, UP).scale(0.6).rotate(PI / 2 - tiltAmount).shift(RIGHT * shiftAmount)
        str9_label.add_updater(
            lambda mobject: mobject.next_to(polygon9, UP).shift(RIGHT * shiftAmount)
        )

        str10_label = Text("streaks of ten").next_to(polygon10, UP).scale(0.6).rotate(PI / 2 - tiltAmount).shift(RIGHT * shiftAmount)
        str10_label.add_updater(
            lambda mobject: mobject.next_to(polygon10, UP).shift(RIGHT * shiftAmount)
        )

        self.play(Write(str1_label),Write(str2_label),Write(str3_label),Write(str4_label),Write(str5_label),Write(str6_label),Write(str7_label),Write(str8_label),Write(str9_label),Write(str10_label))
        dots = Text(". . .").next_to(polygon10, RIGHT)
        self.play(Write(dots))
        vg = VGroup()
        vg.add(str1_label,str2_label,str3_label,str4_label,str5_label,str6_label,str7_label,str8_label,str9_label,str10_label,dots)


        self.wait(1)

        numQ_label = Text("# of questions:").to_edge(LEFT).shift(RIGHT * 0.5)
        decimal = DecimalNumber(
            30,
            show_ellipsis=False,
            num_decimal_places=0,
            include_sign=False,
        )
        decimal.next_to(numQ_label, DOWN).scale(2)

        decimal.add_updater(lambda d: d.set_value((14 - t.get_value()) * 10 - 30))

        self.play(Write(numQ_label),Write(decimal))
        self.wait(1)

        self.play(t.animate.set_value(7))
        self.wait(1)
        self.play(t.animate.set_value(9))
        self.wait(1)
        self.play(t.animate.set_value(8))

        self.wait(1)

        self.play(numQ_label.animate(run_time=1).shift(UP * 2), decimal.animate(run_time=1).shift(UP  * 2))

        aSel_label = Text("Answer selections:").to_edge(LEFT).shift(RIGHT * 0.15, DOWN * 0.5)
        self.play(Write(aSel_label))
        aSel_actual = Text("A - C").next_to(aSel_label, DOWN).scale(1.7).shift(DOWN * 0.5)
        bSel_actual = Text("A - Z").next_to(aSel_label, DOWN).scale(1.7).shift(DOWN * 0.5)
        cSel_actual = Text("A - E").next_to(aSel_label, DOWN).scale(1.7).shift(DOWN * 0.5)
        

        decimal.clear_updaters()

        self.play(t.animate.set_value(6), Write(aSel_actual))
        self.wait(1)
        self.play(t.animate.set_value(10), Transform(aSel_actual, bSel_actual))
        self.wait(1)
        self.play(t.animate.set_value(8), Transform(aSel_actual, cSel_actual))
        self.wait(1)

        self.play(ax.animate(run_time=1).shift(RIGHT * 10), numQ_label.animate(run_time=1).shift(UP * 8), vg.animate(run_time=1).shift(RIGHT * 10), aSel_label.animate(run_time=1).shift(DOWN * 8), aSel_actual.animate(run_time=1).shift(DOWN * 8), decimal.animate(run_time=1).shift(UP * 8))


