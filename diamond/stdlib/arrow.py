"""
Turtle but 10x easier!
"""
import turtle
import sys

class Arrow:
    def __init__(self, name):
        self.name = name
        self._turtle = turtle.Turtle()

    def __repr__(self):
        return f"Arrow {self.name} is callable with {self.name}."

    def line(self, distance, color="black"):
        self._turtle.pencolor(color)
        self._turtle.forward(distance)

    def right(self, angle):
        self._turtle.right(angle)

    def rect(self, width, height, color="white", outline="black"):
        self._turtle.pencolor(outline)
        self._turtle.fillcolor(color)
        self._turtle.begin_fill()
        for _ in range(2):
            self._turtle.forward(width)
            self._turtle.right(90)
            self._turtle.forward(height)
            self._turtle.right(90)
        self._turtle.end_fill()

_arrows = {}

def activate(name):
    if name in _arrows:
        raise Exception("Arrow name already exists")
    new_arrow = Arrow(name)
    caller_module = sys.modules["__main__"]
    setattr(caller_module, name, new_arrow)
    return new_arrow
