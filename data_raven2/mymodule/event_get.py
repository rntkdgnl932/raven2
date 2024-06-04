import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def event_get_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import out_check

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
    from function_game import imgs_set_, click_pos_reg
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
            imgs_ = imgs_set_(100, 300, 225, 750, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("e_in_point_1", imgs_)
                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                break
            time.sleep(0.5)

        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\get\\e_in_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 300, 225, 750, cla, img, 0.8)
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
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import inven_check

    try:
        print("event_get_click")

        # 1 : 방명록
        # 2 : 바트람
        # 3 : 정예
        # 4 : 서리대검
        # 5 : 필드보스

        if is_picture == "1":
            data = "fourteen"
        elif is_picture == "2":
            data = "seven_six"
        elif is_picture == "3":
            data = "8_click"
        elif is_picture == "4":
            data = "eight"
        elif is_picture == "5":
            data = "five"

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

    except Exception as e:
        print(e)
        return 0


