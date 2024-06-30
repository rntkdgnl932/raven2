import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def steegma_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg
    from action_raven2 import menu_open
    from clean_screen_raven2 import clean_screen

    try:
        print("steegma_start")

        get_ = False
        get_count = 0
        while get_ is False:
            get_count += 1
            if get_count > 7:
                get_ = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\steegma\\title_steegma.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title_steegma", imgs_)

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\steegma\\gagin_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(730, 960, 935, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("gagin_btn", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\steegma\\big_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 300, 400, 650, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("big_point", imgs_)
                            click_pos_reg(imgs_.x - 35, imgs_.y + 30, cla)
                    time.sleep(0.5)



                for i in range(10):

                    is_point = False

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\steegma\\small_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(80, 80, 140, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("small_point", imgs_)
                        is_point = True
                        click_pos_reg(imgs_.x - 10, imgs_.y + 5, cla)
                        time.sleep(0.5)

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\steegma\\small_point2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(80, 80, 140, 300, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("small_point2", imgs_)
                        is_point = True
                        click_pos_reg(imgs_.x - 10, imgs_.y + 5, cla)
                        time.sleep(0.5)

                    if is_point == True:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\steegma\\gagin_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(730, 960, 935, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("gagin_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            for c in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\close_window.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 900, 600, 1000, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("close_window", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                time.sleep(0.2)
                    else:
                        get_ = True
                        clean_screen(cla)
                        break

                    time.sleep(0.5)



            else:
                menu_open(cla)
                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\steegma\\title_steegma.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\steegma\\menu_steegma.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 210, 960, 450, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_steegma", imgs_)
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            click_pos_reg(x_reg, y_reg, cla)
                    time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


