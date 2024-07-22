from manim import * 
import math
import random

class ZoomFinalExplainer(MovingCameraScene):
    def construct(self):

        secondSample = ImageMobject("assets/img/secondSampleOther.png").shift(LEFT*4.5,UP*2).scale(0.8)
        thirdSample = ImageMobject("assets/img/thirdSampleOther.png").shift(RIGHT*4.0,UP*1.5).scale(0.8)
        fourthSample = ImageMobject("assets/img/fourthSampleOther.png").shift(RIGHT*4.0,DOWN*2.5).scale(0.8)

        firstRect = Rectangle(width = 6, height = 4, color=WHITE, fill_opacity=1.0, stroke_color=BLACK)
        self.add(firstRect)

        numberText = Text("931 Quintillion").shift(UP * 3)
        self.play(Write(numberText))

        uniqueExams = Text("UNIQUE EXAMS", color = ORANGE).shift(DOWN * 3)
        self.play(FadeIn(uniqueExams))

        self.play(AnimationGroup(FadeIn(secondSample),FadeIn(thirdSample),FadeIn(fourthSample), lag_ratio=0.4))
        vg = VGroup()
        vg.add(numberText,uniqueExams)
        self.wait(2)
        self.play(Transform(vg,firstRect), secondSample.animate(run_time=1).shift(UP * 5,LEFT * 9), thirdSample.animate(run_time=1).shift(UP * 4.5,LEFT * -10), fourthSample.animate(run_time=1).shift(UP * -11,LEFT * -11), self.camera.frame.animate(run_time=2).set(width=3))
        self.wait(3)
