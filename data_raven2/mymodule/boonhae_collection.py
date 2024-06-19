import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def collection_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import confirm_all, menu_open_pure, skip_click
    from clean_screen_raven2 import clean_screen

    try:
        print("collection_start")

        col_ = False
        col_count = 0
        while col_ is False:
            col_count += 1
            if col_count > 7:
                col_ = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\title_collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title_collection", imgs_)

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\col_common.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 80, 200, 600, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("col_common", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\col_jangbi.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 80, 200, 600, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("col_jangbi", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)


                col_point_count = 0
                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\col_common.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 80, 200, 600, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("col_common", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\col_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 140, 670, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("col_point", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            time.sleep(0.3)

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\sign_up_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(815, 970, 940, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("sign_up_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                for c in range(5):
                                    confirm_all(cla)
                                    skip_click(cla)
                                    time.sleep(0.1)
                        else:
                            col_point_count += 1
                            if col_point_count > 2:
                                col_ = True
                                clean_screen(cla)
                                break

                    time.sleep(0.5)

                # 고급 등록
                if v_.onCollection == True:
                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\col_gogb_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 80, 200, 600, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("col_gogb_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\col_gogb_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(20, 80, 200, 600, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("col_gogb_2", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\col_jangbi.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 80, 200, 600, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("col_jangbi", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)


                    col_point_count = 0
                    for i in range(10):
                        is_gogb = False
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\col_gogb_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 80, 200, 600, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("col_gogb_1", imgs_)
                            is_gogb = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.3)
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\col_gogb_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(20, 80, 200, 600, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("col_gogb_2", imgs_)
                                is_gogb = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.3)
                                
                        if is_gogb == True:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\col_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(450, 140, 670, 1020, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("col_point", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                time.sleep(0.3)

                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\sign_up_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(815, 970, 940, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("sign_up_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                    for c in range(5):
                                        confirm_all(cla)
                                        skip_click(cla)
                                        time.sleep(0.1)
                            else:
                                col_point_count += 1
                                if col_point_count > 2:
                                    col_ = True
                                    clean_screen(cla)
                                    break

                        time.sleep(0.5)


            else:
                menu_open_pure(cla)
                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\title_collection.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\collection\\menu_collection.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 120, 960, 450, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_collection", imgs_)
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            click_pos_reg(x_reg, y_reg, cla)
                    time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0


def boonhae_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import confirm_all, bag_open
    from clean_screen_raven2 import clean_screen

    try:
        print("boonhae_start")

        boonhae_ = False
        boonhae_count = 0
        while boonhae_ is False:
            boonhae_count += 1
            if boonhae_count > 7:
                boonhae_ = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\boonhae_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 960, 900, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                x_reg = imgs_.x
                y_reg = imgs_.y
                # click_pos_reg(x_reg, y_reg, cla)

                for i in range(4):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\jungsoo.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(320, 120, 590, 225, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jungsoo", imgs_)
                        click_pos_reg(x_reg, y_reg, cla)
                        time.sleep(0.5)
                        result_confirm = confirm_all(cla)
                        if result_confirm == True:
                            break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\common_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 840, 420, 880, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("common_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                            if v_.onCollection == True:
                                click_pos_2(460, 865, cla)
                                time.sleep(0.5)

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\include_collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 930, 460, 970, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("include_collection", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                    time.sleep(0.5)

                clean_screen(cla)
                boonhae_ = True

                # for i in range(10):
                #     result_confirm = confirm_all(cla)
                #
                #     if result_confirm == True:
                #         clean_screen(cla)
                #         boonhae_ = True
                #         break
                #     else:
                #         full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\boonhae_ready.PNG"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(430, 920, 470, 970, cla, img, 0.8)
                #         if imgs_ is not None and imgs_ != False:
                #             print("boonhae_ready", imgs_)
                #             click_pos_reg(x_reg, y_reg, cla)
                #         else:
                #             full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\common_btn.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(330, 840, 420, 880, cla, img, 0.8)
                #             if imgs_ is not None and imgs_ != False:
                #                 print("common_btn", imgs_)
                #                 click_pos_reg(imgs_.x, imgs_.y, cla)
                #                 time.sleep(0.5)
                #
                #                 full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\include_collection.PNG"
                #                 img_array = np.fromfile(full_path, np.uint8)
                #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #                 imgs_ = imgs_set_(330, 930, 460, 970, cla, img, 0.8)
                #                 if imgs_ is not None and imgs_ != False:
                #                     print("include_collection", imgs_)
                #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                #     time.sleep(0.5)



            else:
                bag_open(cla)
                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\bag_right_janbi_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(890, 160, 960, 500, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("bag_bottom_boonhae_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        time.sleep(0.5)

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\boonhae_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 960, 900, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\bag_bottom_boonhae_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 960, 900, 1020, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("bag_bottom_boonhae_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0



