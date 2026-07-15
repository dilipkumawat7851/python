import pygame
import sys

# Initialize pygame
pygame.init()

# Create the game window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player properties
x = 100
y = 100
speed = 5
size = 50

# Game loop
running = True

while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which key is pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the square
    pygame.draw.rect(screen, BLUE, (x, y, size, size))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()