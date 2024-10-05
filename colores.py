from manim import *
class ccolor(Scene):
    def construct(self):
        self.camera.background_color=BLUE_A
        texto0=Text("Gissela Caizatoa",color=PURPLE_A).move_to(UP*4)
        texto1 = Text("Gissela Caizatoa", color=YELLOW_C).move_to(UP * 3)
        texto2 = Text("Gissela Caizatoa", color=GOLD_C).move_to(UP * 2)
        texto3 = Text("Gissela Caizatoa", color=RED_C).move_to(UP * 1)
        texto4 = Text("Gissela Caizatoa", color=MAROON_E)
        texto5 = Text("Gissela Caizatoa", color=BLUE_E).move_to(DOWN * 1)
        texto6 = Text("Gissela Caizatoa", color=TEAL_C).move_to(DOWN * 2)
        texto7 = Text("Gissela Caizatoa", color=PINK).move_to(DOWN * 3)
        self.play(Write(texto0))
        self.play(Write(texto1))
        self.play(Write(texto2))
        self.play(Write(texto3))
        self.play(Write(texto4))
        self.play(Write(texto5))
        self.play(Write(texto6))
        self.play(Write(texto7))

class ccolor1 (Scene):
    def construct(self):
        color1="#00FED8"
        color2="#FF4D00"
        color3="#9EFF00"
        color4="#5B2517"
        color5="#E8C39E"
        self.camera.background_color = color5
        texto0 = Text("Gissela Caizatoa", color=color1).move_to(UP * 3.5).scale(2)
        texto1 = Text("Gissela Caizatoa").move_to(UP * 3).set_color(color2)
        texto2 = Text("Gissela Caizatoa", color=GOLD_C).move_to(UP * 2)
        texto2.set_color(color3)
        texto3 = Text("Gissela Caizatoa", color=color4).move_to(UP * 1)
        texto4 = Text("Gissela Caizatoa", color=GREY_BROWN)
        texto5 = Text("Gissela Caizatoa").set_color_by_gradient(color1,color2,color3,color4,color5).move_to(DOWN*2.5).scale(2.5)
        self.play(Write(texto0))
        self.play(Write(texto1))
        self.play(Write(texto2))
        self.play(Write(texto3))
        self.play(Write(texto4))
        self.play(Write(texto5))

class ccolor2 (Scene):
    def construct(self):
       texto= MarkupText(f'Aqui va el texto y <span fgcolor="{YELLOW_C}">color que deseemos</span>',color=PINK).move_to(UP*3+LEFT*4)
       texto1= Text("Aqui va el texto y color que deseemos",t2c={'[14:29]':YELLOW_C}).move_to(UP*2+LEFT*4)
       self.play(Write(texto))
       self.play(Write(texto1))
       self.wait()