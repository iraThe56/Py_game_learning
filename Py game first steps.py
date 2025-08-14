import pygame
import pyfalcon
import ParticleSystem

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dots!")

# Game loop
running = True
clock = pygame.time.Clock()
particleSystem = ParticleSystem.ParticleSystem()
particleSystem.add_particle(400,10,1)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))  # Black background
    # Draw a dot
    pygame.draw.circle(screen, (255, 255, 255), (400, 300), 5)

    xlocation,ylocation = pygame.mouse.get_pos()

    pygame.draw.circle(screen, (255, 255, 255), (xlocation, ylocation), 5)
    particleSystem.draw_particles(screen)



    # Update display
    pygame.display.flip()
    clock.tick(90)  # 60 FPS

pygame.quit()