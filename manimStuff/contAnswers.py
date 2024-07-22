from manim import * 
import random

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
Z = 'Z'
arr = [E,D,D,E,D,D,A,D,A,B,E,E,E,D,D,B,A,C,E,D,B,C,B,A,E,D,D,A,A,A,Z,Z,Z,Z,Z]

class ContinualAnswers(MovingCameraScene):
    def construct(self):
        vg = VGroup()

        animations = []
        i = 0
        thrCount = 0
        twoBool = False
        for let in arr:
            if(arr[i] != Z and thrCount == 0 and twoBool == False):
                if(arr[i] == arr[i + 1] and arr[i] == arr[i + 2]):
                    ans = Text(str(i + 1) + "). " + let, color=GREEN)
                    thrCount = 2
                elif(arr[i] == arr[i + 1]):
                    ans = Text(str(i + 1) + "). " + let, color=BLUE_C)
                    twoBool = True
                else:
                    ans = Text(str(i + 1) + "). " + let, color=WHITE)
                animations.append(Write(ans))
                vg.add(ans)
            elif thrCount > 0:
                ans = Text(str(i + 1) + "). " + let, color=GREEN)
                thrCount -= 1
                animations.append(Write(ans))
                vg.add(ans)
            elif twoBool:
                ans = Text(str(i + 1) + "). " + let, color=BLUE_C)
                twoBool = False
                animations.append(Write(ans))
                vg.add(ans)
            
            ans.set_x(-6 + (2.35 * int(i / 5)))
            ans.set_y(3 - (1.5 * i) % 7.5)
            
            i += 1
        
        lastAns = Text("30). A", color=GREEN)
        lastAns.set_x(-6 + (2.35 * 5))
        lastAns.set_y(3 - (1.5 * 4))
        animations.append(Write(lastAns))
        vg.add(lastAns)
        vgorig = vg

        self.play(AnimationGroup(*animations, lag_ratio=0.15))

        firstRect = Rectangle(width=6, height=4, fill_color=LOGO_GREEN, fill_opacity=0.9)
        self.wait(1)
        self.play(Transform(vg,firstRect))
        self.wait(1)

        tlRect = Rectangle(width=6, height=4, fill_color=TEAL_A, fill_opacity=0.9).shift(LEFT * 7, UP * 5)
        tRect = Rectangle(width=6, height=4, fill_color=LOGO_GREEN, fill_opacity=0.9).shift(LEFT * 0, UP * 5)
        trRect = Rectangle(width=6, height=4, fill_color=TEAL_B, fill_opacity=0.9).shift(LEFT * -7, UP * 5)
        lRect = Rectangle(width=6, height=4, fill_color=WHITE, fill_opacity=0.9).shift(LEFT * 7, UP * 0)
        rRect = Rectangle(width=6, height=4, fill_color=TEAL_C, fill_opacity=0.9).shift(LEFT * -7, UP * 0)
        blRect = Rectangle(width=6, height=4, fill_color=RED_A, fill_opacity=0.9).shift(LEFT * 7, UP * -5)
        bRect = Rectangle(width=6, height=4, fill_color=TEAL_A, fill_opacity=0.9).shift(LEFT * 0, UP * -5)
        brRect = Rectangle(width=6, height=4, fill_color=WHITE, fill_opacity=0.9).shift(LEFT * -7, UP * -5)


        vg = VGroup()
        width = 59
        height = 55
        j = 0
        k = 0
        while k < height:
            newRect = Rectangle(width = 6, height = 4, fill_color=TEAL_A, fill_opacity=0.9).shift(LEFT * (7 * (((width - 1)/2) - j)), UP * (5 * (((height - 1)/2) - k)))
            randy = random.randint(0,1000)
            if randy < 300:
                newRect.fill_color = TEAL_A
            elif randy < 600:
                newRect.fill_color = TEAL_B
            elif randy < 680:
                newRect.fill_color = GREY_B
            elif randy < 800:
                newRect.fill_color = WHITE
            elif randy < 930:
                newRect.fill_color = GREY_A
            elif randy < 990:
                newRect.fill_color = TEAL_C
            elif randy < 999:
                newRect.fill_color = RED_A
            else:
                newRect.fill_color = PURPLE
            
            j += 1
            if j >= width:
                j = 0
                k += 1
            
            if j >= (width-1)/2 and j <= (width+1)/2 + 1 and k >= (height-1)/2 - 1 and k <= (height+1)/2:
                pass
            else:
                self.add(newRect)
            
            vg.add(newRect)

        self.play(AnimationGroup(Create(lRect), Create(tRect),Create(rRect),Create(bRect),Create(tlRect),Create(trRect),Create(brRect),Create(blRect),lag_ratio = 0.1), self.camera.frame.animate(run_time=2).set(width=21))
        
        
        self.play(self.camera.frame.animate(run_time=3).set(width=1000))

        overallRect = Rectangle(width = 421.875, height = 281.25, color=GREY_A, fill_opacity=1.0)
        self.play(FadeIn(overallRect))
























        self.wait(2)
