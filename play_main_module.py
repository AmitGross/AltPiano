
                    #a - pygame basis data
                    #b - lists and dict
                    #c - functions

                    #d - run
                        #d1 muscia
                        #d2 notes in scale

                    # a
import pygame
pygame.init()
pygame.font.init()
screena = pygame.display.set_mode([1500, 450])
white=(255,255,255)
black=(90,90,90)
grey=(80,80,110)
shady=(200,80,110)
shady_two=(255,255,0)
black_dark=(0,0,0)
myfont = pygame.font.SysFont('Comic Sans MS', 20)
notesfont = pygame.font.SysFont('Comic Sans MS', 38)
notesfont_two = pygame.font.SysFont('Comic Sans MS', 30)
background=pygame.image.load("Capturetwo.png")
red=(255,0,0)
soundC_two=pygame.mixer.Sound("C.wav")
#soundDb_two=pygame.mixer.Sound("Db.wav")
soundD_two=pygame.mixer.Sound("D.wav")
soundE_two=pygame.mixer.Sound("E.wav")
soundF_two=pygame.mixer.Sound("F.wav")
soundG_two=pygame.mixer.Sound("G.wav")
soundA_two=pygame.mixer.Sound("A.wav")
soundB_two=pygame.mixer.Sound("B.wav")

            #b

dict_of_colors={"C":white,"Db":black_dark,"D":white,"Eb":black_dark,"E":white,"F":black_dark,"Gb":white,"G":black_dark,"Ab":white,"A":black_dark,"Bb":white,"B":black_dark}


dict_notes_to_num={"C":0,"Db":1,"D":2,"Eb":3,"E":4, "F":5,"Gb":6,"G":7,"Ab":8,"A":9,"Bb":10,"B":11, "C_one":12,"Db_one":13,"D_one":14,"Eb_one":15,"E_one":16, "F_one":17,"Gb_one":18,"G_one":19,"Ab_one":20,"A_one":21,"Bb_one":22,"B_one":23, "C_three":24,"Db_three":25,"D_three":26,"Eb_three":27,"E_three":28, "F_three":29,"Gb_three":30,"G_three":31,"Ab_three":32,"A_three":33,"Bb_three":34,"B_three":35}

dic_num_to_notes={0: "C", 1: "Db" ,2:"D"  ,3: "Eb" ,4: "E" ,5: "F" ,6:"Gb"  ,7:"G"  ,8:"Ab"  ,9: "A" ,10:"Bb"  , 11:"B",12:"C",13:"Db",14:"D",15:"Eb",16:"E",17:"F",18:"Gb",19:"G",20:"Ab", 21:"A",22:"Bb",23:"B" }
scales_dict={"major":[0,2,4,5,7,9,11]}
major_scale=[0,2,4,5,7,9,11]
major_chord=[0,4,7]
loc_of_buttons_dic={"C":85 , "Db":185,"D":285,"Eb":385,"E":485,"F":585,"Gb":685,"G":785,"Ab":885,"A":985,"Bb":1085,"B":1185 }
dict_notes_pos={"C":[63,550,1032],"Db":[106,587,1074],"D":[150,631,1114],"Eb":[195,673,1157],"E":[224,714,1200], "F":[279,762,1240],"Gb":[318,801,1280],"G":[359,843,1325],"Ab":[394,873,1360],"A":[433,915,1396],"Bb":[472,952,1438],"B":[507,990,1479]}




                #c

def turn_button_to_glow():

    var=loc_of_buttons_dic.get(a.chosen_note)-40
    pygame.draw.rect(screena, shady_two, [var, 415, 100, 35], 3)

    text_C = notesfont_two.render("C", True, (white))
    screena.blit(text_C, (85, 410))
    text_Db = notesfont_two.render("Db", True, (black_dark))
    screena.blit(text_Db, (185, 410))

    text_D = notesfont_two.render("D", True, (white))
    screena.blit(text_D, (285, 410))

    text_Eb = notesfont_two.render("Eb", True, (black_dark))
    screena.blit(text_Eb, (385, 410))

    text_E = notesfont_two.render("E", True, (white))
    screena.blit(text_E, (485, 410))

    text_F = notesfont_two.render("F", True, (black_dark))
    screena.blit(text_F, (585, 410))

    text_Gb = notesfont_two.render("Gb", True, (white))
    screena.blit(text_Gb, (685, 410))

    text_G = notesfont_two.render("G", True, (black_dark))
    screena.blit(text_G, (785, 410))

    text_Ab = notesfont_two.render("Ab", True, (white))
    screena.blit(text_Ab, (885, 410))

    text_A = notesfont_two.render("A", True, (black_dark))
    screena.blit(text_A, (985, 410))

    text_Bb = notesfont_two.render("Bb", True, (white))
    screena.blit(text_Bb, (1085, 410))


    text_B = notesfont_two.render("B", True, (black_dark))
    screena.blit(text_B, (1185, 410))

    text_back = notesfont_two.render("Back", True, (black_dark))
    screena.blit(text_back, (1300, 410))





def draw_scale(note,scale):
    selected_note_value=dict_notes_to_num.get(note) #0
    selected_scale=scales_dict.get(scale) #major

    notes_in_scale=[] #new modified values of in maajor scale   0,           2,  4,  5,  7,  9,  11
    modified_notes=[]                                           #c,          d , e , f , g,  a,  b
    position_circles=[]                               #[  [63,550,1032],    []                          ]

    for position in selected_scale: #value , major

        var=position+selected_note_value #new modified value in maajor scale


        notes_in_scale.append(var)
        var_two=dic_num_to_notes.get(var)
        modified_notes.append(var_two)
    for modified_note in modified_notes:
        var_three=dict_notes_pos.get(modified_note)
        position_circles.append(var_three)
    i = 0
    v = 0
    class a_color():
        def __init__(self, color_of_a):
            self.current_color_of_a=color_of_a
            if color_of_a==white:
                self.current_color_of_b=black_dark
            else:
                self.current_color_of_b=white
    current_colors=a_color(dict_of_colors.get(a.chosen_note))
    texta = notesfont.render("a", True, (current_colors.current_color_of_a))
    textb = notesfont.render("b", True, (current_colors.current_color_of_b))
    for list_of_pos in position_circles:
        if i<3:
            for item in list_of_pos:
                #pygame.draw.circle(screena, (current_colors.current_color_of_a), (item, 16), 14, 1)
                var_loc = item - 5
                screena.blit(texta, (var_loc, -18))

        if i ==3:
            v+=1
        if v>0:
            for item in list_of_pos:
                #pygame.draw.circle(screena, (current_colors.current_color_of_b), (item, 16), 14, 1)
                var_loc = item - 5
                screena.blit(textb, (var_loc, -14))
        if v==4:
            i=0
            v=0
        i += 1

class chosen_note:
    def __init__(self):
        self.chosen_note="C"
a=chosen_note()



            #d
def play_func():
    screena = pygame.display.set_mode([1500, 450])
    while True:

        screena.fill(black)

        screena.blit(background, (30, 30))
        draw_scale(a.chosen_note, "major")

        turn_button_to_glow()



        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        show_pos = str("( " + str(mouse_x) + " , " + str(mouse_y) + " )")

        #textpos = notesfont.render(show_pos, True, (red))
        #screena.blit(textpos, (0, 0))
        pygame.display.flip()



        for event in pygame.event.get():
            print(event)
            if event.type==pygame.KEYDOWN:
                if event.key== 97:
                    soundC_two.play()
                if event.key== 115:
                    soundD_two.play()
                if event.key== 100:
                    soundE_two.play()

                if event.key == 102:
                    soundF_two.play()
                if event.key == 103:
                    soundG_two.play()
                if event.key == 104:
                    soundA_two.play()
                if event.key == 106:
                    soundB_two.play()


            # d1
            if mouse_y<410:
                if 45<mouse_x<527:
                    #print("octave_1")
                    if mouse_y<250:
                        #print("upper")
                        if 45 < mouse_x < 83:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("C_one")
                        if 83 < mouse_x < 128:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Db_one")
                        if 128 < mouse_x < 169:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("D_one")
                        if 169 < mouse_x < 210:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Eb_one")
                        if 210 < mouse_x < 251:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("E_one")
                        if 251 < mouse_x < 297:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("F_one")
                        if 297 < mouse_x < 335:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Gb_one")
                        if 335 < mouse_x < 373:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("G_one")
                        if 373 < mouse_x < 412:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Ab_one")
                        if 412 < mouse_x < 451:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("A_one")
                        if 451 < mouse_x < 490:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Bb_one")
                        if 490 < mouse_x < 528:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                               print("B_one")
                    else:
                        #print("lower")
                        if 45 < mouse_x < 112:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("C_one")
                        if 115 < mouse_x < 184:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("D_one")
                        if 184 < mouse_x < 251:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("E_one")
                        if 251 < mouse_x < 324:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("F_one")
                        if 324 < mouse_x < 394:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("G_one")
                        if 394 < mouse_x < 465:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("A_one")
                        if 465 < mouse_x < 528:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("B_one")

                if 527<mouse_x<1110:
                    #print("octave_2")
                    if mouse_y<250:
                        #print("upper")
                        if 529 < mouse_x < 569:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("C_two")
                                soundC_two.play()
                        if 569 < mouse_x < 610:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Db_two")
                                #soundDb_two.play()
                        if 610 < mouse_x < 651:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("D_two")
                                soundD_two.play()
                        if 651 < mouse_x < 694:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Eb_two")
                        if 694 < mouse_x < 735:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("E_two")
                                soundE_two.play()
                        if 735 < mouse_x < 779:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("F_two")
                                soundF_two.play()
                        if 779 < mouse_x < 816:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Gb_two")
                        if 816 < mouse_x < 855:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("G_two")
                                soundG_two.play()
                        if 855 < mouse_x < 895:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Ab_two")
                        if 895 < mouse_x < 934:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("A_two")
                                soundA_two.play()
                        if 934 < mouse_x < 972:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Bb_two")
                        if 972 < mouse_x < 1010:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("B_two")
                                soundB_two.play()
                    else:
                        #print("lower")
                        if 528 < mouse_x < 595:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("C_two")
                                soundC_two.play()
                        if 595 < mouse_x < 664:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("D_two")
                                soundD_two.play()
                        if 664 < mouse_x < 734:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("E_two")
                                soundE_two.play()
                        if 734 < mouse_x < 808:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("F_two")
                                soundF_two.play()
                        if 808 < mouse_x < 878:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("G_two")
                                soundG_two.play()
                        if 878 < mouse_x < 948:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("A_two")
                                soundA_two.play()
                        if 948 < mouse_x < 1008:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("B_two")
                                soundB_two.play()
                if 1110<mouse_x<1550:
                    #print("octave_3")
                    if mouse_y<250:
                        #print("upper")
                        if 1012 < mouse_x < 1052:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("C_three")
                        if 1052 < mouse_x < 1095:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Db_three")
                        if 1095 < mouse_x < 1134:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("D_three")
                        if 1134 < mouse_x < 1178:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Eb_three")
                        if 1178 < mouse_x < 1218:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("E_three")
                        if 1218 < mouse_x < 1261:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("F_three")
                        if 1261 < mouse_x < 1302:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Gb_three")
                        if 1302 < mouse_x < 1339:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("G_three")
                        if 1339 < mouse_x < 1377:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Ab_three")
                        if 1377 < mouse_x < 1417:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("A_three")
                        if 1417 < mouse_x < 1455:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("Bb_three")
                        if 1455 < mouse_x < 1498:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print("B_three")
                    else:
                        #print("lower")
                        if 1011 < mouse_x < 1071:
                            print("C_three")
                        if 1071 < mouse_x < 1147:
                            print("D_three")
                        if 1147 < mouse_x < 1218:
                            print("E_three")
                        if 1218 < mouse_x < 1288:
                            print("F_three")
                        if 1288 < mouse_x < 1359:
                            print("G_three")
                        if 1359 < mouse_x < 1429:
                            print("A_three")
                        if 1429 < mouse_x < 1496:
                            print("B_three")

























        # d2
        if mouse_y>410:
            #print(mouse_x)
            if 146>mouse_x>50:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="C"
            if 246>mouse_x>150:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="Db"

            if 346>mouse_x>250:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="D"
            if 446>mouse_x>350:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="Eb"
            if 546>mouse_x>450:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="E"
            if 646>mouse_x>550:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="F"
            if 746>mouse_x>650:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="Gb"

            if 846>mouse_x>750:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="G"
            if 946>mouse_x>850:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="Ab"
            if 1046>mouse_x>950:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="A"
            if 1146>mouse_x>1050:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="Bb"
            if 1246>mouse_x>1150:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a.chosen_note="B"
            if mouse_x>1300:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return



        if event.type == pygame.MOUSEMOTION:
            pass







#12,63