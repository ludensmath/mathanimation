from manim import *

from manim_physics import *

class grav0(SpaceScene):
    def construct(self):
        ground = Line(LEFT * 5, RIGHT * 5, color=ORANGE).shift(DOWN)
        self.add(ground)
        self.make_static_body(ground)
        forms = [
            r"e^{i\pi}+1=0",
            r"\cos(x+y)=\cos x \cos y - \sin x \sin y",
            r"\displaystyle \int_{-\infty }^{\infty }e^{-x^{2}}\,dx={\sqrt {\pi }}",
        ]
        cols = [RED, BLUE, YELLOW]
        for f, col in zip(forms, cols):
            text = MathTex(f, color=col)
            self.add(text)
            self.make_rigid_body(text[0])
            self.wait(2)

class magnt0(Scene):
    def construct(self):
        magnet1 = BarMagnet().shift(LEFT * 2.5)
        #magnet2 = Current(RIGHT * 2.5, direction=IN)

    def rebuild(field):
        field = MagneticField(magnet1)
        field.become(MagneticField(magnet1))
        self.play(Write(field),run_time=4)
        self.play(FadeIn(magnet1), run_time=4)
        self.play(field.animate.shift(DOWN * 3))
        self.play(magnet1.animate.shift(DOWN*3))
