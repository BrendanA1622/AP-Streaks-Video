from manim import *
import math
import random

class graphPlayground(MovingCameraScene):
    
    def construct(self):
        a = ValueTracker(1)

        def get_ax():
            ax1 = Axes(x_range=[-10,10],y_range=[0,10 * a.get_value(),a.get_value()],x_length=5,y_length=5)
            return ax1
        
        ax = always_redraw(get_ax())

        self.add(ax)

        self.play(a.animate.set_value(2))

        self.wait(3)