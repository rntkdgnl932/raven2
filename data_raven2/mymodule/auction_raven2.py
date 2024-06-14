import sys
import os
import time
from PyQt5.QtTest import QTest

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def auction_start(cla):
    from clean_screen_raven2 import clean_screen
    from chango_raven2 import chango_in
    from boonhae_collection import collection_start, boonhae_start

    try:

        chango_in(cla)

        auction_ready(cla)
        auction_sell_start(cla)
        print("끝!")
        clean_screen(cla)

        # 수집, 분해 넣자
        collection_start(cla)
        boonhae_start(cla)



    except Exception as e:
        print(e)

def auction_ready(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action_raven2 import menu_open, confirm_all
    from property_raven2 import my_property_upload

    try:

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\sell_status.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(590, 100, 680, 140, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("거래소 화면")
            my_property_upload(cla)
        else:
            for i in range(5):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\title_auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 150, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("거래소", cla)
                    break
                else:
                    menu_open(cla)
                    for c in range(5):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\title_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 150, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\menu_auction.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(640, 330, 960, 600, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                time.sleep(0.5)


            # 왼쪽 판매 버튼 누르기

            for i in range(7):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\sell_price.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(460, 90, 550, 130, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\sell_btn1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 90, 200, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\sell_btn2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 90, 200, 970, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

            # 일괄회수
            for i in range(10):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\retrieve_ready_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(530, 130, 630, 970, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\checked_yes.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(210, 85, 255, 125, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\retrieve_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(520, 970, 630, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            confirm_all(cla)
                    else:
                        # 체크하기
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\checked_no.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(210, 85, 255, 125, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    break
                time.sleep(0.5)

    except Exception as e:
        print(e)


def auction_sell_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import confirm_all
    from clean_screen_raven2 import clean_screen

    from property_raven2 import my_property_upload

    # file_path = "C:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\auction_list.txt"
    # with open(file_path, "r", encoding='utf-8-sig') as file:
    #     read_data = file.read().splitlines()
    #     print("read_data", read_data)

    my_item = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\list"
    file_list = os.listdir(my_item)
    # print("file_list", file_list)
    # for i in range(len(file_list)):
    #     result_file_list = file_list[i].split(".")
    #     print("result_file_list", result_file_list[0])

    try:

        # full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\list"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(580, 980, 700, 1020, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     click_pos_reg(imgs_.x, imgs_.y, cla)
        #     time.sleep(0.5)

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\last_e.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(630, 120, 870, 990, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("last_e", imgs_)
            y_item = imgs_.y + 50
        else:
            y_item = 990

        # 판매시작
        for i in range(len(file_list)):
            result_file_list = file_list[i].split(".")
            read_data = result_file_list[0]

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\last_e.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(630, 120, 870, 990, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("last_e", imgs_)
                y_item = imgs_.y + 50
            else:
                y_item = 990

            # 종류 쭈욱 시작
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\list\\" + str(read_data) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(630, 120, 870, y_item, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

                can_auction_item = True

                for a in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\not_register_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 115, 600, 150, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        can_auction_item = False
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\not_register_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 115, 600, 150, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            can_auction_item = False
                            break
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\sell_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(370, 310, 460, 360, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                    time.sleep(0.1)

                if can_auction_item == True:

                    # 수량 정하기
                    quan_ = False
                    for last in range(5):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\qun_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(560, 520, 610, 570, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            quan_ = True
                            break
                        time.sleep(0.1)
                    if quan_ == True:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\qun_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(560, 520, 610, 570, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_2(680, 625, cla)
                            time.sleep(0.1)
                            click_pos_2(680, 625, cla)
                            time.sleep(0.1)
                            click_pos_2(680, 625, cla)
                            time.sleep(0.1)
                            click_pos_2(680, 625, cla)
                            time.sleep(0.1)
                    # 다야 갯수 정하기
                    for last in range(5):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\qun_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(560, 600, 610, 640, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_2(570, 395, cla)
                            time.sleep(0.1)
                            click_pos_2(570, 395, cla)
                            time.sleep(0.3)

                            sell_can = True
                            for s in range(5):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\ten.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(410, 110, 550, 150, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sell_can = False
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\last_question.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 600, 550, 650, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("last_question", imgs_)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\sell_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(370, 310, 460, 360, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("confirm : sell_title", imgs_)
                                            confirm_all(cla)
                                time.sleep(0.2)

                            for s in range(5):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\last_question.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 600, 550, 650, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("last_question", imgs_)
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\last_sell_gold.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(522, 550, 580, 580, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("confirm : last_sell_gold", imgs_)
                                        confirm_all(cla)
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\last_cancle.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(370, 640, 480, 690, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("cancle : last_cancle", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    break

                                time.sleep(0.2)


                            if sell_can == False:

                                for e in range(5):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\sell_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(370, 310, 460, 360, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\auction_cancle.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(470, 700, 550, 750, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            QTest.qWait(500)
                                    else:
                                        break
                                    time.sleep(0.5)
                            else:
                                confirm_all(cla)
                            break
                        time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\sell_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 310, 460, 360, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\auction_cancle.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 700, 550, 750, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            QTest.qWait(500)
            time.sleep(0.5)

        # 정산 후 내 재화 파악(settled)
        for i in range(7):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\settled_btn_bottom.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 970, 930, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\settled_btn1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 90, 200, 970, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\settled_btn1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 90, 200, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        for i in range(7):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\no_settled.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 510, 660, 580, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                my_property_upload(cla)
                break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\settled_btn_bottom.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 970, 930, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for c in range(5):
                        confirm_all(cla)
                        time.sleep(0.1)
            time.sleep(0.5)


    except Exception as e:
        print(e)


def mine_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number
    try:

        result_dia = 0
        result_gold = 0

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\dia_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("dia_reg", imgs_)
            x_dia = imgs_.x
            y_dia = imgs_.y

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\gold_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("gold_reg", imgs_)
            x_gold = imgs_.x
            y_gold = imgs_.y

        result_text = text_check_get_reg(x_dia + 8, y_dia - 9, x_gold - 10, y_dia + 9)
        result_text = change_number(result_text)
        result_dia = int_put_(result_text)
        result_dia_num = in_number_check(result_dia)
        print("result_text", result_dia_num, result_dia)

        result_text2 = text_check_get_reg(x_gold + 8, y_gold - 9, x_gold + 70, y_gold + 9)
        result_text2 = change_number(result_text2)
        result_gold = int_put_(result_text2)
        result_gold_num = in_number_check(result_gold)
        print("result_text2", result_gold_num, result_gold)

        if result_dia_num == True:

            return result_gold, result_dia

    except Exception as e:
        print(e)

