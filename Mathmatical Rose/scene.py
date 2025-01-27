from manim import *


class Test(Scene):
    def construct(self):
        axes = Axes(
            x_range=np.array([-1, 1]),
            y_range=np.array([-1, 1]),
            x_length=8,
            y_length=8,
            x_axis_config={"numbers_with_elongated_ticks": [-1, 1]},
            y_axis_config={"numbers_with_elongated_ticks": [-1, 1]},
            tips=False
        )
        n = ValueTracker(0)
        k = 12
        def get_rose():
            func = ParametricFunction(
                lambda t:
                np.array([np.sin(n.get_value()*t) * np.cos(t),
                          np.sin(n.get_value()*t) * np.sin(t), 0]),
                t_range=[0, k * PI],
                color=BLUE,
            ).scale(4)
            """plot = axes.plot(
                lambda t:
                np.array([np.sin(n.get_value()*t) * np.cos(t),
                          np.sin(n.get_value()*t) * np.sin(t), 0]),
                color=BLUE
            )"""
            return func
        graph = always_redraw(get_rose)
        graph.add_updater(lambda x: x.move_to(ORIGIN))
        self.play(Create(axes), Create(graph))
        self.play(n.animate.increment_value(1), run_time=18, rate_func=linear)
