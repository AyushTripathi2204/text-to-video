from manim import *

class PromptScene(Scene):
    def construct(self):
        # Create the triangle
        triangle = Polygon(ORIGIN, 3 * RIGHT, 3 * UP, color=BLUE)
        triangle_label = MathTex("a", color=WHITE).next_to(triangle.get_side(0), UP)
        triangle_label_2 = MathTex("b", color=WHITE).next_to(triangle.get_side(1), RIGHT)
        triangle_label_hypotenuse = MathTex("c", color=WHITE).next_to(triangle.get_side(2), UP + RIGHT)

        # Create squares on each side of the triangle
        square_a = Square(side_length=3, color=GREEN).next_to(triangle.get_side(0), DOWN, buff=0)
        square_b = Square(side_length=3, color=RED).next_to(triangle.get_side(1), LEFT, buff=0)
        square_c = Square(side_length=3 * sqrt(2), color=YELLOW).next_to(triangle.get_side(2), UP + RIGHT, buff=0)

        # Position the squares correctly
        square_a.move_to(triangle.get_vertices()[0] + 1.5 * DOWN + 1.5 * LEFT)
        square_b.move_to(triangle.get_vertices()[0] + 1.5 * DOWN + 1.5 * RIGHT)
        square_c.move_to(triangle.get_vertices()[0] + 1.5 * UP + 1.5 * RIGHT)

        # Add everything to the scene
        self.play(Create(triangle))
        self.play(Write(triangle_label), Write(triangle_label_2), Write(triangle_label_hypotenuse))
        self.wait(1)

        # Show the squares
        self.play(Create(square_a), Create(square_b), Create(square_c))
        self.wait(1)

        # Highlight the Pythagorean theorem
        theorem_text = MathTex("a^2 + b^2 = c^2", color=WHITE).to_edge(UP)
        self.play(Write(theorem_text))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(triangle), FadeOut(square_a), FadeOut(square_b), FadeOut(square_c), FadeOut(theorem_text))