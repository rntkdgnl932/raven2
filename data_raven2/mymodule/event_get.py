import time
# import os
import sys
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def event_get_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg

    try:
        print("event_get_check")

        is_point = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\e_out_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(690, 30, 750, 65, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("e_out_point_1", imgs_)
            is_point = True
            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)




        return is_point
    except Exception as e:
        print(e)
        return 0

def event_get_start(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, drag_pos, click_pos_2, drag_pos_py
    from action_raven2 import inven_check
    from clean_screen_raven2 import clean_screen

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

    try:
        print("event_get_start")

        result_inven = True

        # 폴더 내 파일 개수
        folder_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\get_title"
        file_list = os.listdir(folder_path)
        file_count = len(file_list)
        # print(file_count)



        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\e_in_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(80, 300, 260, 680, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("e_in_point_1", imgs_)
                # click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(80, 300, 260, 680, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("allget_point_3", imgs_)
                    # click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    break
            time.sleep(0.5)

        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\e_in_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(80, 300, 260, 680, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("e_in_point_1", imgs_)
                click_pos_reg(imgs_.x - 15, imgs_.y, cla)

                y_point = imgs_.y

                result_inven = inven_check(cla)
                if result_inven == True:

                    # is_pic = False
                    for n in range(len(file_list)):

                        pic_num_ready = file_list[n]
                        pic_num = pic_num_ready.split(".")[0]

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\get_title\\" + str(
                            pic_num) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 260, 910, 770, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("pic_num", pic_num)
                            is_picture = str(pic_num)
                            event_get_click(cla, is_picture, y_point, "e_in_point_1")
                            break
                else:
                    break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(80, 300, 260, 680, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("allget_point_3", imgs_)
                    click_pos_reg(imgs_.x - 15, imgs_.y, cla)

                    y_point = imgs_.y

                    result_inven = inven_check(cla)
                    if result_inven == True:

                        # is_pic = False
                        for n in range(len(file_list)):

                            pic_num_ready = file_list[n]
                            pic_num = pic_num_ready.split(".")[0]

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\get_title\\" + str(
                                pic_num) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(220, 260, 910, 770, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("pic_num", pic_num)
                                # is_pic = True

                                is_picture = str(pic_num)
                                event_get_click(cla, is_picture, y_point, "allget_point_3")
                                break
                        # if is_pic == True:
                        #     break
                    else:
                        break
                else:
                    drag_pos(140, 680, 140, 330, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\e_in_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(80, 300, 260, 680, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("drag_pos : e_in_point_1", imgs_)
                    else:
                        drag_pos_py(140, 680, 140, 330, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(80, 300, 260, 680, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("drag_pos_py : allget_point_3", imgs_)
                        else:
                            break
            time.sleep(0.5)

        # 다시 샤샤샥
        if result_inven == False:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\e_out_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(690, 30, 750, 65, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("e_out_point_1", imgs_)
                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                event_get_start(cla)
        else:
            clean_screen(cla)

    except Exception as e:
        print(e)
        return 0


def event_get_reg(cla, y_reg, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, drag_pos, click_pos_2
    from action_raven2 import inven_check

    try:
        print("event_get_reg", y_reg, data)
        # data => e_in_point_1, allget_point_3

        is_point = False

        if data == "e_in_point_1":
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\e_in_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(80, y_reg - 20, 260, y_reg + 20, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("e_in_point_1", imgs_)
                is_point = True

        elif data == "allget_point_3":
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(80, y_reg - 20, 260, y_reg + 20, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("allget_point_3", imgs_)
                is_point = True

        return is_point
    except Exception as e:
        print(e)
        return 0

def event_get_click(cla, is_picture, y_point, point):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, drag_pos, click_pos_2
    from action_raven2 import inven_check



    try:
        print("event_get_click", y_point, point)

        # data => e_in_point_1, allget_point_3





        # 1 : 방명록
        # 2 : 바트람
        # 3 : 정예
        # 4 : 서리대검
        # 5 : 필드보스

        ######

        # - :

        # 1 : 바트람의훈련교범(seven_six) o
        # 2 : 정예특무대합류작전(8_click) o

        # 3 : 특무대원특별지원출석(twenty_eight) o

        # 4 : 신입특무대지원작전(8_click) o

        # 5 : 희귀장신구제작미션(six) o

        # 6 : 특무대사냥의뢰(8_click) o

        # 7 : 헛개수특별출석(seven) o

        # 8 :

        # 9 :

        # 10 :

        # 11 :

        # 12 :

        # 13 :

        # 14 :

        # 15 :

        # 16 :

        # 17 :

        # ?? : 탐욕의여름혹서기지원(point_click) 8
        # ?? : 탐욕의여름21일특별출석(twenty_eight) 9
        # ?? : 탐욕의섬탐사미션(seven_six) 10
        # ?? : 탐욕의섬정복미션(ten) 11
        # ?? :


        # 8_click => drag 하는 것
        # eight => 8개 클릭 후 위에 클릭
        # ten => 10개 클릭 후 위에 클릭


        # 예외
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\get_title\\1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(220, 260, 800, 510, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("pic_num", imgs_)
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\get_des\\1_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(220, 260, 800, 510, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("1_1", imgs_)
                is_picture = "five"



        if is_picture == "0" or is_picture == "0":
            data = "fourteen"
        elif is_picture == "1" or is_picture == "10":
            data = "seven_six"
        elif is_picture == "0":
            data = "five"
        elif is_picture == "0":
            data = "six"
        elif is_picture == "7":
            data = "seven"
        elif is_picture == "2" or is_picture == "4" or is_picture == "6":
            data = "8_click"
        elif is_picture == "5":
            data = "eight"
        elif is_picture == "11":
            data = "ten"
        elif is_picture == "0":
            data = "twelve"
        elif is_picture == "0":
            data = "twelve_plus_two"
        elif is_picture == "3" or is_picture == "9":
            data = "twenty_eight"
        elif is_picture == "8":
            data = "point_click"


        if data == "fourteen":
            print("fourteen")
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\fourteen\\checked_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 460, 900, 700, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("checked_2", imgs_)
                click_pos_reg(imgs_.x - 20, imgs_.y + 50, cla)
                result_inven = inven_check(cla)
                if result_inven == True:
                    click_pos_reg(imgs_.x - 20, imgs_.y + 50, cla)
                    time.sleep(0.2)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 50, cla)
                    time.sleep(0.2)

        elif data == "seven":
            print("seven")
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\fourteen\\checked_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 550, 900, 610, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("checked_2", imgs_)
                click_pos_reg(imgs_.x - 20, imgs_.y + 50, cla)
                result_inven = inven_check(cla)
                if result_inven == True:
                    click_pos_reg(imgs_.x - 20, imgs_.y + 50, cla)
                    time.sleep(0.2)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 50, cla)
                    time.sleep(0.2)



        elif data == "seven_six":
            print("seven_six")

            for i in range(10):

                point_ = False
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(240, 440, 900, 490, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("point_1", imgs_)
                    point_ = True
                    click_pos_reg(imgs_.x - 10, imgs_.y + 5, cla)
                    time.sleep(0.3)
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(240, 440, 880, 490, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("point_2", imgs_)
                    point_ = True
                    click_pos_reg(imgs_.x - 10, imgs_.y + 5, cla)
                    time.sleep(0.3)
                if point_ == True:
                    is_checked = False
                    for c in range(10):

                        result_point = event_get_reg(cla, y_point, point)
                        if result_point == True:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 480, 900, 710, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("checked", imgs_)
                                is_checked = True
                                click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                                result_inven = inven_check(cla)
                                if result_inven == True:
                                    click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                                    time.sleep(0.2)
                                    click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                                    time.sleep(0.2)
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked_top.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(730, 300, 900, 420, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("checked_top", imgs_)
                                    is_checked = True
                                    click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                                    result_inven = inven_check(cla)
                                    if result_inven == True:
                                        click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                                        time.sleep(0.2)
                                        click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                                        time.sleep(0.2)
                        else:
                            break
                        time.sleep(0.3)

                    if is_checked == False:
                        for c in range(4):
                            result_point = event_get_reg(cla, y_point, point)
                            if result_point == True:
                                y_reg = 515 + (55 * c)
                                click_pos_2(530, y_reg, cla)
                                time.sleep(0.5)
                                click_pos_2(530, y_reg, cla)
                                time.sleep(0.5)
                            else:
                                break
                        # 510, 825 // 515, 570, 625, 680
                        for c in range(4):
                            result_point = event_get_reg(cla, y_point, point)
                            if result_point == True:
                                y_reg = 515 + (55 * c)
                                click_pos_2(840, y_reg, cla)
                                time.sleep(0.5)
                                click_pos_2(840, y_reg, cla)
                                time.sleep(0.5)
                            else:
                                break
                        result_point = event_get_reg(cla, y_point, point)
                        if result_point == True:
                            click_pos_2(820, 370, cla)
                            time.sleep(0.5)
                            click_pos_2(820, 370, cla)
                            time.sleep(0.5)

                else:
                    break
                time.sleep(0.5)

        elif data == "six":
            print("six")


            # 510, 825 // 515, 570, 625, 680
            for c in range(3):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    y_reg = 515 + (55 * c)
                    click_pos_2(530, y_reg, cla)
                    time.sleep(0.5)
                    click_pos_2(530, y_reg, cla)
                    time.sleep(0.5)
                else:
                    break
            # 510, 825 // 515, 570, 625, 680
            for c in range(3):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    y_reg = 515 + (55 * c)
                    click_pos_2(840, y_reg, cla)
                    time.sleep(0.5)
                    click_pos_2(840, y_reg, cla)
                    time.sleep(0.5)
                else:
                    break

            result_point = event_get_reg(cla, y_point, point)
            if result_point == True:
                click_pos_2(820, 370, cla)
                time.sleep(0.5)
                click_pos_2(820, 370, cla)
                time.sleep(0.5)

        elif data == "eight":
            print("eight")


            # 510, 825 // 515, 570, 625, 680
            for c in range(4):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    y_reg = 515 + (55 * c)
                    click_pos_2(530, y_reg, cla)
                    time.sleep(0.5)
                    click_pos_2(530, y_reg, cla)
                    time.sleep(0.5)
                else:
                    break
            # 510, 825 // 515, 570, 625, 680
            for c in range(4):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    y_reg = 515 + (55 * c)
                    click_pos_2(840, y_reg, cla)
                    time.sleep(0.5)
                    click_pos_2(840, y_reg, cla)
                    time.sleep(0.5)
                else:
                    break

            result_point = event_get_reg(cla, y_point, point)
            if result_point == True:
                click_pos_2(820, 370, cla)
                time.sleep(0.5)
                click_pos_2(820, 370, cla)
                time.sleep(0.5)

        elif data == "ten":
            print("ten")

            drag_pos(550, 600, 550, 700, cla)
            QTest.qWait(500)
            # 510, 825 // 515, 570, 625, 680
            for c in range(5):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    y_reg = 515 + (55 * c)
                    if c == 4:
                        click_pos_2(530, 720, cla)
                        time.sleep(0.5)
                        click_pos_2(530, 720, cla)
                        time.sleep(0.5)
                    else:
                        click_pos_2(530, y_reg, cla)
                        time.sleep(0.5)
                        click_pos_2(530, y_reg, cla)
                        time.sleep(0.5)
                else:
                    break
            # 510, 825 // 515, 570, 625, 680
            for c in range(5):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    y_reg = 515 + (55 * c)
                    if c == 4:
                        click_pos_2(840, 720, cla)
                        time.sleep(0.5)
                        click_pos_2(840, 720, cla)
                        time.sleep(0.5)
                    else:
                        click_pos_2(840, y_reg, cla)
                        time.sleep(0.5)
                        click_pos_2(840, y_reg, cla)
                        time.sleep(0.5)
                else:
                    break

            result_point = event_get_reg(cla, y_point, point)
            if result_point == True:
                click_pos_2(820, 370, cla)
                time.sleep(0.5)
                click_pos_2(820, 370, cla)
                time.sleep(0.5)
        elif data == "twelve":
            print("twelve")

            drag_pos(550, 550, 550, 700, cla)
            QTest.qWait(500)
            # 510, 825 // 515, 570, 625, 680
            for c in range(5):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    y_reg = 515 + (55 * c)
                    if c == 4:
                        click_pos_2(530, 720, cla)
                        time.sleep(0.5)
                        click_pos_2(530, 720, cla)
                        time.sleep(0.5)
                    else:
                        click_pos_2(530, y_reg, cla)
                        time.sleep(0.5)
                        click_pos_2(530, y_reg, cla)
                        time.sleep(0.5)
                else:
                    break
            # 510, 825 // 515, 570, 625, 680
            for c in range(5):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    y_reg = 515 + (55 * c)
                    if c == 4:
                        click_pos_2(840, 720, cla)
                        time.sleep(0.5)
                        click_pos_2(840, 720, cla)
                        time.sleep(0.5)
                    else:
                        click_pos_2(840, y_reg, cla)
                        time.sleep(0.5)
                        click_pos_2(840, y_reg, cla)
                        time.sleep(0.5)
                else:
                    break

            result_point = event_get_reg(cla, y_point, point)
            if result_point == True:
                drag_pos(550, 700, 550, 550, cla)
                QTest.qWait(500)

                click_pos_2(530, 700, cla)
                time.sleep(0.5)
                click_pos_2(530, 700, cla)
                time.sleep(0.5)

                click_pos_2(840, 700, cla)
                time.sleep(0.5)
                click_pos_2(840, 700, cla)
                time.sleep(0.5)

                click_pos_2(820, 370, cla)
                time.sleep(0.5)
                click_pos_2(820, 370, cla)
                time.sleep(0.5)

        elif data == "twelve_plus_two":
            print("twelve_plus_two")

            drag_pos(550, 550, 550, 700, cla)
            QTest.qWait(500)
            # 510, 825 // 515, 570, 625, 680
            for c in range(5):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    y_reg = 515 + (55 * c)
                    if c == 4:
                        click_pos_2(530, 720, cla)
                        time.sleep(0.5)
                        click_pos_2(530, 720, cla)
                        time.sleep(0.5)
                    else:
                        click_pos_2(530, y_reg, cla)
                        time.sleep(0.5)
                        click_pos_2(530, y_reg, cla)
                        time.sleep(0.5)
                else:
                    break
            # 510, 825 // 515, 570, 625, 680
            for c in range(5):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    y_reg = 515 + (55 * c)
                    if c == 4:
                        click_pos_2(840, 720, cla)
                        time.sleep(0.5)
                        click_pos_2(840, 720, cla)
                        time.sleep(0.5)
                    else:
                        click_pos_2(840, y_reg, cla)
                        time.sleep(0.5)
                        click_pos_2(840, y_reg, cla)
                        time.sleep(0.5)
                else:
                    break

            result_point = event_get_reg(cla, y_point, point)
            if result_point == True:
                drag_pos(550, 700, 550, 550, cla)
                QTest.qWait(500)

                click_pos_2(530, 650, cla)
                time.sleep(0.5)
                click_pos_2(530, 650, cla)
                time.sleep(0.5)

                click_pos_2(840, 650, cla)
                time.sleep(0.5)
                click_pos_2(840, 650, cla)
                time.sleep(0.5)

                click_pos_2(530, 700, cla)
                time.sleep(0.5)
                click_pos_2(530, 700, cla)
                time.sleep(0.5)

                click_pos_2(840, 700, cla)
                time.sleep(0.5)
                click_pos_2(840, 700, cla)
                time.sleep(0.5)

                click_pos_2(820, 370, cla)
                time.sleep(0.5)
                click_pos_2(820, 370, cla)
                time.sleep(0.5)

        elif data == "five":
            print("five")
            for c in range(10):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 480, 900, 710, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("checked", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                    result_inven = inven_check(cla)
                    if result_inven == True:
                        click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                        time.sleep(0.2)
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\five\\checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 480, 900, 710, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("checked 2", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                        result_inven = inven_check(cla)
                        if result_inven == True:
                            click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                            time.sleep(0.2)
                time.sleep(0.3)

        elif data == "8_click":
            print("8_click")
            drag_pos(550, 600, 550, 700, cla)
            QTest.qWait(500)
            for c in range(5):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\eight\\8_click_checked_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 480, 900, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("8_click_checked_1", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                    result_inven = inven_check(cla)
                    if result_inven == True:
                        click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                        time.sleep(0.2)


                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 480, 900, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("checked", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                    result_inven = inven_check(cla)
                    if result_inven == True:
                        click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                        time.sleep(0.2)
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked_top.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(730, 300, 900, 420, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("checked_top", imgs_)
                        click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                        result_inven = inven_check(cla)
                        if result_inven == True:
                            click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                            time.sleep(0.2)
                    else:
                        drag_pos(550, 700, 550, 600, cla)
                time.sleep(0.3)

            click_pos_2(820, 370, cla)
            time.sleep(0.5)
            click_pos_2(820, 370, cla)
            time.sleep(0.5)

        elif data == "twenty_eight":
            print("twenty_eight")
            for c in range(5):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\twenty_eight\\28_checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 360, 750, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("28_checked", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                    result_inven = inven_check(cla)
                    if result_inven == True:
                        click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                        time.sleep(0.2)
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\twenty_eight\\28_checked_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 360, 750, 730, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("28_checked_2", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                        result_inven = inven_check(cla)
                        if result_inven == True:
                            click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                            time.sleep(0.2)
                time.sleep(0.3)

            click_pos_2(815, 640, cla)
            time.sleep(0.5)
            click_pos_2(815, 640, cla)
            time.sleep(0.5)
        elif data == "point_click":
            print("point_click")
            for c in range(3):
                result_point = event_get_reg(cla, y_point, point)
                if result_point == True:
                    click_pos_2(580, 650, cla)
                    time.sleep(0.5)
                    click_pos_2(580, 650, cla)
                    time.sleep(0.5)
                    click_pos_2(580, 650, cla)
                    time.sleep(0.5)
                    click_pos_2(580, 650, cla)
                    time.sleep(0.5)
                else:
                    break

    except Exception as e:
        print(e)
        return 0


