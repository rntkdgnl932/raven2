import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


def potion_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_2
    from action_raven2 import juljun_check, out_check
    import pyautogui
    try:
        print("potion_check")

        is_buying = False

        is_potion = False

        is_pass = False

        result_juljun = juljun_check(cla)
        if result_juljun[0] == True:
            print("절전모드")
            for i in range(10):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\juljun_potion\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(450, 1000, 477, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    many = i * 100
                    print_say = str(many) + "개 이상"
                    print("num", print_say)
                    is_potion = True

                    pos = (450, 1000, 477 - 450, 1020 - 1000)
                    pyautogui.screenshot("asd.png", region=pos)

                    break
            if is_potion == False:

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\juljun_off.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(445, 755, 500, 810, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(480, 1000, cla)
                    time.sleep(0.5)

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\juljun_potion\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 840, 477, 970, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        many = i * 100
                        print_say = str(many) + "개 이상"
                        print("num", print_say)
                        is_potion = True
                        pos = (450, 840, 477 - 450, 970 - 840)
                        pyautogui.screenshot("asd.png", region=pos)
                        break
        else:
            print("절전모드 아님")

            result_out = out_check(cla)
            if result_out == True:

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\out_potion\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 982, 288, 1000, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        many = i * 100
                        print_say = str(many) + "개 이상"
                        print("num", print_say)
                        is_potion = True

                        pos = (270, 982, 477 - 270, 1000 - 982)
                        pyautogui.screenshot("asd.png", region=pos)

                        break
                if is_potion == False:

                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\out_off.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(265, 805, 310, 845, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            click_pos_2(290, 980, cla)
                        time.sleep(0.5)

                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\out_potion\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(270, 860, 288, 960, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            many = i * 100
                            print_say = str(many) + "개 이상"
                            print("num", print_say)

                            pos = (270, 860, 288 - 270, 960 - 860)
                            pyautogui.screenshot("asd.png", region=pos)

                            break
                        else:
                            if str(i) == "1":
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\click_out_potion\\1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(270, 860, 288, 960, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    many = i * 100
                                    print_say = str(many) + "개 이상"
                                    print("num", print_say)

                                    pos = (270, 860, 288 - 270, 960 - 860)
                                    pyautogui.screenshot("asd.png", region=pos)

                                    break

            else:
                print("바깥화면 아니다.")
                is_pass = True

        if is_potion == False:
            if is_pass == False:
                v_.potion_count += 1

            if v_.potion_count > 2:
                potion_buy(cla)
                is_buying = True
        else:
            if v_.potion_count > 0:
                v_.potion_count -= 1
        return is_buying
    except Exception as e:
        print(e)
        return 0


def potion_buy(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import go_maul, move_check, confirm_all, juljun_check, out_check, skip_click
    from clean_screen_raven2 import clean_screen
    from chango_raven2 import chango_in
    from massenger import line_to_me
    from schedule import myQuest_play_check

    try:
        print("potion_buy")

        need_skip = False

        # 마을 가기전 튜토 체크하기
        result_schedule = myQuest_play_check(cla, "check")
        character_id = result_schedule[0][1]
        result_schedule_ = result_schedule[0][2]

        if result_schedule_ == "튜토육성":

            result_juljun = juljun_check(cla)
            if result_juljun == False:
                result_out = out_check(cla)
                if result_out == False:

                    need_skip = True

        if need_skip == True:
            click_pos_2(920, 860, cla)
            time.sleep(1)
            result_skip = skip_click(cla)
            if result_skip == False:
                why = "이유가 뭘까"
                print(why)
                line_to_me(cla, why)
            else:
                click_pos_2(920, 860, cla)

        else:
            # 먼저 마을로 가기

            go_maul(cla)

            confirm_all(cla)

            # 창고 한번 가주기

            chango_in(cla)

            # 마을인지 확인되면 정해진 포션 사기

            buy_ = False
            buy_count = 0

            while buy_ is False:
                buy_count += 1
                if buy_count > 7:
                    buy_ = True

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\auto_buy_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 980, 600, 1020, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("auto_buy_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    anymore_buy = False

                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\money_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 980, 650, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("money_point", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\anymore_buy.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(460, 110, 650, 160, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("anymore_buy", imgs_)
                                anymore_buy = True
                                break
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\auto_buy_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 980, 600, 1020, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("auto_buy_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                    if anymore_buy == True:
                        v_.potion_count = 0
                        # clean_screen(cla)
                        buy_ = True
                    else:
                        for i in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\money_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(600, 980, 650, 1020, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("money_point", imgs_)
                                click_pos_2(815, 1000, cla)
                            else:
                                v_.potion_count = 0
                                # clean_screen(cla)
                                buy_ = True
                                break
                            time.sleep(0.5)

                    # 이제 호감도 선물하기

                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\hogamdo_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(320, 80, 440, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("hogamdo_title", imgs_)
                            break
                        else:
                            click_pos_2(920, 400, cla)
                        time.sleep(0.5)


                    # 첫번째
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\sojin.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 270, 860, 340, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("sojin", imgs_)
                        hogamdo_1 = True
                    else:
                        hogamdo_1 = False

                    if hogamdo_1 == False:
                        confirm = False
                        for i in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\hogamdo_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 560, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("hogamdo_confirm", imgs_)
                                confirm = True
                                break
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\anymore_item.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 105, 580, 160, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("anymore_item", imgs_)
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\most_item.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(410, 110, 560, 160, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("most_item", imgs_)
                                        click_pos_2(805, 1000, cla)
                                        time.sleep(0.5)
                                    else:
                                        click_pos_2(840, 330, cla)
                                        time.sleep(0.5)
                            time.sleep(0.5)
                        if confirm == True:
                            for i in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\hogamdo_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 560, 630, 630, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    result_skip = skip_click(cla)
                                    if result_skip == True:
                                        break
                                    else:
                                        time.sleep(0.5)
                                time.sleep(0.5)

                    # 두번째
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\sojin.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 390, 860, 460, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("sojin", imgs_)
                        hogamdo_2 = True
                    else:
                        hogamdo_2 = False

                    if hogamdo_2 == False:
                        confirm = False
                        for i in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\hogamdo_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 560, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("hogamdo_confirm", imgs_)
                                confirm = True
                                break
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\anymore_item.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 105, 580, 160, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("anymore_item", imgs_)
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\most_item.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(410, 110, 560, 160, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("most_item", imgs_)
                                        click_pos_2(805, 1000, cla)
                                        time.sleep(0.5)
                                    else:
                                        click_pos_2(840, 455, cla)
                                        time.sleep(0.5)
                            time.sleep(0.5)
                        if confirm == True:
                            for i in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\hogamdo_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 560, 630, 630, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    result_skip = skip_click(cla)
                                    if result_skip == True:
                                        break
                                    else:
                                        time.sleep(0.5)
                                time.sleep(0.5)
                    # 마무리하고 나가기
                    clean_screen(cla)

                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\jabhwa_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 100, 200, 260, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jabhwa_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        move_count = 0
                        for i in range(50):
                            result_move = move_check(cla)
                            if result_move == False:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\auto_buy_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 980, 600, 1020, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("auto_buy_btn", imgs_)
                                    break
                                else:
                                    move_count += 1
                                    if move_count > 3:
                                        break
                            else:
                                move_count = 0
                            time.sleep(1)
                time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def dead_recover(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import confirm_all
    from clean_screen_raven2 import clean_screen

    try:
        print("dead_recover")

        recover = False

        clean_screen(cla)

        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\exp_recover_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(260, 260, 400, 400, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                recover = True
                break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\boohwal_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(530, 30, 650, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("boohwal_btn", imgs_)
            time.sleep(0.5)

        if recover == True:

            for i in range(15):

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\exp_recover_last.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 440, 530, 500, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("exp_recover_last", imgs_)

                    confirm_all(cla)

                    break

                else:

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\exp_recover_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(260, 260, 400, 400, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("exp_recover_title", imgs_)

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\exp_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 380, 380, 680, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("exp_click", imgs_)
                            # 클릭 후 590, 735
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            click_pos_2(590, 735, cla)

                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\boohwal_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(530, 30, 650, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("boohwal_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

        clean_screen(cla)


    except Exception as e:
        print(e)
        return 0



