import numpy as np
import pygame
import pyfalcon
from pygame import MOUSEBUTTONUP, Color
import cv2
import random
import math


# Initialize
screen_width=500
screen_height=500
screen_size=screen_width,screen_height

pygame.init()
screen = pygame.display.set_mode((screen_size[0], screen_size[1]),pygame.RESIZABLE)
pygame.display.set_caption("Dots!")

# Game loop
running = True
clock = pygame.time.Clock()

class Texture:
    def __init__(self,texture_width,texture_height):
        self.texture_width = texture_width
        self.texture_height = texture_height
        self.texture_array = np.zeros((texture_width,texture_height, 4), int)
    def set_pixel_value(self,texture_pixel_x_position,texture_pixel_y_position,red_value,green_value,blue_value,alpha_value):
        texture_pixel_x_position=texture_pixel_x_position %self.texture_width
        texture_pixel_y_position=texture_pixel_y_position %self.texture_height
        self.texture_array[texture_pixel_x_position,texture_pixel_y_position,0] = red_value
        self.texture_array[texture_pixel_x_position,texture_pixel_y_position,1] = green_value
        self.texture_array[texture_pixel_x_position,texture_pixel_y_position,2] = blue_value
        self.texture_array[texture_pixel_x_position,texture_pixel_y_position,3] = alpha_value
    def return_pixel_value(self,texture_pixel_x_position,texture_pixel_y_position):
        texture_pixel_x_position=texture_pixel_x_position %self.texture_width
        texture_pixel_y_position=texture_pixel_y_position %self.texture_height
        return self.texture_array[texture_pixel_x_position,texture_pixel_y_position]
    def return_pixel_color(self,texture_pixel_x_position,texture_pixel_y_position):
        texture_pixel_x_position=texture_pixel_x_position %self.texture_width
        texture_pixel_y_position=texture_pixel_y_position %self.texture_height
        pixel=self.return_pixel_value(texture_pixel_x_position,texture_pixel_y_position)
        return pixel[0],pixel[1],pixel[2]











class Vector:
    def __init__(self,x_position,y_position,z_position):
        self.x_position = x_position
        self.y_position = y_position
        self.z_position = z_position
    def set_position(self,x_position,y_position,z_position):
        self.x_position = x_position
        self.y_position = y_position
        self.z_position = z_position
    def __add__(self,other):
        new_vector=Vector(0,0,0)
        new_vector.x_position = self.x_position+other.x_position
        new_vector.y_position = self.y_position+other.y_position
        new_vector.z_position = self.z_position+other.z_position
        return new_vector
    def __sub__(self,other):
        new_vector = Vector(0, 0, 0)
        new_vector.x_position = self.x_position-other.x_position
        new_vector.y_position = self.y_position-other.y_position
        new_vector.z_position = self.z_position-other.z_position
        return new_vector
    def get_length(self):
        length=math.sqrt(self.x_position ** 2 + self.y_position ** 2 + self.z_position ** 2)
        return length



#
# class Object:
#     def __init__(self, position_vector: Vector):
#         self.position_vector = postion_vector
#
#
# class Cube(Object):
#     def __init__(self,position_vector):

def get_absolute_distance(vector_1:Vector,vector_2:Vector):
    return  math.sqrt((vector_1.x_position-vector_2.x_position )**2+(vector_1.y_position-vector_2.y_position )**2+(vector_1.z_position-vector_2.z_position )**2 )


max_value=math.sqrt((1/2*screen_height)**2+(1/2*screen_width)**2)/255




texture=Texture(50,50)
for i in range(texture.texture_height):
    for j in range(texture.texture_width):


        texture.set_pixel_value(i,j,1/2*i,1/2*j,40,255)


while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    center_of_screen = Vector(screen_width / 2, screen_height / 2, 0)
    def convert_vector_to_screen_space(vector):
        converted_vector=vector-center_of_screen
        return converted_vector

    screen.fill((0,0,0))
    for i in range(screen_width):
        for j in range(screen_height):
            color=texture.return_pixel_color(i,j)
            screen.set_at((i, j), color)




    pygame.display.flip()
    clock.tick(1 )  # 60 FPS
pygame.quit()