import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def chango_in(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import go_maul, move_check, confirm_all
    from clean_screen_raven2 import clean_screen

    try:
        print("chango_in")

        # 먼저 마을로 가기

        go_maul(cla)

        # 마을인지 확인되면 정해진 포션 사기

        chango_ = False
        chango_count = 0

        while chango_ is False:
            chango_count += 1
            if chango_count > 7:
                chango_ = True

            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\chango_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 30, 150, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("chango_title", imgs_)

                chango_ = True

                # 자동선택
                # for i in range(2):
                #     full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\anymore_item.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(380, 105, 580, 160, cla, img, 0.8)
                #     if imgs_ is not None and imgs_ != False:
                #         print("anymore_item", imgs_)
                #         break
                #     else:
                #         click_pos_2(700, 1000, cla)
                #         time.sleep(0.5)
                #         click_pos_2(800, 1000, cla)
                #     time.sleep(0.5)

                # 꺼내기
                for i in range(5):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\chango_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 680, 600, 740, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("chango_confirm", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break

                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\out_item_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(75, 80, 290, 940, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("out_item_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        else:
                            break
                    time.sleep(1)


                for i in range(5):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\chango_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 680, 600, 740, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("chango_confirm", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break

                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\out_item_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(75, 80, 290, 940, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("out_item_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        else:
                            break
                    time.sleep(1)

                for i in range(5):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\chango_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 680, 600, 740, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    time.sleep(0.5)

                for i in range(5):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\chango_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 680, 600, 740, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("chango_confirm", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break

                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\out_item_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(75, 80, 290, 940, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("out_item_2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        else:
                            break
                    time.sleep(1)

                for i in range(5):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\chango_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 680, 600, 740, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    time.sleep(0.5)

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\potion\\hogamdo\\anymore_item.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 105, 580, 160, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("anymore_item", imgs_)
                        break
                    else:
                        click_pos_2(180, 1000, cla)
                        time.sleep(0.5)
                    time.sleep(0.5)


                ############### 거래소 등록 하면서부터 아래는 잠시 보류...###################
                # # 기타 클릭하기
                # for i in range(5):
                #     full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\clicked.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(870, 290, 910, 420, cla, img, 0.8)
                #     if imgs_ is not None and imgs_ != False:
                #         print("clicked", imgs_)
                #         break
                #     else:
                #         click_pos_2(920, 360, cla)
                #     time.sleep(0.5)
                #
                # # 기타에 있는거 전부 넣기
                # print("으랏차차")
                # for y in range(4):
                #     y_reg = 270 - (y * 50)
                #     for x in range(5):
                #         x_reg = 858 - (x * 52)
                #
                #         cal = 40
                #
                #         full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\null.PNG"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(x_reg - cal, y_reg - cal, x_reg + cal, y_reg + cal, cla, img, 0.6)
                #         if imgs_ is not None and imgs_ != False:
                #             print("pass............", x_reg, y_reg)
                #         else:
                #             click_pos_2(x_reg, y_reg, cla)
                #             time.sleep(0.2)
                #             result_confirm = confirm_all(cla)
                #             if result_confirm == True:
                #                 time.sleep(0.2)
                #
                # click_pos_2(800, 1000, cla)
                # time.sleep(0.1)
                # click_pos_2(800, 1000, cla)
                # time.sleep(0.1)
                #################################################################

                clean_screen(cla)

            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\chango_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 100, 200, 260, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("chango_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    move_count = 0
                    for i in range(50):
                        result_move = move_check(cla)
                        if result_move == False:
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\chango\\chango_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 30, 150, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("chango_title", imgs_)
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




