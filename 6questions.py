import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    """
    Draws a line between two points using PyGame and OpenGL.

    Args:
        x1, y1: Coordinates of the first point.
        x2, y2: Coordinates of the second point.
    """

    glColor3f(1.0, 0.0, 0.0)  # Set color to red
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

# Example usage:
if __name__ == "__main__":
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    gluOrtho2D(0, 500, 0, 500)

    glClear(GL_COLOR_BUFFER_BIT)

    draw_line(50, 50, 450, 450)  # Draw a line from (50, 50) to (450, 450)

    pygame.display.flip()
    pygame.time.wait(1000)  # Wait for 1 second
    pygame.quit()