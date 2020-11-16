
import time

import pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)

def main_tutorial_window():
    screen = pygame.display.set_mode([500,600])

    def wait(t):
        tick = time.time()
        run = 0
        while run < t:
            tock = time.time()
            run = tock - tick

    while True:
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,0,0),(48,50,400,200),2)
        easy_text=myfont.render("easy", True, (255,255,255))
        screen.blit(easy_text,(170,50))



        pygame.draw.rect(screen,(255,0,0),(48,300,400,200),2)
        hard_text=myfont.render("hard", True, (255,255,255))
        screen.blit(hard_text,(170,300))

        pygame.draw.rect(screen,(255,0,0),(0,00,30,30),2)




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

                        return ("easy")
                if 448 > mouse_x > 48:
                    if 500> mouse_y >300:
                        pygame.display.update(chosen_rect_tutorial)
                        wait(0.25)
                        return ("hard")
                if 30 > mouse_x > 0:
                    if 30> mouse_y >0:

                        return 0
