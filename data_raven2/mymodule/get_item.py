import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def get_item_start(cla):

    from guild_raven2 import guild_check

    try:
        print("get_item_start")
        get_post(cla)

        get_gyeyak_sohwan(cla)

        get_upjuk(cla)

        get_sangjum(cla)

        guild_check(cla)


    except Exception as e:
        print(e)
        return 0


def get_post(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_reg
    from action_raven2 import inven_check, confirm_all, menu_open
    from clean_screen_raven2 import clean_screen
    from stop_event18 import _stop_please

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

                is_point = False

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\post_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 80, 110, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("post_point_1", imgs_)
                    is_point = True
                    click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)

                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 130, 210, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("post_point_1 : gyobum_point_2", imgs_)
                        is_point = True
                        click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)
                if is_point == True:
                    time.sleep(0.5)
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
                                            time.sleep(0.5)
                                            _stop_please(cla)
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


def get_gyeyak_sohwan(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_reg, drag_pos
    from action_raven2 import inven_check, confirm_all, menu_open
    from clean_screen_raven2 import clean_screen
    from stop_event18 import _stop_please

    try:
        print("get_gyeyak_sohwan")

        get_ = False
        get_count = 0
        while get_ is False:
            get_count += 1
            if get_count > 10:
                get_ = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\title_gyeyak_sohwan.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title_gyeyak_sohwan", imgs_)

                is_point = False

                for i in range(10):

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 80, 580, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("gyeyak_title", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 300, 880, 400, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("gyeyak_point_1", imgs_)
                            is_point = True
                            click_pos_reg(imgs_.x - 100, imgs_.y + 150, cla)

                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 300, 880, 400, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("gyeyak_point_2", imgs_)
                                is_point = True
                                click_pos_reg(imgs_.x - 100, imgs_.y + 150, cla)
                    time.sleep(0.5)

                if is_point == True:

                    # 여기 반복

                    for g in range(7):

                        is_goods = False
                        # 1
                        for i in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_ready.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 400, 530, 450, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                is_goods = True
                                break

                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\lack_goods.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 400, 530, 450, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("lack_goods", imgs_)

                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_point_mini_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(90, 90, 140, 360, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("gyeyak_point_mini_1", imgs_)
                                        click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)
                                        time.sleep(0.5)
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(400, 970, 630, 1030, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("gyeyak_btn", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_point_mini_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(90, 90, 140, 360, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("gyeyak_point_mini_2", imgs_)
                                            click_pos_reg(imgs_.x - 20, imgs_.y + 5, cla)
                                            time.sleep(0.5)
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_btn.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 970, 630, 1030, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("gyeyak_btn", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        if is_goods == True:
                            # 2
                            for i in range(10):

                                drag = False

                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\rare_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(450, 490, 510, 540, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("rare_confirm", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    for d in range(10):
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\milgi_drag.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(390, 940, 570, 1010, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\milgi_drag_2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(390, 940, 570, 1010, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                break
                                        time.sleep(0.2)


                                    drag_pos(400, 540, 800, 540, cla)
                                    drag = True
                                    time.sleep(2)
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\rare_confirm_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(440, 480, 520, 540, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("rare_confirm_2", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        for d in range(10):
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\milgi_drag.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(390, 940, 570, 1010, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                break
                                            else:
                                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\milgi_drag_2.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(390, 940, 570, 1010, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    break
                                            time.sleep(0.2)

                                        drag_pos(400, 650, 800, 650, cla)
                                        drag = True
                                        time.sleep(2)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\close_window.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(400, 900, 600, 1040, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("close_window", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.5)
                                            break

                                        else:
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\screen_click3.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(300, 900, 600, 1040, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("screen_click3", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.5)
                                                break

                                            else:
                                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_ready.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(480, 400, 530, 450, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("gyeyak_ready", imgs_)
                                                    confirm_all(cla)

                                time.sleep(0.5)

                            if drag == True:
                                for d in range(10):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\exit.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 980, 560, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("gyeyak_ready", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        drag_pos(400, 540, 800, 540, cla)
                                        time.sleep(0.5)
                                    time.sleep(2)
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\milgi_drag.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 940, 570, 1010, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    drag_pos(400, 560, 800, 560, cla)

                            for i in range(10):

                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 80, 580, 140, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("gyeyak_title", imgs_)
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\exit.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 980, 560, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("gyeyak_ready", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                time.sleep(0.3)

                        else:
                            for i in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\gyeyak_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 80, 580, 140, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("gyeyak_title", imgs_)


                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\lack_goods.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 400, 530, 450, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("lack_goods", imgs_)
                                        confirm_all(cla)
                                        time.sleep(0.5)

                                    click_pos_2(25, 60, cla)
                                    time.sleep(1)
                                else:
                                    break
                                time.sleep(0.2)
                            # 반복 끝
                            break
                        time.sleep(0.5)
                else:
                    get_ = True
                    clean_screen(cla)


            else:
                menu_open(cla)

                is_ = False

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\title_gyeyak_sohwan.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\menu_gyeyak_sohwan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(760, 140, 850, 220, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_gyeyak_sohwan", imgs_)

                            x_reg = imgs_.x
                            y_reg = imgs_.y

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\menu_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_reg(x_reg, y_reg - 60, x_reg + 35, y_reg, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("gyeyak_sohwan : menu_point", imgs_)
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
