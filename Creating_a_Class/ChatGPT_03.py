import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Character Battle")

# Load Sound Effects
punch_sound = pygame.mixer.Sound("D:\fisch\Documents\VS Code\Ronan\SimplePyGame\Creating_a_Class\punch.mp3")  # Ensure you have a 'punch.wav' file
fireball_sound = pygame.mixer.Sound("D:\fisch\Documents\VS Code\Ronan\SimplePyGame\Creating_a_Class\fireball.mp3")  # Ensure you have a 'fireball.wav' file

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
        self.projectiles = []

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # Draw health bar
        pygame.draw.rect(screen, RED, (self.x, self.y - 10, 50, 5))
        pygame.draw.rect(screen, BLUE, (self.x, self.y - 10, self.health // 2, 5))
        # Draw projectiles
        for projectile in self.projectiles:
            projectile.draw()

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
            punch_sound.play()
            print(f"{other.color} Health: {other.health}")

    def shoot(self):
        fireball_sound.play()
        self.projectiles.append(Projectile(self.x + self.width, self.y + self.height // 2, 10, 5))

# Enemy AI Class
class Enemy(Character):
    def move_towards(self, target):
        if self.x < target.x:
            self.x += self.speed - 2
        elif self.x > target.x:
            self.x -= self.speed - 2
        if self.y < target.y:
            self.y += self.speed - 2
        elif self.y > target.y:
            self.y -= self.speed - 2

# Projectile Class
class Projectile:
    def __init__(self, x, y, speed, radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = BLACK

    def move(self):
        self.x += self.speed

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Create Player and Enemy
player = Character(100, 250, BLUE)
enemy = Enemy(600, 250, RED)

# Game Loop
running = True
while running:
    pygame.time.delay(30)
    screen.fill(WHITE)

    keys = pygame.key.get_pressed()
    player.move(keys)
    enemy.move_towards(player)
    
    if keys[pygame.K_SPACE]:  # Attack when spacebar is pressed
        player.attack(enemy)
    if keys[pygame.K_f]:  # Shoot fireball with 'F'
        player.shoot()

    for projectile in player.projectiles:
        projectile.move()
        if projectile.x > WIDTH:
            player.projectiles.remove(projectile)
        elif abs(projectile.x - enemy.x) < 40 and abs(projectile.y - enemy.y) < 40:
            enemy.health -= 15
            player.projectiles.remove(projectile)
            print(f"Enemy hit! Health: {enemy.health}")
    
    player.draw()
    enemy.draw()
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
