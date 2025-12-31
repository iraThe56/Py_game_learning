import numpy as np
import pygame
import pyfalcon
from pygame import MOUSEBUTTONUP
import cv2
import random
import pygame_widgets
import ParticleSystem
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from sympy.external.gmpy import invert

pygame.init()
window= pygame.display.set_mode((1000, 600))

def slider_block(window,slider_x,slider_y,slider_width,slider_height,number_of_sliders,slider_spacing):
    sliders=[]
    for i in range(number_of_sliders):
        sliders.append(Slider(window,slider_x+slider_width*(i+1)+(i+1)*slider_spacing,slider_y,slider_width,slider_height,min=0,max=255,step=1,vertical=True,invert=True))
    return sliders



value_sliders=slider_block(window,100,100,10,100,3,10)
#
state = Slider(window, 100, 100, 10, 40, min=1, max=5, step=1,vertical=True,invert=True)
# slider = Slider(window, 100, 100, 10, 40, min=0, max=255, step=1,vertical=True,invert=True)
# slider = Slider(window, 100, 100, 10, 40, min=0, max=255, step=1,vertical=True,invert=True)

output = TextBox(window, 475, 200, 50, 50, fontSize=10)

output.disable()  # Act as label instead of textbox

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
    curent_state=state.get_state()
    if curent_state == 0:
        values = [slider.getValue() for slider in value_sliders]
        r_value, g_value, b_value = values
        window.fill((r_value, g_value, b_value))
    if curent_state == 1:
        values = [slider.getValue() for slider in value_sliders]
        r_value, g_value, b_value = values
        window.fill((r_value, g_value, b_value))






    #
    # print(slider_value)
    # output.setText(str(slider_value))

    pygame_widgets.update(events)
    pygame.display.update()
