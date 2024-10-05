from manim import *
class Mov1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        #logos
        logo=ImageMobject("assets/images/logopaes.png").shift(6.2*RIGHT+3.2*DOWN).set_opacity(0.3).scale(.5)
        logfilo=ImageMobject("assets/images/logofilo.jpg").shift(6.6*RIGHT+3.2*UP).set_opacity(0.3).scale(.5)
        logovcs=ImageMobject("assets/images/logovc.png").shift(4.1*RIGHT+3.14*UP).set_opacity(0.3).scale(0.8)
        logouce=ImageMobject("assets/images/logouce.jpg").shift(5.35*RIGHT+3.2*UP).set_opacity(0.3).scale(0.17)

        Ax=NumberPlane(
            x_range=[-7, 7],
            y_range=[-7, 7],
            axis_config={'stroke_width': 5,"stroke_color": GREY,'include_tip':False,'include_ticks':False},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 2}
        )
        #figuras
        fl1=Arrow(np.array([-3, -3, 0]), np.array([3, 3, 0]),
                  buff=0.1,
                  max_tip_length_to_length_ratio=4,
                  tip_length=2.8,
                  stroke_width=150,
                  max_stroke_width_to_length_ratio=50,
                  stroke_color=BLACK
                  )
        tri=Polygon([-2, -2, 0], [2, -2, 0], [0, 2, 0]).set_color(BLACK)
        position_list = [
            [-2, -1.5, 0],
            [2, -1.5, 0],
            [2, 2.5, 0],
            [0, 1, 0],
            [-2, 2.5, 0]
        ]
        pol1 = Polygon(*position_list,stroke_color=BLACK,stroke_width=3,fill_color=BLACK).set_opacity(1)

        #flechas sentidos horarios
        fle = CurvedArrow(1* LEFT, 1 * RIGHT, radius=-1,stroke_width=4).set_color(BLACK).shift(2*UP+5*RIGHT)
        #sfle=MathTex('+').shift(2*UP+5*RIGHT).scale(1.3).set_color(BLACK)
        fle2 = CurvedArrow(1 * RIGHT, 1 * LEFT, radius=1, stroke_width=4).set_color(BLACK).shift(1 * DOWN)
        #sfle2 = MathTex('-').shift(1*DOWN).scale(1.3).set_color(BLACK)


        s1 = Square().scale(2.5)
        s2 = Triangle().shift(1.3 * DOWN + 1.3 * RIGHT).scale(0.65)
        s3 = Square().shift(1.3 * UP + 1.3 * RIGHT).scale(0.5)
        s4 = RegularPolygon(5).shift(1.3 * DOWN + 1.3 * LEFT).scale(0.65)
        s5 = Circle().shift(1.3 * UP + 1.3 * LEFT).scale(0.6)
        c1 = Cutout(s1, s2, s5, fill_opacity=1, color=GREY, stroke_color=BLACK).scale(0.75)

        rpol1=RegularPolygram(num_vertices=6,stroke_width=3,fill_opacity=1,color=GREY,stroke_color=BLACK,stroke_opacity=1).move_to(Ax.get_center())
        star1= Star(n=5,stroke_width=3,fill_opacity=1,stroke_color=BLACK,stroke_opacity=1,color=GREY).move_to(Ax.get_center())

        p1=Dot(rpol1.get_boundary_point(direction=UP),color=RED)
        arc1=ArcBetweenPoints(start=UP,end=RIGHT,angle=-90*DEGREES,color=BLUE)
        l1=VMobject()
        #l1.add_updater(lambda x:x.become(ArcBetweenPoints(start=[1,1],end=,angle=-90*DEGREES).set_color(PINK)))
        self.add(Ax,rpol1,)
        self.play(
            MoveAlongPath(p1,arc1),
            Rotate(rpol1, angle=-90 * DEGREES),
            Create(l1),
            run_time=3,
            rate_fun=linear
        )

        #self.play(Rotate(rpol1,angle=-90*DEGREES),run_time=3)
        #self.play(Rotate(star1, angle=-90 * DEGREES), run_time=3)

        """tri.set_opacity(1)
        tx=Text('Rotación de 90° sentido horario').shift(UP*3.4+1*LEFT).set_color(BLACK)
        tx1 = Paragraph('Ahora imagínate', '¿Cómo rotarían las figuras', 'en sentido antihorario?',alignment="center").shift(UP * 2.5).set_color(BLACK)
        self.play(FadeIn(Ax,logo,logfilo,logovcs,logouce))
        self.play(Write(tx),FadeIn(fle))
        lista=[tri,pol1,fl1,c1]
        for i in lista:
            self.play(FadeIn(i))
            self.play(Indicate(fle),scale_factor=1.3,color=RED)
            self.play(Rotate(i,angle=-90*DEGREES, rate_func=linear),run_time=3)
            self.wait()
            self.play(FadeOut(i))
            self.wait(1.2)
        self.play(FadeOut(tx,fle))
        self.play(Write(tx1),FadeIn(fle2))
        self.play(Circumscribe(tx1,Rectangle,color=PURE_GREEN,run_time=2))
        self.wait()
        self.play(Indicate(fle2, scale_factor=1.3, color=PURE_GREEN))
        self.wait(2)"""






class fig10(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        #ejes
        Ax = NumberPlane(
            x_range=[-2.5, 2.5],
            y_range=[-1.5,1.5],
            axis_config={'stroke_width': 5, "stroke_color": GREY, 'include_tip': False, 'include_ticks': False},
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 0
            }
        )

        logo=ImageMobject("assets/images/logopaes.png").shift(6.2*LEFT+3.2*DOWN).set_opacity(0.4).scale(.5)

        f1=ImageMobject("assets/images/f1.png").shift(UP)
        tx1 = Paragraph('Identifique la imagen que corresponde', 'a la rotación antihoraria de 270° de la figura mostrada',
                        alignment="left").shift(UP * 3).set_color(BLACK).scale(0.8)
        Ax.save_state()
        Ax.move_to(f1.get_center())
        self.add(Ax)
        a=[1,2,3,4,5]
        etiq = {'A)':1,'B)':2,'C)':3, 'D)':4}
        for i,k in zip(a,etiq):
            i=f1.copy().shift(3*DOWN+(9-3.5*i)*LEFT).rotate((-90*(i+1)*DEGREES))
            self.add(i)
            l1 = Tex(k).set_color(BLACK).scale(0.8).next_to(i, direction=UP, buff=0.1)
            self.add(l1)
        self.add(tx1,f1)
        self.wait(3)
        f1.save_state()
        self.play(Rotate(f1, 270 * DEGREES), run_time=4, rate_func=linear)
        self.wait(2)
        f1.restore()
        self.wait(2)
        self.play(Rotate(f1,-90*DEGREES),run_time=3,rate_func=linear)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class mcua(Scene):
    def construct(self):
        c1=Circle(radius=2,stroke_color=BLACK)
        s1=Sector(outer_radius=0,inner_radius=2,angle=(1/7 *360)*DEGREES,start_angle=0*DEGREES,color=PURE_RED,stroke_color=WHITE,stroke_width=1)
        s2=Sector(outer_radius=0, inner_radius=2, angle=(1/7 *360) * DEGREES, start_angle=(1/7 *360) * DEGREES, color=ORANGE,stroke_color=WHITE,stroke_width=1)
        s3=Sector(outer_radius=0, inner_radius=2, angle=(1/7 *360) * DEGREES, start_angle=(2/7 *360) * DEGREES, color=YELLOW_C,stroke_color=WHITE,stroke_width=1)
        s4=Sector(outer_radius=0, inner_radius=2, angle=(1/7 *360) * DEGREES, start_angle=(3/7 *360) * DEGREES, color=PURE_GREEN,stroke_color=WHITE,stroke_width=1)
        s5 = Sector(outer_radius=0, inner_radius=2, angle=(1/7 *360) * DEGREES, start_angle=(4/7 *360) * DEGREES, color=BLUE,stroke_color=WHITE, stroke_width=1)
        s6=Sector(outer_radius=0, inner_radius=2, angle=(1/7*360) * DEGREES, start_angle=(5/7 *360) * DEGREES, color=PURE_BLUE,stroke_color=WHITE,stroke_width=1)
        s7=Sector(outer_radius=0, inner_radius=2, angle=(1/7*360) * DEGREES, start_angle=(6/7 *360) * DEGREES, color=PINK,stroke_color=WHITE,stroke_width=1)
        a1=Group(s1,s2,s3,s4,s5,s6,s7)
        fps=60
        dt=1/fps
        self.add(a1)
        for i in range(fps*2):
            a1.rotate(dt*80000*DEGREES)
            self.wait(dt)

