import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def out_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("out_check")

        out_ = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\out\\talk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(5, 900, 50, 960, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out : talk", imgs_)
            out_ = True



        return out_
    except Exception as e:
        print(e)
        return 0

def attck_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("attck_check")

        attack_ = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\out\\talk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(5, 900, 50, 960, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out : talk", imgs_)
            attack_ = True



        return attack_
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

        # 레벨업
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\level_up.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 100, 600, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skip : level_up", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 퀘스트 완료
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\tuto\\quest_complete_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 450, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("quest_complete_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 화면 클릭하기
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\screen_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 900, 600, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("screen_click", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

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

        else:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\skip_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 30, 950, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("skip_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                skip_ = True

        if skip_ == True:
            for i in range(3):
                result_confirm = confirm_all(cla)
                if result_confirm == True:
                    break
                time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0



def confirm_all(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("confrim_all")

        confirm_ = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\confirm\\move_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 500, 700, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("confirm : move_confirm", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            confirm_ = True
        else:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\confirm\\skip_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 500, 700, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("confirm : skip_confirm", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                confirm_ = True
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\confirm\\all_y.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 500, 700, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("confirm : all_y", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    confirm_ = True

        return confirm_
    except Exception as e:
        print(e)
        return 0

def menu_open(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_raven2 import clean_screen
    from massenger import line_to_me

    try:
        print("menu_open")

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
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(925, 60, cla)

                    for m in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\character_select_and_game_start\\menu_character_select.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 930, 920, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu : menu_character_select", imgs_)
                            break
                        time.sleep(0.5)


            time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0


def jangsigan_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from massenger import line_to_me

    try:
        print("jangsigan_check")

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\monitor\\jangsigan.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 400, 700, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jangsigan", imgs_)
            confirm_all(cla)

            # 추후 재접속
            why = "장시간"
            line_to_me(cla, why)

    except Exception as e:
        print(e)
        return 0



