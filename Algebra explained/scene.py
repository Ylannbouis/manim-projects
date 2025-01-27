from manim import *

class Test(Scene): #this is for reference on parametric curves

    def graphFunc(self, t):
        return np.array((np.sin(2 * t), np.sin(3 * t), 0))  # parametric curve function

    def construct(self):
        circle = Circle()
        p0 = 3 * DOWN + 5 * LEFT
        v0 = 2.8 * UP + 1.5 * RIGHT
        g = 0.9 * DOWN

        graph = ParametricFunction(
            self.graphFunc,
            t_range = np.array([0, TAU]),
            fill_opacity=0
        ).set_color(BLUE)
        self.add(graph.scale(3)) # not animated (because why would you?)
        self.play(Create(circle))
        self.play(MoveAlongPath(circle, graph, run_time=5), rate_func=linear)
        self.wait(1)

class Runners(Scene):

    def construct(self):
        # You
        head1 = Circle().set_stroke(color=BLUE)
        neck1 = Line(
            start = head1.get_bottom(),
            end = [head1.get_bottom()[0], head1.get_bottom()[1] - 4, 0],
            color = BLUE
        )
        leg11 = Line(
            start = neck1.get_bottom(),
            end = [neck1.get_bottom()[0] - 1.5, neck1.get_bottom()[1] - 2, 0],
            color = BLUE
        )
        leg12 = Line(
            start = neck1.get_bottom(),
            end = [neck1.get_bottom()[0] + 1.5, neck1.get_bottom()[1] - 2, 0],
            color = BLUE
        )
        arm11 = Line(
            start = [neck1.get_center()[0], neck1.get_center()[1] + 1, 0],
            end = [neck1.get_center()[0] + 2, neck1.get_center()[1] - 1, 0],
            color = BLUE
        )
        arm12 = Line(
            start = [neck1.get_center()[0], neck1.get_center()[1] + 1, 0],
            end = [neck1.get_center()[0] - 2,neck1.get_center()[1] - 1,0 ],
            color = BLUE
        )

        # Alex

        head2 = Circle().set_stroke(color=RED)
        neck2 = Line(
            start=head2.get_bottom(),
            end=[head2.get_bottom()[0], head2.get_bottom()[1] - 4, 0],
            color=RED
        )
        leg21 = Line(
            start=neck2.get_bottom(),
            end=[neck2.get_bottom()[0] - 1.5, neck2.get_bottom()[1] - 2, 0],
            color=RED
        )
        leg22 = Line(
            start=neck2.get_bottom(),
            end=[neck2.get_bottom()[0] + 1.5, neck2.get_bottom()[1] - 2, 0],
            color=RED
        )
        arm21 = Line(
            start=[neck2.get_center()[0], neck2.get_center()[1] + 1, 0],
            end=[neck2.get_center()[0] + 2, neck2.get_center()[1] - 1, 0],
            color=RED
        )
        arm22 = Line(
            start=[neck2.get_center()[0], neck2.get_center()[1] + 1, 0],
            end=[neck2.get_center()[0] - 2, neck2.get_center()[1] - 1, 0],
            color=RED
        )

        alex = VGroup(head2, neck2, leg21, leg22, arm21, arm22).scale(0.2)
        alex.set_x(-6).set_y(-1.5)

        you = VGroup(head1, neck1, leg11, leg12, arm11, arm12).scale(0.2)
        you.set_x(-6).set_y(2.5)

        you_head_coord = you.get_top()
        alex_head_coord = alex.get_top()

        # race tracks
        your_track = NumberLine(
            x_range=[0, 30, 1],
            length=12
        ).set_x(you.get_bottom()[0] + 6).set_y(you.get_bottom()[1] - 0.3)
        alex_track = NumberLine(
            x_range=[0, 30, 1],
            length=12
        ).set_x(alex.get_bottom()[0] + 6).set_y(alex.get_bottom()[1] - 0.3)

        # trackers
        tick_mark_you = Line(
            start = [you.get_bottom()[0], you.get_bottom()[1] - 0.1, 0],
            end = [you.get_bottom()[0], you.get_bottom()[1] - 0.5, 0],
            color = GREEN
        )
        tick_mark_you.add_updater(lambda mark: mark.set_x(you.get_bottom()[0]))

        tick_mark_alex = Line(
            start=[alex.get_bottom()[0], alex.get_bottom()[1] - 0.1, 0],
            end=[alex.get_bottom()[0], alex.get_bottom()[1] - 0.5, 0],
            color=GREEN
        )
        tick_mark_alex.add_updater(lambda mark: mark.set_x(alex.get_bottom()[0]))

        you_text = Tex("You", color=BLUE, font_size = 30).scale(1.5)
        alex_text = Tex("Alex", color=RED, font_size = 30).scale(1.5)
        you.move_to(ORIGIN)
        alex.move_to(ORIGIN)
        you.shift(UP * 2).scale(2)
        alex.shift(DOWN * 2).scale(2)
        surround_rect_you = SurroundingRectangle(you, color=BLUE, stroke_opacity=0.7)
        you_text.next_to(surround_rect_you, RIGHT)

        # scene
        self.play(Create(you))
        self.play(Create(alex))
        self.wait(0.7)
        self.play(Create(surround_rect_you), Write(you_text))
        self.play(FadeOut(surround_rect_you))
        self.wait(0.4)
        self.play(
            you.animate.set_x(-6).set_y(2.5).scale(0.5),
            alex.animate.set_x(-6).set_y(-1.5).scale(0.5),
            you_text.animate.set_x(you_head_coord[0]).set_y(you_head_coord[1] + 0.25).scale(0.7),
        )
        surround_rect_alex = SurroundingRectangle(alex, color=RED, stroke_opacity=0.7)
        alex_text.set_x(alex_head_coord[0]).set_y(alex_head_coord[1] + 0.25).scale(0.7)
        self.wait(1)
        self.play(Create(surround_rect_alex), Write(alex_text))
        self.play(FadeOut(surround_rect_alex))

        you_text.add_updater(lambda d: d.set_x(you.get_top()[0]))
        alex_text.add_updater(lambda d: d.set_x(alex.get_top()[0]))

        self.play(Create(your_track), Create(alex_track))
        self.play(Write(tick_mark_you), Write(tick_mark_alex))
        self.wait(1)

        self.play(alex.animate.set_x(-6 + (6* (12/30))), run_time=1.3)
        self.wait(1)

        alex_headstart_brace = BraceBetweenPoints(alex_track.get_left(), tick_mark_alex.get_center())
        alex_headstart_brace_label = Tex("6", color=GREEN).set_x(alex_headstart_brace.get_bottom()[0]).set_y(alex_headstart_brace.get_bottom()[1] - 0.2)
        self.play(Write(alex_headstart_brace), Write(alex_headstart_brace_label), run_time=1.3)
        self.wait(1)

        race_total_time = 8
        time_tracker = ValueTracker(0)
        time = DecimalNumber(0)
        time.add_updater(lambda d: d.set_value(time_tracker.get_value()))
        time_text = Tex("Time:")
        time_text.shift(MED_SMALL_BUFF * LEFT)
        time.next_to(time_text, RIGHT)

        time_label = VGroup(time_text, time)
        time_label.center().to_edge(DOWN)
        self.play(Write(time_label))
        def you_updater(d):
            if time_tracker.get_value() >= 7.5:
                d.clear_updaters()
                d.set_x(15*12/30)
            else:
                d.set_x((4 * (12 / 30) * time_tracker.get_value()) - (15 * 12 / 30))
        def alex_updater(d):
            if time_tracker.get_value() >= 8:
                d.clear_updaters()
                d.set_x(15*12/30)
            else:
                d.set_x((3 * (12 / 30) * time_tracker.get_value()) - (9 * 12 / 30))

        you.add_updater(you_updater)
        alex.add_updater(alex_updater)

        you_velocity = Arrow(start=you.get_right(), end=[you.get_right()[0] + 1.5, you.get_right()[1], 0], color=BLUE)
        alex_velocity = Arrow(start=alex.get_right(), end=[alex.get_right()[0] + 1, alex.get_right()[1],0], color=RED)
        you_velocity.add_updater(lambda d: d.put_start_and_end_on(
            you.get_right(),
            [you.get_right()[0] + 1.5, you.get_right()[1], 0]
        ))
        alex_velocity.add_updater(lambda d: d.put_start_and_end_on(
            alex.get_right(),
            [alex.get_right()[0] + 1, alex.get_right()[1], 0]
        ))

        you_velocity_label = Tex("4 m/s", color=BLUE).set_x(you_velocity.get_center()[0]).set_y(you_velocity.get_center()[1] + 0.3).scale(0.5)
        alex_velocity_label = Tex("3 m/s", color=RED).set_x(alex_velocity.get_center()[0]).set_y(alex_velocity.get_center()[1] + 0.3).scale(0.5)
        you_velocity_label.add_updater(lambda d: d.set_x(you_velocity.get_center()[0]))
        alex_velocity_label.add_updater(lambda d: d.set_x(alex_velocity.get_center()[0]))

        self.play(Create(alex_velocity), Write(alex_velocity_label))
        self.wait(1)
        self.play(FadeOut(alex_headstart_brace), Unwrite(alex_headstart_brace_label), run_time=0.5)
        self.play(time_tracker.animate.set_value(race_total_time), rate_func=linear, run_time=8)
        # self.play(FadeOut(alex_velocity), Unwrite(alex_velocity_label))
        self.wait(3)

        you.clear_updaters()
        alex.clear_updaters()
        time_tracker.set_value(0)

        self.play(you.animate.set_x(-15 * 12/30), alex.animate.set_x(-9 * 12/30))
        self.wait(1)
        you.add_updater(you_updater)
        alex.add_updater(alex_updater)
        self.play(Create(you_velocity), Write(you_velocity_label))
        self.play(time_tracker.animate.set_value(race_total_time), rate_func=linear, run_time=8)
        # self.play(FadeOut(you_velocity), Unwrite(you_velocity_label))
        self.wait(1)

        you.clear_updaters()
        alex.clear_updaters()
        time_tracker.set_value(0)

        self.play(you.animate.set_x(-15 * 12 / 30), alex.animate.set_x(-9 * 12 / 30))
        self.wait(1)
        you.add_updater(you_updater)
        alex.add_updater(alex_updater)
        # self.play(Create(you_velocity), Write(you_velocity_label), Create(alex_velocity), Write(alex_velocity_label))
        self.play(time_tracker.animate.set_value(6), rate_func=linear, run_time=6)
        you.clear_updaters()
        alex.clear_updaters()

        question_mark = Tex("?", color=GREEN).move_to(time).scale(2)
        self.remove(time)
        self.play(FadeOut(you_velocity), Unwrite(you_velocity_label), FadeOut(alex_velocity), Unwrite(alex_velocity_label), run_time=0.4)
        self.play(Write(question_mark))
        distance_brace = BraceBetweenPoints(your_track.get_left(),tick_mark_you.get_center())
        question_mark_copy = question_mark.copy()
        question_mark_copy.move_to([distance_brace.get_center()[0], distance_brace.get_center()[1]-0.6,0])
        self.wait(2)
        self.play(Write(distance_brace), Write(question_mark_copy))
        self.wait(1)


        # all that for ONE PARAGRAPH!!!!!!!!!!!!!!!!!!!

        go_out_text = Tex("Go out into the world!", color=BLUE, font_size=30).move_to(ORIGIN).scale(3)

        screen_rect = ScreenRectangle(fill_color = BLACK, fill_opacity = 0.8).scale(5).set_stroke(color=BLACK)
        self.play(FadeIn(screen_rect))
        self.play(Write(go_out_text))
        self.wait(1)

class AlgebraBeta(Scene):
    def construct(self):


        # This would be much better with pictures by the use of svg files


        algebra_text = Tex("Algebra", color = BLUE, font_size=30).scale(3).move_to(ORIGIN)
        logic_and_reasoning_text = Tex("Logic and reasoning", color=GRAY, font_size=30).scale(3).move_to([algebra_text.get_x(), algebra_text.get_y() + 3, 0])
        real_world_apps_text = Tex("Real world applications", color=RED, font_size=30).scale(3).move_to([algebra_text.get_x(), algebra_text.get_y() - 3, 0])
        arr1 = Arrow(start=logic_and_reasoning_text.get_bottom(), end = algebra_text.get_top(), color=BLUE)
        arr2 = Arrow(start=algebra_text.get_bottom(), end = real_world_apps_text.get_top(), color=RED)

        self.play(Write(algebra_text))
        self.wait(2)
        self.play(Write(logic_and_reasoning_text))
        self.play(Create(arr1))
        self.wait(2)
        self.play(Write(real_world_apps_text))
        self.play(Create(arr2))
        self.wait(2)

class familiar_topics(Scene):

    def construct(self):
        pass
