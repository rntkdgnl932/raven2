import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def get_item_start(cla):

    try:
        print("get_item_start")
        get_post(cla)

        get_upjuk(cla)

        get_sangjum(cla)


    except Exception as e:
        print(e)
        return 0


def get_post(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_reg
    from action_raven2 import inven_check, confirm_all, menu_open
    from clean_screen_raven2 import clean_screen

    try:
        print("get_post")

        get_ = False
        get_count = 0
        while get_ is False:
            get_count += 1
            if get_count > 4:
                get_ = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\title_post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title_post", imgs_)

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\post_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 80, 110, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("post_point_1", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\get.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 370, 560, 450, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("get", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\close_window.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 900, 600, 1000, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("close_window", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\close_post.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(180, 80, 240, 800, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("close_post", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    result_inven = inven_check(cla)
                                    if result_inven == True:
                                        click_pos_2(870, 1000, cla)
                                        result_inven = inven_check(cla)
                                        if result_inven == True:
                                            confirm_all(cla)
                                            inven_check(cla)
                                else:
                                    click_pos_2(870, 1000, cla)
                                    result_inven = inven_check(cla)
                                    if result_inven == True:
                                        confirm_all(cla)
                                        time.sleep(0.2)
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\close_window.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(400, 900, 600, 1000, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("close_window", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.5)
                                        break
                        time.sleep(0.5)
                else:
                    get_ = True
                    clean_screen(cla)


            else:
                menu_open(cla)

                is_ = False

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\title_post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\menu_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 940, 800, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_post", imgs_)

                            x_reg = imgs_.x
                            y_reg = imgs_.y

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\menu_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_reg(x_reg, y_reg - 60, x_reg + 35, y_reg, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("post : menu_point", imgs_)
                                click_pos_reg(x_reg, y_reg, cla)
                                is_ = True
                    time.sleep(0.5)
                if is_ == False:
                    get_ = True
                    clean_screen(cla)
    except Exception as e:
        print(e)
        return 0


def get_upjuk(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_reg
    from action_raven2 import menu_open
    from clean_screen_raven2 import clean_screen

    try:
        print("get_upjuk")

        get_ = False
        get_count = 0
        while get_ is False:
            get_count += 1
            if get_count > 4:
                get_ = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\upjuk\\title_upjuk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title_upjuk", imgs_)

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\upjuk\\upjuk_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(140, 180, 210, 500, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("upjuk_point_1", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\get.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 370, 560, 450, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("get", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\close_window.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 900, 600, 1000, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("close_window", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\upjuk\\upjuk_point_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(140, 180, 210, 500, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("upjuk_point_1", imgs_)
                                    click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)
                                    time.sleep(0.5)
                                    click_pos_2(870, 1000, cla)
                                    time.sleep(0.2)
                                    click_pos_2(870, 1000, cla)
                                    time.sleep(0.2)
                                    click_pos_2(870, 1000, cla)
                                    time.sleep(0.2)
                                else:
                                    break
                        time.sleep(0.5)
                else:
                    get_ = True
                    clean_screen(cla)


            else:
                menu_open(cla)

                is_ = False

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\title_post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\upjuk\\menu_upjuk.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 440, 960, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_upjuk", imgs_)

                            x_reg = imgs_.x
                            y_reg = imgs_.y

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\menu_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_reg(x_reg, y_reg - 60, x_reg + 35, y_reg, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("upjuk: menu_point", imgs_)
                                click_pos_reg(x_reg, y_reg, cla)
                                is_ = True
                    time.sleep(0.5)
                if is_ == False:
                    get_ = True
                    clean_screen(cla)

    except Exception as e:
        print(e)
        return 0


def get_sangjum(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_reg
    from action_raven2 import confirm_all, menu_open, skip_click
    from clean_screen_raven2 import clean_screen

    try:
        print("get_sangjum")

        get_ = False
        get_count = 0
        while get_ is False:
            get_count += 1
            if get_count > 4:
                get_ = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\sangjum\\title_sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\sangjum\\ilgwal_goomae_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(155, 315, 260, 370, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("ilgwal_goomae_title", imgs_)

                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\sangjum\\checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(175, 615, 270, 660, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            result_confirm = confirm_all(cla)
                            if result_confirm == True:
                                time.sleep(0.3)
                                confirm_all(cla)
                                time.sleep(0.3)
                                confirm_all(cla)
                                time.sleep(0.5)
                                skip_click
                                get_ = True
                                break
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\sangjum\\all_select_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(175, 615, 270, 660, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("all_select_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)




                else:
                    for i in range(5):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\sangjum\\anymore_ilgwal_massage.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(370, 100, 600, 170, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("anymore_ilgwal_massage", imgs_)
                            get_ = True
                            break
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\sangjum\\ilgwal_goomae_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(155, 315, 260, 370, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\sangjum\\ilgwal_goomae_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 970, 200, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("ilgwal_goomae_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)


            else:
                menu_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_x.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(630, 30, 780, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("close_btn_x..", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\sangjum\\title_sangjum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\sangjum\\menu_sanjum.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(600, 30, 960, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_sanjum", imgs_)

                                x_reg = imgs_.x
                                y_reg = imgs_.y
                                click_pos_reg(x_reg, y_reg, cla)
                    time.sleep(0.5)

        clean_screen(cla)

    except Exception as e:
        print(e)
        return 0
