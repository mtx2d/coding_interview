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
    BLUE,
    BLUE_E,
    UP,
    DOWN,
    RIGHT,
    LEFT,
    Rectangle,
    FadeIn,
)

class ProblemStatement(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(Create(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()

        text = Text(
            """ Dynamic Programming is a technique used to 
            help reduce overlapping computations
            """
        )

        self.play(Write(text))

class Pillars(Scene):
    def construct(self):
        def get_pillars(num = 8, max_height = 8):
            pillars = []
            heights = [random.randint(1, max_height) for _ in range(num)]
            for i, h in enumerate(heights):
                rec = Rectangle(height=h, width=1.0).shift(UP * h / 2)
                pillars.append(rec)
            return VGroup(*pillars).arrange(buff=0.5, aligned_edge=DOWN)

        self.play(*[FadeIn(r) for r in get_pillars(8)])
        self.wait(10)
