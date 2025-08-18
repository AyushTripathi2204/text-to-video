from manim import *

class TestMath(Scene):
    def construct(self):
        eq = MathTex("a^2 + b^2 = c^2")
        self.add(eq)
