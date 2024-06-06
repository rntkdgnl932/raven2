import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dead_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import out_check

    from schedule import myQuest_play_check

    try:

        result_schedule = myQuest_play_check(cla, "check")
        character_id = result_schedule[0][1]
        result_schedule_ = result_schedule[0][2]

        print("dead_check")

        dead_ = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\dead_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 400, 500, 500, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dead_1", imgs_)
            dead_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\dead_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(450, 690, 560, 760, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dead_2", imgs_)
            dead_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)

        if "일반" in result_schedule_ or "특수" in result_schedule_ or result_schedule_ == "자동사냥":

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\boohwal_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(530, 30, 650, 100, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("boohwal_btn", imgs_)
                dead_ = True


        return dead_
    except Exception as e:
        print(e)
        return 0

def dead_check_2(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import out_check

    try:
        print("dead_check_2")

        dead_ = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\dead_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 400, 500, 500, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dead_1", imgs_)
            dead_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\dead_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(450, 690, 560, 760, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dead_2", imgs_)
            dead_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)


        return dead_
    except Exception as e:
        print(e)
        return 0



def dead_recover(cla):
    import numpy as np
    import cv2
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import out_check, confirm_all
    from clean_screen_raven2 import clean_screen
    from massenger import line_to_me

    try:
        print("dead_recover")

        recover = False

        clean_screen(cla)

        click_count = 0

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
                imgs_ = imgs_set_(530, 30, 650, 100, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    click_count += 1
                    if click_count > 9:
                        why = "boohwal_btn 클릭이 안된다"
                        print("boohwal_btn 클릭이 안된다")
                        line_to_me(cla, why)
                    print("boohwal_btn", imgs_)
                    ran_int_x = random.randint(0, 2)
                    ran_int_y = random.randint(0, 2)
                    click_pos_reg(imgs_.x + ran_int_x, imgs_.y + ran_int_y, cla)
            time.sleep(0.5)

        if recover == True:

            for i in range(7):

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\exp_recover_last.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 440, 530, 500, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("exp_recover_last", imgs_)

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\free_recover.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(520, 520, 600, 560, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("free_recover", imgs_)
                        confirm_all(cla)
                    else:
                        break

                    break

                else:

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\exp_recover_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(260, 260, 400, 400, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("exp_recover_title", imgs_)


                        for c in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\today_free_recover.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(270, 700, 700, 760, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_2(600, 360, cla)
                            time.sleep(0.5)


                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\exp_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 380, 380, 680, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("exp_click", imgs_)
                            # 클릭 후 590, 735
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            not_free_recover = False
                            for f in range(5):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\not_free_recover.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(100, 100, 900, 680, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("not_free_recover", cla)
                                    not_free_recover = True
                                    break
                                time.sleep(0.1)

                            if not_free_recover == True:
                                break
                            else:
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

def dead_recover_jadong(cla):
    import numpy as np
    import cv2
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import out_check, confirm_all
    from clean_screen_raven2 import clean_screen
    from massenger import line_to_me

    try:
        print("dead_recover")

        recover = False

        clean_screen(cla)

        click_count = 0

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
                imgs_ = imgs_set_(530, 30, 650, 100, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    click_count += 1
                    if click_count > 9:
                        why = "boohwal_btn 클릭이 안된다"
                        print("boohwal_btn 클릭이 안된다")
                        line_to_me(cla, why)
                    print("boohwal_btn", imgs_)
                    ran_int_x = random.randint(0, 2)
                    ran_int_y = random.randint(0, 2)
                    click_pos_reg(imgs_.x + ran_int_x, imgs_.y + ran_int_y, cla)
            time.sleep(0.5)

        if recover == True:

            for i in range(7):

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\exp_recover_last.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 440, 530, 500, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("exp_recover_last", imgs_)

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\free_recover.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(520, 520, 600, 560, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("free_recover", imgs_)
                        confirm_all(cla)
                    else:
                        break

                    break

                else:

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\exp_recover_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(260, 260, 400, 400, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("exp_recover_title", imgs_)


                        for c in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\today_free_recover.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(270, 700, 700, 760, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_2(600, 360, cla)
                            time.sleep(0.5)


                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\exp_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 380, 380, 680, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("exp_click", imgs_)
                            # 클릭 후 590, 735
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            not_free_recover = False
                            for f in range(5):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\not_free_recover.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(100, 100, 900, 680, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("not_free_recover", cla)
                                    not_free_recover = True
                                    break
                                time.sleep(0.1)

                            if not_free_recover == True:
                                break
                            else:
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

