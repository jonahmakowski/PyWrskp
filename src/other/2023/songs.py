import pygame

pygame.init()
song = input("Input your song's file name (ie if your name is Schifoan.mp3, enter Schifoan)")
pygame.mixer.music.load('../music/{}.mp3'.format(song))
pygame.mixer.music.play()

input('press enter to end music')
