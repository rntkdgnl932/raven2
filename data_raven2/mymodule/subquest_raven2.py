import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def subquest_start(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import inven_check, menu_open, confirm_all, skip_click
    from clean_screen_raven2 import clean_screen

    try:
        print("subquest_start", data)

        # data => 벨루시아, 데론, 로메른, 시너림

        sub_in = False
        sub_in_count = 0
        while sub_in is False:
            sub_in_count += 1
            if sub_in_count > 5:
                sub_in = True
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\quest_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(320, 30, 420, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest_title", imgs_)
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\sub_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(390, 30, 540, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("sub_title", imgs_)
                    result_inven = True
                    # 완료 시키기
                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\mission_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(560, 80, 620, 600, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                            time.sleep(0.3)
                            click_pos_2(760, 1000, cla)
                            result_inven = inven_check(cla)
                            if result_inven == True:
                                skip_click(cla)
                            else:
                                break
                        else:
                            break
                        time.sleep(0.2)

                    if result_inven == True:

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\mission_ing.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(560, 80, 620, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("mission_ing", imgs_)

                            click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                            time.sleep(0.3)

                            # 서브 진행

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\now_move_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(760, 970, 880, 1020, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("now_move_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)

                                for i in range(10):
                                    result_confirm = confirm_all(cla)
                                    if result_confirm == False:
                                        break

                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\tg_ing.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(300, 80, 620, 160, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("서브퀘...현재 진행중...", imgs_)
                                        sub_in = True
                                        break
                                    time.sleep(0.2)

                                if sub_in == True:
                                    clean_screen(cla)

                                    # 절전모드 후 어택 또는 이동은 진행중이고, 절전모드가 풀리면 스킵 발동 및 브레이크하고 다시 퀘스트 받기 하면 됨

                                    juljun_sub_play(cla)

                        else:
                            # ing 없으면 보상받기 후 특무대 받기
                            subquest_get(cla, data)

                    else:
                        sub_in_count = 0
                else:
                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\sub_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(390, 30, 540, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("break : sub_title", imgs_)
                            break
                        else:
                            click_pos_2(920, 205, cla)
                        time.sleep(0.5)

            else:
                menu_open(cla)

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\menu_quest.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(630, 200, 960, 450, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu_quest", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    for i in range(5):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\quest_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(320, 30, 420, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\not_available.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 80, 800, 250, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("not_available", imgs_)
                                available_sub_play(cla)
                                break
                        time.sleep(0.2)


    except Exception as e:
        print(e)
        return 0

def subquest_get(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos, drag_pos_py
    from action_raven2 import inven_check, menu_open, confirm_all, skip_click
    from schedule import myQuest_play_add
    from clean_screen_raven2 import clean_screen

    try:
        print("subquest_get", data)

        # data = "서브퀘스트_벨루시아"
        now_sub_ready = data.split("_")
        if now_sub_ready[1] == "벨루시아":
            now_sub = "beloosia"
        elif now_sub_ready[1] == "데론":
            now_sub = "delon"
        elif now_sub_ready[1] == "로메른":
            now_sub = "lomeln"
        elif now_sub_ready[1] == "시너림":
            now_sub = "sinerim"



        for i in range(5):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\down_clicked.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 80, 360, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("down_clicked", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)

        for i in range(5):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\down_clicked.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 80, 360, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("down_clicked", imgs_)
                break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\" + str(now_sub) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 80, 440, 1030, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
            time.sleep(0.5)

        # 완료부터 없애기
        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\sub_complete.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(560, 120, 620, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                time.sleep(0.2)
                click_pos_2(760, 1000, cla)
                result_inven = inven_check(cla)
                if result_inven == True:
                    skip_click(cla)
                    time.sleep(0.2)
                else:
                    break
            else:
                break
            time.sleep(0.3)

        is_sub_point = True

        # 즉시이동
        for i in range(7):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\sub_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(390, 30, 540, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sub_title", imgs_)

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\sub_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(560, 120, 620, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("sub_point", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\now_move_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(760, 970, 880, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("now_move_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        confirm_all(cla)
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\sub_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(560, 120, 620, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sub_point", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    drag_pos(450, 850, 450, 300, cla)
                    time.sleep(0.5)
                    drag_pos(450, 850, 450, 300, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\sub_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(560, 120, 620, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("sub_point", imgs_)
                    else:
                        # 완료부터 없애기
                        for c in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\sub_complete.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(560, 120, 620, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                                time.sleep(0.2)
                                click_pos_2(760, 1000, cla)
                                result_inven = inven_check(cla)
                                if result_inven == True:
                                    skip_click(cla)
                                    time.sleep(0.2)
                                else:
                                    break
                            else:
                                break
                            time.sleep(0.3)


                        is_sub_point = False
                        break

            else:
                break
            time.sleep(0.5)
        if is_sub_point == True:
            # 수락
            for i in range(10):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\soolock_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 940, 910, 990, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("soolock_confirm", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    break
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\sub_click_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(610, 850, 700, 950, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("sub_click_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\subquest\\sub_click_btn2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(610, 850, 700, 950, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sub_click_btn2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            confirm_all(cla)
                            skip_click(cla)
                time.sleep(0.5)
        else:
            myQuest_play_add(cla, data)
            clean_screen(cla)

    except Exception as e:
        print(e)
        return 0

def juljun_sub_play(cla):
    from action_raven2 import juljun_check, juljun_on, juljun_off
    from potion_raven2 import potion_check
    from dead_raven2 import dead_check_2, dead_recover
    from clean_screen_raven2 import clean_screen

    try:
        print("juljun_sub_play")



        sub_play = True
        sub_play_count = 0
        sub_break_count = 0
        while sub_play is True:
            sub_play_count += 1
            result_juljun = juljun_check(cla)
            if result_juljun[0] == True:
                if result_juljun[1] == "attack" or result_juljun[1] == "move":
                    sub_break_count = 0

                    print(sub_play_count, "번째 체크중")
                    result_dead_2 = dead_check_2(cla)
                    if result_dead_2 == True:
                        dead_recover(cla)
                        sub_play = False
                    else:
                        result_buy = potion_check(cla)
                        if result_buy == True:
                            sub_play = False
                else:
                    sub_break_count += 1
                    if sub_break_count > 2:
                        sub_play = False
            else:
                juljun_on(cla)
            time.sleep(1)


    except Exception as e:
        print(e)
        return 0

def available_sub_play(cla):
    from potion_raven2 import potion_check
    from dead_raven2 import dead_check_2, dead_recover
    from action_raven2 import juljun_check, juljun_off, juljun_on
    from function_game import click_pos_2

    try:
        print("available_sub_play")



        sub_play = True
        sub_play_count = 0
        while sub_play is True:
            result_juljun = juljun_check(cla)
            if result_juljun[0] == True:
                if result_juljun[1] == "attack" or result_juljun[1] == "move":
                    sub_play = False
                    juljun_sub_play(cla)

                elif result_juljun[1] == "ready":
                    sub_play_count += 1
                    if sub_play_count > 1:
                        sub_play = False
                        juljun_off(cla)
                        time.sleep(0.3)
                        click_pos_2(820, 125, cla)
                        time.sleep(0.3)
                        juljun_on(cla)
            else:
                juljun_on(cla)
            time.sleep(1)


    except Exception as e:
        print(e)
        return 0