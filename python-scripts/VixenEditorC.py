#PyGameChannelDisplay
import pygame
import os
import time
from vixen import Vixen

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
ORANGE   = ( 255, 153,   0)
YELLOW   = ( 255, 255,   0)
BLUE     = ( 0,   0,   255)

COLOR = ORANGE

vix = Vixen()
vixfilename = "C:\\Users\\BOSCIA\\Portable\\Vixen 2.1.1.0\\Sequences\\Arduino6ChannelThisIsHolloweenMain.vix"
#vixfilename = 'C:\Users\BOSCIA\Portable\Vixen 2.1.1.0\Sequences\PythonDecodeSample2.vix'
#vixfilename = 'C:\Users\BOSCIA\Portable\Vixen 2.1.1.0\Sequences\Arduino6ChannelTechNewsToday.vix'
#vixfilename = 'C:\Users\BOSCIA\Portable\Vixen 2.1.1.0\Sequences\Arduino8ChannelPatternsSample.vix'
#vixfilename = 'C:\Users\BOSCIA\Portable\Vixen 2.1.1.0\Sequences\Arduino8ChannelChristmasLinusAndLucy.vix'

musfile = 'C:/Users/BOSCIA/Documents/Projects/VixenDecode/03 - This Is Halloween.ogg'
#musfile = 'C:\Users\BOSCIA\Portable\Vixen 2.1.1.0\Audio\tnt0858.mp3'
#vixfilename = "./VixenFiles/Sequences/Arduino6ChannelThisIsHolloweenMain.vix"
#vixfilename = "./VixenFiles/Sequences/Arduino6ChannelThisIsHolloweenMain.vix"
#musfile = '03 - This Is Halloween.ogg'


#vixfilename = "C:\\Users\\BOSCIA\\Portable\\Vixen 2.1.1.0\\Sequences\\Arduino8ChannelChristmasLinusAndLucy.vix"
#musfile = 'C:\\Users\\BOSCIA\\Portable\\Vixen 2.1.1.0\\Audio\\04-A Charlie Brown Christmas-Linus and Lucy.mp3'


vix.loadfile(vixfilename)
vix.channels = 6
vix.processdata(vix.event_values,vix.channels)
#musfile = "C:\\Users\\BOSCIA\\Portable\\Vixen 2.1.1.0\\Audio\\" + vix.musicfilename
vix.loadmusic(musfile)
channels = vix.channels

box_width = 100
box_gap   = 20
box_off   = 50
per = 0

pygame.font.init()
mfont = pygame.font.SysFont(None, 25)	

#Opening and setting the window size
size = (box_off*2+(vix.channels*(box_gap+box_width)), box_off*2+box_width)
vix.set_screen(size)
pygame.display.set_caption(vix.title)
clock = pygame.time.Clock()
offset = 0
modchannel = [-1,-1,-1,-1,-1,-1,-1,-1]
edits = [x for x in range(0,vix.periods)]
for x in edits:
	edits[x] = [-1,-1,-1,-1,-1,-1,-1,-1]

print "%s channels, %s periods" % (str(vix.channels),str(vix.periods))

seq = vix.sequence
vix.play()

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
				modchannel[0] = -1
			if event.key == pygame.K_w:
				modchannel[1] = -1
			if event.key == pygame.K_e:
				modchannel[2] = -1
			if event.key == pygame.K_r:
				modchannel[3] = -1
			if event.key == pygame.K_u:
				modchannel[4] = -1
			if event.key == pygame.K_i:
				modchannel[5] = -1
			if event.key == pygame.K_o:
				modchannel[6] = -1
			if event.key == pygame.K_p:
				modchannel[7] = -1
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_ESCAPE:
				done = True 
			if event.key == pygame.K_UP:
				pass
				#offset += 100 
			if event.key == pygame.K_DOWN: 
				pass
				#offset -= 100 
			if event.key == pygame.K_LEFT: 
				per = 0
				pygame.mixer.music.stop()
				pygame.mixer.music.play()
				print pygame.mixer.music.get_pos()
				#continue
				#offset = 0 
			if event.key == pygame.K_SPACE: 
				print "PAUSE",
				if pause == True:
					print "setting to true"
					pause = False
				else:
					pause = True
					print "[%s]" % (pause),
			"""channel letters"""
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
	if per >= vix.periods:
		print "Done"
		pygame.time.wait(2000)
		done = True
		break

	# --- Game logic should go here
	print '%s:' % str(per),

	# --- Drawing code should go here
 
	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	vix.screen.fill(BLACK)
	label = mfont.render(vix.title + " [" +  vix.period_str(per) + "]"  , True, [x*.5 for x in COLOR])
	vix.screen.blit(label, (box_off, box_off+box_width+box_gap/2))
	print edits[per],
	#edits[per][0] = 50
	for ch in range(vix.channels):
		#print ch
		#value = ord(seq[ch][per])
		if modchannel[ch] >= 0:
			value = modchannel[ch]
			#vix.set_value(ch,per,value)
			edits[per][ch] = value
			chcolor = WHITE
		elif edits[per][ch] >= 0:
			value = edits[per][ch]
			chcolor = RED
		else:
			value = vix.value(ch,per)
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
	print 'ticks: %s' % str(vix.ticks_at_per(per)), 
	print 'pos: %d' % vix.get_pos(), 
	print 'diff: %s' % str(vix.get_pos() - vix.ticks_at_per(per)),

	#pygame.draw.rect(vix.screen, BLUE , [10,10,20,20], 1)
	#pygame.draw.rect(vix.screen, BLACK, [30,10,20,20], 1)
	#pygame.draw.rect(vix.screen, UNK  , [50,10,20,20], 1)
	#pygame.draw.rect(vix.screen, GREEN, [70,10,20,20], 1)
	
	print pygame.mixer.music.get_pos(),
	print vix.get_pos(),

	# --- Attempt to sync to music	
	vix.pos_syncwait(per+1,offset)
		#print pygame.mixer.music.get_pos(), ((per+1) * millis + offset)
		#print loop_ticks, pygame.time.get_ticks()
	
 
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	per += 1
 
