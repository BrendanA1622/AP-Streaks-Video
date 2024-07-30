from manim import *
import math
import random

class apRandGraphCompare(MovingCameraScene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1]),
        ]
    
    def construct(self):

        ax = Axes(x_range=[0, 6], y_range=[0.0, 0.2, 0.02], x_length=4, y_length=4, axis_config={"include_numbers": True, "include_tip": False},).shift(UP * 8)
        labely = Text("Proportion of all streaks").shift(UP * 10.4,LEFT * 1.8).scale(0.6)
        labelx = Text("Streak length").shift(UP * 6,LEFT * -3.9).scale(0.7)
        self.add(ax,labely)
        self.play(ax.animate(run_time=1).shift(DOWN * 8), labely.animate(run_time=1).shift(DOWN * 8), labelx.animate(run_time=1).shift(DOWN * 8))

        apAcorn = ImageMobject("assets/img/apAcorn2.png").shift(DOWN * -2, RIGHT * 3)
        self.play(FadeIn(apAcorn))

        self.wait(1)

        finalCenter = Circle().shift(RIGHT * 5.5)
        self.play(self.camera.frame.animate.set(width=20).move_to(finalCenter))

#########################################################################################
        self.wait(1)

        ax2 = Axes(x_range=[0, 6], y_range=[0.0, 0.2, 0.02], x_length=4, y_length=4, axis_config={"include_numbers": True, "include_tip": False},).shift(UP * 10, RIGHT * 10)
        labely2 = Text("Proportion of all streaks").shift(UP * 12.4,LEFT * -8.2).scale(0.6)
        labelx2 = Text("Streak length").shift(UP * 8,LEFT * -13.9).scale(0.7)
        self.add(ax2,labely2)
        self.play(ax2.animate(run_time=1.2).shift(DOWN * 10), labely2.animate(run_time=1.2).shift(DOWN * 10), labelx2.animate(run_time=1.2).shift(DOWN * 10))

        diceCartoon = ImageMobject("assets/img/DiceCartoon.png").scale(0.5).shift(LEFT * -13, DOWN * -1.7)
        self.play(FadeIn(diceCartoon))

        self.wait(1)

        t = ValueTracker(0)
        def get_rectangle1():
            polygon1 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0.6, 0), (1.4, t.get_value())
                    )
                ]
            )
            polygon1.stroke_width = 1
            polygon1.set_fill(WHITE, opacity=0.9)
            polygon1.set_stroke(WHITE)
            return polygon1
        polygon1 = always_redraw(get_rectangle1)
        self.add(polygon1)

        r = ValueTracker(0)
        def rget_rectangle1():
            rpolygon1 = Polygon(
                *[
                    ax2.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0.6, 0), (1.4, r.get_value())
                    )
                ]
            )
            rpolygon1.stroke_width = 1
            rpolygon1.set_fill(WHITE, opacity=0.9)
            rpolygon1.set_stroke(WHITE)
            return rpolygon1
        rpolygon1 = always_redraw(rget_rectangle1)
        self.add(rpolygon1)

        self.play(t.animate.set_value(0.8340), r.animate.set_value(0.8066))

        self.wait(1)

        t2 = ValueTracker(0)
        def get_rectangle2():
            polygon2 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (1.6, 0), (2.4, t2.get_value())
                    )
                ]
            )
            polygon2.stroke_width = 1
            polygon2.set_fill(BLUE, opacity=0.9)
            polygon2.set_stroke(WHITE)
            return polygon2
        polygon2 = always_redraw(get_rectangle2)
        self.add(polygon2)

        r2 = ValueTracker(0)
        def rget_rectangle2():
            rpolygon2 = Polygon(
                *[
                    ax2.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (1.6, 0), (2.4, r2.get_value())
                    )
                ]
            )
            rpolygon2.stroke_width = 1
            rpolygon2.set_fill(BLUE, opacity=0.9)
            rpolygon2.set_stroke(WHITE)
            return rpolygon2
        rpolygon2 = always_redraw(rget_rectangle2)
        self.add(rpolygon2)

        self.play(t2.animate.set_value(0.1405), r2.animate.set_value(0.1560))

        self.wait(1)

        t3 = ValueTracker(0)
        def get_rectangle3():
            polygon3 = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (2.6, 0), (3.4, t3.get_value())
                    )
                ]
            )
            polygon3.stroke_width = 1
            polygon3.set_fill(GREEN, opacity=0.9)
            polygon3.set_stroke(WHITE)
            return polygon3
        polygon3 = always_redraw(get_rectangle3)
        self.add(polygon3)

        r3 = ValueTracker(0)
        def rget_rectangle3():
            rpolygon3 = Polygon(
                *[
                    ax2.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (2.6, 0), (3.4, r3.get_value())
                    )
                ]
            )
            rpolygon3.stroke_width = 1
            rpolygon3.set_fill(GREEN, opacity=0.9)
            rpolygon3.set_stroke(WHITE)
            return rpolygon3
        rpolygon3 = always_redraw(rget_rectangle3)
        self.add(rpolygon3)

        self.play(t3.animate.set_value(0.02554), r3.animate.set_value(0.03015))

        self.wait(1)

        finalCenter.move_to(ax2)
        finalCenter.shift(DOWN * 0.8,RIGHT * 0.6)

        self.play(self.camera.frame.animate.set(width=7).move_to(finalCenter))

        r4 = ValueTracker(0)
        def rget_rectangle4():
            rpolygon4 = Polygon(
                *[
                    ax2.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (3.6, 0), (4.4, r4.get_value())
                    )
                ]
            )
            rpolygon4.stroke_width = 1
            rpolygon4.set_fill(PINK, opacity=0.9)
            rpolygon4.set_stroke(WHITE)
            return rpolygon4
        rpolygon4 = always_redraw(rget_rectangle4)
        self.add(rpolygon4)

        r5 = ValueTracker(0)
        def rget_rectangle5():
            rpolygon5 = Polygon(
                *[
                    ax2.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (4.6, 0), (5.4, r5.get_value())
                    )
                ]
            )
            rpolygon5.stroke_width = 1
            rpolygon5.set_fill(GOLD_A, opacity=0.9)
            rpolygon5.set_stroke(WHITE)
            return rpolygon5
        rpolygon5 = always_redraw(rget_rectangle5)
        self.add(rpolygon5)

        r6 = ValueTracker(0)
        def rget_rectangle6():
            rpolygon6 = Polygon(
                *[
                    ax2.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (5.6, 0), (6.4, r6.get_value())
                    )
                ]
            )
            rpolygon6.stroke_width = 1
            rpolygon6.set_fill(PURPLE, opacity=0.9)
            rpolygon6.set_stroke(WHITE)
            return rpolygon6
        rpolygon6 = always_redraw(rget_rectangle6)
        self.add(rpolygon6)

        self.play(r4.animate.set_value(0.00582), r5.animate.set_value(0.00112), r6.animate.set_value(0.000216))

        self.play(self.camera.frame.animate.set(width=3).move_to(rpolygon5))

        self.wait(2)

        finalCenter.move_to(ax).shift(DOWN*0.8)

        self.play(self.camera.frame.animate.set(width=7).move_to(finalCenter))

        self.wait(1)

        nothingText = Text("None!").scale(0.7).shift(DOWN * 1.5,RIGHT * 1.33)

        self.play(FadeIn(nothingText))

        self.wait(2)

        blackOut = Circle(radius = 500, color = BLACK, fill_opacity=1.0)
        self.play(FadeIn(blackOut))






        self.wait(3)