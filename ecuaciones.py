from manim import*
class ecu(Scene):
    def construct(self):
        eq0=MathTex("\\frac{1}{2}x^2-7^2 x-140=\sqrt{x} \\",substrings_to_isolate="x").move_to(UP*3+LEFT*3)
        eqo = MathTex(r"\frac{1}{2}x^2-7^2 x-140=\sqrt{x} ", substrings_to_isolate="x").move_to(UP * 3 + LEFT * 3)
        eqo.set_color_by_tex("x",BLUE)
        eq1 = MathTex(r"\frac{1}{2}x^2-7^2 x-140=\sqrt{x}").move_to(UP * 1.5 + LEFT * 3)
        eq1.set_color_by_tex("x",TEAL)
        eq2 = MathTex(r"x=\frac{-b \pm \sqrt{b^2-4ac}}{2a}").move_to(UP *0.5 + LEFT * 3)
       # m2 = Matrix([[1,0,0],[1,0,1]]).move_to(RIGHT*3+DOWN*2)
        #m1 = Matrix([["2","3","4"],["6","6","6"],["1","0","0"]]).move_to(RIGHT * 3 + UP * 2)
        self.play(Write(eqo))
        self.play(Write(eq1))
        self.play(Write(eq2))
        #self.add(m2[1],m2[3])
        #self.add(m1[0],m1[2])
        self.wait()
       # self.play(Transform(m1[0],m2[0]),run_time=3)

class ecu1(Scene):
    def construct(self):
        eq0 = MathTex("\\frac{1}{2}x^2","-7^2 x","-140","=","\\sqrt{x}").move_to(UP * 3 + LEFT * 3).scale(0.7)
        eq1 = MathTex(r"\frac{1}{2}x^2-7^2 x-140=\sqrt{x}").move_to(UP * 1.5 + LEFT * 3).scale(1.2)
        eq2 = MathTex(r"x=-b \pm \sqrt{b^2-4ac}","\over","{2a}",color=TEAL_A).move_to(DOWN * 1.5).scale(2)
        eq2[0].set_color(PINK)
        eq2[2].set_color(GREEN_A)
        self.play(Write(eq0[0]))
        self.wait()
        self.play(Write(eq0[1]))
        self.wait()
        self.play(Write(eq0[2]))
        self.wait()
        self.play(Write(eq0[3]))
        self.wait()
        self.play(Write(eq0[4]))
        self.wait()
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait()

class ecu2(Scene):
    def construct(self):
        self.camera.background_color = BLUE_A
        texto=Text("Valor numérico",color=RED_A).move_to(UP*3)
        eq0=MathTex(
                    "(x-","(-2)",")^2+(y-","10",")^2=(","3",")^2"
                    ).move_to(UP*2).set_color_by_gradient(GOLD_E,TEAL_E,BLUE_D,MAROON)
        eq1=MathTex("h=","-2").set_color(ORANGE).move_to(LEFT*3+UP)
        eq2 = MathTex("k=","10").set_color(TEAL_E).move_to(UP)
        eq3 = MathTex("r=","3").set_color(GOLD_D).move_to(RIGHT*3+UP)
        self.play(Write(texto))
        self.wait(2)
        self.play(Write(eq0[0]),Write(eq0[2]),Write(eq0[4]),Write(eq0[6]))
        self.add(eq3,eq2,eq1)
        self.wait(4)
        self.play(Transform(eq3[1],eq0[5]),Transform(eq2[1],eq0[3]),Transform(eq1[1],eq0[1]))
        self.wait(4)

class ecu3(Scene):
    def construct(self):
        eq0=MathTex(r'x+3&=","5\\ "-3","+x+3&=","5","-3"\\ "x&=", "2" ').move_to(UP*3)
        self.add(eq0)