from manim import *

class PromptScene(Scene):
    def construct(self):
        milestones = VGroup()
        colors = [BLUE, GREEN, RED, YELLOW, PURPLE]
        for i, color in enumerate(colors):
            milestone = Dot(color=color)
            milestone.scale(0)
            milestone.move_to(LEFT_SIDE + i * 0.25 * RIGHT)
            milestone.generate_target()
            milestone.target.scale(0.5)
            milestones.add(milestone)
        
        self.play(
            *[GrowFromCenter(milestone) for milestone in milestones]
        )
        
        arrows = VGroup()
        for i in range(len(milestones) - 1):
            arrow = Arrow(milestones[i].get_center(), milestones[i+1].get_center())
            arrows.add(arrow)
        
        self.play(
            *[GrowArrow(arrow) for arrow in arrows]
        )
        
        progress_dot = Dot(color=WHITE)
        progress_dot.move_to(milestones[0].get_center())
        self.play(
            MoveAlongPath(progress_dot, VGroup(*[milestone.target for milestone in milestones])),
            run_time=5
        )
        
        self.wait(1)

    def GrowArrow(arrow):
        return GrowArrow(arrow)