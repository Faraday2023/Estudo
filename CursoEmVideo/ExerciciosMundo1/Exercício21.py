# Faça um programa em Python qeu abra e reproduza o áudio de um arquivo mp3

#from os import environ
#environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\marco\\Downloads\\Maranata.mp3')
pygame.mixer.music.play()
print("Audio will play for 4 seconds")

time.sleep(4)

"""import pygame
pygame.init()
pygame.mixer.music.load('C:\\Users\\marco\\Downloads\\Maranata.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()"""
