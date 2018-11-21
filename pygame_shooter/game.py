# 1. Include pygame
# We needed pip to get this for us because Python doesn't ship with it 
import pygame
from Hero import Hero
from BadGuy import BadGuy
# 2. Initialize Pygame.
# Why do we need to do this? Because they told us to.
pygame.init()

# 3. Make a screen with a size. Thie size MUST be a tuple
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
# set the title of the window that opens...
pygame.display.set_caption("HawkEye")

theHero = Hero()
bad_guy = BadGuy()

# ===============VARIABLES FOR OUR GAME===========================
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('arrow.png')
# heroLoc = {
#     'x' : 0,
#     'y' : 0
# }

#================MAIN GAME LOOP==============================
game_on = True
# The loop will run as long as our bool is True
while game_on: #short hand for game_on == True
    # We are in the game loop from here on out!
    # 5. Listen for events and quit if the user clicks the X
    #============EVENT CHECKER=================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # THE USER CLICKED THE RED DOT!
            #These aren't the droids were lookin for. quit
            game_on = False
        elif event.type == pygame.KEYDOWN:
            print (event.key)
            if event.key == 275:
                # The user pressed the right arrow! move our dude right
                # heroLoc['x'] += 10
                # theHero.x += 10
                theHero.shouldMove('right')
            elif event.key == 276: #Left Arrow
                theHero.shouldMove('left')
            if event.key == 273: # Up Arrow
                theHero.shouldMove('up')
            elif event.key == 274: # Down Arrow
                theHero.shouldMove('down')

        elif event.type == pygame.KEYUP: # The user RELEASED a key
            print (event.key)
            if event.key == 275: #Up Arrow
                theHero.shouldMove('right',False)
            elif event.key == 276: #Left Arrow
                theHero.shouldMove('left',False)
            if event.key == 273: # Up Arrow
                theHero.shouldMove('up',False)
            elif event.key == 274: # Down Arrow
                theHero.shouldMove('down',False)   
    #=================DRAW STUFF===============================        
    # We use blit to draw on the screen. blit = block image transfer
    # blit is a method, that takes 2 arg:
    # 1. What to draw
    # 2. Where to draw it
    # in the docs... SURFACE = our "pygame_screen"
    pygame_screen.blit(background_image,[0,0])
    theHero.draw_me()
    bad_guy.update_me(theHero)
    pygame_screen.blit(hero_image,[theHero.x,theHero.y])
    pygame_screen.blit(monster_image, [bad_guy.x, bad_guy.y])
   
    pygame.display.flip()
