import pygame
import os

def hello():
	pass

file = "C:\\Users\\BOSCIA\\Documents\\Projects\\VixenDecode\\03 - This Is Halloween.mp3"
file = 'C:/Users/BOSCIA/Documents/Projects/VixenDecode/03 - This Is Halloween.ogg'
#file = '03 - This Is Halloween.ogg'
print os.path.exists(file);
print file
pygame.init()
pygame.display.set_mode((200,100))
#pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(0)

#while pygame.mixer.music.get_busy(): 
#    pygame.time.Clock().tick(10000)
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)	
#while True:
#	print "playing"