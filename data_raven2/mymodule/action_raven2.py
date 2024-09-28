import time
# import os
import sys
from PyQt5.QtTest import *



import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def out_check(cla):
    import numpy as np
    import cv2
    import os

    from massenger import line_to_me
    from function_game import imgs_set_, click_pos_reg

    try:

        out_ = False

        # 응답없음 확인하기
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\no_response.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 600, 30, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("no_response", imgs_)
            no_response = True
            for i in range(60):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\no_response.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 600, 30, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("no_response", imgs_)
                else:
                    no_response = False
                    break
                time.sleep(2)
            if no_response == True:
                why = "응답없음 2분 넘어갔다."
                print(why)
                line_to_me(cla, why)

                dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
                file_path = dir_path + "\\start.txt"
                # cla.txt
                cla_data = str(cla) + "cla"
                file_path2 = dir_path + "\\" + cla_data + ".txt"
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    data = 'no'
                    file.write(str(data))
                    time.sleep(0.2)
                with open(file_path2, "w", encoding='utf-8-sig') as file:
                    data = cla
                    file.write(str(data))
                    time.sleep(0.2)
                os.execl(sys.executable, sys.executable, *sys.argv)

        else:
            # 화면 닫기
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\close_window.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 900, 600, 1000, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("close_window", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            # 게임 오류 체크
            game_check(cla)




            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_mode_check.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 50, 600, 120, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                juljun_time_check(cla)
            else:

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\menu_character_select.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 930, 920, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu : menu_character_select...end", imgs_)
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\out\\talk.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(5, 900, 50, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("out : talk", imgs_)
                        out_ = True
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\out\\talk2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(5, 900, 50, 960, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("out : talk", imgs_)
                            out_ = True

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\get.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 370, 560, 450, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_off_result_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 310, 500, 4000, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    confirm_all(cla)


        return out_
    except Exception as e:
        print(e)
        return 0


def attack_on(cla):
    import numpy as np
    import cv2
    import os
    from function_game import click_pos_2

    try:
        print("attack_check")

        click_pos_2(920, 860, cla)

        attack_ = True

        result_inven = inven_check(cla)
        if result_inven == False:
            attack_ = False

        return attack_
    except Exception as e:
        print(e)
        return 0


def juljun_attack_check(cla):
    import numpy as np
    import cv2
    import os
    from function_game import text_check_get_reg, imgs_set_, in_number_check, int_put_

    try:
        print("juljun_attack_check")

        attack_ = False

        result_text_1 = 0
        result_text_2 = 0

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_mode_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 50, 600, 120, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("juljun_attack_check : juljun_mode_check", imgs_)

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_gold.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 100, 50, 300, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("juljun_attack_check : juljun_gold", imgs_)
                x_reg = imgs_.x
                y_reg = imgs_.y
                # 27, 167
                for i in range(20):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_mode_check.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 50, 600, 120, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        result_text_1 = text_check_get_reg(x_reg + 10, y_reg - 10, x_reg + 100, y_reg + 10)
                        result_text_1 = int_put_(result_text_1)
                        result_text_1_num_check = in_number_check(result_text_1)
                        if result_text_1_num_check == True:
                            result_text_1 = int(result_text_1)
                            break
                    else:
                        break
                    time.sleep(1)

                for i in range(20):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_mode_check.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 50, 600, 120, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        result_text_2 = text_check_get_reg(x_reg + 10, y_reg - 10, x_reg + 100, y_reg + 10)
                        result_text_2 = int_put_(result_text_2)
                        result_text_2_num_check = in_number_check(result_text_2)
                        if result_text_2_num_check == True:
                            result_text_2 = int(result_text_2)
                            if result_text_1 != result_text_2:
                                print(result_text_1, result_text_2)
                                attack_ = True
                                break
                    else:
                        break
                    time.sleep(1)

        print("gold...???", result_text_1, result_text_2)

        return attack_
    except Exception as e:
        print(e)
        return 0

def organize_start(cla):

    from boonhae_collection import collection_start, boonhae_start
    from chango_raven2 import chango_in

    try:
        print("organize_start")

        chango_in(cla)
        collection_start(cla)
        boonhae_start(cla)

    except Exception as e:
        print(e)
        return 0

def move_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("move_check")

        move_ = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\quest_move\\quest_move_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 800, 600, 930, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("move : quest_move_1", imgs_)
            move_ = True
        else:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\quest_move\\move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 800, 600, 930, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("move : move_1", imgs_)
                move_ = True
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\quest_move\\move_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 800, 600, 930, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("move : move_2", imgs_)
                    move_ = True



        return move_
    except Exception as e:
        print(e)
        return 0

def skip_click(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("skip_click")

        clicked = False

        # 아이템 획득
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\get.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 370, 560, 450, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("get", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            clicked = True

        # 화면 닫기
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\close_window.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 900, 600, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("close_window", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            clicked = True

        # 소환 나가기
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\middle_exit_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(250, 960, 750, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("middle_exit_btn", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            clicked = True

        # 레벨업
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\level_up.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 100, 600, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skip : level_up", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            clicked = True

        # 퀘스트 완료
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\quest_complete_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 450, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("quest_complete_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            clicked = True

        # 화면 클릭하기
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\screen_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 900, 600, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("screen_click", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            clicked = True
        else:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\screen_click2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 900, 600, 1000, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("screen_click2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                clicked = True
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\screen_click3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 900, 600, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("screen_click3", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    clicked = True

        # 퀘스트 완료

        skip_ = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(760, 30, 950, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skip_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            skip_ = True
            clicked = True

        else:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\skip_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 30, 950, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("skip_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                skip_ = True
                clicked = True

        if skip_ == True:
            for i in range(3):
                result_confirm = confirm_all(cla)
                if result_confirm == True:
                    break
                time.sleep(0.5)

        return clicked
    except Exception as e:
        print(e)
        return 0



def confirm_all(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, drag_pos

    try:
        print("confrim_all")

        confirm_ = False

        # 보상선택
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\confirm\\bosang_select.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 650, 550, 750, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("confirm : bosang_select", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            confirm_ = True
        else:
            # 이동
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\confirm\\move_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 500, 700, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("confirm : move_confirm", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                confirm_ = True
            # else:
            #     # 즉시이동
            #     full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\confirm\\immediately_move_confirm.PNG"
            #     img_array = np.fromfile(full_path, np.uint8)
            #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            #     imgs_ = imgs_set_(350, 500, 960, 1030, cla, img, 0.8)
            #     if imgs_ is not None and imgs_ != False:
            #         print("confirm : immediately_move_confirm", imgs_)
            #         click_pos_reg(imgs_.x, imgs_.y, cla)
            #         confirm_ = True
            else:
                # 확인
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\confirm\\skip_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 500, 700, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("confirm : skip_confirm", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    confirm_ = True
                else:
                    # y
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\confirm\\all_y.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 500, 700, 800, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("confirm : all_y", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        confirm_ = True
                    else:
                        # 분해
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\boonhae\\boonhae_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 580, 610, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm : boonhae_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            confirm_ = True
                        else:
                            # 소환시 바닥에 모두 확인 버튼
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\confirm\\all_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 580, 800, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm : all_confirm", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                confirm_ = True
                            else:
                                # sohwan drag
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\rare_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 490, 750, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("rare_confirm", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    drag_pos(400, 540, 800, 540, cla)
                                    time.sleep(2)
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\gyeyak_sohwan\\exit.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 980, 560, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("gyeyak_ready", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)


        return confirm_
    except Exception as e:
        print(e)
        return 0

def menu_open(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_reg
    from clean_screen_raven2 import clean_screen
    from massenger import line_to_me
    from get_item import get_post

    from event_get import event_get_check, event_get_start
    from event_allget import event_allget_check, event_allget_start
    from gyobum_raven2 import gyobum_check, gyobum_start

    try:
        print("menu_open")

        not_available = False

        for i in range(10):

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\menu_character_select.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 930, 920, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("menu : menu_character_select...end", imgs_)
                break
            else:


                result_out = out_check(cla)
                if result_out == True:

                    result_gyobum = gyobum_check(cla)
                    if result_gyobum == True:
                        gyobum_start(cla)
                        time.sleep(1)
                        clean_screen(cla)

                    result_event_allget = event_allget_check(cla)
                    if result_event_allget == True:
                        event_allget_start(cla)
                        time.sleep(1)
                        clean_screen(cla)

                    result_event_get = event_get_check(cla)
                    if result_event_get == True:
                        event_get_start(cla)
                        time.sleep(1)
                        clean_screen(cla)

                    click_pos_2(925, 60, cla)

                    for m in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\menu_character_select.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 930, 920, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu : menu_character_select", imgs_)

                            #우편 확인 후 받도록 하기...
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
                                    time.sleep(0.5)
                                    get_post(cla)


                            break

                        time.sleep(0.5)
                else:
                    clean_screen(cla)

            QTest.qWait(500)


        return not_available
    except Exception as e:
        print(e)
        return 0


def menu_open_pure(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_reg
    from clean_screen_raven2 import clean_screen
    from massenger import line_to_me
    from get_item import get_post

    from event_get import event_get_check, event_get_start
    from event_allget import event_allget_check, event_allget_start
    from gyobum_raven2 import gyobum_check, gyobum_start

    try:
        print("menu_open_pure")

        for i in range(10):

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\menu_character_select.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 930, 920, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("menu : menu_character_select...end", imgs_)
                break
            else:
                clean_screen(cla)
                time.sleep(0.5)
                click_pos_2(925, 60, cla)
            time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0

def game_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from massenger import line_to_me
    from character_select_and_game_start import game_start_screen
    from schedule import myQuest_play_check

    import os

    try:
        print("게임 오류 체크...game_check")

        out_ = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\monitor\\jangsigan.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 400, 700, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jangsigan", imgs_)
            out_ = True

            # 추후 재접속
            why = "장시간"
        else:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\monitor\\join_out.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 490, 570, 570, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("join_out", imgs_)
                out_ = True

                why = "운영자에의해접속종료"

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\monitor\\dongihwa_info.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 400, 650, 800, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dongihwa_info", imgs_)
                out_ = True

                why = "동기화정보"
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\monitor\\network_status.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 400, 650, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("dongihwa_info", imgs_)
                    out_ = True

                    why = "네트워크 상태 이상"
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\monitor\\fix_game.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 400, 650, 800, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("fix_game", imgs_)
                        out_ = True

                        why = "서버점검"


        if out_ == True:
            line_to_me(cla, why)

            result_schedule = myQuest_play_check(cla, "check")
            print("game_check : result_schedule", result_schedule)
            character_id = result_schedule[0][1]
            result_schedule_ = result_schedule[0][2]

            if why == "장시간" or why == "동기화정보":



                confirm_all(cla)
                time.sleep(1)

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\gameout\\my_character_seach.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 900, 950, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        game_start_screen(cla, character_id)
                        break
                    time.sleep(2)





            elif why == "운영자에의해접속종료":

                confirm_all(cla)
                time.sleep(60)
                game_start_screen(cla, character_id)

                # # 끝내기
                # dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
                # file_path = dir_path + "\\start.txt"
                # # cla.txt
                # cla_data = str(cla) + "cla"
                # file_path2 = dir_path + "\\" + cla_data + ".txt"
                # with open(file_path, "w", encoding='utf-8-sig') as file:
                #     data = 'no'
                #     file.write(str(data))
                #     time.sleep(0.2)
                # with open(file_path2, "w", encoding='utf-8-sig') as file:
                #     data = cla
                #     file.write(str(data))
                #     time.sleep(0.2)
                # os.execl(sys.executable, sys.executable, *sys.argv)
            elif why == "서버점검":

                confirm_all(cla)
                time.sleep(1)
                # 끝내기
                dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
                file_path = dir_path + "\\start.txt"
                # cla.txt
                cla_data = str(cla) + "cla"
                file_path2 = dir_path + "\\" + cla_data + ".txt"
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    data = 'no'
                    file.write(str(data))
                    time.sleep(0.2)
                with open(file_path2, "w", encoding='utf-8-sig') as file:
                    data = cla
                    file.write(str(data))
                    time.sleep(0.2)
                os.execl(sys.executable, sys.executable, *sys.argv)
        return out_

    except Exception as e:
        print(e)
        return 0

def go_maul(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from clean_screen_raven2 import clean_screen
    from massenger import line_to_me
    from dead_raven2 import dead_check, dead_recover
    from schedule import myQuest_play_check

    try:
        print("go_maul")



        maul_in = False
        maul_in_count = 0

        is_move = True

        result_juljun = juljun_check(cla)
        if result_juljun[0] == True:
            while maul_in is False:
                maul_in_count += 1
                if maul_in_count > 7:
                    maul_in = True

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\jabhwa_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 100, 200, 260, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    is_move = True
                    maul_in = True
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\maul_move_juljun.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 900, 950, 1040, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("maul_move_juljun", imgs_)
                        is_move = True
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\jabhwa_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 100, 200, 260, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)
                    else:
                        result_gamecheck = game_check(cla)
                        if result_gamecheck == False:
                            print("마을 이동서 없다")
                            why = "절전 마을이동서 없다. 정비해라"
                            line_to_me(cla, why)
                            is_move = False
                time.sleep(0.5)



        else:
            clean_screen(cla)
            for i in range(4):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\jabhwa_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 100, 200, 260, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("jabhwa_btn", imgs_)
                    is_move = True
                    maul_in = True
                    break
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\map_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(190, 100, 280, 160, cla, img, 0.75)
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
                time.sleep(0.5)



            while maul_in is False:
                maul_in_count += 1
                if maul_in_count > 7:
                    maul_in = True

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\jabhwa_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 100, 200, 260, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    is_move = True
                    maul_in = True
                else:
                    result_dead = dead_check(cla)
                    if result_dead == True:
                        dead_recover(cla)
                    else:
                        clean_screen(cla)
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\maul_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(360, 940, 470, 1010, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("maul_move", imgs_)
                            is_move = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            for i in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\jabhwa_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 100, 200, 260, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(1)
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\milgi_drag.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(390, 940, 570, 1010, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                drag_pos(400, 560, 800, 560, cla)

                            else:
                                is_game = False

                                for i in range(10):
                                    full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                                        v_.data_folder) + "\\imgs\\check\\game_title_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        is_game = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                                            v_.data_folder) + "\\imgs\\check\\game_title_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            is_game = True
                                            break
                                    time.sleep(1)

                                if is_game == True:
                                    click_pos_2(930, 55, cla)
                                    time.sleep(0.2)
                                    skip_click(cla)

                                    result_gamecheck = game_check(cla)
                                    if result_gamecheck == False:
                                        print("마을 이동서 없다")
                                        why = "마을이동서 없다. 정비해라"
                                        line_to_me(cla, why)
                                        is_move = False

                                else:
                                    why = "게임 꺼졌다."
                                    line_to_me(cla, why)
                                    is_move = False


                time.sleep(0.5)
        if is_move == False:
            dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
            file_path = dir_path + "\\start.txt"
            # cla.txt
            cla_data = str(cla) + "cla"
            file_path2 = dir_path + "\\" + cla_data + ".txt"
            with open(file_path, "w", encoding='utf-8-sig') as file:
                data = 'no'
                file.write(str(data))
                time.sleep(0.2)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                data = cla
                file.write(str(data))
                time.sleep(0.2)
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            clean_screen(cla)
    except Exception as e:
        print(e)
        return 0

def go_random(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_raven2 import clean_screen
    from massenger import line_to_me

    try:
        print("go_random")

        is_random = False

        result_juljun = juljun_check(cla)
        if result_juljun[0] == True:
            juljun_off(cla)

        for r in range(5):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\maul\\random_move.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 940, 470, 1010, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("random_move", imgs_)

                is_random = True

                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)

                for i in range(5):
                    result_out = out_check(cla)
                    if result_out == True:
                        break
                    time.sleep(0.5)
                break
            else:
                clean_screen(cla)
            time.sleep(0.5)

        if is_random == False:
            why = "랜덤이동서 안보인다"
            line_to_me(cla, why)

            dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
            file_path = dir_path + "\\start.txt"
            # cla.txt
            cla_data = str(cla) + "cla"
            file_path2 = dir_path + "\\" + cla_data + ".txt"
            with open(file_path, "w", encoding='utf-8-sig') as file:
                data = 'no'
                file.write(str(data))
                time.sleep(0.2)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                data = cla
                file.write(str(data))
                time.sleep(0.2)
            os.execl(sys.executable, sys.executable, *sys.argv)

    except Exception as e:
        print(e)
        return 0


def juljun_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_raven2 import clean_screen
    from dead_raven2 import dead_check, dead_recover

    try:
        print("juljun_check")

        # 게임 오류 체크
        game_check(cla)

        juljun_ = False
        position = "none"

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_mode_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 50, 600, 120, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("juljun_mode_check", imgs_)
            juljun_ = True

            juljun_time_check(cla)



            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\juljun_off.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(445, 755, 500, 810, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\attack2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 910, 470, 970, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("attack2 : 절전모드에서 공격중", imgs_)
                    position = "attack"
                else:
                    # 물약 체크 중인데 자동사냥중인지 파악 안될때 내리기

                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\juljun_off.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(445, 755, 500, 810, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(480, 1000, cla)
                            time.sleep(0.2)
                        else:
                            break
                        time.sleep(0.5)


            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\ready.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 910, 550, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("ready", imgs_)
                position = "ready"
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\attack.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 910, 550, 970, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("attack", imgs_)
                    position = "attack"
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\move.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 910, 550, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("move", imgs_)
                        position = "move"

            if position == "attack":
                result_attack = juljun_attack_check(cla)
                if result_attack == False:
                    position = "ready"
        else:
            result_dead = dead_check(cla)
            if result_dead == True:
                dead_recover(cla)
        return juljun_, position
    except Exception as e:
        print(e)
        return 0


def juljun_on(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_raven2 import clean_screen
    from massenger import line_to_me

    try:
        print("juljun_on")

        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_mode_check.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 50, 600, 120, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("juljun_mode_check", imgs_)
                break
            else:

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 700, 600, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_btn..", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for j in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_mode_check.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 50, 600, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("juljun_mode_ing..", imgs_)
                            break
                        time.sleep(0.5)
                else:
                    clean_screen(cla)
                    click_pos_2(30, 880, cla)
                    juljun_ = True
                    for c in range(7):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_cannot.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 100, 520, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("juljun_cannot..", imgs_)
                            juljun_ = False
                            break
                        time.sleep(0.1)
                    if juljun_ == False:
                        organize_start(cla)


            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

def juljun_off(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_2, drag_pos_click, drag_pos_py
    from clean_screen_raven2 import clean_screen
    from dead_raven2 import dead_check, dead_recover

    try:
        print("juljun_off")



        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_mode_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 50, 600, 120, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            for i in range(5):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_mode_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 50, 600, 120, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_mode_check", imgs_)
                    drag_pos_click(250, 520, 750, 520, cla)
                    time.sleep(0.5)

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_mode_check.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 50, 600, 120, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("juljun_mode_check", imgs_)
                        drag_pos_py(250, 520, 750, 520, cla)
                        time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_off_result_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 310, 500, 4000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        result_confirm = confirm_all(cla)
                        if result_confirm == True:
                            break
                    else:
                        result_out = out_check(cla)
                        if result_out == True:
                            break
                time.sleep(0.5)
        else:
            result_dead = dead_check(cla)
            if result_dead == True:
                dead_recover(cla)


    except Exception as e:
        print(e)
        return 0



def bag_open(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_2, click_pos_reg, drag_pos
    from clean_screen_raven2 import clean_screen

    try:
        print("bag_open")

        clean_screen(cla)



        for i in range(10):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag_checked.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(860, 220, 930, 340, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bag_checked", imgs_)
                break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\bag_jabhwa.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(880, 230, 960, 330, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("bag_jabhwa", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                else:
                    click_pos_2(865, 65, cla)
            time.sleep(0.5)

        sohwan_ = True
        sohwan_count = 0
        while sohwan_ is True:
            sohwan_count += 1
            if sohwan_count > 7:
                sohwan_ = False

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\bag_jabhwa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 230, 960, 330, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                sohwan_ = False

                my_bag_item = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag"
                file_list = os.listdir(my_bag_item)
                print("file_list", file_list)
                for s in range(len(file_list)):
                    result_file_list = file_list[s].split(".")

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\" + str(result_file_list[0]) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 75, 900, 850, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print(result_file_list[0], imgs_)


                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)

                        for i in range(4):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag_select.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 400, 530, 460, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("bag_select", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                                confirm_all(cla)
                            else:
                                confirm_all(cla)
                            time.sleep(0.5)

                        for i in range(10):

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\right__drag.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 490, 750, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("rare_confirm", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                drag_pos(400, 540, 800, 540, cla)
                                time.sleep(2)

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\middle_exit_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 960, 750, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("middle_exit_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                sohwan_count = 0

                                for c in range(10):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_x.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(630, 30, 780, 100, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("close_btn_x..", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag_checked.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(860, 220, 930, 340, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("bag_checked", imgs_)
                                            break
                                        else:
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\bag_jabhwa.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(880, 230, 960, 330, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("bag_jabhwa", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.1)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.1)

                                            else:
                                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\middle_exit_btn.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(250, 960, 750, 1040, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("middle_exit_btn", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                break
                            else:
                                confirm_all(cla)
                                time.sleep(0.3)
                                # 화면 클릭하기
                                for c in range(10):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag_checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(860, 220, 930, 340, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("bag_checked", imgs_)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\bag_jabhwa.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(880, 230, 960, 330, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("bag_jabhwa", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            break
                                        else:
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\screen_click.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(300, 900, 600, 1000, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("screen_click", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            else:
                                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\screen_click2.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(300, 900, 600, 1000, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("screen_click2", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)
                            time.sleep(0.5)
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\middle_exit_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 960, 750, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("middle_exit_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    sohwan_count = 0

                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 220, 930, 340, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("bag_checked", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\bag_jabhwa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(880, 230, 960, 330, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("bag_jabhwa", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\middle_exit_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(250, 960, 750, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("middle_exit_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

            time.sleep(1)

    except Exception as e:
        print(e)
        return 0



def bag_item_open(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_
    from clean_screen_raven2 import clean_screen

    try:
        print("bag_item_open")

        item_list = ['devil_1', 'devil_2', 'devil_3', 'sung_1', 'sung_2', 'gold_box', 'box_ganhwasuk', 'box_jangsingoo', 'box_bangugoo', 'box_moogi', 'box_jejak']

        open_ = False

        for i in range(len(item_list)):

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\bag\\" + str(item_list[i]) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 75, 900, 850, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print(item_list[i], imgs_)
                open_ = True

        return open_
    except Exception as e:
        print(e)
        return 0


def inven_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("inven_check")

        inven = True
        for c in range(5):
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\juljun\\juljun_cannot.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 80, 600, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("juljun_cannot..", imgs_)
                inven = False
                break
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\attack\\attack_cannot.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(320, 160, 560, 230, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("attack_cannot..", imgs_)
                    inven = False
                    break
                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\get_item\\post\\insufficient_inven.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 90, 700, 190, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("insufficient_inven..", imgs_)
                        inven = False
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\clean_screen\\close_btn_x.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(630, 30, 780, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("close_btn_x..", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\action\\attack\\can_not_attack_aim.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 100, 780, 170, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("can_not_attack_aim..", imgs_)
                                go_maul(cla)
                                break
            time.sleep(0.1)
        if inven == False:
            organize_start(cla)

        return inven
    except Exception as e:
        print(e)
        return 0




def juljun_time_check(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_
    from datetime import datetime
    from massenger import line_to_me
    try:
        print("juljun_time_check")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3
        elif cla == "five":
            plus = 960 * 4
        elif cla == "six":
            plus = 960 * 5

        nowTime = int(datetime.today().strftime("%M"))

        print("nowTime", nowTime)

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\juljun_time\\slush.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(440, 100, 530, 165, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("slush", imgs_)
            x_start = imgs_.x - plus


            now_time = ""

            for i in range(10):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\juljun_time\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_start, 100, 600, 165, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("자리", i, imgs_)

            for i in range(10):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\juljun_time\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_start, 100, x_start + 50, 165, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("10 자리", i, imgs_)
                    x_start = imgs_.x - plus
                    now_time += str(i)
                    break

            for i in range(10):
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\juljun_time\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_start, 100, x_start + 50, 165, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("1 자리", i, imgs_)
                    now_time += str(i)
                    break



            if now_time == "":
                print("값이 없다")
            else:
                now_time = int(now_time)
                print("now_time", now_time)
                if now_time < 70:

                    if nowTime >= 50 and now_time < 10:
                        now_time += 60
                    elif now_time >= 50 and nowTime < 10:
                        nowTime += 60

                    result_cal = abs(nowTime - now_time)

                    if result_cal > 19:

                        v_.time_count += 1

                        if v_.time_count > 5:

                            print("멈춰있는 상태", result_cal)

                            why = "현재분 : " + str(nowTime) + "파악된분 : " + str(now_time) + str(result_cal) + "분 차이...다운되거나 인터넷이 끊긴것이 확실하다"
                            print(why)
                            line_to_me(cla, why)

                            dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
                            file_path = dir_path + "\\start.txt"
                            # cla.txt
                            cla_data = str(cla) + "cla"
                            file_path2 = dir_path + "\\" + cla_data + ".txt"
                            with open(file_path, "w", encoding='utf-8-sig') as file:
                                data = 'no'
                                file.write(str(data))
                                time.sleep(0.2)
                            with open(file_path2, "w", encoding='utf-8-sig') as file:
                                data = cla
                                file.write(str(data))
                                time.sleep(0.2)
                            os.execl(sys.executable, sys.executable, *sys.argv)

                    else:
                        v_.time_count = 0
                        print("정상 작동 중", result_cal)

    except Exception as e:
        print(e)
        return 0











