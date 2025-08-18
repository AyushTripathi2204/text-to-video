from manim import *

class PromptScene(Scene):
    def construct(self):
        milestones = VGroup()

        colors = [BLUE, GREEN, RED, YELLOW, PURPLE]
        for i, color in enumerate(colors):
            milestone = Dot(radius=0.1, color=color)
            milestone.move_to(LEFT_SIDE + i * 0.25 * RIGHT)
            milestones.add(milestone)
            self.play(GrowFromCenter(milestone))

        arrows = VGroup()
        for i in range(len(milestones) - 1):
            arrow = Arrow(milestones[i].get_center(), milestones[i+1].get_center(), buff=0)
            arrows.add(arrow)

        progress_dot = Dot(radius=0.1, color=WHITE)
        progress_dot.move_to(milestones[0].get_center())

        self.play(Create(milestones), Create(arrows))

        self.play(AnimationGroup(*[
            progress_dot.animate.move_to(milestone.get_center())
            for milestone in milestones[1:]
        ], lag_ratio=0.5))

        self.wait(1)