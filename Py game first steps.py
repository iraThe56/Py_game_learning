import numpy as np
import pygame
import pyfalcon
from pygame import MOUSEBUTTONUP
import cv2
import random

import ParticleSystem

screen_size=[2000,800]
# Initialize
pygame.init()
screen = pygame.display.set_mode((screen_size[0], screen_size)[1],pygame.RESIZABLE)
pygame.display.set_caption("Dots!")

# Game loop
running = True
clock = pygame.time.Clock()
particleSystem = ParticleSystem.ParticleSystem()


## basic demo 1,draws three manually added particles

# particleSystem.add_particle(1000,500,0,0,500)
# particleSystem.add_particle(200,100,40,1,4)
# particleSystem.add_particle(300,40,30,1,4)


##basic demo 2 creates one hundred particles in a spyral

# particle_radisus = 0
# particle_theta = 0
# for i in range(100):
#     particle_radisus = 1 + particle_radisus
#     particle_theta = particle_theta + (np.pi / 1/12)
#     particle_x = np.cos(particle_theta) * particle_radisus + 500
#     particle_y = np.sin(particle_theta) * particle_radisus + 400
#     particleSystem.add_particle(particle_x, particle_y, 0, 0, 4)
# print()

# basic demo 3, draws 10,000 particles randomly across the screen

for i in range(10000):
    particleSystem.add_particle(float(random.random()*1000)+500,float(random.random()*400+300),0, 0, .1)


# count=100
# for i in range(count):
#     side=(np.sqrt(count))
#     particleSystem.add_particle((1/side)*i+250,(1/side)*i+250,0, 0, .1)


#
# def create_particle_in_radius(radius):
#     particles_x = (random.random() - 0.5) * 2 * radius  # x in [-radius, radius]
#     particles_y = (random.random() - 0.5) * 2 * radius  # y in [-radius, radius]
#     if np.sqrt((particles_x**2)+(particles_y**2)) > radius:
#         create_particle_in_radius(radius)
#         return None
#     else:
#         particleSystem.add_particle(particles_x + 800, particles_y + 350, 0, 40, .05)
#         return None
#
#
# radius=10
# for i in range(1000):
#     create_particle_in_radius(radius)
#
# #
# particle_theta=0
# particle_radisus = 0
# for i in range(1000):
#     particle_radisus = .4 + particle_radisus
#     particle_theta = particle_theta + (np.pi / 1/100)
#     particle_x = np.cos(particle_theta) * particle_radisus + 500
#     particle_y = np.sin(particle_theta) * particle_radisus + 400
#     particleSystem.add_particle(particle_x, particle_y, 0, 0, .1)
#





# def save_frame(screen):
#     # Convert pygame surface to numpy array
#     # frame = pygame.surfarray.array3d(screen)
#     # frame = frame.swapaxes(0, 1)  # Rotate for opencv
#     # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#     # video_writer.write(frame)



# Fix: Define fps, width, height
# fps = 60
# width, height = screen.get_size()
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# video_writer = cv2.VideoWriter('planet.mp4', fourcc, fps, (width, height))

# Fix: Initialize mouse state
mouse_clicked_state = False
last_mouse_clicked_state = False

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Fix: Move mouse click handling inside event loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked_state = True
        if event.type == MOUSEBUTTONUP:
            mouse_clicked_state = False
            # if last_mouse_clicked_state:
            particleSystem.add_particle(int(mouse_x), int(mouse_y), 0, 0, 40)




    # Clear screen

    # gameloop
    # screen.fill((50, 50, 140)) $ Black background
    screen.fill((0,0,0))

    # pygame.draw.circle(screen, (255, 255, 255), (mouse_x, mouse_y), 5)
    particleSystem.draw_particles(screen)
    accelerations = particleSystem.calculate_acceleration()
    particleSystem.update_velocities(accelerations)


 # if demo 3 swap to second set
    particleSystem.update(.05)

    # particleSystem.update(.01)
    # particleSystem.apply_drag(.001)

    last_mouse_clicked_state = mouse_clicked_state
    # save_frame(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

# Fix: Release video writer after loop ends
# video_writer.release()
pygame.quit()