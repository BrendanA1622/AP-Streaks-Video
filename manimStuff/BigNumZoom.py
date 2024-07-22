from manim import * 
import math
import random

class BigNumZoom(MovingCameraScene):
    def construct(self):
        firstRect = Rectangle(width = 6, height = 4, color=GREY_A, fill_opacity=1.0, stroke_color=BLACK)
        self.add(firstRect)

        tlRect = Rectangle(width=6, height=4, fill_color=GREY_B, fill_opacity=0.9).shift(LEFT * 7, UP * 5)
        tRect = Rectangle(width=6, height=4, fill_color=GREY_A, fill_opacity=0.9).shift(LEFT * 0, UP * 5)
        trRect = Rectangle(width=6, height=4, fill_color=GREY_A, fill_opacity=0.9).shift(LEFT * -7, UP * 5)
        lRect = Rectangle(width=6, height=4, fill_color=GREY_B, fill_opacity=0.9).shift(LEFT * 7, UP * 0)
        rRect = Rectangle(width=6, height=4, fill_color=GREY_D, fill_opacity=0.9).shift(LEFT * -7, UP * 0)
        blRect = Rectangle(width=6, height=4, fill_color=GREY_B, fill_opacity=0.9).shift(LEFT * 7, UP * -5)
        bRect = Rectangle(width=6, height=4, fill_color=GREY_A, fill_opacity=0.9).shift(LEFT * 0, UP * -5)
        brRect = Rectangle(width=6, height=4, fill_color=GREY_A, fill_opacity=0.9).shift(LEFT * -7, UP * -5)

        vg = VGroup()
        width = 59
        height = 55
        j = 0
        k = 0
        while k < height:
            newRect = Rectangle(width = 6, height = 4, fill_color=GREY_A, fill_opacity=0.9).shift(LEFT * (7 * (((width - 1)/2) - j)), UP * (5 * (((height - 1)/2) - k)))
            randy = random.randint(0,1000)
            if randy < 300:
                newRect.fill_color = GREY_A
            elif randy < 600:
                newRect.fill_color = GREY_B
            elif randy < 900:
                newRect.fill_color = GREY_C
            elif randy < 950:
                newRect.fill_color = GRAY
            else:
                newRect.fill_color = GREY_D
            
            j += 1
            if j >= width:
                j = 0
                k += 1
            
            if j >= (width-1)/2 and j <= (width+1)/2 + 1 and k >= (height-1)/2 - 1 and k <= (height+1)/2:
                pass
            else:
                self.add(newRect)
            
            vg.add(newRect)



        self.play(AnimationGroup(Create(lRect), Create(tRect),Create(rRect),Create(bRect),Create(tlRect),Create(trRect),Create(brRect),Create(blRect),lag_ratio = 0.1))

        self.play(self.camera.frame.animate(run_time=3).set(width=1000))
        overallRect = Rectangle(width = 421.875, height = 281.25, color=GREEN_A, fill_opacity=1.0)
        self.play(FadeIn(overallRect))
        self.wait(0.3)
