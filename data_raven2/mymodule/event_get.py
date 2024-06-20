import time
# import os
import sys


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
            imgs_ = imgs_set_(80, 300, 225, 680, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("e_in_point_1", imgs_)
                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 300, 225, 765, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("allget_point_2", imgs_)
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    break
            time.sleep(0.5)

        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\e_in_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(80, 300, 225, 680, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("e_in_point_1", imgs_)
                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                result_inven = inven_check(cla)
                if result_inven == True:

                    # is_pic = False
                    for n in range(file_count):

                        pic_num = n + 1

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\get_title\\" + str(
                            pic_num) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 320, 800, 400, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("pic_num", pic_num)
                            # is_pic = True
                            is_picture = str(pic_num)
                            event_get_click(cla, is_picture)
                            break
                    # if is_pic == True:
                    #     break
                else:
                    break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 300, 225, 765, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("allget_point_2", imgs_)
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    result_inven = inven_check(cla)
                    if result_inven == True:

                        # is_pic = False
                        for n in range(file_count):

                            pic_num = n + 1

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\get_title\\" + str(
                                pic_num) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(220, 320, 800, 400, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("pic_num", pic_num)
                                # is_pic = True
                                is_picture = str(pic_num)
                                event_get_click(cla, is_picture)
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
                    imgs_ = imgs_set_(80, 300, 225, 680, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("drag_pos : e_in_point_1", imgs_)
                    else:
                        drag_pos_py(140, 680, 140, 330, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\e_in_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        iimgs_ = imgs_set_(80, 300, 225, 680, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("drag_pos_py : e_in_point_1", imgs_)
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


    except Exception as e:
        print(e)
        return 0


def event_get_click(cla, is_picture):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, drag_pos, click_pos_2
    from action_raven2 import inven_check

    try:
        print("event_get_click")

        # 1 : 방명록
        # 2 : 바트람
        # 3 : 정예
        # 4 : 서리대검
        # 5 : 필드보스

        ######

        # 1 : 특무대합류기념방명록  o
        # 2 : 바트람의훈련교범  o
        # 3 : 정예특무대합류작전  o
        # 4 : 서리대검획득작전  o
        # 5 : 필드보스사냥소집령  o
        # 6 : 길드던전보급출석  o
        # 7 : 특무대길드소집령  o
        # 8 : 균열보스사냥소집령  o
        # 9 : 벨린다의별빛마법출석  o
        # 10 : 벨린다의신비한성장지원  o
        # 11 : 벨린다의마물사냥소집령  o
        # 12 : 샬럿상단의증서지원출석  +
        # 13 : 14일성의출석  +
        # 14 : 14일사역마출석  +
        # 15 : 샬럿의골드거래제안  +
        # 16 : 샬럿의강회의뢰 +

        if is_picture == "1" or is_picture == "13" or is_picture == "14":
            data = "fourteen"
        elif is_picture == "2":
            data = "seven_six"
        elif is_picture == "3":
            data = "8_click"
        elif is_picture == "4" or is_picture == "10" or is_picture == "11" or is_picture == "16" or is_picture == "15":
            data = "eight"
        elif is_picture == "5" or is_picture == "7" or is_picture == "8":
            data = "five"
        elif is_picture == "6" or is_picture == "9" or is_picture == "12":
            data = "seven"


        if data == "fourteen":
            print("fourteen")
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\fourteen\\checked_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 460, 870, 700, cla, img, 0.75)
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
            print("fourteen")
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\fourteen\\checked_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 550, 870, 610, cla, img, 0.75)
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
                imgs_ = imgs_set_(240, 440, 880, 490, cla, img, 0.8)
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
                    for c in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 480, 860, 710, cla, img, 0.8)
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
                            imgs_ = imgs_set_(730, 300, 860, 420, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("checked_top", imgs_)
                                click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                                result_inven = inven_check(cla)
                                if result_inven == True:
                                    click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                                    time.sleep(0.2)
                                    click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                                    time.sleep(0.2)
                        time.sleep(0.3)
                else:
                    break
                time.sleep(0.5)

        elif data == "eight":
            print("eight")


            # 510, 825 // 515, 570, 625, 680
            for c in range(4):
                y_reg = 515 + (55 * c)
                click_pos_2(510, y_reg, cla)
                time.sleep(0.5)
                click_pos_2(510, y_reg, cla)
                time.sleep(0.5)
            # 510, 825 // 515, 570, 625, 680
            for c in range(4):
                y_reg = 515 + (55 * c)
                click_pos_2(825, y_reg, cla)
                time.sleep(0.5)
                click_pos_2(825, y_reg, cla)
                time.sleep(0.5)

            # for c in range(10):
            #     full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked.PNG"
            #     img_array = np.fromfile(full_path, np.uint8)
            #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #     imgs_ = imgs_set_(480, 480, 860, 710, cla, img, 0.8)
            #     if imgs_ is not None and imgs_ != False:
            #         print("checked", imgs_)
            #         click_pos_reg(imgs_.x - 20, imgs_.y, cla)
            #         result_inven = inven_check(cla)
            #         if result_inven == True:
            #             click_pos_reg(imgs_.x - 20, imgs_.y, cla)
            #             time.sleep(0.2)
            #             click_pos_reg(imgs_.x - 20, imgs_.y, cla)
            #             time.sleep(0.2)
            #     else:
            #         full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked_top.PNG"
            #         img_array = np.fromfile(full_path, np.uint8)
            #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #         imgs_ = imgs_set_(730, 300, 860, 420, cla, img, 0.8)
            #         if imgs_ is not None and imgs_ != False:
            #             print("checked_top", imgs_)
            #             click_pos_reg(imgs_.x - 30, imgs_.y, cla)
            #             result_inven = inven_check(cla)
            #             if result_inven == True:
            #                 click_pos_reg(imgs_.x - 30, imgs_.y, cla)
            #                 time.sleep(0.2)
            #                 click_pos_reg(imgs_.x - 30, imgs_.y, cla)
            #                 time.sleep(0.2)
                time.sleep(0.3)
        elif data == "five":
            print("five")
            for c in range(10):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 480, 860, 710, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("checked", imgs_)
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
            for c in range(5):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\data\\seven_six\\checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 480, 860, 710, cla, img, 0.8)
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
                    imgs_ = imgs_set_(730, 300, 860, 420, cla, img, 0.8)
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

    except Exception as e:
        print(e)
        return 0


