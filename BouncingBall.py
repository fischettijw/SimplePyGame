import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen size
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initial Ball settings
BALL_RADIUS = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# Game loop control
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    # Fill the screen with black
    screen.fill(BLACK)

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce off the walls
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
        ball_speed_x = -ball_speed_x

    # Bounce off the ceiling and floor
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Exit the game
pygame.quit()
sys.exit()
