import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def event_allget_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg

    try:
        print("event_allget_check")

        is_point = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\out_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(280, 30, 315, 55, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out_point_1", imgs_)
            is_point = True
            click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)




        return is_point
    except Exception as e:
        print(e)
        return 0

def event_allget_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import inven_check

    try:
        print("event_allget_start")

        result_inven = True

        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(60, 300, 260, 765, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("allget_point_1", imgs_)
                break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 300, 260, 765, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("allget_point_2", imgs_)
                    break
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 300, 260, 765, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("allget_point_3", imgs_)
                        break
            time.sleep(0.5)

        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(60, 300, 260, 765, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("allget_point_1", imgs_)
                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                time.sleep(0.5)
                click_pos_2(800, 730, cla)
                result_inven = inven_check(cla)
                if result_inven == True:
                    click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    time.sleep(0.5)
                    click_pos_2(800, 730, cla)
                    time.sleep(0.5)
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 300, 260, 765, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("allget_point_2", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    time.sleep(0.5)
                    click_pos_2(800, 730, cla)
                    result_inven = inven_check(cla)
                    if result_inven == True:
                        click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        time.sleep(0.5)
                        click_pos_2(800, 730, cla)
                        time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\event\\allget\\allget_point_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 300, 260, 765, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("allget_point_3", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        time.sleep(0.5)
                        click_pos_2(800, 730, cla)
                        result_inven = inven_check(cla)
                        if result_inven == True:
                            click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                            time.sleep(0.5)
                            click_pos_2(800, 730, cla)
                            time.sleep(0.5)
                    else:
                        break
            time.sleep(0.5)

        if result_inven == False:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\out_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 30, 315, 55, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("out_point_1", imgs_)
                click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                event_allget_start(cla)

    except Exception as e:
        print(e)
        return 0



