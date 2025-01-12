import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Entangled Triangles")

# Define colors
blue = (0, 0, 255)
white = (255, 255, 255)
purple = (128, 0, 128)

# Function to draw triangles
def draw_triangles(screen):
    # Define the outer triangle vertices
    outer_triangle = [(200, 50), (100, 300), (300, 300)]
    # Define the inner triangle vertices
    inner_triangle = [(150, 200), (250, 200), (200, 300)]
    
    # Draw the outer triangle
    pygame.draw.polygon(screen, blue, outer_triangle)
    # Draw the inner triangle
    pygame.draw.polygon(screen, white, inner_triangle)

    # Calculate the center position for the point
    center_point = (200, 200)
    # Draw the purple point (circle)
    pygame.draw.circle(screen, purple, center_point, 5)  # Radius of 5

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    screen.fill(white)
    
    # Draw the triangles and point
    draw_triangles(screen)

    # Update the display
    pygame.display.flip()