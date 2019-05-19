import pygame, sys

def check_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


def main_window_blit(screen, image_main_window, main_window):
	screen.blit(image_main_window, main_window)

def logo_blit(screen, color, logo):
	pygame.draw.rect(screen, color, logo)

def hero_blit(screen, image_hero, hero):
	screen.blit(image_hero, hero)

def enemy_blit(screen, image_enemy, enemy):
	screen.blit(image_enemy, enemy)

def personages_update(screen, image_hero, hero, image_enemy, enemy):
	hero_blit(screen, image_hero, hero)
	enemy_blit(screen, image_enemy, enemy)

def display_update(screen, image_main_window, main_window, 
					color, logo,
					image_hero, hero,
					image_enemy, enemy):
	
	main_window_blit(screen, image_main_window, main_window)
	logo_blit(screen, color, logo)
	hero_blit(screen, image_hero, hero)
	enemy_blit(screen, image_enemy, enemy)
	pygame.display.flip()

