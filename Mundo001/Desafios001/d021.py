# Faça um programa em Python que abra e reproduza
# o áudio de um arquivo MP3.

"""import pygame
print(f'{"Desafio 021":=^30}')
a = pygame.mixer_music()"""

import pygame
import time

pygame.init()  # iniciar o uso da biblioteca pygame
pygame.mixer.music.load('spiritriders.mp3')
pygame.mixer.music.play()
time.sleep(130.99998)
# pygame.event.wait()  # espera o evento terminar para encerrar o programa
# por algum motivo pygame.event.wait() não funciona mais sozinho
# usei a biblioteca 'time' para delimitar o tempo em que a música toca
