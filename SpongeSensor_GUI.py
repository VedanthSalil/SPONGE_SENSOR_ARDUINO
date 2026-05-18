import pygame
import sys
import storage 
import importlib


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Pygame Window")


BACKGROUND_COLOR = (30, 30, 40)  


clock = pygame.time.Clock()
FPS = 1000 


running = True
while running:
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   


    screen.fill(BACKGROUND_COLOR)

    importlib.reload(storage)
        
    SpongeSensor_value = storage.value
    print(SpongeSensor_value)


    #text 

    font_path = "OpenSans-VariableFont_wdth,wght.ttf"
    my_font = pygame.font.Font(font_path, 30) #50 is the size
    text_sponge = my_font.render("Hello, Pygame!", True, (255,0,0)) #true for  'Antialiasing'
    label_surface = my_font.render("Sponge sensor value ->", True, (255, 255, 255))
    screen.blit(label_surface, (50, 200))
    value_surface = my_font.render(str(SpongeSensor_value), True, (0, 225, 225))
    screen.blit(value_surface, (50, 270))
    #####################################################################
    # decoration border box for the bar things 
    pygame.draw.rect(screen, (255,255,255), (490,90,10,410)) #x_pos , y_pos , x_length , y_length
    pygame.draw.rect(screen, (255,255,255), (750,90,10,410))
    pygame.draw.rect(screen, (255,255,255), (500,80,250,10))
    pygame.draw.rect(screen, (255,255,255), (500,500,250,10))
   #red bar 1
    if SpongeSensor_value >= 3 and SpongeSensor_value<10:
         bar1= pygame.draw.rect(screen, (225,0,0), (500, 450,250,50))
         bar2= pygame.draw.rect(screen,(100,0,0),(500,390,250,50))
         bar3 = pygame.draw.rect(screen,(110,90,0),(500,330,250,50))
         bar4 = pygame.draw.rect(screen,(110,90,0),(500,270,250,50))
         
         bar5 = pygame.draw.rect(screen,(0,100,0),(500,210,250,50))
         bar6 = pygame.draw.rect(screen,(0,100,0),(500,150,250,50))
         bar7 = pygame.draw.rect(screen,(0,100,0),(500,90,250,50))
    #red bar 2
    elif SpongeSensor_value >= 10  and SpongeSensor_value <15 :
        bar1= pygame.draw.rect(screen, (225,0,0), (500, 450,250,50))
        bar2= pygame.draw.rect(screen,(225,0,0),(500,390,250,50))
        bar3 = pygame.draw.rect(screen,(110,90,0),(500,330,250,50))
        bar4 = pygame.draw.rect(screen,(110,90,0),(500,270,250,50))
         
        bar5 = pygame.draw.rect(screen,(0,100,0),(500,210,250,50))
        bar6 = pygame.draw.rect(screen,(0,100,0),(500,150,250,50))
        bar7 = pygame.draw.rect(screen,(0,100,0),(500,90,250,50))
        #yellow1
    elif SpongeSensor_value >= 15 and SpongeSensor_value <20 :
        bar1= pygame.draw.rect(screen, (225,0,0), (500, 450,250,50))
        bar2= pygame.draw.rect(screen,(225,0,0),(500,390,250,50))
        bar3 = pygame.draw.rect(screen,(225,225,0),(500,330,250,50))
        bar4 = pygame.draw.rect(screen,(110,90,0),(500,270,250,50))
         
        bar5 = pygame.draw.rect(screen,(0,100,0),(500,210,250,50))
        bar6 = pygame.draw.rect(screen,(0,100,0),(500,150,250,50))
        bar7 = pygame.draw.rect(screen,(0,100,0),(500,90,250,50))
#yellow2
    elif SpongeSensor_value >= 20 and SpongeSensor_value <25:
        bar1= pygame.draw.rect(screen, (225,0,0), (500, 450,250,50))
        bar2= pygame.draw.rect(screen,(225,0,0),(500,390,250,50))
        bar3 = pygame.draw.rect(screen,(225,225,0),(500,330,250,50))
        bar4 = pygame.draw.rect(screen,(225,225,0),(500,270,250,50))
         
        bar5 = pygame.draw.rect(screen,(0,100,0),(500,210,250,50))
        bar6 = pygame.draw.rect(screen,(0,100,0),(500,150,250,50))
        bar7 = pygame.draw.rect(screen,(0,100,0),(500,90,250,50))

    #green1

    elif SpongeSensor_value >=25 and SpongeSensor_value <30:
        bar1= pygame.draw.rect(screen, (225,0,0), (500, 450,250,50))
        bar2= pygame.draw.rect(screen,(225,0,0),(500,390,250,50))
        bar3 = pygame.draw.rect(screen,(225,225,0),(500,330,250,50))
        bar4 = pygame.draw.rect(screen,(225,225,0),(500,270,250,50))
         
        bar5 = pygame.draw.rect(screen,(0,225,0),(500,210,250,50))
        bar6 = pygame.draw.rect(screen,(0,100,0),(500,150,250,50))
        bar7 = pygame.draw.rect(screen,(0,100,0),(500,90,250,50))
    elif SpongeSensor_value >=30 and  SpongeSensor_value<35: #green2
        bar1= pygame.draw.rect(screen, (225,0,0), (500, 450,250,50))
        bar2= pygame.draw.rect(screen,(225,0,0),(500,390,250,50))
        bar3 = pygame.draw.rect(screen,(225,225,0),(500,330,250,50))
        bar4 = pygame.draw.rect(screen,(225,225,0),(500,270,250,50))
         
        bar5 = pygame.draw.rect(screen,(0,225,0),(500,210,250,50))
        bar6 = pygame.draw.rect(screen,(0,225,0),(500,150,250,50))
        bar7 = pygame.draw.rect(screen,(0,100,0),(500,90,250,50))
    elif SpongeSensor_value >= 35:
        bar1= pygame.draw.rect(screen, (225,0,0), (500, 450,250,50))
        bar2= pygame.draw.rect(screen,(225,0,0),(500,390,250,50))
        bar3 = pygame.draw.rect(screen,(225,225,0),(500,330,250,50))
        bar4 = pygame.draw.rect(screen,(225,225,0),(500,270,250,50))
         
        bar5 = pygame.draw.rect(screen,(0,225,0),(500,210,250,50))
        bar6 = pygame.draw.rect(screen,(0,225,0),(500,150,250,50))
        bar7 = pygame.draw.rect(screen,(0,225,0),(500,90,250,50))
    else :
        bar1= pygame.draw.rect(screen, (100,0,0), (500, 450,250,50))
        bar2= pygame.draw.rect(screen,(100,0,0),(500,390,250,50))
        bar3 = pygame.draw.rect(screen,(110,90,0),(500,330,250,50))
        bar4 = pygame.draw.rect(screen,(110,90,0),(500,270,250,50))
         
        bar5 = pygame.draw.rect(screen,(0,100,0),(500,210,250,50))
        bar6 = pygame.draw.rect(screen,(0,100,0),(500,150,250,50))
        bar7 = pygame.draw.rect(screen,(0,100,0),(500,90,250,50))

    
 
   
    
 
    pygame.display.flip()

   
    clock.tick(FPS)



pygame.quit()
sys.exit()