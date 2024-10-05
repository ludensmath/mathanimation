from manim import *


class planogrid(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        plano1 = NumberPlane(
            x_range=[0, 11],
            y_range=[0, 11],
            y_length=7,
            x_length=7,
            background_line_style={"stroke_width": 3, "stroke_color":PURE_BLUE, "stroke_opacity": 2},
            axis_config={
                'include_numbers': True,
                'length': 10,
                "include_ticks": True,
                "exclude_origin_tick": False,
            },
            y_axis_config={"label_direction": LEFT, "line_to_number_buff": MED_SMALL_BUFF, "color": BLACK},
            x_axis_config={"label_direction": DOWN, "line_to_number_buff": MED_SMALL_BUFF, "color": BLACK}
            # faded_line_style='DashedLine'
        )
        # lblx=plano1.get_axis_labels(x_label="x", y_label="y").set_color(BLACK)
        tix = plano1.get_y_axis_label(label="y", edge=UP, buff=0.3).set_color(BLACK)
        tiy = plano1.get_x_axis_label(label="x", edge=RIGHT, direction=DOWN + RIGHT, buff=0.1).set_color(BLACK)
        r = plano1.get_x_axis()
        r.numbers.set_color(BLACK)
        s = plano1.get_y_axis()
        s.numbers.set_color(BLACK)
        # lblx.to_edge(plano1,buff=SMALL_BUFF).scale(0.8)

        self.add(tix, tiy,plano1,r,s)


class numberplano(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        # Plano
        planop = NumberPlane(
            x_range=[-100, 100],
            y_range=[-1, 3, 0.05],
            y_length=8,
            x_length=16,
            background_line_style={'stroke_color': LIGHT_GRAY, "stroke_opacity": 0},

            axis_config={
                'include_numbers': False,
                'length': 7,
                "include_ticks": False,
            }

        )
        # tracker
        k = ValueTracker(0.2)

        # funcion
        def func(x):
            return 1 / x

        # func0=planop.plot(function=lambda x:1/x,x_range=[0.0001,10,0.001])
        # func1 = planop.plot(function=lambda x: 1 / x, x_range=[-10, -0.0001,0.001])
        fct = planop.plot(function=func, x_range=[0.05, 100, 0.01])
        # punto
        p0 = [planop.coords_to_point(k.get_value(), func(k.get_value()))]
        D1 = Dot(point=p0, color=BLUE)
        D1.add_updater(lambda d: d.move_to(planop.coords_to_point(k.get_value(), func(k.get_value()))))
        # x_space = np.linspace(*planop.x_range[:2], 200)
        # minimum_index = func(x_space).argmin()
        self.add(planop, fct, D1)
        self.play(self.camera.frame.animate.scale(0.5).move_to(D1))

        def update_curve(mob):
            mob.move_to(D1.get_center())

        self.camera.frame.add_updater(update_curve)
        # self.play(k.animate.set_value(x_space[minimum_index]),rate_func=linear, run_time=4)

        self.play(k.animate.set_value(100),
                  # self.camera.frame.animate.scale(0.5).move_to(planop.coords_to_point(k.get_value(), func(k.get_value()))),run_time=5
                  MoveAlongPath(D1, fct, rate_func=linear)
                  , run_time=5
                  )
