#PyGameChannelDisplay
import pygame
import os
import time
from vixen import Vixen
from ArduinoSerial import ArduinoSerial

ard = ArduinoSerial()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
ORANGE   = ( 255, 153,   0)
YELLOW   = ( 255, 255,   0)
BLUE     = ( 0,   0,   255)

COLOR = BLUE

vix = Vixen()
vix.channels = 8

channels = vix.channels

box_width = 10
box_gap   = 20
box_off   = 50
per = 0

pygame.font.init()
mfont = pygame.font.SysFont(None, 25)	

vix.periods=10000

#Opening and setting the window size
size = (box_off*2+(vix.channels*(box_gap+box_width)), box_off*2+box_width)
vix.set_screen(size)
pygame.display.set_caption(vix.title)
clock = pygame.time.Clock()
modchannel = [0,0,0,0,0,0,0,0]
prevmodchannel = [0,0,0,0,0,0,0,0]
period=1

#print [ord(x) for x in seq[0][0]]
pause = False
paused = False
done = False
while not done:
	# --- Main event loop
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: # If user clicked close
			done = True
		if event.type == pygame.KEYUP: 
			if event.key == pygame.K_q:
				modchannel[0] = 0
			if event.key == pygame.K_w:
				modchannel[1] = 0
			if event.key == pygame.K_e:
				modchannel[2] = 0
			if event.key == pygame.K_r:
				modchannel[3] = 0
			if event.key == pygame.K_u:
				modchannel[4] = 0
			if event.key == pygame.K_i:
				modchannel[5] = 0
			if event.key == pygame.K_o:
				modchannel[6] = 0
			if event.key == pygame.K_p:
				modchannel[7] = 0
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_ESCAPE:
				done = True 
			if event.key == pygame.K_SPACE: 
				"""channel letters"""
				pass
			if event.key == pygame.K_q:
				modchannel[0] = 255
			if event.key == pygame.K_w:
				modchannel[1] = 255
			if event.key == pygame.K_e:
				modchannel[2] = 255
			if event.key == pygame.K_r:
				modchannel[3] = 255
			if event.key == pygame.K_u:
				modchannel[4] = 255
			if event.key == pygame.K_i:
				modchannel[5] = 255
			if event.key == pygame.K_o:
				modchannel[6] = 255
			if event.key == pygame.K_p:
				modchannel[7] = 255
	
	#print "pause %s paused %s" % (pause, paused),
	if pause and not paused:
		print "Pausing"
		pygame.mixer.music.pause()
		paused = True
		continue
	elif pause and paused:
		#print "paused"
		continue
	elif not pause and paused:
		pygame.mixer.music.unpause()
		paused = False
		continue
	else:
		pass
	
	print

	# --- Game logic should go here
	print '%s:' % str(per),

	# --- Drawing code should go here
 
	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	vix.screen.fill(BLACK)
	label = mfont.render("QWER POIU"  , True, [x*.5 for x in COLOR])
	vix.screen.blit(label, (box_off, box_off+box_width+box_gap/2))
	#edits[per][0] = 50
	for ch in range(vix.channels):
		#print ch
		#value = ord(seq[ch][per])
		if modchannel[ch] >= 0:
			value = modchannel[ch]
			#vix.set_value(ch,per,value)
			chcolor = WHITE
		else:
			value = 0 
			chcolor = COLOR
		print '{:3d}'.format(value),
		box_on = False
		if value > 1:
			box_on = True
		lef = box_off + ch*(box_gap + box_width)
		top = box_off
		wid = box_width
		hgt = box_width
		#print "[%d,%d,%d,%d] " % (lef,top,wid,hgt)
		r = value*(chcolor[0]/255.0)
		g = value*(chcolor[1]/255.0)
		b = value*(chcolor[2]/255.0)
		#print
		#print "color: (%d,%d,%d)" % (r,g,b)
		if box_on == True:
			pygame.draw.rect(vix.screen, (r, g, b), [lef,top,wid,hgt], 0)

	#print 'per: %s' % str(per),
	#print 'ticks: %s' % str(vix.ticks_at_per(per)), 
	#print 'pos: %d' % vix.get_pos(), 
	#print 'diff: %s' % str(vix.get_pos() - vix.ticks_at_per(per)),

	ard.send(modchannel)
	prevmodchannel = modchannel
	 
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	per += 1
	pygame.time.wait(100) 
