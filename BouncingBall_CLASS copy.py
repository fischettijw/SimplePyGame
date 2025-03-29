import pygame
import sys
import random

import os; os.system("cls")


# START: Ball class --------------------------------------------------------------------
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        is_uniform_ball_radius = False      # Set 'True' for Uniform ball radius
                                            # distribution and 'False' for Gaussian
        if is_uniform_ball_radius == True:
            min_ball_radius = 10
            max_ball_radius = 50
            self.radius = random.randint(min_ball_radius,max_ball_radius)
        else:
            ball_average_radius = 20
            sigma = 25
            self.radius = random.gauss(ball_average_radius,sigma)

        speed = random.randint(-5,5)
        self.speed_x = speed if speed != 0 else 1
        speed = random.randint(-5,5)
        self.speed_y = speed if speed != 0 else -1   

        self.color = (random.randint(0, 255), random.randint(0, 255),
                      random.randint(0, 255))

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x = -self.speed_x

        # Bounce off ceiling and floor
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y = -self.speed_y

    def draw(self):
        # pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.radius, self.radius))
    
# END: Ball class ----------------------------------------------------------------------


# Initialize Pygame
pygame.init()

# Screen size
WIDTH = 1024
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls with Ball Class")

# Colors
BLACK = (0, 0, 0)

# Create balls with random initial positions
num_of_balls = 200
balls = []
for _ in range(num_of_balls):
    x = random.randint(100, WIDTH - 100)
    y = random.randint(100, HEIGHT - 100)
    balls.append(Ball(x, y))

# Game loop control
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    # Fill the screen with black
    screen.fill(BLACK)

    # Move and draw each ball
    for ball in balls:
        ball.move()
        ball.draw()

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
