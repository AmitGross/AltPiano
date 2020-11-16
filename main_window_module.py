import time

import pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)



def wait(t):
    tick=time.time()
    run=0
    while run<t:
        tock=time.time()
        run=tock-tick



def main_window():
    screen = pygame.display.set_mode([500,600])


    while True:
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,0,0),(48,50,400,200),2)
        play_text=myfont.render("play", True, (255,255,255))
        screen.blit(play_text,(170,50))



        pygame.draw.rect(screen,(255,0,0),(48,300,400,200),2)
        tutorial_text=myfont.render("Tutorial", True, (255,255,255))
        screen.blit(tutorial_text,(60,300))




        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        show_pos = str("( " + str(mouse_x) + " , " + str(mouse_y) + " )")

        pygame.display.flip()
        chosen_rect_play=pygame.draw.rect(screen,(255,255,0),(48,50,400,200),10)
        chosen_rect_tutorial = pygame.draw.rect(screen, (255, 255, 0), (48, 300, 400, 200), 10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:


                if 448>mouse_x>48:
                    if 250>mouse_y>50:
                        pygame.display.update(chosen_rect_play)

                        wait(0.25)

                        return ("play")
                if 448 > mouse_x > 48:
                    if 500> mouse_y >300:
                        pygame.display.update(chosen_rect_tutorial)
                        wait(0.25)
                        return ("tutorial")
