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

    from function_game import imgs_set_, drag_pos, text_check_get, imgs_set_for
    from tuto_raven2 import way_point_click, tuto_start
    from action_raven2 import move_check, menu_open, go_maul, juljun_check, juljun_on, juljun_off
    from clean_screen_raven2 import clean_screen
    from potion_raven2 import potion_buy, potion_check
    from chango_raven2 import chango_in
    from dungeon_raven2 import dungeon_in, dungeon_check
    from jadong_raven2 import jadong_in



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

    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\anymore_buy.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(460, 110, 650, 160, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("anymore_buy", imgs_)

    # text_check_get(280, 982, 288, 1000, cla)
    #
    # for i in range(10):
    #     full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\out_potion\\" + str(i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(280, 982, 288, 1000, cla, img, 0.8)
    #     if imgs_ is not None and imgs_ != False:
    #         print("num", i)
    #         break

    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\jadong\\jadong_click_btn_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(20, 70, 80, 570, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("jadong_click_btn_2", imgs_)

    # data = "일반_발바르_4"
    # dungeon_in(cla, data)

    # menu_open(cla)

    # result = text_check_get(440, 520, 550, 540, cla)
    # print("result", result)

    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\monitor\\join_out.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(350, 490, 570, 570, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("join_out", imgs_)
    #
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\confirm\\skip_confirm.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(350, 500, 700, 700, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("confirm : skip_confirm", imgs_)



    #     drag_pos(imgs_.x, imgs_.y + 30, imgs_.x, imgs_.y + 100, cla)