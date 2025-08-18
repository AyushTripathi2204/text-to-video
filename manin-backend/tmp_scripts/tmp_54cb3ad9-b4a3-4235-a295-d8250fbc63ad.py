from manim import *

class PromptScene(Scene):
    def construct(self):
        milestones = VGroup()

        colors = [BLUE, GREEN, RED, YELLOW, PURPLE]
        for i, color in enumerate(colors):
            milestone = Dot(radius=0.1, color=color)
            milestone.move_to(LEFT_SIDE + i * 0.25 * RIGHT)
            milestones.add(milestone)

        self.play(Create(milestones))

        arrows = VGroup()
        for i in range(len(milestones) - 1):
            arrow = Arrow(milestones[i].get_center(), milestones[i+1].get_center(), buff=0)
            arrows.add(arrow)

        self.play(Create(arrows))

        progress_dot = Dot(radius=0.1, color=ORANGE)
        progress_dot.move_to(LEFT_SIDE)
        self.play(Create(progress_dot))
        self.play(progress_dot.animate.move_to(RIGHT_SIDE, run_time=5))

        self.wait()