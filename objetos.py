from manim import *
config.frame_width = 9
config.frame_height = 20

class jeto(Scene):
    def construct(self):
        dot=Dot(DOWN*3+LEFT*3)
        circu=Circle().shift(UP*3)
        cuadra=Square().shift(DOWN*3)
        tria=Triangle().shift(LEFT*3)
        self.play(FadeIn(circu,shift=DOWN),FadeIn(cuadra,shift=LEFT),FadeIn(tria,target_position=dot),run_time=6)
        self.remove(circu,cuadra,tria)
        self.wait(2)
        self.play(GrowFromPoint(circu,ORIGIN),run_time=4)
        self.play(GrowFromCenter(cuadra),point_color=RED_A)
        self.wait()
        self.play(GrowFromEdge(tria, DOWN))

class gigi(Scene):
    def construct(self):
        text0=Text("Gissela Caizatoa").move_to(UP*3)
        text1=Text("Gissela Caizatoa").move_to(UP*2)
        text2 = Text("Gissela Caizatoa").move_to(UP)
        text3 = Text("Gissela Caizatoa").move_to(DOWN)
        self.play(ApplyWave(text0,direction=UP,time_width=1.5,amplitude=0.7))
        self.wait(2)
        self.play(ApplyWave(text1, direction=UP, time_width=0.5, amplitude=0.2))
        self.wait(2)
        self.play(ApplyWave(text2, direction=DOWN, time_width=2, amplitude=0.1))
        self.wait(2)
        self.play(ApplyWave(text3, direction=LEFT, time_width=0.2, amplitude=2))
        self.play(Create(Square(fill_color=PINK,fill_opacity=0.7)))

class objetos(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        rpol1=RegularPolygram(radius=3,num_vertices=5,fill_opacity=1,color=GREY,stroke_color=BLACK)
        star1=Star(n=5,outer_radius=2,inner_radius=1,density=1,fill_opacity=1,color=GREY,stroke_color=BLACK)
        #star1.round_corners(radius=1)
        ell1=Ellipse()
        s1 = Square().scale(2.5)
        s2 = Triangle().shift(1.3*DOWN + 1.3*RIGHT).scale(0.65)
        s3 = Square().shift(1.3*UP + 1.3*RIGHT).scale(0.5)
        s4 = RegularPolygon(5).shift(1.3*DOWN + 1.3*LEFT).scale(0.65)
        s5 = Circle().shift(1.3*UP + 1.3*LEFT).scale(0.6)


        Ax=NumberPlane()

        c1 = Cutout(s1, s2, s5, fill_opacity=1, color=GREY, stroke_color=BLACK)
        c2 = Cutout(s1, s3, s4, fill_opacity=1, color=GREY, stroke_color=BLACK)
        self.add(c2)

class taptana0(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        Plano=NumberPlane(
            x_range=[-10, 10],
            y_range=[-15, 15],
            axis_config={'stroke_width': 5,"stroke_color": GREY,'include_tip':False,'include_ticks':False},background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2},faded_line_ratio=5)
        for i in range(1,10):
            c1=Circle(radius=0.3,color=YELLOW_E).shift((6.5-(i*0.9))*DOWN+2*RIGHT)
            c2 = Circle(radius=0.3,color=PURE_BLUE).shift((6.5-(i*0.9))*DOWN+0*RIGHT)
            c3= Circle(radius=0.3,color=PURE_RED).shift((6.5-(i*0.9))*DOWN+2*LEFT)
            c4 = Circle(radius=0.3,color=PURE_GREEN).shift((6.5-(i*0.9))*DOWN+3*LEFT)
            self.add(c1,c2,c3)
        cuadrado1=Square(side_length=0.8,color=YELLOW_E).shift(2.5*UP+2*RIGHT)
        t1=Text('U',color=YELLOW_E).shift(2.5*UP+2*RIGHT).scale(0.6)
        cuadrado2 = Square(side_length=0.8, color=PURE_BLUE).shift(2.5 * UP + 0 * RIGHT)
        t2 = Text('D', color=PURE_BLUE).shift(2.5 * UP + 0 * RIGHT).scale(0.6)
        cuadrado3 = Square(side_length=0.8, color=PURE_RED).shift(2.5 * UP + 2 * LEFT)
        t3 = Text('C', color=PURE_RED).shift(2.5* UP + 2 * LEFT).scale(0.6)
        cuadrado4 = Square(side_length=0.8, color=PURE_GREEN).shift(2.5 * UP + 3 * LEFT)
        t4 = Text('UM', color=PURE_GREEN).shift(2.5 * UP + 3 * LEFT).scale(0.6)
        fle = Arc(radius=4,start_angle=0,angle=PI).set_color(BLACK).shift(2*UP)
        l1=Line(start=4*LEFT+2*UP,end=4*LEFT+6.2*DOWN,color=BLACK)
        l2 = Line(start=4 * RIGHT + 2 * UP, end=4 * RIGHT + 6.2 * DOWN, color=BLACK)
        l3=Line(start=6.2*DOWN+4 * RIGHT,end=6.2*DOWN+4 * LEFT,color=BLACK)
        cr1=Circle(radius=1,color=BLACK).shift(4.5*UP)
        self.add(cuadrado1,t1,cuadrado2,t2,cuadrado3,t3,fle,l1,l2,l3,cr1)

class taptana(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        Plano=NumberPlane(
            x_range=[-10, 10],
            y_range=[-15, 15],
            axis_config={'stroke_width': 5,"stroke_color": GREY,'include_tip':False,'include_ticks':False},background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2},faded_line_ratio=5)
        for i in range(1,10):
            c1=Circle(radius=0.3,color=YELLOW_E).shift((6.5-(i*0.9))*DOWN+3*RIGHT)
            c2 = Circle(radius=0.3,color=PURE_BLUE).shift((6.5-(i*0.9))*DOWN+1*RIGHT)
            c3= Circle(radius=0.3,color=PURE_RED).shift((6.5-(i*0.9))*DOWN+1*LEFT)
            c4 = Circle(radius=0.3,color=PURE_GREEN).shift((6.5-(i*0.9))*DOWN+3*LEFT)
            self.add(c1,c2,c3,c4)
        cuadrado1=Square(side_length=0.8,color=YELLOW_E).shift(2.5*UP+3*RIGHT)
        t1=Text('U',color=YELLOW_E).shift(2.5*UP+3*RIGHT).scale(0.6)
        cuadrado2 = Square(side_length=0.8, color=PURE_BLUE).shift(2.5 * UP + 1 * RIGHT)
        t2 = Text('D', color=PURE_BLUE).shift(2.5 * UP + 1 * RIGHT).scale(0.6)
        cuadrado3 = Square(side_length=0.8, color=PURE_RED).shift(2.5 * UP + 1 * LEFT)
        t3 = Text('C', color=PURE_RED).shift(2.5* UP + 1 * LEFT).scale(0.6)
        cuadrado4 = Square(side_length=0.8, color=PURE_GREEN).shift(2.5 * UP + 3 * LEFT)
        t4 = Text('UM', color=PURE_GREEN).shift(2.5 * UP + 3 * LEFT).scale(0.6)
        fle = Arc(radius=4,start_angle=0,angle=PI).set_color(BLACK).shift(2*UP)
        l1=Line(start=4*LEFT+2*UP,end=4*LEFT+6.2*DOWN,color=BLACK)
        l2 = Line(start=4 * RIGHT + 2 * UP, end=4 * RIGHT + 6.2 * DOWN, color=BLACK)
        l3=Line(start=6.2*DOWN+4 * RIGHT,end=6.2*DOWN+4 * LEFT,color=BLACK)
        cr1=Circle(radius=1,color=BLACK).shift(4.5*UP)
        self.add(cuadrado1,t1,cuadrado2,t2,cuadrado3,t3,cuadrado4,t4,fle,l1,l2,l3,cr1)

class taptana1(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        Plano=NumberPlane(
            x_range=[-10, 10],
            y_range=[-15, 15],
            axis_config={'stroke_width': 5,"stroke_color": GREY,'include_tip':False,'include_ticks':False},background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2},faded_line_ratio=5)
        for i in range(1,10):
            c1=Circle(radius=0.5,color=YELLOW_E).shift((6.5-(i*1.2))*DOWN+2.5*RIGHT)
            c2 = Circle(radius=0.5,color=PURE_BLUE).shift((6.5-(i*1.2))*DOWN)
            c3= Circle(radius=0.5,color=PURE_RED).shift((6.5-(i*1.2))*DOWN+2.5*LEFT)
            c4 = Circle(radius=0.5,color=PURE_GREEN).shift((6.5-(i*1.2))*DOWN+3*LEFT)
            self.add(c1,c2,c3)
        cuadrado1=Square(side_length=1.2,color=YELLOW_E).shift(5.5*UP+2.5*RIGHT)
        t1=Text('U',color=YELLOW_E).shift(5.5*UP+2.5*RIGHT)
        cuadrado2 = Square(side_length=1.2, color=PURE_BLUE).shift(5.5 * UP)
        t2 = Text('D', color=PURE_BLUE).shift(5.5 * UP )
        cuadrado3 = Square(side_length=1.2, color=PURE_RED).shift(5.5 * UP + 2.5 * LEFT)
        t3 = Text('C', color=PURE_RED).shift(5.5 * UP + 2.5 * LEFT)
        cuadrado4 = Square(side_length=1.2, color=PURE_GREEN).shift(5.5 * UP + 3 * LEFT)
        t4 = Text('UM', color=PURE_GREEN).shift(5.5 * UP + 3 * LEFT)
        self.add(cuadrado1,t1,cuadrado2,t2,cuadrado3,t3)

class taptana2(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        Plano=NumberPlane(
            x_range=[-10, 10],
            y_range=[-15, 15],
            axis_config={'stroke_width': 5,"stroke_color": GREY,'include_tip':False,'include_ticks':False},background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2},faded_line_ratio=5)
        for i in range(1,10):
            c1=Circle(radius=0.5,color=YELLOW_E).shift((6.5-(i*1.2))*DOWN+0.8*LEFT)
            c2 = Circle(radius=0.5,color=PURE_BLUE).shift((6.5-(i*1.2))*DOWN+2.3*LEFT)
            c3= Circle(radius=0.5,color=PURE_RED).shift((6.5-(i*1.2))*DOWN+3.8*LEFT)
            c4 = Circle(radius=0.5,color=PURE_GREEN).shift((6.5-(i*1.2))*DOWN+0.5*RIGHT)
            c5 = Circle(radius=0.5, color=PURPLE_A).shift((6.5 - (i * 1.2)) * DOWN + 0.8 * RIGHT)
            c6 = Circle(radius=0.5, color=LIGHT_BROWN).shift((6.5 - (i * 1.2)) * DOWN + 2.3 * RIGHT)
            c7 = Circle(radius=0.5, color=PURE_GREEN).shift((6.5 - (i * 1.2)) * DOWN + 3.8 * RIGHT)
            self.add(c1,c2,c3,c5,c6,c7)
        cuadrado1=Square(side_length=1,color=YELLOW_E).shift(5.5*UP+0.8*LEFT)
        t1=Text('U',color=YELLOW_E).shift(5.5*UP+0.8*LEFT)
        cuadrado2 = Square(side_length=1, color=PURE_BLUE).shift(5.5 * UP+2.3*LEFT)
        t2 = Text('D', color=PURE_BLUE).shift(5.5 * UP +2.3*LEFT)
        cuadrado3 = Square(side_length=1, color=PURE_RED).shift(5.5 * UP + 3.8 * LEFT)
        t3 = Text('C', color=PURE_RED).shift(5.5 * UP + 3.8 * LEFT)
        cuadrado4 = Square(side_length=1, color=PURE_GREEN).shift(5.5 * UP +0.8*RIGHT)
        t4 = Text('UM', color=PURE_GREEN).shift(5.5 * UP +0.8*RIGHT)
        cuadrado5 = Square(side_length=1, color=PURPLE_A).shift(5.5 * UP + 0.8*RIGHT)
        t5 = Text('d', color=PURPLE_A).shift(5.5 * UP + 0.8*RIGHT)
        cuadrado6 = Square(side_length=1, color=LIGHT_BROWN).shift(5.5 * UP + 2.3 * RIGHT)
        t6 = Text('c', color=LIGHT_BROWN).shift(5.5 * UP + 2.3 * RIGHT)
        cuadrado7 = Square(side_length=1, color=PURE_GREEN).shift(5.5 * UP + 3.8 * RIGHT)
        t7 = Text('m', color=PURE_GREEN).shift(5.5 * UP + 3.8 * RIGHT)
        r1=Rectangle(height=0.5,width=1.5,color=BLACK).shift(6.2*DOWN)
        T1=Text(',',color=BLACK).shift(6.2*DOWN)
        l1=Line(start=6*UP,end=5.8*DOWN,color=BLACK,stroke_width=6)
        self.add(cuadrado1,t1,cuadrado2,t2,cuadrado3,t3,cuadrado5,t5,cuadrado6,t6,cuadrado7,t7,r1,l1,T1)