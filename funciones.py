from manim import*

class fct(Scene):

    def construct(self):
        #x14 y8
        ejes=Axes(
            x_range=[0,10,1],
            y_range=[0,10,1],
            x_length=5,
            y_length=2.5,
            axis_config={"include_tip": True,
                         "include_numbers": True,
                         #'tip_shape':ArrowTriangleFilledTip,
                         'font_size':20,
                         'stroke_width':1
                         }
        ).add_coordinates()
        ejes.to_edge(DL)
        lbejes=ejes.get_axis_labels(x_label="x",y_label="f(x)")
        cur1=ejes.plot(lambda x: x,color=PINK)
        cur2 = ejes.plot(lambda x: np.sin(x+1),color=BLUE)
        cur3 = ejes.plot(lambda x: np.cos(x), color=ORANGE)
        cur4 = ejes.plot(lambda y: y**2,color=RED,x_range=[0,2.5])
        cur5 = ejes.plot(lambda x:x**0.5,x_range=[0,9],color=PURPLE)
        self.play(DrawBorderThenFill(ejes),DrawBorderThenFill(lbejes))
        self.wait(2)
        self.play(Write(cur1),Write(cur2),Write(cur3),Write(cur4),Write(cur5),run_time=10)
        self.wait(3)
        allfct=VGroup(ejes,lbejes,cur1,cur2,cur3,cur4,cur5)
        self.play(allfct.animate.shift(UP*4))
        self.wait()
        self.play(ejes.animate.shift(DOWN*4))
        self.wait()
        self.play(lbejes.animate.shift(DOWN * 4))
        self.wait()
        self.play(cur1.animate.shift(RIGHT * 7))
        self.wait()
        self.play(cur2.animate.shift(RIGHT * 7+DOWN*7))
        self.wait()
        self.play(cur3.animate.shift(ORIGIN))
        self.wait()
        self.play(cur4.animate.shift(DOWN * 4+RIGHT*5))
        self.wait()

class fct1(Scene):
    def construct(self):
        plano=NumberPlane(
            x_range=[-1,10],
            y_range=[-1,10],
            x_length=5,
            y_length=2.5,
        )
        plano.add_coordinates()
        plano.shift(UR)
        curv1=plano.plot(lambda x:x**2,x_range=[1,3.5],color=GREEN)
        acurv1=plano.get_area(graph=curv1,x_range=[1,3],color=(RED,YELLOW_C),opacity=1)
        texto=MathTex("f(x)=x^2").next_to(plano,UP,buff=0)
        self.play(Create(plano),run_time=4)
        self.play(Create(curv1))
        self.play(Create(texto))
        self.wait(3)
        self.play(FadeIn(acurv1),run_time=1)
        self.wait(3)




class fct2(MovingCameraScene):
    def construct(self):
       #self.camera.background_color = BLUE_A
        self.camera.frame.save_state()
        ejes=Axes(
            x_range=[-5,5,1],
            #x_length=,
            #y_length=,
            y_range=[-5,5,1],
            axis_config={"include_tip":True,"include_numbers":True}
        )
        ejes.move_to(DOWN*2+LEFT*2)
        etqx = ejes.get_axis_labels(x_label="x", y_label="f(x)")
        tit = Text("Área bajo una Curva").move_to(UP * 3.5)
        cur1=ejes.plot(lambda x:x**3 + 2*x**2 -3*x-2,x_range=[-2,4.5],color=PINK)
        acur1=ejes.get_area(graph=cur1,x_range=[-2,1],color=(YELLOW_A,ORANGE),opacity=1)
        cur1tx = MathTex("f(x)=x^3+2x^2-x-2").next_to(ejes, UP + LEFT, buff=0.2).set_color(PURPLE)
        r1cur1=ejes.get_riemann_rectangles(graph=cur1,x_range=[-4,2],dx=1)
        r2cur1 = ejes.get_riemann_rectangles(graph=cur1, x_range=[-4, 2], dx=0.8)
        r3cur1 = ejes.get_riemann_rectangles(graph=cur1, x_range=[-4, 2], dx=0.6)
        r4cur1 = ejes.get_riemann_rectangles(graph=cur1, x_range=[-4, 2], dx=0.4)
        r5cur1 = ejes.get_riemann_rectangles(graph=cur1, x_range=[-4, 2], dx=0.2)
        r6cur1 = ejes.get_riemann_rectangles(graph=cur1, x_range=[-4, 2], dx=0.1)
        r7cur1 = ejes.get_riemann_rectangles(graph=cur1, x_range=[-4, 2], dx=0.06)
        r8cur1 = ejes.get_riemann_rectangles(graph=cur1, x_range=[-4, 2], dx=0.01)
        int1=MathTex(r'\int_{-2}^{1} f(x) \quad dx').move_to(RIGHT*2).set_color_by_gradient(GOLD_E,MAROON_B)
        self.play(Write(tit))
        self.play(DrawBorderThenFill(ejes),DrawBorderThenFill(etqx),run_time=6)
        self.wait()
        self.play(Create(cur1),run_time=3)
        self.play(FadeIn(cur1tx))
        self.wait()
        self.play(FadeIn(acur1),FadeIn(int1),run_time=5)
        self.wait()
        self.play(self.camera.frame.animate.scale(1.5).move_to(etqx), Create(r1cur1), run_time=7)
        self.wait(2)
        self.play(ReplacementTransform(r1cur1,r2cur1))
        self.play(ReplacementTransform(r2cur1, r3cur1))
        self.play(ReplacementTransform(r3cur1, r4cur1))
        self.play(ReplacementTransform(r4cur1, r5cur1))
        self.play(ReplacementTransform(r5cur1, r6cur1))
        self.play(ReplacementTransform(r6cur1, r7cur1))
        self.play(ReplacementTransform(r7cur1, r8cur1))
        self.wait(2)



class fct3(Scene):
    def construct(self):
        mplano=Axes(
            x_range=[-1,7,0.5],
            y_range=[-1,7,1],
            axis_config={"include_tip": True, "include_numbers": True,"font_size":15}
        )
        etqs=mplano.get_axis_labels(x_label="x",y_label="f(x)")
        curv1=mplano.plot(lambda x:x**3+5*x**2-2,color=MAROON_B)
        cr1=mplano.coords_to_point(2,2)
        p1=Dot(cr1).set_color(YELLOW_C)
        lin1=mplano.get_horizontal_line(cr1,line_config={"dashed_ratio":0.2})
        lin2=mplano.get_vertical_lines_to_graph(graph=curv1,x_range=[0,2],num_lines=10,color=BLUE_D)
        self.play(Create(mplano,run_time=3),Create(etqs,run_time=2))
        self.wait(2)
        self.play(Create(curv1,run_time=4),Create(p1))
        self.play(Create(lin1),Create(lin2),run_time=5)
        self.wait(2)


from manim import *

class fct4(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=WHITE, x_range=[0, 3 * PI])

        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        self.add(ax, graph, dot_1, dot_2)

        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
        self.play(self.camera.frame.animate.move_to(dot_2))
        self.play(Restore(self.camera.frame))
        self.wait()

class fctrig(Scene):
    def construct(self):
        plano = NumberPlane(x_range=(-3, 3), y_range=(-4, 4), axis_config={'stroke_width': 0})
        plano.move_to(4*LEFT)
        ax=Axes(
            x_range=(-1.5,1.5),
            y_range=(-1.5,1.5),
            x_length=6,
            y_length=6,
            axis_config={
            'tip_shape':StealthTip,'tip_height':0.25,'include_numbers':True,'font_size':26}
        )
        ax.move_to(plano)
        dt1=plano.coords_to_point(2,2)
        dt2 = plano.coords_to_point(-2, 2)
        dt3 = plano.coords_to_point(-2, -2)
        dt4 = plano.coords_to_point(2, -2)
        p1=Dot(dt1)
        l1=plano.get_vertical_line(dt1, line_config={"dashed_ratio": 0.85})
        l1.set_color(RED)
        L1=Line(start=plano.get_center(),end=dt1)
        L2 = Line(start=plano.get_center(), end=dt2)
        L3 = Line(start=plano.get_center(), end=dt3)
        L4 = Line(start=plano.get_center(), end=dt4)
        c1=Circle(radius=2*(2**(1/2)),color=GOLD_C).move_to(plano.get_center())
        self.add(plano,ax,l1,p1)
        self.play(Write(c1))
        self.play(MoveAlongPath(L1,c1))
        de=self.play(ReplacementTransform(L1,L2),run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(L2,L3), run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(L3,L4), run_time=3)

class fctsmov(Scene):
    def construct(self):
        self.camera.background_color = BLUE_A
        ejes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": True,
                         "include_numbers": True,
                         'tip_shape':StealthTip,
                         'tip_width': 0.2,
                         'tip_height': 0.3,
                         'font_size': 24,
                         'stroke_width': 1
                         }
        ).add_coordinates()
        ejes.set_color(BLACK)

        lbejes = ejes.get_axis_labels(x_label="x", y_label="f(x)").set_color(BLACK)
        cur1 = ejes.plot(lambda x: x, color=PINK,x_range=[-4,4])
        t1=MathTex('f(x)=mx+b').set_color(PINK)
        t1.move_to(ejes,UL).shift(LEFT)
        G1=VGroup(ejes,lbejes,cur1,t1).move_to(LEFT*3)

        k = ValueTracker(-3)
        cur1.add_updater(lambda x: x.set_x(k.get_value()))
        self.add(ejes,lbejes,cur1,t1)
        self.wait(3)
        self.play(k.animate.set_value(-6), rate_func=smooth, run_time=3.5)
        self.wait(2)