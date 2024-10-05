from manim import*

class Vtracker(Scene):
    def construct(self):
        #con Axes
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

        # Value Tracker forma 1
        k = ValueTracker(0)  # pongo solo el valor númerico que se va a actualizar
        p2 = Dot(ejesp.coords_to_point(0, 3), color=MAROON_E)
        p2.add_updater(lambda x: x.set_x(
            k.get_value()))  # necesito ponerle un updater a un elemento del Mobject, en este caso es la coordenada en x
        # self.add(p2,k) #en esta forma tengo que añadir al valuetracker
        k.add_updater(lambda mobject, dt: mobject.increment_value(dt))  # empieza a darle valores en función del tiempo
        # self.wait(6)

        # Value Tracker forma 2
        p2.add_updater(lambda q: q.set_x(k.get_value()))
        self.add(p2)
        self.play(k.animate.set_value(2), rate_func=linear, run_time=4)