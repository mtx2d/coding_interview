import random
from cmath import tau
from manim import (
    Circle,
    Square,
    Scene,
    Create,
    Group,
    ReplacementTransform,
    Text,
    Write,
    BLUE,
    BLUE_E,
    UP,
    RIGHT,
    LEFT,
    Rectangle,
    FadeIn,
)

def get_pillars():
    pillars = []
    
    return pillars


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

class SquareFlipRight(Scene):
    def construct(self):
        square = Square()
        square.flip(RIGHT)
        self.play(Create(square))

class RectangleExample(Scene):
    def construct(self):
        rec = Rectangle()
        self.play(Create(rec))

class Pillars(Scene):
    # cannot simply pass in a list of items to play
    def construct(self):
        
        def get_pillars():
            pillars = []
            heights = [random.randint(1, 8) for _ in range(8)]
            for i,h in enumerate(heights):
                rec=Rectangle(height = h, width = 1.0).shift(UP * h/2)
                pillars.append(rec)
            return Group(*pillars).arrange(buff=0.5)

        self.play(*[FadeIn(r) for r in get_pillars()])
        self.wait(10)


