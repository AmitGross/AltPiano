
try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass
from main_window_module import main_window
from tutorial_a_module import main_tutorial_window
from play_main_module import play_func
from hard_main_module import main_hard_window
while True:
    a=main_window()

    if a=="play":
        b=play_func()
    if a=="tutorial":
        c="tutorial"
        while c=="tutorial":

            b=main_tutorial_window()

            if b=="easy":
                pass
                #c=main_easy_window()
            if b=="hard":
                c=main_hard_window()
            if b ==0:
                c=None