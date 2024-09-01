# Install and use an external module

from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("Hello World", font='big'),
            int(screen.height / 2 - 8)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)