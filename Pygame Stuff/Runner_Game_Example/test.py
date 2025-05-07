import pygame
from sys import exit

pygame.init() # Initialize pygame

# Variables
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')

while True:
    # Check for all types of player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface, (200, 100))

    pygame.display.update() # Display game to the player
    clock.tick(60)