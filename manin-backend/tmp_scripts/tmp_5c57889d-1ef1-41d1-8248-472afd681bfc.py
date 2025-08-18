from manim import *

class PromptScene(Scene):
    def construct(self):
        milestones = VGroup()
        colors = [BLUE, GREEN, RED, YELLOW, PURPLE]
        for i, color in enumerate(colors):
            milestone_dot = Dot(color=color)
            milestone_dot.scale(0)
            milestone_dot.move_to(LEFT_SIDE + i * 0.25 * RIGHT)
            milestone_dot.animate.scale(1)
            milestones.add(milestone_dot)
        
        self.play(Create(milestones))

        arrows = VGroup()
        for i in range(len(milestones) - 1):
            arrow = Arrow(milestones[i].get_center(), milestones[i+1].get_center(), buff=0)
            arrows.add(arrow)

        self.play(Create(arrows))

        progress_dot = Dot(color=WHITE)
        progress_dot.move_to(LEFT_SIDE)
        self.play(MoveAlongPath(progress_dot, Line(LEFT_SIDE, RIGHT_SIDE), rate_func=linear))