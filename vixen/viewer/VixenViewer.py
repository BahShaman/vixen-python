#PyGameChannelDisplay

class VixenViewer(Vixen):

    @staticmethod
    def __init__(vix,ard):
        pass

    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    GREEN    = (   0, 255,   0)
    RED      = ( 255,   0,   0)
    ORANGE   = ( 255, 153,   0)
    YELLOW   = ( 255, 255,   0)
    BLUE     = ( 0,   0,   255)

    COLOR = ORANGE

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


    print "%s channels, %s periods" % (str(vix.channels),str(vix.periods))

    seq = vix.sequence
    vix.play()

    #print [ord(x) for x in seq[0][0]]
    done = False
    while not done:
        # --- Main event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # If user clicked close
                done = True
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
                    pass
                    #offset = 0 
        
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
        
        for ch in range(vix.channels):
            #print ch
            #value = ord(seq[ch][per])
            value = vix.value(ch,per)
            print '{:3d}'.format(value),
            box_on = False
            if value > 1:
                box_on = True
            lef = box_off + ch*(box_gap + box_width)
            top = box_off
            wid = box_width
            hgt = box_width
            #print "[%d,%d,%d,%d] " % (lef,top,wid,hgt)
            r = value*(COLOR[0]/255.0)
            g = value*(COLOR[1]/255.0)
            b = value*(COLOR[2]/255.0)
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
        
        # --- Attempt to sync to music	
        vix.pos_syncwait(per+1,offset)
            #print pygame.mixer.music.get_pos(), ((per+1) * millis + offset)
            #print loop_ticks, pygame.time.get_ticks()
        
    
        # --- Go ahead and update the screen with what we've drawn.
        #print vix.period_arr(per),
        ard.send(vix.period_arr(per))
        pygame.display.flip()
        per += 1
 
