import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, drag_pos, text_check_get
    from tuto_raven2 import way_point_click, tuto_start
    from action_raven2 import move_check, menu_open
    from clean_screen_raven2 import clean_screen


    print("test")
    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    # tuto_start(cla)

    # tuto_start(cla)

    menu_open(cla)

    # result = text_check_get(440, 520, 550, 540, cla)
    # print("result", result)

    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\way\\drag_down_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(10, 30, 945, 1025, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("drag_down_1", imgs_)
    #     drag_pos(imgs_.x, imgs_.y + 30, imgs_.x, imgs_.y + 100, cla)