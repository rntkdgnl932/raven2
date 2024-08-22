import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def guild_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import menu_open, move_check, confirm_all
    from clean_screen_raven2 import clean_screen

    try:
        print("guild_check")



        guild = False
        guild_count = 0

        while guild is False:
            guild_count += 1
            if guild_count > 7:
                guild = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\guild\\guild_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 150, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("guild_title", imgs_)

                guild = True

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\guild\\donation_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(760, 970, 900, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("donation_btn", imgs_)

                    # 출석
                    for i in range(4):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\guild\\guild_chulsuk.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 350, 540, 410, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("guild_chulsuk", imgs_)
                            break
                        else:
                            click_pos_2(700, 1000, cla)
                        time.sleep(0.5)

                    for i in range(4):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\guild\\donation_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 320, 220, 360, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("donation_title", imgs_)
                            break
                        else:
                            click_pos_2(840, 1000, cla)
                        time.sleep(0.5)

                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\guild\\donation_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 320, 220, 360, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\guild\\anymore_donation.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(370, 100, 600, 160, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("anymore_donation", imgs_)
                                break
                            else:
                                click_pos_2(285, 655, cla)
                                time.sleep(0.5)
                        time.sleep(0.5)


                else:
                    print("아직 미가입")



                clean_screen(cla)

            else:

                menu_open(cla)

                guild_btn = False

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\guild\\guild_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 150, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\guild\\menu_guild_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(640, 390, 800, 510, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_guild_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            guild_btn = True

                    time.sleep(0.3)
                if guild_btn == False:
                    guild = True

            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0




