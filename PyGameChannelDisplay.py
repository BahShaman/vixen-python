#PyGameChannelDisplay
import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
UNK      = ( 255, 255,   0)
BLUE     = ( 0,   0,   255)

#Opening and setting the window size
size = (500, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Channel Display")
done = False
clock = pygame.time.Clock()

while not done:
	# --- Main event loop
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
 
	# --- Game logic should go here
 
	# --- Drawing code should go here
 
	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	screen.fill(BLACK)
	box_width = 20
	box_gap   = 20
	box_off   = 10
	box_on = False
	for i in range(6):
		box_on = False
		if i % 1 == 0:
			box_on = True
		lef = box_off + i*(box_gap + box_width)
		top = box_off
		wid = box_width
		hgt = box_width
		print "[%d,%d,%d,%d] " % (lef,top,wid,hgt)
		if box_on == True:
			pygame.draw.rect(screen, BLUE, [lef,top,wid,hgt], 1)
		

	print "---"
	#pygame.draw.rect(screen, BLUE , [10,10,20,20], 1)
	#pygame.draw.rect(screen, BLACK, [30,10,20,20], 1)
	#pygame.draw.rect(screen, UNK  , [50,10,20,20], 1)
	#pygame.draw.rect(screen, GREEN, [70,10,20,20], 1)
	
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
	# --- Limit to 60 frames per second
	clock.tick(10)
