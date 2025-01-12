import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the canvas dimensions
    width, height = 500, 400
    screen = pygame.display.set_mode((width, height))

    # Set the title of the canvas
    pygame.display.set_caption("My Pygame Canvas")

    # Fill the canvas with white color
    screen.fill((255, 255, 255))

    # Draw a red line
    start_pos = (50, 50)
    end_pos = (start_pos[0] + 200, start_pos[1])  # 200 pixels to the right
    line_color = (255, 0, 0)  # Red color
    line_width = 3

    pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    pygame.quit()
                    sys.exit()

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()