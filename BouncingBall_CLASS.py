import pygame
import sys
import random
import os; os.system("cls")

# Initialize Pygame
pygame.init()

# Screen size
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls with Classes")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ball class
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.speed_x = random.randint(-5,5) 
        self.speed_y = random.randint(-5,5)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]
        # self.color =  random.choice(["red", "green", "blue", "yellow", "magenta", "cyan"])


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
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Create balls
balls = []
for _ in range(50):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
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
