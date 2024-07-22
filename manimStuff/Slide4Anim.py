from manim import * 
import math
import random

class Slide4Anim(MovingCameraScene):
    def construct(self):
        circle = Circle(radius=0.00).shift(LEFT * 1.1)
        self.add(circle)
        self.camera.frame.move_to(circle)
        self.camera.frame.set(width=1.0)
        self.camera.frame.save_state()
        self.camera.frame.set(width=0.1)
        fourB = Text("B  B  B  B", color=MAROON_C)
        self.play(Write(fourB, run_time=2), Restore(self.camera.frame))
        self.play(self.camera.frame.animate.set(width=3).move_to(fourB))
        self.wait(1)

        i = 0
        randFor1 = 0
        while i < 300:
            randLetter = Text("")
            randFor1 = random.randint(0,4)

            i += 1



        fourA1 = Text("A  A  A  A", color=MAROON_C).rotate(PI/7).shift(UP * 2, LEFT * 5)
        fourA2 = Text("A  A  A  A", color=MAROON_C).rotate(PI/12).shift(UP * -3.5, LEFT * 1)
        fourB1 = Text("B  B  B  B", color=MAROON_C).rotate(-PI/9).shift(UP * 1, LEFT * -7)
        fourC1 = Text("C  C  C  C", color=MAROON_C).rotate(-PI/8).shift(UP * 3.5, LEFT * 1)
        fourD1 = Text("D  D  D  D", color=MAROON_C).rotate(PI/8).shift(UP * -2, LEFT * 6)
        fourD2 = Text("D  D  D  D", color=MAROON_C).rotate(-PI/14).shift(UP * -3, LEFT * -6.5)
        fourE1 = Text("E  E  E  E", color=MAROON_C).rotate(PI/6).shift(UP * 2, LEFT * -4)

        fiveE = Text("E  E  E  E  E", color=GOLD_A).rotate(PI/6.5).shift(UP * -1, LEFT * -5)

        self.play(self.camera.frame.animate.set(width=20), AnimationGroup(Write(fourA1), Write(fourD1),Write(fourC1),Write(fiveE),Write(fourD2),Write(fourE1),Write(fourB1),Write(fourA2), lag_ratio=0.3))
        
        fourStreaks = VGroup()
        fourStreaks.add(fourB,fourA1,fourA2,fourB1,fourC1,fourD1,fourD2,fourE1)
        
        goldRect = Rectangle(width=30.0, height=2, color=GOLD_A, fill_color=GOLD_A, fill_opacity=0.9).shift(RIGHT * 30, DOWN * 5)
        pinkRect = Rectangle(width=30.0, height=6, color=MAROON_B, fill_color=MAROON_B, fill_opacity=0.9).shift(RIGHT * 0, DOWN * 3)
        greenRect = Rectangle(width=30.0, height=20.0, color=GREEN, fill_color=GREEN, fill_opacity=0.9).shift(RIGHT * -30, DOWN * -4)
        blueRect = Rectangle(width=30.0, height=80.0, color=BLUE_C, fill_color=BLUE_C, fill_opacity=0.9).shift(RIGHT * -60, DOWN * -34)
        whiteRect = Rectangle(width=30.0, height=250.0, color=WHITE, fill_color=WHITE, fill_opacity=0.9).shift(RIGHT * -90, DOWN * -119)

        self.add(greenRect,blueRect,whiteRect)
        finalcenter = Circle(radius=1)
        finalcenter.shift(UP * 125, LEFT * 30)
        almostcenter = Circle(radius=1)
        self.play(Transform(fourStreaks, pinkRect),Transform(fiveE, goldRect), self.camera.frame.animate.set(width=50).move_to(almostcenter))
        self.wait(0.5)
        self.play(self.camera.frame.animate.set(width=550).move_to(finalcenter))
        self.wait(1)

        self.remove(fourStreaks,fiveE)

        leftamount = 450

        self.play(AnimationGroup(whiteRect.animate(run_time=1).shift(LEFT * leftamount),blueRect.animate(run_time=1).shift(LEFT * leftamount),greenRect.animate(run_time=1).shift(LEFT * leftamount),pinkRect.animate(run_time=1).shift(LEFT * leftamount),goldRect.animate(run_time=1).shift(LEFT * leftamount), lag_ratio=0.15))
        























        self.wait(1)