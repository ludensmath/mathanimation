import numpy as np
from manim import *
class leccion1(Scene):
    def construct(self):
        text1=Text("El origen del cálculo integral se remonta a la época de Arquímedes  (287-212 a.C.), matemático griego de la antigüedad, que obtuvo resultados tan importantes como el valor del área encerrada por un segmento parabólico.")
        self.add(text1)
        self.wait(3)

class leccion2(Scene):
    def construct(self):
        text2=Text("El origen del cálculo integral se remonta a la época de Arquímedes (287-212 a.C.), matemático griego de la antigüedad")
        self.add(text2)
        self.wait(3)
        self.remove(text2)
        self.wait(3)

class leccion3(Scene):
    def construct(self):
        text3=Text("El orígen del Cálculo integral se remonta a la época de Arquímides")
        self.play(FadeIn(text3))
        self.wait(3)
        self.play(FadeOut(text3))
        self.wait(3)
        self.play(Write(text3))
        self.wait(3)

class leccion4(Scene):
    def construct(self):
        ejes=NumberPlane()
        self.add(ejes)
        self.wait()
        texto4=Text("Carmen").move_to(LEFT+UP)
        texto5=Text("Gissela").move_to(DOWN*2+RIGHT*2)
        texto6=Text("Caizatoa").move_to(np.array([3,3,0]))
        texto7=Text("Llumiquinga").move_to(np.array([-3,-3,0]))
        self.add(texto4,texto5,texto6,texto7)
        self.wait(6)



