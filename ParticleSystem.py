import pygame
import numpy as np


class ParticleSystem:
    def __init__(self, max_particles=100000):
        # Pre-allocate arrays for maximum particles
        self.positions = np.zeros((max_particles, 2))
        self.velocities = np.zeros((max_particles, 2))
        self.masses = np.zeros(max_particles)

        self.count = 0  # How many particles are actually "active"
        self.max_particles = max_particles

    def add_particle(self, x, y, vx=0, vy=0, mass=1.0):
        if self.count < self.max_particles:
            self.positions[self.count] = [x, y]
            self.velocities[self.count] = [vx, vy]
            self.masses[self.count] = mass
            self.count += 1
            return True  # Successfully added
        return False  # Array full

    def draw_particles(self, screen):
        # Only draw the active particles (0 to count)
        for i in range(self.count):
            x, y = self.positions[i]
            pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    def update(self, dt):
        # Only update active particles
        active_positions = self.positions[:self.count]
        active_velocities = self.velocities[:self.count]

        # Vectorized update on just the active slice
        active_positions += active_velocities * dt

    # def update(self, dt):

# Vectorized operations on arrays