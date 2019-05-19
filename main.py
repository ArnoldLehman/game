import pygame
import sys

import game_functions as gf

def run_game():
	pygame.init()
	
	#Создание дисплея
	screen = pygame.display.set_mode((800, 500))
	pygame.display.set_caption("Vikings")
	
	#Создание окна "Лого"
	screen_rect = screen.get_rect()
	logo = pygame.Rect(0, 0, 800, 200)
	logo.bottom = screen_rect.bottom
	logo_color = (215, 215, 215)
	
	#Создание главного окна
	image_main_window = pygame.image.load('images/arena.png')
	main_window = image_main_window.get_rect()
	
	#Создание и расположение Главного героя на главном окне
	image_hero = pygame.image.load('images/Монах2.0.png')
	hero = image_hero.get_rect()
	hero.centery = main_window.centery
	hero.x = 650
	
	#Создание и расположение Противника на главном окне
	image_enemy = pygame.image.load('images/Жнец.png')
	enemy = image_enemy.get_rect()
	enemy.centery = main_window.centery
	enemy.x = 70
	
	while True:
		gf.check_events()
		gf.display_update(screen, image_main_window, main_window, 
		logo_color, logo, image_hero, hero, image_enemy, enemy)

run_game()
