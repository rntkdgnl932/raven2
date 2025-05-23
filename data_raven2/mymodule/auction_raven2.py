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
    from function_game import click_pos_2
    try:

        chango_in(cla)

        # 수집, 분해 넣자
        collection_start(cla)
        boonhae_start(cla)

        auction_ready(cla)
        click_pos_2(900, 235, cla)
        time.sleep(1)
        auction_sell_start(cla, "jangbi")
        click_pos_2(900, 320, cla)
        time.sleep(1)
        auction_sell_start(cla, "jabhwa")
        click_pos_2(900, 390, cla)
        time.sleep(1)
        auction_sell_start(cla, "item")
        print("끝!")

        settled(cla)

        clean_screen(cla)





    except Exception as e:
        print(e)

def auction_ready(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action_raven2 import menu_open, confirm_all
    from property_raven2 import my_property_upload

    try:

        # full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\sell_status.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(590, 100, 680, 140, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("거래소 화면")
        #     my_property_upload(cla)
        # else:
        for i in range(5):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\title_auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 150, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("거래소", cla)
                my_property_upload(cla)
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

        print("왼쪽 판매 버튼 누르기")
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

        print("일괄회수 준비")
        # 일괄회수 준비
        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\retrieve_ready_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(530, 130, 630, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\retrieve_ready_btn2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(530, 130, 630, 970, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
            time.sleep(0.5)

        print("일괄회수")
        # 일괄회수
        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\retrieve_ready_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(530, 130, 630, 970, cla, img, 0.7)
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
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\retrieve_btn_2.PNG"
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


def auction_sell_start(cla, data):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import confirm_all


    # file_path = "C:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\auction_list.txt"
    # with open(file_path, "r", encoding='utf-8-sig') as file:
    #     read_data = file.read().splitlines()
    #     print("read_data", read_data)

    my_item = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\list\\" + str(data)
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

        y_item = 970

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\last_e.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(630, 120, 870, 990, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("last_e2", imgs_)
            y_item = imgs_.y + 50
        else:
            y_item = 990

        # 판매시작
        print("판매시작..", y_item, len(file_list))
        for i in range(len(file_list)):
            result_file_list = file_list[i].split(".")
            read_data = result_file_list[0]

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\last_e.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(630, 120, 870, 990, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("last_e_1", imgs_)
                y_item = imgs_.y + 50
                # break
            else:
                y_item = 990

            # 종류 쭈욱 시작
            print("str(read_data)", str(read_data))
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\list\\" + str(data) + "\\" + str(read_data) + ".PNG"
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
                            imgs_ = imgs_set_(370, 300, 480, 360, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                    time.sleep(0.1)

                if can_auction_item == True:

                    # 거래 내역 있는지 확인하기
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\not_trade.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 370, 610, 520, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        for e in range(5):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\sell_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(370, 300, 480, 360, cla, img, 0.8)
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

                        # 수량 정하기
                        quan_ = False
                        for last in range(5):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\qun_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(570, 530, 620, 580, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                quan_ = True
                                break
                            time.sleep(0.1)
                        if quan_ == True:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\qun_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(570, 530, 620, 580, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.3)

                                for m in range(5):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\maximum_quantity.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 100, 580, 160, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        click_pos_2(700, 635, cla)
                                        time.sleep(0.2)
                                    time.sleep(0.2)
                        # 다야 갯수 정하기
                        for last in range(5):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\qun_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(560, 610, 620, 660, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                                click_pos_2(585, 380, cla)
                                time.sleep(0.1)
                                click_pos_2(585, 380, cla)
                                time.sleep(0.3)

                                sell_can = True
                                for s in range(5):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\ten.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(410, 110, 570, 150, cla, img, 0.8)
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
                                            imgs_ = imgs_set_(370, 300, 480, 360, cla, img, 0.8)
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
                                        imgs_ = imgs_set_(370, 300, 480, 360, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\auction_cancle.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(470, 700, 600, 760, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                QTest.qWait(500)
                                        else:
                                            break
                                        time.sleep(0.5)
                                else:
                                    for c in range(5):
                                        result_confirm = confirm_all(cla)
                                        if result_confirm == False:
                                            break
                                        QTest.qWait(1000)
                                break
                            time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\sell_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 300, 480, 360, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\auction_cancle.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 700, 600, 760, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            QTest.qWait(500)
            time.sleep(0.5)




    except Exception as e:
        print(e)

def settled(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    from property_raven2 import my_property_upload
    from action_raven2 import confirm_all

    try:
        # 정산 후 내 재화 파악(settled)
        print("정산 후 내 재화 파악(settled)")
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

##################거래 단가 구하기##################


def get_sell_price(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number
    try:
        print("get_sell_price")
        sell_price = 0

        # 최근 거래 단가
        result_now = get_low_price(cla, "now")
        # 현재 최저 단가
        result_low = get_low_price(cla, "low")

        print("result now", result_now)
        print("result low", result_low)

        if result_now == 1:
            sell_price = result_low
        else:
            if result_low > result_now:
                sell_price = result_low
            else:
                sell_price = (result_low + result_now) / 2


        print("##########################")
        print("sell_price", sell_price)
        sell_price = round(sell_price, 2)
        print("sell_price", sell_price)
        print("##########################")

    except Exception as e:
        print(e)



def get_low_price(cla, data):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_reg

    if cla == 'one':
        plus = 0
    if cla == 'two':
        plus = 960
    if cla == 'three':
        plus = 960 * 2
    if cla == 'four':
        plus = 960 * 3
    if cla == 'five':
        plus = 960 * 4
    if cla == 'six':
        plus = 960 * 5

    try:
        print("auction_item", data)

        # 최근
        if data == "now":
            x_1 = 500 + plus
            x_2 = 600 + plus
            point_reg = x_2
        else:
            x_1 = 700 + plus
            x_2 = 820 + plus
            point_reg = x_2
        y_1 = 375
        y_2 = 405

        is_point = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("point", imgs_)
            is_point = True
            point_reg = imgs_.x
            x_2 = point_reg

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\dia_start.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dia_start", imgs_)
            x_1 = imgs_.x + 7
            x_2 = x_1 + 10

        # 포인트가 있으면 9차이, 없으면 7차이

        print("##################")
        print("x_1", x_1)
        print("x_2", x_2)
        print("#######################")
        #
        # result = text_check_get_reg(x_1, y_1, x_2, y_2)
        # print("result", result)

        # 소수점 이전
        num = False
        num_count = 0
        result_num = ""
        while num is False:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\price_num\\" + str(num_count) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("is num...", str(num_count), imgs_)

                x_1 = imgs_.x
                x_2 = x_1 + 14

                if is_point == True:
                    if imgs_.x > point_reg:
                        num = True
                    else:
                        result_num += str(num_count)
                else:
                    result_num += str(num_count)
                # print("result_num...", result_num)
                num_count = 0
            else:
                num_count += 1
                if num_count > 9:
                    num = True

        # 소수점 이후
        if is_point == True:

            x_1 = point_reg
            x_2 = x_1 + 10

            result_num += "."

            print("result_num(point)", result_num)

            num = False
            num_count = 0
            while num is False:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\auction\\price_num\\" + str(num_count) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("is num...", str(num_count), imgs_)

                    x_1 = imgs_.x
                    x_2 = x_1 + 14
                    result_num += str(num_count)
                    # print("result_num...", result_num)
                    num_count = 0
                else:
                    num_count += 1
                    if num_count > 9:
                        num = True



        result_num = float(result_num)
        print("result_num", result_num)


        return result_num
    except Exception as e:
        print(e)
        return 0

