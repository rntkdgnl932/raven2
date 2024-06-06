import time
# import os
import sys

import pyautogui

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import out_check, skip_click, move_check, confirm_all, juljun_check, juljun_off, bag_open
    from dead_raven2 import dead_check_2, dead_recover
    from schedule import myQuest_play_add
    from clean_screen_raven2 import clean_screen

    from massenger import line_to_me

    try:
        print("tuto_start")

        result_juljun = juljun_check(cla)
        if result_juljun[0] == True:
            juljun_off(cla)

        result_dead = dead_check_2(cla)

        if result_dead == True:

            dead_recover(cla)

            myQuest_play_add(cla, "튜토육성")



        else:

            # 가방 열렸으면 닫아주기

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\bag_jabhwa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 230, 960, 330, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bag_jabhwa", imgs_)
                clean_screen(cla)

            result_move_check = move_check(cla)

            if result_move_check == True:
                print("피통 및 dead 관리하자")

            else:

                result_out = out_check(cla)

                if result_out == True:

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\quest_yagcho.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(650, 90, 900, 150, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("quest_yagcho", imgs_)
                        bag_open(cla)
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\yagcho_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 75, 900, 850, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)

                            for i in range(3):
                                confirm_all(cla)
                                time.sleep(0.5)
                            clean_screen(cla)
                    else:
                        click_pos_2(880, 105, cla)

                        for i in range(5):
                            result_confirm = confirm_all(cla)
                            if result_confirm == True:
                                break
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\quest_youngyak.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 100, 650, 150, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    bag_open(cla)
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\youngyak_click.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(600, 75, 900, 850, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.2)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.2)

                                        for c in range(3):
                                            confirm_all(cla)
                                            time.sleep(0.5)
                                        clean_screen(cla)
                            time.sleep(0.1)

                        skip_click(cla)

                        way_point_click(cla)

                else:
                    # click_pos_2(480, 600, cla)

                    for i in range(5):
                        skip_click(cla)

                        ################sub##################
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\sub_click_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 850, 700, 950, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sub : sub_click_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\sub_soolock_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 940, 910, 950, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sub : sub_soolock_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        time.sleep(0.1)

                    way_point_click(cla)




    except Exception as e:
        print(e)
        return 0

def quest_complete(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import out_check

    try:
        print("quest_complete")

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\quest_complete_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 450, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("quest_complete_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0


def way_point_click(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos_reg, drag_pos_reg_click
    from action_raven2 import out_check

    try:
        print("way_point_click")

        click_loop = True

        while click_loop is True:

            click_loop = False

            ###############################[[ up ]]##########################
            # up
            x_cal = 0
            y_cal = -40

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\way\\up_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 945, 1025, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("up_1", imgs_)
                click_pos_reg(imgs_.x + x_cal, imgs_.y + y_cal, cla)
                click_loop = True
            else:
                # up_right
                x_cal = 50
                y_cal = -40

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\way\\up_right_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 30, 945, 1025, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("up_right_1", imgs_)
                    click_pos_reg(imgs_.x + x_cal, imgs_.y + y_cal, cla)
                    click_loop = True

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\way\\up_right_long.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 945, 1025, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("up_right_1", imgs_)
                        pyautogui.mouseDown()
                        time.sleep(5)
                        pyautogui.mouseUp()

                else:

                    ###############################[[ down ]]##########################

                    # down
                    x_cal = 0
                    y_cal = +40

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\way\\down_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 945, 1025, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("down_1", imgs_)
                        drag_pos_reg_click(imgs_.x + x_cal, imgs_.y + y_cal, cla)
                        click_loop = True
                    else:
                        # down_left
                        x_cal = -50
                        y_cal = +40

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\way\\down_left_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 30, 945, 1025, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("down_left_1", imgs_)
                            click_pos_reg(imgs_.x + x_cal, imgs_.y + y_cal, cla)
                            click_loop = True


            ###############################[[ drag ]]##########################
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\way\\drag_down_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 945, 1025, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("drag_down_1", imgs_)
                drag_pos_reg_click(imgs_.x, imgs_.y + 30, imgs_.x, imgs_.y + 100, cla)
                click_loop = True

            time.sleep(1)


    except Exception as e:
        print(e)
        return 0
