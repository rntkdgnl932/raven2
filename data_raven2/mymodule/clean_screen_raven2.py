import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def clean_screen(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import skip_click, juljun_check, juljun_off

    try:
        print("clean_screen")

        for i in range(10):
            clean = True

            result_juljun = juljun_check(cla)
            if result_juljun[0] == True:
                juljun_off(cla)

            skip_click(cla)

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("close_btn_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("close_btn_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("close_btn_3", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_4.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("close_btn_4", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_5.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("close_btn_5", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clean = False

            if clean == True:
                break

            time.sleep(0.3)



    except Exception as e:
        print(e)
        return 0



