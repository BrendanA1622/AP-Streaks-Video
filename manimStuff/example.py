from manim import * 
import random

vg = VGroup()

class oneMCQAnswer(Scene):
    def construct(self):

        texts1 = VGroup(Text('A').set_x(-2), Text('B').set_x(-1), Text('C'), Text('D').set_x(1), Text('E').set_x(2))

        self.play(FadeIn(texts1))
        self.wait(1)

        selectionCircle = Circle(radius=0.5, color=BLUE).set_x(random.randint(-2,2))
        self.play(Write(selectionCircle))
        self.wait(1)

        vg.add(texts1)
        vg.add(selectionCircle)

        self.play(vg.animate.shift(UP))
        self.wait(1)


        for i in range(3):
            texts1 = VGroup(Text('A').set_x(-2), Text('B').set_x(-1), Text('C'), Text('D').set_x(1), Text('E').set_x(2))

            self.play(FadeIn(texts1))

            selectionCircle = Circle(radius=0.5, color=BLUE).set_x(random.randint(-2,2))
            self.play(Write(selectionCircle))

            vg.add(texts1)
            vg.add(selectionCircle)

            if i < 2:
                self.play(vg.animate.shift(UP))
            else:
                self.play(vg.animate.shift(UP * 5))
        




