import pygame
import os
import time

pygame.init()

screen=pygame.display.set_mode((1200,720))
clock=pygame.time.Clock()

print(screen.get_width())

r=True

while r:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			r=False

	screen.fill('Black')

	pygame.display.flip()

	clock.tick(60)

pygame.quit()

