import random
from cmath import tau
from manim import (
    Circle,
    Square,
    Scene,
    Create,
    VGroup,
    ReplacementTransform,
    Text,
    Write,
    UP,
    DOWN,
    RIGHT,
    LEFT,
    Rectangle,
    FadeIn,
)


class ProblemStatement(Scene):
    def construct(self):

        text = Text(
            """ Dynamic Programming is a technique used to avoid 
            redundant computations when there is overlapping sub-problems.
            """
        )

        self.play(Write(text))


class Pillars(Scene):
    def construct(self):
        def get_pillars(num=8, max_height=8):
            pillars = []
            heights = [random.randint(1, max_height) for _ in range(num)]
            for i, h in enumerate(heights):
                rec = Rectangle(height=h, width=1.0).shift(UP * h / 2)
                pillars.append(rec)
            return VGroup(*pillars).arrange(buff=0.5, aligned_edge=DOWN)

        self.play(*[FadeIn(r) for r in get_pillars(8)])
        self.wait(10)
