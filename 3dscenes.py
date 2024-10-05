from manim import *
class ejes3d(ThreeDScene):
    def construct(self):
        plano=ThreeDAxes()
        labl = plano.get_axis_labels(Tex("x"),Tex("y"),Tex("z"))
        p1=Dot3D(point=[1,1,1])
        arr1=Arrow3D(start=np.array([0,0,0]),end=np.array([-2,-2,2]),resolution=10,color=BLUE_E)
        arr2 = Arrow3D(start=np.array([0, 0, 0]), end=np.array([2, 2, -2]),resolution=10,color=ORANGE)
        cub1=Cube(side_length=1,fill_opacity=0.15,fill_color=TEAL,stroke_width=2,stroke_color=BLUE)

        #self.add_fixed_in_frame_mobjects(labl)
        self.set_camera_orientation(phi=45*DEGREES, theta=30*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.play(FadeIn(plano,labl),run_time=4)
        self.play(FadeIn(p1))
        self.wait()
        self.play(FadeIn(arr1,arr2),run_time=3)
        for i in range(0,8):
            cub2 = cub1.copy().move_to(np.array([0, 0,(i/2)]))
            cub3 = cub1.copy().move_to(np.array([0, 0, -(i / 2)]))
            cub4 = cub1.copy().move_to(np.array([-(i / 2), 0, 0]))
            cub5 = cub1.copy().move_to(np.array([(i / 2), 0, 0]))
            cub6 = cub1.copy().move_to(np.array([0, -(i / 2), 0]))
            cub7 = cub1.copy().move_to(np.array([0, (i / 2), 0]))
            self.play(FadeIn(cub2,cub3,cub4,cub5,cub7,cub6), run_time=3)
        self.stop_ambient_camera_rotation()
        self.set_camera_orientation(phi=0 * DEGREES, theta=0* DEGREES)
        self.wait(3)


