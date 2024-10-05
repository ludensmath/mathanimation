from manim import*
class katarif(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        plano = NumberPlane(x_range=(-200,200),y_range=(-200,200),
                            background_line_style={
                                "stroke_color":BLACK,
                                "stroke_width":2,
                            },
                            axis_config={
                                "stroke_width": 0,
                                "include_ticks": False,
                                "include_tip": False
                            }
                            )
        self.add(plano)

        tex1 = Text("Universidad Central del Ecuador").move_to(UP * 3.5).scale(1.3).set_color(BLACK)
        tex2 = Paragraph('Carrera de Pedagogía de las Ciencias Experimentales','Matemática y Física',alignment="center").move_to(UP * 2).scale(.9).set_color(BLACK)
        tex3 = Text("Docente: Msc. Edgar Casanova").move_to(DOWN * 3 + RIGHT * -2).scale(1).set_color(BLACK)
        ex3 = Text("Quinto B").move_to(DOWN * 3 + RIGHT * 5).scale(1).set_color(BLACK)
        texto = Text("Geometría Fractal Andina", ).set_color_by_gradient(RED, GOLD, YELLOW, GREEN, TEAL, BLUE)
        texto.scale(1.5)

        self.play(Write(tex1))
        self.play(Write(tex2))
        self.play(Write(tex3))
        self.play(Write(ex3))
        self.play(Write(texto))
        self.play(Circumscribe(texto),run_time=1.3,color=RED)
        self.play(FadeOut(tex3,tex2,tex1,texto,ex3))
        self.wait(2)
#yellowB, yellowC linea, y Gold B circl
        for j in range(1,11):
            C1 = Square(side_length=(2**(j-1))**1/2, color=RED).set_style(stroke_width=20)
            Cup=Rectangle(height=4**j,width=2).set_color(RED)
            Cdw=Rectangle(height=4**j,width=2).set_color(RED)
            Crht=Rectangle(height=2,width=4**j).set_color(RED)
            Clt=Rectangle(height=2,width=4**j).set_color(RED)
            Cup.set_opacity(0.1).shift(UP*(j+1))
            Cdw.set_opacity(0.1).shift(DOWN * (j + 1))
            Clt.set_opacity(0.1).shift(LEFT * (j + 1))
            Crht.set_opacity(0.1).shift(RIGHT * (j + 1))
            l1= DashedLine(start=np.array([j+4,-j-4,0]),end=np.array([-j-4,j+4,0]))
            l2 = DashedLine(start=np.array([-j-4,-j-4,0]),end=np.array([j+4,j+4,0]))
            l1.set_color(MAROON).scale(3)
            l2.set_color(MAROON).scale(3)
            self.play(Create(C1), run_time=0.5)
            self.add(l1,l2)
            self.play(self.camera.frame.animate.scale((j+1)/(j)))
            self.add(Cup,Cdw,Clt,Crht)

        for i in range(8,1,-1):
            O1 = Circle(color=ORANGE, radius=((2**i)**1/2)*0.5).set_style(stroke_width=20)
            self.play(Create(O1), run_time=.5)
            self.play(self.camera.frame.animate.scale((i)/(i+1.8)),run_time=i/(i+1))

        self.wait(3)



