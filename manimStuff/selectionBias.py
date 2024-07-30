from manim import *
import math
import random

class selectionBias(Scene):

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"

    def construct(self):
        ex1Text = Text("Test #1)  A E B B D A C C E D").shift(UP * 3)
        ex2Text = Text("Test #2)  E C E B D D A A D A").shift(UP * 1.5)
        ex3Text = Text("Test #3)  D E B A E D C C C C")
        ex3streak = Text("C C C C", color=RED).shift(RIGHT * 3.25, UP * 0.05)
        ex4Text = Text("Test #4)  D A C C E E E B A D").shift(UP * -1.5)
        ex5Text = Text("Test #5)  E B C C A B E A D C").shift(UP * -3)

        animations = [
            Write(ex1Text),
            Write(ex2Text),
            Write(ex3Text),
            Write(ex4Text),
            Write(ex5Text),
        ]

        self.play(AnimationGroup(*animations, lag_ratio = 0.2))
        self.play(FadeIn(ex3streak))

        self.wait(3)