from manim import *

class PromptScene(Scene):
    def construct(self):
        # Create a right triangle
        triangle = Triangle(stroke_color=WHITE).scale(2)
        triangle.set_fill(WHITE, opacity=0.3)
        triangle.next_to(ORIGIN, LEFT)

        # Create squares on each side of the triangle
        a_square = Square(side_length=2, stroke_color=BLUE, fill_color=BLUE, fill_opacity=0.3)
        a_square.next_to(triangle, direction=RIGHT, buff=0)
        b_square = Square(side_length=2, stroke_color=RED, fill_color=RED, fill_opacity=0.3)
        b_square.next_to(triangle, direction=DOWN, buff=0)
        c_square = Square(side_length=2, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.3)
        c_square.next_to(triangle, direction=RIGHT+DOWN, buff=0)

        # Label the sides of the triangle
        a_label = MathTex("a").next_to(a_square, direction=RIGHT)
        b_label = MathTex("b").next_to(b_square, direction=DOWN)
        c_label = MathTex("c").next_to(c_square, direction=RIGHT+DOWN)

        self.play(Create(triangle))
        self.play(Create(a_square), Create(b_square), Create(c_square))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)

        # Show the equation a^2 + b^2 = c^2
        equation = MathTex("a^2 + b^2 = c^2").move_to(3*UP)
        self.play(Write(equation))
        self.wait(2)