import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_triangle():
    """
    Draws a purple triangle using PyGame and OpenGL.
    """

    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    # Set up OpenGL
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    gluOrtho2D(0, 500, 0, 500)  # Set up 2D orthographic projection

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

        # Draw the purple triangle
        glColor3f(0.5, 0.0, 0.5)  # Set color to purple
        glBegin(GL_TRIANGLES)
        glVertex2f(100, 100)
        glVertex2f(300, 100)
        glVertex2f(200, 300)
        glEnd()

        pygame.display.flip()  # Swap buffers
        pygame.time.wait(10)  # Wait for a short time

    pygame.quit()

if __name__ == "__main__":
    draw_triangle()