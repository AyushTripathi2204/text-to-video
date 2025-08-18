from manim import *

class PromptScene(Scene):
    def construct(self):
        milestones = VGroup()

        colors = [BLUE, GREEN, RED, YELLOW, PURPLE]
        for i, color in enumerate(colors):
            milestone = Dot(color=color)
            milestone.scale(0)
            milestones.add(milestone)

        milestones.arrange(RIGHT, buff=2)
        milestones.move_to(LEFT_SIDE + UP)

        self.play(*[GrowFromCenter(milestone) for milestone in milestones])

        arrows = VGroup()
        for i in range(len(milestones) - 1):
            arrow = Arrow(milestones[i].get_center(), milestones[i+1].get_center(), buff=0)
            arrows.add(arrow)

        self.play(*[GrowArrow(arrow) for arrow in arrows])

        progress_dot = Dot(color=WHITE)
        progress_dot.move_to(milestones[0].get_center())

        self.play(MoveAlongPath(progress_dot, milestones, rate_func=linear))

        self.wait(1)