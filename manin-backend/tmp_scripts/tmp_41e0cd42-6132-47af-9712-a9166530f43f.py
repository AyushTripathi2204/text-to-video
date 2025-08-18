from manim import *

class PromptScene(Scene):
    def construct(self):
        milestones = VGroup()
        colors = [BLUE, GREEN, RED, YELLOW, PURPLE]
        
        for i in range(5):
            milestone_dot = Dot(color=colors[i], radius=0.1)
            milestone_dot.move_to(LEFT_SIDE + i * 0.25 * RIGHT)
            milestones.add(milestone_dot)
            self.play(GrowFromCenter(milestone_dot))
        
        arrows = VGroup()
        for i in range(4):
            arrow = Arrow(milestones[i].get_center(), milestones[i+1].get_center(), buff=0)
            arrows.add(arrow)
        
        self.play(Create(arrows))
        
        progress_dot = Dot(color=WHITE, radius=0.1)
        progress_dot.move_to(LEFT_SIDE)
        self.play(MoveAlongPath(progress_dot, Line(LEFT_SIDE, RIGHT_SIDE), run_time=5, rate_func=linear))
        
        self.wait()