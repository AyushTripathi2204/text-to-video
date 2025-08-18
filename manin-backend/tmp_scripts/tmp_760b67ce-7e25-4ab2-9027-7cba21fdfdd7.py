from manim import *

class PromptScene(Scene):
    def construct(self):
        # Define milestone positions
        milestone_positions = [LEFT * 4 + DOWN, LEFT * 2 + DOWN, ORIGIN + DOWN, RIGHT * 2 + DOWN, RIGHT * 4 + DOWN]
        milestone_colors = [RED, GREEN, BLUE, ORANGE, PURPLE]
        milestone_labels = ["Milestone 1", "Milestone 2", "Milestone 3", "Milestone 4", "Milestone 5"]

        # Create milestones and labels
        milestones = []
        labels = []
        for pos, color, label in zip(milestone_positions, milestone_colors, milestone_labels):
            milestone = Dot(point=pos, color=color, radius=0.2)
            milestones.append(milestone)
            label = Text(label, font_size=24).next_to(milestone, UP)
            labels.append(label)

        # Create arrows between milestones
        arrows = []
        for i in range(len(milestones) - 1):
            arrow = Arrow(start=milestones[i].get_center(), end=milestones[i + 1].get_center(), buff=0.2)
            arrows.append(arrow)

        # Create a progress dot
        progress_dot = Dot(point=milestones[0].get_center(), color=YELLOW, radius=0.15)

        # Animate milestones and labels
        for milestone, label in zip(milestones, labels):
            self.play(GrowFromCenter(milestone), Write(label))

        # Animate arrows
        for arrow in arrows:
            self.play(Create(arrow))

        # Animate progress dot moving across the timeline
        for milestone in milestones[1:]:
            self.play(progress_dot.animate.move_to(milestone.get_center()), run_time=1)

        self.wait(1)