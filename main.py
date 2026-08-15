import pygame
from sys import exit
import os
import time

pygame.init()

dim_x,dim_y=25,150

pos_l_x, pos_l_y=0,0
pos_r_x, pos_r_y=1200-dim_x,0

d_width,d_height=1200,720

base_screen=pygame.display.set_mode((d_width,d_height))
clock=pygame.time.Clock()

pygame.display.set_caption('')

class bars:
	def __init__(self,x,y):
		self.surface=pygame.Surface((x,y))
		self.surface.fill('White')
		

	def pos_w(self):
		global pos_l_y
		if pos_l_y>=0:
			pos_l_y-=5
			return pos_l_y

	def pos_s(self):
		global pos_l_y
		if pos_l_y+dim_y<=720:
			pos_l_y+=5
			return pos_l_y

	def pos_up(self):
		global pos_r_y
		if pos_r_y>=0:
			pos_r_y-=5
			return pos_r_y

	def pos_down(self):
		global pos_r_y
		if pos_r_y+dim_y<=720:
			pos_r_y+=5
			return pos_r_y

l_b=bars(dim_x,dim_y)
r_b=bars(dim_x,dim_y)

while True:

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			exit()

	base_screen.fill('Black')
	mouse_pos=pygame.mouse.get_pos()
	
	
	keys=pygame.key.get_pressed()
	
	if keys[pygame.K_w]:
		l_b.pos_w()
	if keys[pygame.K_s]:
		l_b.pos_s()

	if keys[pygame.K_UP]:
		r_b.pos_up()
	if keys[pygame.K_DOWN]:
		r_b.pos_down()

	base_screen.blit(l_b.surface,(pos_l_x,pos_l_y))
	base_screen.blit(r_b.surface,(pos_r_x,pos_r_y))

	pygame.display.flip()
	pygame.display.update()

	clock.tick(60)

pygame.quit()