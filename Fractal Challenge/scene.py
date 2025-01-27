from manim import *
import random
from math import *

class Questions(Scene):

    def construct(self):
        num_1 = MathTex(r"\text{1. }", r"\text{Find the fixed points of }", "f(z) = z^2 + c", font_size=15).scale(3)
        num_1.set_color_by_tex("f(z)",YELLOW)
        num_2 = MathTex(r"\text{2. }", r"\text{Determine when at least one fixed point is attracting}", font_size=15).scale(3)
        num_3 = MathTex(r"\text{3. }", r"\text{Show that the set of values of c satisfying this form a cardioid.}", font_size=15).scale(3)
        problems = VGroup(num_1, num_2, num_3).arrange(DOWN, buff=2)
        problems.move_to(ORIGIN)
        rect = SurroundingRectangle(num_3).set_stroke(color=BLUE)
        screen_rect = ScreenRectangle(fill_color=BLACK, fill_opacity=0.9).scale(5).set_stroke(color=BLACK)
        self.play(Write(num_1[0]))
        self.wait(0.5)
        self.play(Write(num_1[1]))
        self.play(Write(num_1[2]))
        self.wait(2)
        self.play(Write(num_2[0]))
        self.wait(0.5)
        self.play(Write(num_2[1]))
        self.wait(2)
        self.play(Write(num_3[0]))
        self.wait(0.5)
        self.play(Write(num_3[1]))
        self.wait(1)
        self.play(Create(rect), run_time=1.5)
        self.wait(3)
        self.play(FadeIn(screen_rect), num_1.animate.scale(1.3).move_to([0,0,-1]))
        self.wait(1)

class Problem_1(Scene):
    CONFIG = {
        "axes_config": {
            "x_range": [-5, 5, 1],
            "y_range": [-5, 5, 1],
            "x_length": 8,
            "y_length": 8,
            "axis_config": {
                "include_ticks": False,
            },
            "tips": False
        }
    }
    def construct(self):
        s = Axes(**self.CONFIG["axes_config"])
        point = Dot([-2, 3, 0], color=BLUE)
        arrow = Arrow(start=point.get_center(), end=point.get_center(), path_arc = 2 * PI)
        self.play(Create(s))
        self.play(Create(point))
        self.play(Create(arrow)) #arrow that should point 360 degrees towards itself.

class Vect:

    def __init__(self, coords):
        self.coords = coords
        self.dimension = len(coords)
        self.manimcoords = [self.coords[0], self.coords[1], 0]

    def get_magnitude(self):
        result = 0
        for component in self.coords:
            result += component ** 2
        return sqrt(result)

    def scale(self, scalar):
        new_coords = self.coords.copy()
        for i, component in enumerate(self.coords):
            new_coords[i] = component * scalar
        return Vect(new_coords)

    def get_arrow(self):
        return Arrow(start=[0,0,0], end=self.coords)


    def add(self, vect2):
        return Vect([self.coords[0] + vect2.coords[0], self.coords[1] + vect2.coords[1]])

    def subtract(self, vect2):
        return self.add(vect2.scale(-1))

class Body:

    def __init__(self, position, velocity, mass, color, sf):
        self.position = position # Vector
        self.velocity = velocity # Vector
        self.mass = mass
        self.color = color
        self.rel_pos = self.position.scale(sf) # Vector
        self.rel_vel = self.velocity.scale(sf) # Vector
        self.body = Circle().set_color(self.color).move_to(self.rel_pos.manimcoords).scale((1/40) * self.mass * sf)
        self.vel_arrow = Arrow(start=self.body.get_center(), end=[
                self.body.get_x() + self.rel_vel.coords[0],
                self.body.get_y() + self.rel_vel.coords[1],
                0
            ]).scale(5 * sf, about_point=self.body.get_center()).set_color(BLUE)




class Test(Scene):

    # This is an attempt at making an n body simulator

    @staticmethod
    def get_x_acceleration(i, bodies): # these are both lists of vectors, i is just the index of the body
        G = 1
        result = Vect([0, 0])
        for k, n in enumerate(range(0, len(bodies))):
            if k != i:
                new_force = (bodies[k].position.subtract(bodies[i].position)).scale(G * (bodies[k].mass) / ((bodies[k].position.subtract(bodies[i].position)).get_magnitude() ** 3))
                if new_force.get_magnitude() > Vect([1.5, 1.5]).get_magnitude():
                    new_force = new_force.scale(Vect([1.5, 1.5]).get_magnitude() / new_force.get_magnitude())
                result = result.add(new_force)
        return result

    def construct(self):
        n = 0 # number of bodies
        t = 5 # number of seconds
        dt = 1/15
        sf = 2 # scale factor
        bodies = []
        colors = [BLUE, RED, GREEN, YELLOW]
        for i, body in enumerate(range(n)): #defining lists, don't get confused.
            bodies.append(Body(
                Vect([(random.random() * 6 - 3), (random.random() * 6 - 3)]), # actual position
                Vect([(random.random() * 1 - 0.5), (random.random() * 1 - 0.5)]), # actual velocity
                1, # mass
                colors[i % len(colors)], # colors
                sf # scale factor
            ))

        # "sun"
        G = 1
        m1 = 1
        m2 = 0.07
        r = 1
        Fc = (G * m1 * m2) / (r * r)
        v = sqrt(G * m1 / r)
        'v = sqrt((Fc * r)/(m2))'
        bodies.append(Body(
            Vect([0, 0, 0]),
            Vect([0, 0, 0]),
            m1,
            YELLOW,
            15 * sf/m1
        ))

        bodies.append(Body(
            Vect([r, 0, 0]),
            Vect([0, v, 0]),
            m2,
            GREEN,
            4 * sf/m2
        ))

        self.wait(1)
        for i, body in enumerate(bodies):
            body.acceleration = Vect(Test.get_x_acceleration(i, bodies).coords.copy())
            body.rel_acc = body.acceleration.scale(sf)
            """body.acc_arrow = Arrow(start=body.body.get_center(), end=[
                    body.body.get_x() + body.rel_acc.coords[0],
                    body.body.get_y() + body.rel_acc.coords[1],
                    0
                ]).scale(20/3, about_point=body.body.get_center()).set_color(RED)

            self.play(Create(body.acc_arrow))
            self.play(Create(body.vel_arrow))"""
            self.add(body.body)
        self.wait(1)

        for x in range(0, round(t * (1/dt))):
            for i, body in enumerate(bodies):
                body.position = body.position.add(body.velocity.scale(dt))
                body.rel_pos = body.position.scale(sf)
                body.body.move_to(body.rel_pos.manimcoords)

                body.acceleration = Vect(Test.get_x_acceleration(i, bodies).coords.copy())
                body.rel_acc = body.acceleration.scale(sf)

                body.velocity = body.velocity.add(body.acceleration.scale(dt))
                body.rel_vel = body.velocity.scale(sf)


                # just updating arrows, no fancy stuff here
                """self.remove(body.vel_arrow)
                self.remove(body.acc_arrow)
                body.vel_arrow = Arrow(start=body.body.get_center(), end=[
                    body.body.get_x() + body.rel_vel.coords[0],
                    body.body.get_y() + body.rel_vel.coords[1],
                    0
                ]).scale(15/3, about_point=body.body.get_center()).set_color(BLUE)
                body.acc_arrow = Arrow(start=body.body.get_center(), end=[
                    body.body.get_x() + body.rel_acc.coords[0],
                    body.body.get_y() + body.rel_acc.coords[1],
                    0
                ]).scale(20 / 3, about_point=body.body.get_center()).set_color(RED)
                self.add(body.vel_arrow)
                self.add(body.acc_arrow)"""

            self.wait(dt)
        self.wait(1)

