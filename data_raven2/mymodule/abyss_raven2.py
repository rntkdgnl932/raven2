import time
# import os
import sys
from PyQt5.QtTest import *


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def abyss_start(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import juljun_check, juljun_off, juljun_on, attack_on
    from potion_raven2 import potion_check
    from clean_screen_raven2 import clean_screen
    try:
        print("abyss_start")

        result_juljun = juljun_check(cla)
        # result_juljun[0] => True : 절전 맞음
        # result_juljun[1] => attack : 사냥 중 맞음, ready : 사냥 아님, no_spot : 사냥터로 ㄱㄱ
        if result_juljun[0] == False:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\abyss_maul.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(55, 105, 120, 170, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("abyss_maul..", imgs_)
                abyss_sangjum(cla, data)
                abyss_dun_in(cla, data)
            else:
                juljun_on(cla)
        elif result_juljun[0] == True:

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\juljun_spot\\abyss_1_tongok.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 120, 130, 170, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("abyss_1_tongok", imgs_)



                if result_juljun[1] == "attack":
                    print("어비스 사냥중")
                    potion_check(cla)
                    # 포션 체크...
                    # 절전 중 집 가기...
                else:
                    juljun_off(cla)
                    clean_screen(cla)
                    attack_on(cla)
                    juljun_on(cla)
            else:
                print("어비스 아니다")
                abyss_sangjum(cla, data)
                abyss_dun_in(cla, data)


        # # 사냥터 가기전 물약 및 입장권 구매
        # abyss_sangjum(cla, data)
        #
        # # 사냥터 들어가기
        # abyss_dun_in(cla, data)



    except Exception as e:
        print(e)
        return 0



def abyss_sangjum(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import menu_open, go_maul, confirm_all

    try:
        print("abyss_sangjum")

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\abyss_maul.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(55, 105, 120, 170, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("abyss_maul..", imgs_)
        else:
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
                        print("title_abyss_sangjum_go", imgs_)

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
                                        if result_data[1] == "2":
                                            confirm_all(cla)

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
                            anymore = False
                            for i in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    print("anymore_buy", imgs_)
                                    anymore = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("anymore_buy_2", imgs_)
                                        anymore = True
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
                            if anymore == True:
                                for i in range(10):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("anymore_buy", imgs_)
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                        if imgs_ is not None and imgs_ != False:
                                            print("anymore_buy_2", imgs_)
                                        else:
                                            break
                                    time.sleep(0.5)
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
                            anymore = False
                            for i in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    print("anymore_buy", imgs_)
                                    anymore = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("anymore_buy_2", imgs_)
                                        anymore = True
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

                            if anymore == True:
                                for i in range(10):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("anymore_buy", imgs_)
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                        if imgs_ is not None and imgs_ != False:
                                            print("anymore_buy_2", imgs_)
                                        else:
                                            break
                                    time.sleep(0.5)
                if added == False:
                    # 어비스시간충전석석

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\sold_out.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 270, 450, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("sold_out", imgs_)
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\character_level_low.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 270, 450, 300, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("character_level_low", imgs_)
                            # add
                            myQuest_play_add(cla, data)
                            abyss_maul_in = True
                        else:
                            anymore = False
                            for i in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    print("anymore_buy", imgs_)
                                    anymore = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("anymore_buy_2", imgs_)
                                        anymore = True
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
                            if anymore == True:
                                for i in range(10):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("anymore_buy", imgs_)
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\anymore_buy_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(390, 115, 580, 150, cla, img, 0.75)
                                        if imgs_ is not None and imgs_ != False:
                                            print("anymore_buy_2", imgs_)
                                        else:
                                            break
                                    time.sleep(0.5)
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



def abyss_dun_in(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import menu_open, go_maul, move_check, move_wait, attack_on, juljun_on
    from schedule import myQuest_play_add

    try:
        # 여기에 완료 되는거 추가해야함
        print("abyss_dun_in")

        # 마을에서만 입장 가능
        go_maul(cla)

        result_data = data.split("_")
        # 어비스_1

        abyss_maul_in = False
        abyss_maul_in_count = 0
        while abyss_maul_in is False:
            abyss_maul_in_count += 1
            if abyss_maul_in_count > 15:
                abyss_maul_in = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\map_abyss_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 35, 530, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("map_abyss_title..", imgs_)


                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\abyss_1_tongok.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 80, 830, 130, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("abyss_1_tongok..", imgs_)
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\red_jungsoo.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(690, 715, 750, 800, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("red_jungsoo..", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\spot_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 420, 660, 470, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("red_jungsoo..", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            for i in range(10):
                                result_move = move_check(cla)
                                if result_move == True:
                                    move_wait(cla)
                                    break
                                time.sleep(1)
                            attack_on(cla)
                            juljun_on(cla)
                            abyss_maul_in = True

                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\map_abyss_1_tongok.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 200, 800, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("map_abyss_1_tongok..", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)


            else:

                click_pos_2(140, 155, cla)

                abyss_in = False
                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\map_abyss_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 35, 530, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("map_abyss_title..", imgs_)
                        abyss_in = True
                        break
                    time.sleep(0.5)

                if abyss_in == False:

                    menu_open(cla)

                    for i in range(10):

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\title_abyss.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 120, 170, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("title_abyss", imgs_)

                            if result_data[1] == "1":
                                y_reg = 180
                            elif result_data[1] == "2":
                                y_reg = 300

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\abyss_in_btn.PNG"
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
                                        click_pos_2(925, 60, cla)
                                        break

                                    time.sleep(1)

                                # 나가기
                                for x in range(5):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\title_abyss_gyohwan.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 30, 180, 100, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("title_abyss_gyohwan", imgs_)
                                        click_pos_2(925, 60, cla)
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\abyss\\title_abyss.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(30, 30, 120, 170, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("title_abyss", imgs_)
                                        else:
                                            break
                                    QTest.qWait(500)
                                break

                            else:
                                click_pos_2(100, y_reg, cla)
                            time.sleep(0.5)

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








