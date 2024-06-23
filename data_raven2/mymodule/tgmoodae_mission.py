import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tgmoodae_mission_start(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import inven_check, menu_open, confirm_all, skip_click
    from schedule import myQuest_play_add
    from clean_screen_raven2 import clean_screen
    from potion_raven2 import potion_check
    from dead_raven2 import dead_check_2, dead_recover

    try:
        print("tgmoodae_mission_start", data)

        tg_in = False
        tg_in_count = 0
        while tg_in is False:
            tg_in_count += 1
            if tg_in_count > 5:
                tg_in = True
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\quest_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(320, 30, 420, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest_title", imgs_)
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\tcmoodae_mission_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(390, 30, 540, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("tcmoodae_mission_title", imgs_)
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
                        imgs_ = imgs_set_(560, 80, 620, 600, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("mission_ing", imgs_)

                            click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                            time.sleep(0.3)

                            # 특무대 진행

                            click_pos_2(820, 1000, cla)
                            time.sleep(0.3)

                            for i in range(10):
                                result_confirm = confirm_all(cla)
                                if result_confirm == False:
                                    break

                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\tg_ing.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 80, 620, 160, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("tg_ing...현재 진행중...", imgs_)
                                    tg_in = True
                                    break
                                time.sleep(0.2)

                            if tg_in == True:
                                clean_screen(cla)

                                for i in range(20):

                                    print(i, "번째 체크중")
                                    result_dead_2 = dead_check_2(cla)
                                    if result_dead_2 == True:
                                        dead_recover(cla)
                                        break
                                    else:
                                        result_buy = potion_check(cla)
                                        if result_buy == True:
                                            break

                                    time.sleep(1)

                        else:
                            # ing 없으면 보상받기 후 특무대 받기
                            print("get tgmoodae")
                            tgmoodae_mission_get_ready(cla, data)

                            # 완료부터 없애기
                            for i in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\maul_complete.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(210, 80, 270, 500, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                                    time.sleep(0.2)
                                    click_pos_2(820, 1000, cla)
                                    result_inven = inven_check(cla)
                                    if result_inven == True:
                                        skip_click(cla)
                                        time.sleep(0.2)
                                    else:
                                        break
                                else:
                                    break
                                time.sleep(0.3)

                            if result_inven == True:

                                # 특무대 받다가 진행 없으면 완료
                                tgmoodae_mission_get(cla)

                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\maul_ing.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(210, 80, 270, 500, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("ing")
                                    click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                                    time.sleep(0.5)

                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\jadong\\immediately_move.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(770, 900, 930, 950, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("immediately_move", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)

                                    confirm_all(cla)
                                else:
                                    tg_in = True
                                    myQuest_play_add(cla, data)
                                    clean_screen(cla)
                                    print("끝")
                            else:
                                tg_in_count = 0
                    else:
                        tg_in_count = 0
                else:
                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\tcmoodae_mission_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(390, 30, 540, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("break : tcmoodae_mission_title", imgs_)
                            break
                        else:
                            click_pos_2(920, 280, cla)
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
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\quest_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(320, 30, 420, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)


    except Exception as e:
        print(e)
        return 0



def tgmoodae_mission_get(cla):
    import numpy as np
    import cv2
    import random
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_raven2 import confirm_all, inven_check, skip_click
    from clean_screen_raven2 import clean_screen


    from massenger import line_to_me

    try:
        print("tgmoodae_mission_get")


        # 완료부터 없애기
        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\maul_complete.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(210, 80, 270, 500, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                time.sleep(0.2)
                click_pos_2(820, 1000, cla)
                result_inven = inven_check(cla)
                if result_inven == True:
                    skip_click(cla)
                    time.sleep(0.2)
                else:
                    break
            else:
                break
            time.sleep(0.3)

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\maul_get_point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_for(210, 80, 270, 500, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # print("maul_get_point", imgs_)
            #
            len_imgs = len(imgs_)
            # print("len_imgs", len_imgs)
            # print("imgs_[len_imgs - 1]", imgs_[len_imgs - 1])
            # x_reg = imgs_[len_imgs - 1][0]
            y_reg = imgs_[len_imgs - 1][1]

            for i in range(10):
                is_clicked = False
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\three.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 90, 70, y_reg + 30, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("three", imgs_)
                    click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                    is_clicked = True
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\two.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 90, 70, y_reg + 30, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("two", imgs_)
                        click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                        is_clicked = True
                if is_clicked == True:
                    time.sleep(0.5)
                    click_pos_2(820, 1000, cla)
                else:
                    click_pos_2(150, 1000, cla)
                    time.sleep(0.5)
                    confirm_all(cla)
                time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0


def tgmoodae_mission_get_ready(cla, data):
    import numpy as np
    import cv2
    import random
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import out_check, confirm_all, move_check
    from clean_screen_raven2 import clean_screen

    from massenger import line_to_me

    try:
        print("tgmoodae_mission_get_ready")

        # 특무대_엘베름, 특무대_하코트

        tgmoodae = data.split("_")

        tgmoodae_detail = tgmoodae[1]

        clean_screen(cla)

        spot_in = False
        spot_in_count = 0

        while spot_in is False:
            spot_in_count += 1
            if spot_in_count > 7:
                spot_in = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\map\\map_open.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 950, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("map_open", imgs_)

                is_tg = False

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\map_tgmoodae_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 70, 80, 570, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("map_tgmoodae_btn", imgs_)
                        is_tg = True
                        break
                    else:
                        click_pos_2(305, 980, cla)

                    time.sleep(0.5)

                if is_tg == False:
                    why = "맵에 특무대 지정해줘야한다"

                else:

                    if tgmoodae_detail == "엘베름":
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\elbelm_kingdom.PNG"
                    elif tgmoodae_detail == "하코트":
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\harcote.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(70, 70, 230, 570, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print(tgmoodae_detail, imgs_)
                        x_reg = imgs_.x
                        y_reg = imgs_.y
                        click_pos_reg(x_reg, y_reg, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\tg_junlyung_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 130, 850, 570, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("tg_junlyung_click", imgs_)
                                break
                            time.sleep(0.4)

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\tg_junlyung_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 130, 850, 570, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("tg_junlyung_click", imgs_)

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\jadong\\immediately_move.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(770, 900, 930, 950, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("immediately_move", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                for i in range(10):
                                    result_out = out_check(cla)
                                    if result_out == True:
                                        break
                                    else:
                                        confirm_all(cla)
                                    time.sleep(0.5)

                                # 상인들 보기

                                for i in range(5):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\jabhwa_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 100, 200, 260, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jabhwa_btn", imgs_)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\map_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(190, 100, 280, 160, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("map_btn", imgs_)
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\change_btn_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(190, 100, 280, 160, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("change_btn_1", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            else:
                                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\change_btn_2.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(190, 100, 280, 160, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("change_btn_2", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.7)

                    else:
                        is_tg = False

                        why = "맵에 특무대를 다시 지정해줘라"


                    # 이제 찾아가자
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\maul_tg_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 200, 200, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("maul_tg_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        move_ = True
                        move_count = 0
                        while move_ is True:
                            result_move = move_check(cla)
                            if result_move == True:
                                move_count = 0

                            else:
                                move_count += 1
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\title_tgmoodae.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 230, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("title_tgmoodae", imgs_)
                                    move_ = False
                                    spot_in = True

                                else:
                                    if (move_count % 3 == 0):
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\maul_tg_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(50, 200, 200, 300, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("maul_tg_btn", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            if move_count > 19:
                                move_ = False

                            time.sleep(1)
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tgmoodae_mission\\title_tgmoodae.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 230, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("title_tgmoodae", imgs_)
                            spot_in = True


                if is_tg == False:
                    spot_in = True

                    line_to_me(cla, why)

                    dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
                    file_path = dir_path + "\\start.txt"
                    # cla.txt
                    cla_data = str(v_.now_cla) + "cla"
                    file_path2 = dir_path + "\\" + cla_data + ".txt"
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        data = 'no'
                        file.write(str(data))
                        time.sleep(0.2)
                    with open(file_path2, "w", encoding='utf-8-sig') as file:
                        data = v_.now_cla
                        file.write(str(data))
                        time.sleep(0.2)
                    os.execl(sys.executable, sys.executable, *sys.argv)

            else:

                for i in range(4):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\map\\map_open.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 950, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("map_open", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\map_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(190, 100, 280, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("map_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\jabhwa_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 100, 200, 260, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("jabhwa_btn", imgs_)
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\change_btn_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(190, 100, 280, 160, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("change_btn_1", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\change_btn_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(190, 100, 280, 160, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("change_btn_2", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                clean_screen(cla)
                    time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0



