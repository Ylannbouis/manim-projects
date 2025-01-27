from manim import *

class DoFourier(Scene):
    dt = 0.001
    mass_num_of_vects = 30 # *not exactly how many there are*
    object = SVGMobject("./svg-path.svg").scale(3)

    def curve_function(self, t):
        # as t ranges from 0 to 1

        scale_factor = 3
        object = self.object

        # return [scale_factor*4.3*(t-0.5), scale_factor*1.2*np.sin(2 * np.pi * t),0]

        # maybe define this here down below as a parametric function
        return object[0].point_from_proportion(t)
    def parametric_curve_function(self):
        # parametric for the one above
        return ParametricFunction(
            self.curve_function,
            t_range = [0,1],
            fill_opacity=0
        ).set_color(BLUE)
    def compute_integral(self, n):
        dt = self.dt
        result = [0, 0]
        for t in np.arange(0, 1, dt):
            result_func = self.curve_function(t)
            result[0] += (result_func[0] * np.cos(-2 * n * np.pi * t) - result_func[1] * np.sin(-2 * n * np.pi * t)) * dt
            result[1] += (result_func[0]* np.sin(-2 * n * np.pi * t) + result_func[1] * np.cos(-2 * n * np.pi * t)) * dt
        return result
    def package_coords_into_list(self):
        vects = self.mass_num_of_vects
        vect_coords = []
        n = 0
        for i in range(2 * vects + 1):
            if n == 0:
                n = 0
                result = self.compute_integral(n)
                vect_coords.append(result[0])
                vect_coords.append(result[1])
                n += 1
            else:
                if n > 0:
                    result = self.compute_integral(n)
                    vect_coords.append(result[0])
                    vect_coords.append(result[1])
                    n = -1 * n
                elif n < 0:
                    result = self.compute_integral(n)
                    vect_coords.append(result[0])
                    vect_coords.append(result[1])
                    n = (-1 * n) + 1
        n = 0
        return vect_coords

    def complex_multiply(self, x1, y1, x2, y2):
        return [(x1 * x2) - (y1 * y2), (x1 * y2) + (y1 * x2)]

    def construct(self):
        # vars
        dt = self.dt
        vects = self.mass_num_of_vects # check note about this
        vect_coords = self.package_coords_into_list() # something goes wrong here (probably computation time.
        t = ValueTracker(0)
        def get_arrows():
            result = [0,0]
            results = []
            results.append(result)
            arrows = []
            coord = [0,0, 0]
            vect_num=0
            n = 0
            colors = [RED_A, RED_C, RED_B]
            for i in range(2 * vects + 1):
                vect_num += 1
                result = self.complex_multiply(vect_coords[2*vect_num-2], vect_coords[2*vect_num-1], np.cos(2*n*np.pi*t.get_value()), np.sin(2*n*np.pi*t.get_value()))
                previous_coord = coord
                coord = [previous_coord[0] + result[0], previous_coord[1] + result[1], 0]
                results.append(result)
                new_arrow = Line(start=[previous_coord], end=[coord], color=colors[i%3])
                arrows.append(new_arrow)
                if n == 0:
                    n += 1
                elif n > 0:
                    n = -1 * n
                elif n < 0:
                    n = -1 * n + 1

            return VGroup(*arrows)
        all_arrows = always_redraw(get_arrows)
        # self.add(self.parametric_curve_function())
        self.play(Write(self.object))
        # self.wait(1)
        self.play(Create(all_arrows))
        # self.wait(1)
        self.play(t.animate.set_value(3), run_time=30, rate_func=linear)
class Test(Scene):
    def construct(self):
        object = SVGMobject("./svg-path.svg").scale(3)
        self.play(Write(object))
        for point in np.arange(0,1, 0.01):
            self.add(Dot(object[0].point_from_proportion(point)))
            self.wait(0.5)
        self.wait(1)