from manim import *
import math
import random

class apToRandom(Scene):
    def construct(self):

        sep = 3.5

        apAcorn = ImageMobject("assets/img/apAcorn(3).jpg")
        apText = Text("AP ANSWERS").shift(UP*2)
        diceCartoon = ImageMobject("assets/img/DiceCartoon.png").scale(0.5).shift(DOWN * 0.4, RIGHT*sep)
        diceText = Text("RANDOM ANSWERS").shift(UP*2,RIGHT*sep)

        self.play(FadeIn(apAcorn))
        self.play(Write(apText))
        self.wait(0.5)
        self.play(apAcorn.animate(run_time=1.5).shift(LEFT*sep), apText.animate(run_time=1.5).shift(LEFT*sep))

        self.wait(1)

        self.play(FadeIn(diceCartoon))
        self.play(Write(diceText))
        self.wait(1)

        unequalTop = Rectangle(width=3.0, height=0.5, fill_color=RED, color=RED, fill_opacity=1.0).shift(UP * 0.5,LEFT*10)
        unequalBot = Rectangle(width=3.0, height=0.5, fill_color=RED, color=RED, fill_opacity=1.0).shift(UP * -0.5,RIGHT*10)
        unequalSlash = Rectangle(width=3.0, height=0.5, fill_color=RED, color=RED, fill_opacity=1.0).rotate(PI/3.5).shift(UP*10)

        self.add(unequalTop,unequalBot,unequalSlash)

        self.play(unequalTop.animate(run_time=1).shift(RIGHT*10),unequalBot.animate(run_time=1).shift(LEFT*10))
        self.play(unequalSlash.animate(run_time=1.5).shift(DOWN*10))


        self.wait(3)

        animations = [
            unequalBot.animate.shift(DOWN * 8),
            unequalSlash.animate.shift(DOWN * 8),
            unequalTop.animate.shift(DOWN * 8),
            apText.animate.shift(UP * 8),
            apAcorn.animate.shift(UP * 8),
            diceText.animate.shift(UP * 8),
            diceCartoon.animate.shift(UP * 8)
        ]

        self.play(AnimationGroup(*animations, lag_ratio=0.1))

        self.wait(3)