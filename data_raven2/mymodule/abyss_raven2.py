import time
# import os
import sys
from PyQt5.QtTest import *


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def abyss_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("abyss_start")
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_x.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(630, 30, 780, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("close_btn_x..", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0



def abyss_sangjum(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import menu_open, go_maul

    try:
        print("abyss_sangjum")

        # 마을에서만 입장 가능
        go_maul(cla)

        result_data = data.split("_")
        # 어비스_1

        abyss_maul_in = False
        abyss_maul_in_count = 0
        while abyss_maul_in is False:
            abyss_maul_in_count += 1
            if abyss_maul_in_count > 7:
                abyss_maul_in = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\abyss_maul.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(55, 105, 120, 170, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("abyss_maul..", imgs_)
                abyss_maul_in = True

                abyss_sangjum_gyohwan(cla, data)

            else:
                menu_open(cla)

                for i in range(10):

                    maul_in = False

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\title_abyss.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 120, 170, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("title_abyss", imgs_)

                        if result_data[1] == "1":
                            y_reg = 120
                        elif result_data[1] == "2":
                            y_reg = 240

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\abyss_maul_" + str(result_data[1]) + "_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(750, 980, 840, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("abyss", result_data[1], imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)

                            for o in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\already_dun_in.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(375, 100, 600, 160, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("already_dun_in", imgs_)
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\abyss_maul.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(55, 105, 120, 170, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        maul_in = True
                                        break
                                    else:

                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\abyss_maul_" + str(
                                            result_data[1]) + "_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(750, 980, 840, 1020, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("abyss", result_data[1], imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)


                        else:
                            click_pos_2(100, y_reg, cla)
                        time.sleep(0.5)

                        if maul_in == True:
                            break

                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\menu_abyss_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(875, 315, 955, 395, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_abyss_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
            QTest.qWait(500)



    except Exception as e:
        print(e)
        return 0


def abyss_sangjum_gyohwan(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import move_check
    from schedule import myQuest_play_add

    try:
        print("abyss_sangjum_gyohwan")

        result_data = data.split("_")
        # 어비스_1

        abyss_maul_in = False
        abyss_maul_in_count = 0
        while abyss_maul_in is False:
            abyss_maul_in_count += 1
            if abyss_maul_in_count > 7:
                abyss_maul_in = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\title_abyss_gyohwan.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 180, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title_abyss_gyohwan", imgs_)
                abyss_maul_in = True

                added = False

                # 첫번째
                if result_data[1] == "1":
                    # 저항물약

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\sold_out.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 135, 450, 165, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("sold_out", imgs_)
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\character_level_low.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 135, 450, 165, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("character_level_low", imgs_)
                            # add
                            myQuest_play_add(cla, data)
                            added = True
                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    print("anymore_buy", imgs_)
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("anymore_buy_2", imgs_)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\level_low.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                        if imgs_ is not None and imgs_ != False:
                                            print("level_low", imgs_)
                                            myQuest_play_add(cla, data)
                                            added = True
                                            break
                                        else:
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\most.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(180, 115, 310, 185, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("most", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            else:
                                                click_pos_2(440, 150, cla)
                                QTest.qWait(500)
                elif result_data[1] == "2":
                    # 저항물약

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\sold_out.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 200, 450, 230, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("sold_out", imgs_)
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\character_level_low.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 200, 450, 230, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("character_level_low", imgs_)
                            # add
                            myQuest_play_add(cla, data)
                            added = True
                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    print("anymore_buy", imgs_)
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("anymore_buy_2", imgs_)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\level_low.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                        if imgs_ is not None and imgs_ != False:
                                            print("level_low", imgs_)
                                            myQuest_play_add(cla, data)
                                            added = True
                                            break
                                        else:
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\most.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(180, 180, 310, 250, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("most", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            else:
                                                click_pos_2(440, 220, cla)
                                QTest.qWait(500)
                if added == False:
                    # 어비스시간충전석석
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\sold_out.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 270, 435, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("sold_out", imgs_)
                    else:

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\sold_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 200, 450, 230, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sold_out", imgs_)
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\character_level_low.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 200, 450, 230, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("character_level_low", imgs_)
                                # add
                                myQuest_play_add(cla, data)
                                abyss_maul_in = True
                            else:

                                for i in range(10):

                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("anymore_buy", imgs_)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                        if imgs_ is not None and imgs_ != False:
                                            print("anymore_buy_2", imgs_)
                                            break
                                        else:
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\level_low.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                            if imgs_ is not None and imgs_ != False:
                                                print("level_low", imgs_)
                                                myQuest_play_add(cla, data)
                                                abyss_maul_in = True
                                                break
                                            else:
                                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\most.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(180, 250, 310, 315, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("most", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                else:
                                                    click_pos_2(440, 285, cla)
                                    QTest.qWait(500)

                    # 심연초대장장
                    for i in range(3):

                        if result_data[1] == "1":
                            click_pos_2(440, 355, cla)
                        elif result_data[1] == "2":
                            click_pos_2(440, 415, cla)
                        time.sleep(0.5)

                    # 구매하기
                    for i in range(5):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\gold.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(610, 980, 650, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("gold", imgs_)
                            click_pos_2(810, 1000, cla)
                        else:
                            break
                        QTest.qWait(500)

                # 나가기
                for i in range(5):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\title_abyss_gyohwan.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 180, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("title_abyss_gyohwan", imgs_)
                        click_pos_2(925, 60, cla)
                    else:
                        break
                    QTest.qWait(500)

            else:
                result_move = move_check(cla)

                if result_move == False:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\abyss_gyohwan_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(55, 130, 120, 170, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("abyss_gyohwan_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\title_abyss_gyohwan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 180, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("title_abyss_gyohwan", imgs_)
                            break
                        else:
                            result_move = move_check(cla)
                            if result_move == True:
                                time.sleep(1)
                        time.sleep(1)


            QTest.qWait(500)



    except Exception as e:
        print(e)
        return 0