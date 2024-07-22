from manim import * 
import random


class ContinualAnswers(Scene):
    def construct(self):
        examImg = ImageMobject("assets/img/examImg3.png").shift(RIGHT * 2.6,DOWN * 23)
        circleQ1 = Circle(radius=0.4, color=RED).shift(LEFT * 0.4,UP * 1.68)
        circleQ2 = Circle(radius=0.4, color=GREEN).shift(LEFT * 0.4,DOWN * 1.02)
        circleQ3 = Circle(radius=0.4, color=BLUE).shift(LEFT * 0.4,UP * 0.48)
        circleQ4 = Circle(radius=0.4, color=BLUE).shift(LEFT * 0.4,UP * 0.33)
        circleQ5 = Circle(radius=0.4, color=BLUE).shift(LEFT * 0.4,UP * 0.22)
        circleQ6 = Circle(radius=0.4, color=BLUE).shift(LEFT * 0.4,UP * 0.05)
        examImg.scale(2.2)
        self.add(examImg)
        # self.play(Create(circleQ1))
        # self.play(Create(circleQ2))
        # self.play(Create(circleQ3))
        # self.play(Create(circleQ4))
        # self.play(Create(circleQ5))
        # self.play(Create(circleQ6))
        self.wait(1)

        numbers = Text("1).\n\n2).\n\n3).\n\n4).\n\n5).\n\n6).", font="sans-serif")
        numbers.shift(LEFT*5)

        answers1 = Text("A", font="comic-sans-ms", t2c={"A": RED}).shift(UP * 3.3)
        answers2 = Text("D", font="sans-serif", t2c={"D": GREEN}).shift(UP * 1.95)
        answers3 = Text("B", font="sans-serif", t2c={"B": BLUE}).shift(UP * 0.666)
        boundary1 = AnimatedBoundary(answers3, colors=[YELLOW,RED,GREEN], cycle_rate=0.5, max_stroke_width=2)
        
        answers4 = Text("B", font="sans-serif", t2c={"B": BLUE}).shift(DOWN * 0.666)
        boundary2 = AnimatedBoundary(answers4, colors=[YELLOW,RED,GREEN], cycle_rate=0.5, max_stroke_width=2)
        
        answers5 = Text("B", font="sans-serif", t2c={"B": BLUE}).shift(DOWN * 1.95)
        boundary3 = AnimatedBoundary(answers5, colors=[YELLOW,RED,GREEN], cycle_rate=0.5, max_stroke_width=2)
        
        answers6 = Text("B", font="sans-serif", t2c={"B": BLUE}).shift(DOWN * 3.3)
        boundary4 = AnimatedBoundary(answers6, colors=[YELLOW,RED,GREEN], cycle_rate=0.5, max_stroke_width=2)
        
        answers = VGroup(answers1,answers2,answers3,answers4,answers5,answers6)
        answers.shift(LEFT*4)
        self.wait(0.5)
        self.play(examImg.animate(run_time=2).shift(UP * 10), SpiralIn(numbers))
        self.wait(0.1)
        self.play(Create(circleQ1))
        self.play(Write(answers1))
        self.wait(0.5)
        self.play(examImg.animate(run_time=2).shift(UP * 5.1), circleQ1.animate(run_time=2).shift(UP * 5.1))
        self.play(Create(circleQ2))
        self.play(Write(answers2))
        self.wait(0.5)
        self.play(examImg.animate(run_time=2).shift(UP * 5.4), circleQ2.animate(run_time=2).shift(UP * 5.5))
        self.play(Create(circleQ3))
        self.play(Write(answers3))
        self.wait(0.5)
        self.play(examImg.animate(run_time=2).shift(UP * 5.3), circleQ3.animate(run_time=2).shift(UP * 5.3))
        self.play(Create(circleQ4))
        self.play(Write(answers4))
        self.wait(0.5)
        self.play(examImg.animate(run_time=2).shift(UP * 5.4), circleQ4.animate(run_time=2).shift(UP * 5.4))
        self.play(Create(circleQ5))
        self.play(Write(answers5))

        self.add(boundary1,boundary2,boundary3,boundary4)

        self.wait(0.5)
        self.play(examImg.animate(run_time=2).shift(UP * 5.3), circleQ5.animate(run_time=2).shift(UP * 5.3))
        self.play(Create(circleQ6))
        self.play(Write(answers6))
        # self.add(boundary4)
        self.wait(0.5)

        self.wait(0.5)
        self.remove(boundary1,boundary2,boundary3,boundary4)
        self.play(examImg.animate(run_time=2).shift(UP * 10), circleQ6.animate(run_time=2).shift(UP * 10), numbers.animate(run_time=2).shift(UP * 10), answers1.animate(run_time=2).shift(UP * 10), answers2.animate(run_time=2).shift(UP * 10), answers3.animate(run_time=2).shift(DOWN * 0.666, RIGHT).scale(3), answers4.animate(run_time=2).shift(UP * 0.666, RIGHT * 3).scale(3), answers5.animate(run_time=2).shift(UP * 1.95, RIGHT * 5).scale(3), answers6.animate(run_time=2).shift(UP * 3.3, RIGHT * 7).scale(3))
        self.wait(0.5)
        self.play(answers3.animate(run_time=2).shift(UP * 6, LEFT * 8), answers4.animate(run_time=2).shift(UP * 9, LEFT * 4), answers5.animate(run_time=2).shift(UP * 9, RIGHT * 4), answers6.animate(run_time=2).shift(UP * 6, RIGHT * 8))
        
        self.wait(1)