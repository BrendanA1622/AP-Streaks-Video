from manim import * 
import math
import random

class Slide2Anim(Scene):
    def construct(self):
        AP1 = ImageMobject("assets/img/APCourseEmblems/AP1.png")
        AP2 = ImageMobject("assets/img/APCourseEmblems/AP2.png")
        AP3 = ImageMobject("assets/img/APCourseEmblems/AP3.png")
        AP4 = ImageMobject("assets/img/APCourseEmblems/AP4.png")
        AP5 = ImageMobject("assets/img/APCourseEmblems/AP5.png")
        AP6 = ImageMobject("assets/img/APCourseEmblems/AP6.png")
        AP7 = ImageMobject("assets/img/APCourseEmblems/AP7.png")
        AP8 = ImageMobject("assets/img/APCourseEmblems/AP8.png")
        AP9 = ImageMobject("assets/img/APCourseEmblems/AP9.png")
        AP10 = ImageMobject("assets/img/APCourseEmblems/AP10.png")
        AP11 = ImageMobject("assets/img/APCourseEmblems/AP11.png")
        AP12 = ImageMobject("assets/img/APCourseEmblems/AP12.png")
        AP13 = ImageMobject("assets/img/APCourseEmblems/AP13.png")
        AP14 = ImageMobject("assets/img/APCourseEmblems/AP14.png")
        AP15 = ImageMobject("assets/img/APCourseEmblems/AP15.png")
        AP16 = ImageMobject("assets/img/APCourseEmblems/AP16.png")
        AP17 = ImageMobject("assets/img/APCourseEmblems/AP17.png")
        AP18 = ImageMobject("assets/img/APCourseEmblems/AP18.png")
        AP19 = ImageMobject("assets/img/APCourseEmblems/AP19.png")
        AP20 = ImageMobject("assets/img/APCourseEmblems/AP20.png")
        AP21 = ImageMobject("assets/img/APCourseEmblems/AP21.png")
        AP22 = ImageMobject("assets/img/APCourseEmblems/AP22.png")
        AP23 = ImageMobject("assets/img/APCourseEmblems/AP23.png")
        AP24 = ImageMobject("assets/img/APCourseEmblems/AP24.png")
        AP25 = ImageMobject("assets/img/APCourseEmblems/AP25.png")
        AP26 = ImageMobject("assets/img/APCourseEmblems/AP26.png")
        AP27 = ImageMobject("assets/img/APCourseEmblems/AP27.png")
        AP28 = ImageMobject("assets/img/APCourseEmblems/AP28.png")
        AP29 = ImageMobject("assets/img/APCourseEmblems/AP29.png")
        AP30 = ImageMobject("assets/img/APCourseEmblems/AP30.png")
        AP31 = ImageMobject("assets/img/APCourseEmblems/AP31.png")
        AP32 = ImageMobject("assets/img/APCourseEmblems/AP32.png")
        AP33 = ImageMobject("assets/img/APCourseEmblems/AP33.png")
        AP34 = ImageMobject("assets/img/APCourseEmblems/AP34.png")
        AP35 = ImageMobject("assets/img/APCourseEmblems/AP35.png")
        AP36 = ImageMobject("assets/img/APCourseEmblems/AP36.png")
        AP37 = ImageMobject("assets/img/APCourseEmblems/AP37.png")
        AP38 = ImageMobject("assets/img/APCourseEmblems/AP38.png")
        AP39 = ImageMobject("assets/img/APCourseEmblems/AP39.png")

        APEuro = ImageMobject("assets/img/APMCQTimes/APEuro.png")
        APCalcBC = ImageMobject("assets/img/APMCQTimes/APCalcBC.png")
        APBiology = ImageMobject("assets/img/APMCQTimes/APBiology.png")
        APLit = ImageMobject("assets/img/APMCQTimes/APLit.png")
        APChem = ImageMobject("assets/img/APMCQTimes/APChem.png")
        APPhysEM = ImageMobject("assets/img/APMCQTimes/APPhysEM.png")

        imgArray = [AP1,AP2,AP3,AP4,AP5,AP6,AP7,AP8,AP9,AP10,AP11,AP12,AP13,AP14,AP15,AP16,AP17,AP18,AP19,AP20,AP21,AP22,AP23,AP24,AP25,AP26,AP27,AP28,AP29,AP30,AP31,AP32,AP33,AP34,AP35,AP36,AP37,AP38,AP39,]

        i = 0
        j = 0

        for specAP in imgArray:
            specAP.shift(DOWN * 6)
            specAP.scale(4)
            self.add(specAP)
            self.play(specAP.animate(run_time=2 / ((j * 10 + i) + 2)).shift(UP * (9.5 - (i * 0.8)), LEFT * (6 - (j * 4))).scale(0.2))

            i += 1
            if i >= 10:
                i = 0
                j += 1

        self.wait(3)

        l1 = Line()
        APEuro.set_y(AP11.get_y() - 1)
        APEuro.set_x(AP11.get_x() - 2)
        APEuro.scale(2.3)
        l1.put_start_and_end_on(APEuro.get_center(), AP11.get_center())

        l2 = Line()
        APCalcBC.set_y(AP22.get_y() - 1)
        APCalcBC.set_x(AP22.get_x() + 1)
        APCalcBC.scale(1.8)
        l2.put_start_and_end_on(APCalcBC.get_center(), AP22.get_center())

        l3 = Line()
        APBiology.set_y(AP25.get_y() - 1)
        APBiology.set_x(AP25.get_x() + 1)
        APBiology.scale(1.8)
        l3.put_start_and_end_on(APBiology.get_center(), AP25.get_center())

        l4 = Line()
        APLit.set_y(AP7.get_y() + 1.5)
        APLit.set_x(AP7.get_x() + 1.5)
        APLit.scale(1.8)
        l4.put_start_and_end_on(APLit.get_center(), AP7.get_center())

        l5 = Line()
        APChem.set_y(AP38.get_y())
        APChem.set_x(AP38.get_x() - 5)
        APChem.scale(1.8)
        l5.put_start_and_end_on(APChem.get_center(), AP38.get_center())

        l6 = Line()
        APPhysEM.set_y(AP30.get_y() + 0.5)
        APPhysEM.set_x(AP30.get_x() - 5)
        APPhysEM.scale(1.4)
        l6.put_start_and_end_on(APPhysEM.get_center(), AP30.get_center())

        animations = [
            FadeIn(l1),
            FadeIn(APEuro),
            FadeIn(l2),
            FadeIn(APCalcBC),
            FadeIn(l3),
            FadeIn(APBiology),
            FadeIn(l4),
            FadeIn(APLit),
            FadeIn(l5),
            FadeIn(APChem),
            FadeIn(l6),
            FadeIn(APPhysEM),
        ]

        self.play(AnimationGroup(*animations, lag_ratio=0.3))

        self.wait(4)

        outimations = [
            FadeOut(AP1),
            FadeOut(AP2),
            FadeOut(AP3),
            FadeOut(AP4),
            FadeOut(AP5),
            FadeOut(AP6),
            FadeOut(AP7),
            FadeOut(AP8),
            FadeOut(AP9),
            FadeOut(AP10),
            FadeOut(AP11),
            FadeOut(AP12),
            FadeOut(AP13),
            FadeOut(AP14),
            FadeOut(AP15),
            FadeOut(AP16),
            FadeOut(AP17),
            FadeOut(AP18),
            FadeOut(AP19),
            FadeOut(AP20),
            FadeOut(AP21),
            FadeOut(AP22),
            FadeOut(AP23),
            FadeOut(AP24),
            FadeOut(AP25),
            FadeOut(AP26),
            FadeOut(AP27),
            FadeOut(AP28),
            FadeOut(AP29),
            FadeOut(AP30),
            FadeOut(AP31),
            FadeOut(AP32),
            FadeOut(AP33),
            FadeOut(AP34),
            FadeOut(AP35),
            FadeOut(AP36),
            FadeOut(AP37),
            FadeOut(AP38),
            FadeOut(AP39),
            FadeOut(l1),
            FadeOut(APEuro),
            FadeOut(l2),
            FadeOut(APCalcBC),
            FadeOut(l3),
            FadeOut(APBiology),
            FadeOut(l4),
            FadeOut(APLit),
            FadeOut(l5),
            FadeOut(APChem),
            FadeOut(l6),
            FadeOut(APPhysEM),
        ]

        self.play(AnimationGroup(*outimations, lag_ratio=0.05))
        self.wait(4)
