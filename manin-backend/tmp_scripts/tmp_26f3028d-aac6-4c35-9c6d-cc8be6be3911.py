from manim import *

class PromptScene(Scene):
    def construct(self):
        # Create a right triangle
        triangle = Polygon(
            ORIGIN, 3*RIGHT, 3*RIGHT+4*UP,
            stroke_color=WHITE,
            stroke_width=2,
            fill_color=BLUE,
            fill_opacity=0.5
        )

        # Create squares on each side of the triangle
        square1 = Square(side_length=3, color=WHITE, fill_opacity=0.5).move_to(triangle.get_vertices()[0])
        square2 = Square(side_length=4, color=WHITE, fill_opacity=0.5).move_to(triangle.get_vertices()[1])
        square3 = Square(side_length=5, color=WHITE, fill_opacity=0.5).move_to(triangle.get_vertices()[2])

        self.play(Create(triangle))
        self.play(Create(square1), Create(square2), Create(square3))
        self.wait(1)