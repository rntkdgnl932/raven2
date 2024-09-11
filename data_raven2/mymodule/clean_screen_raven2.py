import time
# import os
import sys
from PyQt5.QtTest import *


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def clean_screen(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import skip_click, juljun_check, juljun_off, confirm_all, out_check

    try:
        print("clean_screen")

        juljun_off(cla)

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_off_result_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 310, 600, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            confirm_all(cla)

        skip_click(cla)

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("close_btn_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("close_btn_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("close_btn_3", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("close_btn_4", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_5.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(5, 30, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("close_btn_5", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        for i in range(5):
            clean = True

            result_out = out_check(cla)

            print("clean_screen : result_out", result_out, i)

            if result_out == True:
                break
            else:

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_off_result_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 310, 600, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    confirm_all(cla)
                    clean = False

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

            QTest.qWait(500)



    except Exception as e:
        print(e)
        return 0



