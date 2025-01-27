from manim import *
import math

class Negativesa(Scene):
    def construct(self):
        text0 = MarkupText(f"Multiplication and division with <span foreground='red'>Negative numbers</span>",font_size=40)
        self.play(Write(text0))
        self.wait(1)


class Addsubnegatives(Scene):
    def construct(self):
        text0 = MarkupText(f"<span foreground='teal'>Adding</span> and <span foreground='red'>subtracting</span>",font_size=30).scale(1).set_x(-4).set_y(3)
        numline = NumberLine(
            length=10,
            x_range=[-5,5,1],
            include_numbers=True,
            numbers_with_elongated_ticks=[0],
            stroke_width=5
        )
        eq = MarkupText(f"<span foreground='teal'>1 </span><span foreground='red'>- 3</span>", font_size=30).scale(2.5).set_x(0).set_y(2)
        self.play(Write(numline), Write(text0))
        self.play(Write(eq))
        
        self.wait(1)
        dot0 = Dot(point=[1,0,0], color=RED, radius = 0.15)
        self.play(Write(dot0))
        for n in range(3):
            self.play(Create(CurvedArrow(start_point=[1-n,0,0],end_point=[-n,0,0],color=RED)),run_time=0.5)
            self.wait(0.1)

        dot1 = Dot(point=[-2,0,0], color=GREEN, radius = 0.15)
        text1 = MarkupText(f"<span foreground='green'>= -2</span>",font_size=30).set_x(0).set_y(-2).scale(3)
        self.play(Write(dot1),Write(text1))
        self.wait(1)

class Negativesb(Scene):
    def construct(self):
        
        eq1 = MathTex(r"3 \cdot (-2) =", substrings_to_isolate="-", font_size=30).set_x(0).set_y(0).scale(3)
        eq1.set_color_by_tex("-",RED)
        
        num = MathTex("6",font_size=30).set_x(3.2).set_y(0).scale(3)
        
        sign1 = MathTex("+", font_size=30).set_x(2.5).set_y(0).scale(3)
        sign1.set_color_by_tex("+",TEAL)
        
        sign2 = MathTex("-", font_size=30).set_x(2.5).set_y(0).scale(3)
        sign2.set_color_by_tex("-",RED)
        
        self.play(Write(eq1))
        self.play(Write(num))
        self.wait(1)
        self.play(Write(sign1), run_time=0.4)
        for n in range(2):
            self.play(FadeOut(sign1),Write(sign2), run_time=0.4)
            self.play(FadeOut(sign2),Write(sign1), run_time=0.4)
        self.play(FadeOut(sign1), run_time=0.4)
        self.wait(0.5)
        text0 = MathTex(r"?",font_size=30).set_x(2.5).set_y(0).scale(3)
        text0.set_color_by_tex("?",GREEN)
        self.play(Write(text0),run_time=1)
        self.wait(3)

        
        eq2 = MathTex(r"(-5) \cdot (-6) =", substrings_to_isolate="-", font_size=30).set_x(0).set_y(0).scale(3)
        eq2.set_color_by_tex("-",RED)

        sign3 = MathTex("+", font_size=30).set_x(3.3).set_y(0).scale(3)
        sign3.set_color_by_tex("+",TEAL)

        sign4 = MathTex("-", font_size=30).set_x(3.3).set_y(0).scale(3)
        sign4.set_color_by_tex("-",RED)

        self.play(Transform(eq1,eq2), FadeOut(text0), FadeOut(num))
        num2 = MathTex(r"30",font_size=30).set_x(4.2).set_y(0).scale(3)
        self.play(Write(num2))
        arr = Arrow(start=[sign3.get_x(),-2,0],end=[sign3.get_x(),-0.2,0], color=YELLOW)

        self.wait(2)
        self.play(Create(arr))
        self.wait(0.5)
        for n in range(2):
            self.play(FadeOut(sign3),Write(sign4), run_time=0.4)
            self.play(FadeOut(sign4),Write(sign3), run_time=0.4)
        self.play(FadeOut(sign3), run_time=0.4)
        self.wait(0.5)
        text0 = MathTex(r"?",font_size=30).set_x(sign3.get_x()).set_y(0).scale(3)
        text0.set_color_by_tex("?",GREEN)
        self.play(Write(text0),run_time=1)
        self.wait(1)
        
        

class Negativesc(Scene):
    def construct(self):
        #function to make life easier
        def represent_equation(num1, num2, op):
            divnum2 = 1 / num2
            # func variables
            if op == "multiplication":
                eq = MathTex("{{(%d)}}"%num1," \cdot ","{{(%d)}}"%num2, color = GRAY, font_size=30).set_x(0).set_y(2).scale(3)
            elif op == "division":
                eq = MathTex("{{(%d)}}"%num1," / {{(%d)}}"%divnum2, color = GRAY, font_size=30).set_x(0).set_y(2).scale(3)
                
            if num1 < 0 or num2 < 0:
                eq.set_color_by_tex("-",RED)
            arr = Arrow(color=YELLOW).put_start_and_end_on([-0.5 * num1, 1, 0],[0.5 * num1, 1, 0])
            arr2 = Arrow(color=RED).put_start_and_end_on([eq[2].get_bottom()[0], eq[2].get_bottom()[1] - 1, 0], eq[2].get_bottom())
            textflip = MathTex(r"flip",font_size=30).scale(1.5).set_x(0).set_y(-1)
            textflip.set_color_by_tex("p",RED)

            #func scene
            self.play(Write(eq))
            self.wait(1)
            self.play(Transform(eq[0], arr))
            self.add(arr)
            self.remove(eq[0])
            self.play(arr.animate.put_start_and_end_on([0,0,0],[num1,0,0]))
            if num2 < 0:
                if num1 < 0:
                    self.play(Create(arr2))
                    self.play(Write(textflip), run_time=0.5)
                    self.play(Rotate(arr, -PI, about_point=[0,0,0]), run_time=1.5)
                    self.play(FadeOut(textflip), FadeOut(arr2), run_time=0.3)
                elif num1 >= 0:
                    self.play(Create(arr2))
                    self.play(Write(textflip), run_time=0.5)
                    self.play(Rotate(arr, PI, about_point=[0,0,0]), run_time=1.5)
                    self.play(FadeOut(textflip), FadeOut(arr2), run_time=0.3)
            temp_num = abs(divnum2)
            temp_num2= abs(num2)
            if op == "multiplication":
                textnum = MathTex("\cdot","%d"%temp_num2,color=YELLOW, font_size=30).scale(2).set_x(0.5 * ((num1 * num2)/ abs(num2))).set_y(0.5)
            elif op == "division":
                textnum = Text("shrink by {}".format(int(temp_num)),color=YELLOW, font_size=25).scale(2).set_x(0.5 * ((num1 * num2)/ abs(num2))).set_y(0.5)
            self.wait(0.4)
            action_text = VGroup(eq[1], eq[2])
            self.play(Transform(action_text, textnum))
            self.add(textnum)
            self.remove(action_text)
            self.play(arr.animate.put_start_and_end_on([0,0,0],[num2 * num1,0,0]), textnum.animate.set_x(0.5 * num1 * num2))
            dot = Dot(point=[num2 * num1, 0, 0], color=GREEN)
            self.play(FadeOut(textnum), Create(dot), run_time=0.3)
            self.wait(0.65)
            self.play(FadeOut(arr), FadeOut(dot))
            self.wait(1)
        
        # text
        text0 = MarkupText(f"How to <span foreground='teal'>Multiply and Divide</span> by <span foreground='red'>Negative Numbers</span>", font_size=30).set_x(0).set_y(0).scale(1.5)
        text1 = MarkupText(f"<span foreground='gray'>Remember?</span>",font_size=30).set_x(0).set_y(2).scale(1.5)
        surround_rect = SurroundingRectangle(text0)
        surround_rect.set_stroke(color=BLUE, opacity=0.7)
        
        # number lines
        numline = NumberLine(
            length=12,
            x_range=[-6,6,1],
            include_numbers=True,
            numbers_with_elongated_ticks=[0],
            stroke_width=5
        )
        
        # Scene
        self.play(Write(text0))
        self.play(Create(surround_rect))
        self.wait(1.5)
        self.play(FadeOut(surround_rect),run_time=0.4)
        self.play(text0.animate.set_x(-3.5).set_y(3).scale(0.5))
        self.wait(1)
        self.play(Write(numline), Write(text1))
        self.play(FadeOut(text1))
        self.wait(1)
        represent_equation(2,3,"multiplication")
        represent_equation(3,2,"multiplication")
        represent_equation(3, -2, "multiplication")
        represent_equation(-2, -3, "multiplication")
        represent_equation(6, 0.5, "division")
        represent_equation(6, -0.5, "division")
        represent_equation(-4,-0.5, "division")
        self.wait(3)
        represent_equation(-6,0.5, "division")
        represent_equation(6,-0.5, "division")

class Negativesd(Scene):
    def construct(self):
        # variables
        eq0 = MathTex(r"{{3}} * {{-2}} = -6", font_size=30).scale(3).set_x(0).set_y(0)
        eq0transformed = MathTex(r"{{-3}} * {{2}} = -6", font_size=30).scale(3).set_x(0).set_y(0)

        # Scene
        self.play(Write(eq0))
        self.wait(1.5)
        self.play(TransformMatchingTex(eq0, eq0transformed), run_time=0.7)
        self.remove(eq0)
        self.add(eq0transformed)
        self.wait(1)

class Negativese(Scene):
    def construct(self):
        pos_pos = MathTex("(+)", " \cdot ", "(+)", " = ", "(+)",tex_to_color_map={"+":TEAL},font_size=30).scale(3)
        neg_neg = MathTex("(-)", " \cdot ", "(-)", " = ", "(+)",tex_to_color_map={"+":TEAL, "-":RED},font_size=30).scale(3)
        pos_neg = MathTex("(+)", " \cdot ", "(-)", " = ", "(-)",tex_to_color_map={"+":TEAL, "-":RED},font_size=30).scale(3)
        neg_pos = MathTex("(-)", " \cdot ", "(+)", " = ", "(-)",tex_to_color_map={"+":TEAL, "-":RED},font_size=30).scale(3)

        rules = VGroup(pos_pos, pos_neg, neg_neg).arrange(DOWN)
        neg_pos.set_x(pos_neg.get_x()).set_y(pos_neg.get_y())
        self.play(Write(pos_pos))
        self.wait(5)
        self.play(Write(pos_neg))
        self.wait(1)
        self.play(TransformMatchingTex(pos_neg, neg_pos))
        self.add(neg_pos)
        self.remove(pos_neg)
        self.wait(4)
        self.play(Write(neg_neg))
        self.wait(1)
        newgroup = VGroup(pos_pos, neg_pos, pos_neg, neg_neg)
        self.play(newgroup.animate.arrange(DOWN)) # animating this makes pos_neg (previously removed) automatically show up
        self.wait(1)
