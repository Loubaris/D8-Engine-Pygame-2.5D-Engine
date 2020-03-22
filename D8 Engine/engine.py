import pygame
from random import randrange
from time import sleep
pygame.init()



pygame.display.set_caption("D8 Engine")
screen = pygame.display.set_mode((1000, 600))

print("Engine launched")

matin = pygame.image.load("assets/matin.png").convert()
jour = pygame.image.load("assets/jour.png").convert()
nuit = pygame.image.load("assets/nuit.png").convert()
gun = pygame.image.load("assets/gun.png").convert_alpha()
gunfire = pygame.image.load("assets/gunfire.png").convert_alpha()
sol = pygame.image.load("assets/sol.png").convert_alpha()
pygame.mixer.music.load("assets/fire.mp3")
viseur = pygame.image.load("assets/viseur.png").convert_alpha()
tree = pygame.image.load("assets/tree.png").convert_alpha()
stree = pygame.image.load("assets/tree.png").convert_alpha()
statue = pygame.image.load("assets/statue.png")

running = True



# Initialisation de l'engine

time = randrange(0, 5)
print(time)
fire = 0
soly = 0
chrono = 0
munition = 10
treey = 500
streey = 300
statuey = 1600


	


while running:	



# Cycle Jour / Nuit

	if time >= 0:
		if time < 6:
			screen.blit(matin, (0, 0))
		elif time > 6 and time < 18:
			screen.blit(jour, (0, 0))
		elif time > 18:
			screen.blit(nuit, (0, 0))


# Le sol

	screen.blit(sol, (0, soly))
	x, y = pygame.mouse.get_pos()
	if y < 210 and y > 0:
		if soly < 80:
			soly += 0.5
	elif y > 400 and y < 600:
		if soly > 0:
			soly -= 0.5

# La souris
	screen.blit(tree, (treey, soly))
	screen.blit(stree, (streey, soly))
	screen.blit(statue, (statuey, soly))
	if x > 450:
		treey -= 1
		streey -= 1
		statuey -= 1
	elif x < 150:
		treey+= 1
		streey += 1
		statuey += 1

	if treey > 2000:
		treey = 1
	elif treey < -1000:
		treey = 999
	elif streey > 2000:
		streey = 1
	elif streey < -1000:
		streey = 999
	elif statuey > 2000:
		statuey = 1
	elif statuey < -1000:
		statuey = 999
	



# Joueur

	if fire == 0:
		screen.blit(gun, (350, 305))   # Pistolet 
	elif fire == 1:
		screen.blit(gunfire, (350, 305))
		screen.blit(viseur, (x-30, y-26))





# Quittez le moteur

	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			if munition > 0:
				fire = 1
				chrono = 0
				pygame.mixer.music.play()
				munition -= 1
	chrono += 1
	if chrono > 20 and chrono < 40:
		fire = 0
	elif chrono >= 1000:
		chrono = 0
		time += 0.5

		
