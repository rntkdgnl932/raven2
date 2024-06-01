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

    from function_game import imgs_set_, drag_pos, text_check_get, imgs_set_for, drag_pos_click, click_pos_2
    from tuto_raven2 import way_point_click, tuto_start
    from action_raven2 import move_check, menu_open, go_maul, juljun_check, juljun_on, juljun_off, bag_open
    from clean_screen_raven2 import clean_screen
    from potion_raven2 import potion_buy, potion_check
    from chango_raven2 import chango_in
    from dungeon_raven2 import dungeon_in, dungeon_check
    from jadong_raven2 import jadong_in
    from gyobum_raven2 import gyobum_check, gyobum_get, gyobum_start
    from event_allget import event_allget_check, event_allget_start
    from event_get import event_get_check, event_get_start
    from get_item import get_post, get_upjuk, get_item_start
    from steegma import steegma_start
    from boonhae_collection import collection_start, boonhae_start




    print("test")

    cla = "four"

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

    # click_pos_2(30, 880, cla)
    #
    # for c in range(7):
    #     full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_cannot.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(350, 100, 520, 160, cla, img, 0.8)
    #     if imgs_ is not None and imgs_ != False:
    #         print("juljun_cannot..", imgs_)
    #         break
    #     time.sleep(0.1)

    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\box_jangsingoo.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(600, 75, 900, 850, "two", img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("box_ganhwasuk", imgs_)
    else:
        print("아노ㄴㅇ")

    #
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\bag_jabhwa.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(880, 230, 960, 330, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("bag_jabhwa", imgs_)
    #
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\devil_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(600, 75, 900, 850, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("devil_1", imgs_)
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\devil_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(600, 75, 900, 850, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("devil_2", imgs_)
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\devil_3.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(600, 75, 900, 850, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("devil_3", imgs_)
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\sung_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(600, 75, 900, 850, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("sung_1", imgs_)
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\sung_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(600, 75, 900, 850, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("sung_2", imgs_)


    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\fourteen\\checked_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(240, 460, 870, 700, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("checked_2", imgs_)
    #
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\point_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(240, 440, 880, 490, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("point_1", imgs_)
    #
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked_top.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(730, 300, 860, 420, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("checked_top", imgs_)

    # folder_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\get_title"
    # file_list = os.listdir(folder_path)
    # file_count = len(file_list)
    # # print(file_count)
    #
    # for i in range(file_count):
    #
    #     pic_num = i + 1
    #
    #     full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\get_title\\" + str(pic_num) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(220, 320, 800, 400, cla, img, 0.8)
    #     if imgs_ is not None and imgs_ != False:
    #         print("pic_num", pic_num)
    #         break

    # # 지역 도감 체크 부분 파악
    # # x + 90 클릭
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\region_checked_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_for(300, 940, 750, 1020, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("region_checked", imgs_)
    #     last = len(imgs_)
    #     print("region_checked[last - 1]", imgs_[last - 1])

    # # 바깥 부분 클릭
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\out_point_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(50, 260, 100, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("out_point_1", imgs_)
    #
    # # 몬스터 도감 소제목 클릭
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(50, 70, 600, 105, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("gyobum_point_1", imgs_)
    #
    # # 몬스터 도감 자세한 부분 클릭
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_for(50, 130, 210, 700, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("gyobum_point_2", imgs_)
    #     last = len(imgs_)
    #     print("gyobum_point_2[last - 1]", imgs_[last - 1])

    # # 몬스터 도감 마지막 포인트 클릭
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_3.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(220, 180, 900, 1000, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("gyobum_point_3", imgs_)
    #
    # # 몬스터 도감 분석 클릭
    # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\monster_boonsuk.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(500, 500, 800, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("monster_boonsuk", imgs_)

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