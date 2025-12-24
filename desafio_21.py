# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


import pygame

pygame.init() # inicia o pygame
pygame.mixer.music.load("musica.mp3") # música.mp3 = música escolhida.
pygame.mixer.music.play() # play
pygame.event.wait() # toca a música até acabar.

# Obs: A versão do python 3.14 não está funcionando o pygame.
