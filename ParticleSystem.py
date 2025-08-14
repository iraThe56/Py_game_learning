import pygame
class ParticleSystem:
    def __init__(self):
        self.positions = np.array()
        self.velocities = np.array()
        self.masses = np.array()
    def draw_particles(self, screen):
        for pos in self.positions:
            x, y = pos
            pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)
    def add_particles(self, x_position,y_position,mass):
        self.positions.append((x_position,y_position))
        self.velocities.append()
        self.masses.append(mass)


    def update(self, dt):

# Vectorized operations on arrays