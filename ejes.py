from manim import *


class ejesengrid(Scene):
    def construct(self):
        ejes = Axes(x_range=[-5, 5, 1],
                    y_range=[-5, 5, 1], x_length=4,
                    y_length=4,
                    axis_config={"include_numbers": True,
                                 "include_tip": True,
                                 # 'tip_shape':ArrowTriangleFilledTip,
                                 'tip_width': 0.2,
                                 'tip_height': 0.3,
                                 'font_size': 20,  # maneja tamaño de los números
                                 'stroke_width': 3  # maneja el grosor de los ejes
                                 # 'label_direction': 45*DEGREES,
                                 }
                    ).scale(0.75)
        ejes1 = ejes.copy()
        ejes2 = ejes.copy()
        ejes3 = ejes.copy()
        g = Group(ejes, ejes1, ejes3, ejes2).arrange_in_grid(buff=0.5)
        lista = [ejes, ejes1, ejes2, ejes3]
        self.play(FadeIn(g))
        for i in lista:
            fct = i.plot(lambda x: np.cos(x), color=ORANGE)
            self.play(Create(fct))


class modeloejes(Scene):
    def construct(self):
        ejesp = Axes(
            x_range=[-10, 10, 1],
            y_range=[-5, 5, 1],
            x_length=13,
            y_length=7,
            axis_config={"include_numbers": True,
                         "include_tip": True,
                         # 'tip_shape':ArrowTriangleFilledTip,
                         'tip_width': 0.2,
                         'tip_height': 0.3,
                         'font_size': 25,  # maneja tamaño de los números
                         'stroke_width': 4  # maneja el grosor de los ejes
                         # 'label_direction': 45*DEGREES,
                         }
            # x_axis_config={"x_tick_frequency":2}
        )
        xlb = ejesp.get_x_axis_label(label="x", edge=RIGHT, direction=DOWN + RIGHT, buff=0.1)
        ylb = ejesp.get_y_axis_label(label="f(x)", edge=UP, direction=1.5 * UP + LEFT, buff=0.1)
        lbls = Group(ejesp, xlb, ylb)
        self.add(lbls)



class ejesejemplo(Scene):

    def construct(self):
        ejesp = Axes(x_range=[-10, 10, 1], y_range=[-5, 5, 1], x_length=13, y_length=7,
                     axis_config={"include_numbers": True,
                                  "include_tip": True,
                                  # 'tip_shape':ArrowTriangleFilledTip,
                                  'tip_width': 0.2,
                                  'tip_height': 0.3,
                                  'font_size': 25,  #maneja tamaño de los números
                                  'stroke_width': 4
                                  }
                     )  #maneja el grosor de los ejes

        #ejes y etiquetas
        xlb = ejesp.get_x_axis_label(label="x", edge=RIGHT, direction=DOWN + RIGHT, buff=0.1)
        ylb = ejesp.get_y_axis_label(label="f(x)", edge=UP, direction=1.5 * UP + LEFT, buff=0.1)
        lbls = Group(ejesp, xlb, ylb)

        #puntos y lineas axuliares
        p1 = Dot(ejesp.coords_to_point(-4, -4), color=GREEN)
        l1=ejesp.get_lines_to_point(ejesp.c2p(-4,-4),color=BLUE)
        lh=ejesp.get_horizontal_line(ejesp.coords_to_point(2,3))
        lv = ejesp.get_vertical_line(ejesp.coords_to_point(5, -1.5))

        #funcion por .plot
        graf = ejesp.plot(lambda x: np.sin(x), color=PINK, x_range=[-2*PI, 3 * PI])
        l2 = ejesp.get_vertical_lines_to_graph(graph=graf, x_range=[0, 9], num_lines=40)

        #etiqueta del grafo
        lbgraf=ejesp.get_graph_label(graph=graf,label=MathTex(r'f(x)=sin \ x'),x_val=7,direction=UR,buff=0.3,color=RED,dot=True)

        #areas
        area1=ejesp.get_area(graph=graf,x_range=[0,2*PI],color=(ORANGE,BLUE,WHITE),opacity=1)
        self.add(lbls,p1,l1,lh,lv,l2)
        self.add(area1,graf,lbgraf)

        #riemman rectangulos
        rimanrec=ejesp.get_riemann_rectangles(graph=graf,
                                              x_range=[-2*PI,0],
                                              dx=0.1,
                                              input_sample_type='center', #left o right
                                              stroke_width=2, #grosor de los recta
                                              stroke_color=WHITE, #color de los recta
                                              fill_opacity=1,
                                              color=(BLUE,RED_C,PURE_BLUE,PURE_GREEN),
                                              show_signed_area=True, #invierte colores in negativ values
                                              width_scale_factor=1.07)
        self.add(rimanrec)

        #antiderivada y der
        grafant=ejesp.plot_antiderivative_graph(graph=graf,y_intercept=-3.5,samples=10)
        grafder=ejesp.plot_derivative_graph(graph=graf,color=TEAL)

        #recta tangente

        #Decimal Number
        decimal=DecimalNumber(number=0,
                              num_decimal_places=4,
                              include_sign=True,
                              show_ellipsis=True, #puntos suspensivos
                              unit="mm",
                              digit_buff_per_font_unit=0.002, #espacio entre números 0,002
                              include_background_rectangle=True,
                              font_size=36, #tamaño de los números
                              stroke_width=5, #grosor de números
                              fill_opacity=0,
                              color=GREEN,
                              )
        decimal.add_updater(lambda x: x.next_to(p1,LEFT))
        decimal.add_updater(lambda x: x.set_value(p1.get_center()[1]))
        Plane = NumberPlane()
        #self.add(decimal,Plane)
        #self.play(p1.animate.shift(4*UP), rate_func=linear, run_time=5)


