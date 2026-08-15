import pygame
from sys import exit
import os
import time

pygame.mixer.init()


dim_x,dim_y=25,150

pos_l_x, pos_l_y=0,0
pos_r_x, pos_r_y=1200-dim_x,0

d_width,d_height=1200,720

pygame.init()

base_screen=pygame.display.set_mode((d_width,d_height))
clock=pygame.time.Clock()

pygame.display.set_caption('')

sound_button_click=pygame.mixer.Sound(fr'Assets\UI_Sound\Minimalist1.mp3')

class button:
	def __init__(self,image):
		self.img_load=pygame.image.load(image).convert_alpha()
	
	def new_game(self):
		self.img_rect=self.img_load.get_rect(midbottom=(base_screen.get_rect().center))
	def quit(self,a):
		self.img_rect=self.img_load.get_rect(topleft=a)
	def draw(self):
		base_screen.blit(self.img_load,self.img_rect)


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

# class ball:
# 	def __init__(self,x,y):
# 		self.surface=pygame.Surface

st_button_load=fr"Assets\Menu Buttons\Large Buttons\Large Buttons\New game Button.png"
qt_button_load=fr"Assets\Menu Buttons\Large Buttons\Large Buttons\Quit Button.png"


st_button=button(st_button_load)
st_button.new_game()

st_button_bottomleft_cd=list(st_button.img_rect.bottomleft)
qt_button_topleft_cd=(st_button_bottomleft_cd[0],st_button_bottomleft_cd[1]+40)


qt_button=button(qt_button_load)
qt_button.quit(qt_button_topleft_cd)




l_b=bars(dim_x,dim_y)
r_b=bars(dim_x,dim_y)

game_state='Menu'

while True:

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			exit()

	base_screen.fill('Black')
	mouse_pos=pygame.mouse.get_pos()
	
	if game_state=='Menu':
		st_button.draw()
		qt_button.draw()
	
	if pygame.mouse.get_pressed()[0] and qt_button.img_rect.collidepoint(mouse_pos):
		sound_button_click.play()
		game_state='exit'
		pygame.time.wait(60)
		exit()
	if pygame.mouse.get_pressed()[0] and st_button.img_rect.collidepoint(mouse_pos):

		sound_button_click.play()
		pygame.time.wait(60)
		game_state='Gameplay'
	
	if game_state=='Gameplay':
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