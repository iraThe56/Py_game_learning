import pygame
import numpy as np
import pyfalcon
import random


class ParticleSystem:
    def __init__(self, max_particles=100000):
        # Pre-allocate arrays for maximum particles
        self.positions = np.zeros((max_particles, 3))
        self.velocities = np.zeros((max_particles, 3))
        self.masses = np.zeros(max_particles)
        self.colors = np.zeros((max_particles))
        self.count = 0  # How many particles are actually "active"
        self.max_particles = max_particles
        self.g_value = 100

    def add_particle(self, x, y, vx=0, vy=0, mass=1.0):
        # Check if position already exists (with small tolerance
        # (pyflacon crashes it two particles are in the same space))
        if self.count > 0:
            existing_positions = self.positions[:self.count, :2]  # Only x,y, only active particles
            new_position = np.array([x, y])
            tolerance = 1e-10
            distances = np.linalg.norm(existing_positions - new_position, axis=1)
            if np.any(distances < tolerance):
                return False  # Position already exists, silently skip
        if self.count < self.max_particles:
            self.positions[self.count] = [x, y, 0]
            self.velocities[self.count] = [vx, vy, 0]
            self.masses[self.count] = mass
            self.count += 1
            return True  # Successfully added
        return False  # Array full

    def draw_particles(self, screen):
        # # Only draw the active particles (0 to count)
        for i in range(self.count):
            x, y, z = self.positions[i]
            # if self.masses[i] > 100:
            #     continue
            # pygame.draw.circle(screen, (round(random.random()*255), round(random.random()*255), round(random.random()*255)), (int(x), int(y)),max( round(0+np.sqrt(abs(self.masses[i]))),1  ))
            # pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)),max( round(0+np.sqrt(abs(self.masses[i]))),1  ) )
            # pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)),  1)
            velocity_magnitude=np.sqrt(self.velocities[i,0]**2 +self.velocities[i,1]**2+self.velocities[i,2]**2)
            velocity_color_magnitude=255-min((velocity_magnitude),225)
            pygame.draw.circle(screen,(velocity_color_magnitude,velocity_color_magnitude, 225), (int(x), int(y)),max( round(0+np.sqrt(abs(self.masses[i]))),1  ) )



    def update(self, dt):
        # Only update active particles
        active_positions = self.positions[:self.count]
        active_velocities = self.velocities[:self.count]
        # Vectorized update on just the active slice
        active_positions += active_velocities * dt
    def calculate_acceleration(self):
        if self.count > 2:
            mask = self.masses != 0
            active_positions = self.positions[mask]
            active_masses = self.masses[mask]

            active_accelerations = pyfalcon.gravity(active_positions.astype(np.float32), active_masses,eps=100)
            multiplied_active_accelerations= active_accelerations[0] * self.g_value

            empty_accelerations=np.zeros((self.max_particles, 3))

            empty_accelerations[mask] = multiplied_active_accelerations
            return empty_accelerations
        else:
            return np.zeros((self.max_particles, 3))


    def update_velocities(self, accelerations):
        self.velocities += (accelerations.astype(float))
                            # +np.random.normal(size=(self.max_particles, 3)))
        



    def apply_drag(self,drag_coefficient):
        self.velocities = self.velocities- self.velocities * drag_coefficient



    # def prevent_overlaping_particles(self):
    #     mask = self.masses != 0
    #     active_positions = self.positions[mask]
    #     active_masses = self.masses[mask]
    #     for i in range(active_positions):
    #         active_masses[i] = self.masses[i]





# Vectorized operations on arrays