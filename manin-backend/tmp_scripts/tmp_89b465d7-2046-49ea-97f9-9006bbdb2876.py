from manim import *

class PromptScene(Scene):
    def construct(self):
        # Create the triangle
        triangle = Polygon(ORIGIN, 3 * RIGHT, 3 * UP, color=BLUE)
        triangle_label = MathTex("c").next_to(triangle.get_edge_center(UP), UP)
        a_label = MathTex("a").next_to(triangle.get_edge_center(RIGHT), RIGHT)
        b_label = MathTex("b").next_to(triangle.get_edge_center(LEFT), LEFT)

        # Create squares on each side of the triangle
        square_a = Square(side_length=3, color=GREEN).next_to(triangle.get_edge_center(RIGHT), DOWN, buff=0)
        square_b = Square(side_length=3, color=RED).next_to(triangle.get_edge_center(UP), LEFT, buff=0)
        square_c = Square(side_length=3**0.5 * 3, color=YELLOW).next_to(triangle, DOWN, buff=0)

        # Position the squares correctly
        square_a.move_to(triangle.get_edge_center(RIGHT) + 1.5 * DOWN)
        square_b.move_to(triangle.get_edge_center(UP) + 1.5 * LEFT)
        square_c.move_to(triangle.get_center() + 1.5 * DOWN)

        # Add all elements to the scene
        self.play(Create(triangle), Write(a_label), Write(b_label), Write(triangle_label))
        self.wait(1)
        self.play(Create(square_a), Create(square_b))
        self.wait(1)
        self.play(Create(square_c))
        self.wait(2)

        # Show the Pythagorean theorem equation
        theorem = MathTex("a^2 + b^2 = c^2").to_edge(DOWN)
        self.play(Write(theorem))
        self.wait(2)