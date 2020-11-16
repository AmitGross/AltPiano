import time

import pygame

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
myfont_small = pygame.font.SysFont('Comic Sans MS', 13)

screen = pygame.display.set_mode([500, 500])


def main_hard_window():
    def glow(rect):
        tick = time.time()
        run = 0
        while run < 0.25:
            tock = time.time()
            run = tock - tick
            pygame.display.update(rect)
    def wait():
        tick = time.time()
        run = 0
        while run < 0.25:
            tock = time.time()
            run = tock - tick



    def value_button(mousex,mousey,current_value,s):

        chk_next = pygame.Rect(335,545,130,40).collidepoint(mousex, mousey)
        chk_back = pygame.Rect(35, 545, 130, 40).collidepoint(mousex, mousey)
        if current_value>0:
            if chk_back==1:
                to_return=current_value-1
                s=0
                t=(to_return,s,True)
                vrect=pygame.draw.rect(screen,(255,255,0),(35, 545, 130, 40),2)
                glow(vrect)
                return t
        if chk_next==1:
            s=0
            to_return = current_value + 1
            t=(to_return,s,True)

            vrect = pygame.draw.rect(screen, (255, 255, 0), (335,545,130,40), 2)
            glow(vrect)

            return t

        else:
            t=(current_value,s,False)
            return t


    red=(255,0,0)
    green=(0,255,100)
    blue=(0,0,255)
    yellow=(255,255,0)

    def text( text_str,text_font,xpos,ypos,color):


        vtext=text_font.render(text_str,True, color )
        screen.blit(vtext,(xpos,ypos) )

    def glow_text(text_var,xpos,ypos):
        text(text_var, myfont, xpos,ypos, yellow)
        pygame.display.flip()
        wait()

    def erase(xpos,ypos,xleng,yleng):
        screen.fill((0,0,0),rect=(xpos,ypos,xleng,yleng))

    def renew_screen(lesson):
        screen.fill((0, 0, 0))
        background = pygame.image.load("short_keyboard.png")
        screen.blit(background, (30, 30))
        text("next lesson",myfont,350,550,green)
        text("last lesson", myfont,50, 550,green)
        lesson_text=str("lesson"+str(lesson))
        text(lesson_text,myfont,100,10,red)
        pygame.draw.rect(screen,(255,0,0),(335,545,130,40),1)
        pygame.draw.rect(screen, (255, 0, 0), (35, 545, 130, 40), 1)
        chosen_rect_back = pygame.draw.rect(screen, (255, 255, 0), (0, 0, 30, 30), 5)
        text("back", myfont, 0, 0, red)

    list_of_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    list_of_pos = [40, 68, 100, 145, 175, 210, 240, 275, 300, 330, 360, 385]
    major_scale=[0,2,4,5,7,9,11]
    letters_list_str="aaabbbb"
    i = 0
    color = (0, 0, 0)
    s = 0
    renew_screen("1")
    pygame.display.flip()
    while True:

        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        show_pos = str("( " + str(mouse_x) + " , " + str(mouse_y) + " )")



        for event in pygame.event.get():
            if 30 > mouse_x > 0:
                if 30 > mouse_y > 0:
                    return 0
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                t = value_button(mouse_x, mouse_y, i,s)
                i=t[0]
                s=t[1]



                if i==0:


                    if s==0:
                        renew_screen(1)
                        text("click anywhere to start tutorial", myfont, 150, 450,red)

                        pygame.display.flip()

                    if s==1:
                        glow_text("click anywhere to start tutorial",150,450)
                        erase(150,450,300,50)
                        text("click anywhere to see all notes in an octave", myfont, 50, 450,red)
                        pygame.display.flip()
                    if 14>s>1:

                        d=s-2
                        var = myfont.render(list_of_num[d], True, (0, 255, 255))
                        screen.blit(var, (list_of_pos[d], 100))
                        pygame.display.flip()


                    if s>13:
                        erase(50,450,400,50)
                        text("very good, continue to the next lesson", myfont, 50,450,red)
                        pygame.display.flip()
                        wait()
                        glow_text("very good, continue to the next lesson", 50 ,450)
                        wait()

                    s+=1
                if i==1:
                    if s==0 :
                        renew_screen(2)
                        erase(10, 450, 450, 50)
                        text("click anywhere to start the second lesson", myfont, 10, 450,red)
                        pygame.display.flip()
                    if s==1:
                        erase(10, 450, 450, 50)
                        text("instead of counting by numbers, we can also count by color", myfont_small, 10, 450,red)
                        pygame.display.flip()
                    if s==2:

                        erase(10, 450, 450, 50)
                        text("we will count in refrenece to the note we choose", myfont, 10, 450,red)
                        pygame.display.flip()
                    if s==3:
                        erase(10, 450, 450, 50)
                        text("for example if we choose the note C", myfont, 10, 450,red)
                        pygame.display.flip()
                    if s==4:
                        erase(10, 450, 450, 50)
                        text("for example if we choose the note C", myfont, 10, 450,red)
                        text("C", myfont, 35, 200,red)
                        pygame.display.flip()
                    if s==5:

                        erase(10, 450, 400, 50)
                        text("C is white, and therefore we will count in refrence to its color", myfont_small, 10, 450,red)
                        pygame.display.flip()
                    if s==5:
                        erase(10, 450, 400, 50)
                        text("we will call our color of refrence a, and the second color b", myfont_small, 10, 450,red)
                        pygame.display.flip()
                    if s==6:
                        erase(10, 450, 400, 50)
                        text("click to see how to refer to the octave by color ", myfont_small, 10, 450,red)
                        pygame.display.flip()
                        var_letter="b"
                    if 19>s>6:
                        if var_letter=="b":
                            var_letter="a"
                        else:
                            var_letter="b"
                        var_num=s-7

                        text(list_of_num[var_num],myfont,list_of_pos[var_num],55,red)
                        text(var_letter, myfont, list_of_pos[var_num], 75,red)

                        pygame.display.flip()
                    if s==19:
                        erase(10, 450, 400, 50)
                        text("great, continue to next lesson ", myfont_small, 10, 450,red)
                        pygame.display.flip()



                    s+=1

                if i == 3:
                    renew_screen(4)
                    if s == 0:
                        erase(10, 450, 450, 50)
                        text("on maintneance", myfont, 10, 450,red)
                        pygame.display.flip()











                if i==2:

                    if s==0:
                        renew_screen(3)
                        text("click anywhere to start third lesson", myfont, 50, 450,red)
                        pygame.display.flip()

                    if s==1:
                        erase(10, 450, 400, 50)
                        text("scale means we will play just part of the 12 notes we counted in the last lesson", myfont_small, 20, 450,red)
                        pygame.display.flip()
                    if s==2:
                        erase(0, 450, 500, 50)
                        text("click anywhere to see which notes are in major scale",myfont, 10, 450,red)
                        pygame.display.flip()

                    if s==3:


                        var_count=0
                        var_letter = "b"
                        for item in list_of_num:
                            var=myfont.render(item,True, (50,205,255))
                            screen.blit(var, (list_of_pos[var_count],45))


                            if var_letter=="b":
                                var_letter="a"
                            else:
                                var_letter="b"


                            text(var_letter, myfont, list_of_pos[var_count], 30,red)
                            var_count += 1




                        pygame.display.flip()
                    if 11>s>3:
                        erase(0, 450, 500, 50)
                        text("click anywhere to see count major scale notes", myfont, 10, 450,red)
                        current_var=s-4
                        major_scale_value=major_scale[current_var]
                        pygame.draw.circle(screen,(255,0,0),(int(list_of_pos[major_scale_value]+7),85),10)

                        pygame.display.flip()
                    if s==11:
                        erase(0, 450, 500, 50)
                        text("u can see only 7 out of 12 notes are in major scale", myfont, 10, 450,red)
                        pygame.display.flip()
                    if s==12:
                        erase(0, 450, 500, 50)
                        text("scales have constant gaps in thier notes", myfont, 10, 450,red)
                        pygame.display.flip()
                    if s==13:
                        text("and u may see major scale consist of:", myfont, 10, 500,red)

                        pygame.display.flip()
                        varx=40

                    if 21>s>13:
                        erase(0, 450, 500, 80)
                        text("and u may see major scale consist of:", myfont, 10, 380,red)
                        text("the numbers 1,3,5,6,8,10,12", myfont, 10, 410,red)
                        text("and also the letters aaabbbb", myfont, 10, 450,red)
                        standards=s-14
                        #print(" stand is {}".format(standards))
                        major_scale_value = major_scale[standards]


                        pygame.draw.rect(screen,(0,255,255),(list_of_pos[major_scale_value],30,20,80),2 )
                        text(letters_list_str[standards],myfont,varx,300 ,(110,255,0))
                        pygame.display.flip()
                        varx+=10

                    s += 1









"""

    def change_var_button(rectx,recty,rect_x_pos,rect_y_pos, text,text_font,text_x,text_y, value_to_return, mousex,mousey):
        vrect = (rectx, recty,rect_x_pos,rect_y_pos)
        glowrect=pygame.draw.rect(screen,(255,255,0),(vrect),1)
        vtext=text_font.render(text,True, (255,0,0) )
        screen.blit(vtext,(text_x,text_y) )

        chk = pygame.Rect(glowrect).collidepoint(mousex, mousey)
        print(chk)
        print(mouse_x)
        if chk==1:
            glow(vrect)
            pygame.display.flip()
            return value_to_return

"""



