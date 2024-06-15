import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def game_start_screen(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from massenger import line_to_me



    try:

        # 완전 바깥 화면인지 파악하며 기다리기
        game_ready(cla)


        # 실수로 새 캐릭터 클릭시...
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\class_select.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(20, 30, 200, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # 이건 잘못 클릭시 나가기
            click_pos_2(45, 60, cla)
            print("class_select", imgs_)
            why = "캐릭 선택 잘 못 누름"
            line_to_me(cla, why)

            for i in range(10):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 900, 920, 1020, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.5)

        # 캐릭터 선택 화면
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 900, 920, 1020, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            character_change(cla, character_id)

        else:
            dir_path = "C:\\my_games\\" + str(v_.game_folder) + ""
            if cla == 'one':
                file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
            elif cla == 'two':
                file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
            elif cla == 'three':
                file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
            elif cla == 'four':
                file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"
            elif cla == 'five':
                file_path = dir_path + "\\mysettings\\myschedule\\five_now_id.txt"
            elif cla == 'six':
                file_path = dir_path + "\\mysettings\\myschedule\\six_now_id.txt"

            same = False

            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    read_id = file.read()
                    if str(character_id) == str(read_id):
                        # 메뉴 안 열어도 됨
                        same = True
            if same == False:
                character_change(cla, character_id)


    except Exception as e:
        print(e)

def character_change(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_raven2 import out_check, menu_open, confirm_all

    from massenger import line_to_me
    try:



        print(str(character_id), "번으로 캐릭터 체인지")


        cha_select = False
        cha_select_count = 0
        while cha_select is False:
            cha_select_count += 1
            if cha_select_count > 10:
                cha_select = True
                line_to_me(cla, "처음 스타트 화면에 문제가 있다.")

            # 실수로 새 캐릭터 클릭시...
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\class_select.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                # 이건 잘못 클릭시 나가기
                click_pos_2(45, 60, cla)
                print("class_select", imgs_)
                why = "캐릭 선택 잘 못 누름"
                line_to_me(cla, why)

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 900, 920, 1020, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)

            # 저장된 캐릭 번호 불러오기
            dir_path = "C:\\my_games\\" + str(v_.game_folder) + ""
            if cla == 'one':
                file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
            elif cla == 'two':
                file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
            elif cla == 'three':
                file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
            elif cla == 'four':
                file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"
            elif cla == 'five':
                file_path = dir_path + "\\mysettings\\myschedule\\five_now_id.txt"
            elif cla == 'six':
                file_path = dir_path + "\\mysettings\\myschedule\\six_now_id.txt"

            # 캐릭터 선택 화면
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 900, 920, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                x_reg = imgs_.x
                y_reg = imgs_.y

                # select 1 (730, 360)
                # select 2 (730, 435)

                y_click = 50 + (int(character_id) * 68)

                click_pos_2(777, y_click, cla)
                time.sleep(0.5)
                click_pos_reg(x_reg, y_reg, cla)
                time.sleep(0.1)

                #진입 버튼 누르면서 캐릭번호 저장하기
                save = False
                save_count = 0
                while save is False:
                    save_count += 1
                    if save_count > 15:
                        save = True
                    if os.path.isfile(file_path) == True:
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            read_id = file.read()
                            if str(character_id) == str(read_id):
                                save = True
                            else:
                                with open(file_path, "w", encoding='utf-8-sig') as file:
                                    file.write(str(character_id))
                            time.sleep(0.3)
                    else:
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(str(character_id))

                # 대기 화면 있는지 확인하면서 진입확인하기
                joined = False
                joined_count = 0
                while joined is False:
                    joined_count += 1
                    if joined_count > 30:
                        joined = True

                    result_out = out_check(cla)
                    if result_out == True:
                        joined = True
                        cha_select = True

                        print("게임 접속 끝")
                        time.sleep(0.1)
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 900, 920, 1020, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            x_reg = imgs_.x
                            y_reg = imgs_.y

                            # select 1 (730, 360)
                            # select 2 (730, 435)

                            y_click = 50 + (int(character_id) * 68)

                            click_pos_2(777, y_click, cla)
                            time.sleep(0.5)
                            click_pos_reg(x_reg, y_reg, cla)
                            time.sleep(0.1)

                    time.sleep(1)
            else:
                # 캐릭 번호와 체인지 하려는 번호 비교하기

                same = False

                if os.path.isfile(file_path) == True:
                    with open(file_path, "r", encoding='utf-8-sig') as file:
                        read_id = file.read()
                        if str(character_id) == str(read_id):
                            # 메뉴 안 열어도 됨
                            same = True
                            cha_select = True
                if same == False:

                    # 포션만 채우기(수집 분해도 함)

                    # 장비 빼기

                    # 메뉴 열기
                    menu_open(cla)
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\menu_character_select.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 930, 920, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("menu_character_select", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        for i in range(5):
                            result_confirm = confirm_all(cla)
                            if result_confirm == True:
                                break
                            time.sleep(0.5)


                else:
                    print("같은 번호의 캐릭이라서 체인지 안함")

    except Exception as e:
        print(e)

def game_ready(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, text_check_get
    from action_raven2 import confirm_all


    try:

        ready_ = False

        # 완전 바깥일 경우 일딴 들어가기
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\gameout\\my_character_seach.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 900, 950, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            confirm_all(cla)
            time.sleep(0.3)


            click_pos_2(500, 600, cla)



            for i in range(10):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 900, 920, 1020, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\join_ready_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        ready_ = True
                        break
                time.sleep(0.5)

        else:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\join_ready_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                ready_ = True
            else:
                confirm_all(cla)
            #     for i in range(10):
            #         full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\gameout\\my_character_seach.PNG"
            #         img_array = np.fromfile(full_path, np.uint8)
            #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #         imgs_ = imgs_set_(800, 900, 950, 1000, cla, img, 0.8)
            #         if imgs_ is not None and imgs_ != False:
            #             break
            #         else:
            #             result_confirm = confirm_all(cla)
            #         time.sleep(0.5)


        # 접속대기일 경우 기다리기
        game_ready_count = 0
        while ready_ is True:

            result = "none"

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\join_ready_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                game_ready_count += 1

                result = text_check_get(440, 520, 550, 540, cla)
                print("result", result)

                print("기다리는중", game_ready_count, "초", result)


            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 900, 920, 1020, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    ready_ = False
            time.sleep(1)



    except Exception as e:
        print(e)