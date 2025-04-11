import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Character Battle")

# Character Class
class Character:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 50
        self.height = 50
        self.health = 100
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.speed

    def attack(self, other):
        if abs(self.x - other.x) < 60 and abs(self.y - other.y) < 60:
            other.health -= 10
            print(f"Enemy Health: {other.health}")

# Create Player and Enemy
player = Character(100, 250, BLUE)
enemy = Character(600, 250, RED)

# Game Loop
running = True
while running:
    pygame.time.delay(30)
    screen.fill(WHITE)

    keys = pygame.key.get_pressed()
    player.move(keys)

    if keys[pygame.K_SPACE]:  # Attack when spacebar is pressed
        player.attack(enemy)

    player.draw()
    enemy.draw()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
