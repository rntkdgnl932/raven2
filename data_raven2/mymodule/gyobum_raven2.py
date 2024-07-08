import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def gyobum_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg

    try:
        print("gyobum_check")

        is_point = False

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\out_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(240, 30, 275, 55, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out_point_1", imgs_)
            is_point = True
            click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)




        return is_point
    except Exception as e:
        print(e)
        return 0


def gyobum_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import inven_check

    try:
        print("gyobum_start")

        gyobum_in = False
        gyobum_in_count = 0
        result_inven = True

        while gyobum_in is False:
            gyobum_in_count += 1
            if gyobum_in_count > 5:
                gyobum_in = True


            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("gyobum_title", imgs_)

                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\get_gyobum_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(630, 130, 800, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("get_gyobum_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        result_inven = inven_check(cla)
                        if result_inven == True:

                            screen_clicked = False
                            for c in range(4):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\screen_click2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 900, 600, 1000, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("screen_click2", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    screen_clicked = True
                                    break
                                time.sleep(0.5)
                            if screen_clicked == False:
                                click_pos_2(100, 60, cla)
                                time.sleep(0.5)
                        else:
                            break

                    else:
                        break
                    time.sleep(0.5)

                if result_inven == True:

                    gyobum_in = True

                    know_ = False

                    for i in range(10):

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\out_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 250, 120, 900, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("out_point_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for t in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\title_monster.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    gyobum_get(cla)
                                    break
                                else:
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\title_region.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        gyobum_get(cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\title_knowledge.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            know_ = True
                                            gyobum_get(cla)
                                            break
                                time.sleep(0.5)

                        else:
                            # 끝
                            break

                        if know_ == True:
                            break

                        time.sleep(0.5)

                else:
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\out_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(240, 30, 275, 55, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("out_point_1", imgs_)
                        click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)

            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\out_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(240, 30, 275, 55, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("out_point_1", imgs_)
                    click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0


def gyobum_get(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_raven2 import confirm_all, organize_start, inven_check, skip_click

    try:
        print("gyobum_get")

        result_inven = True

        ######################################
        ###########지식은 아직 보완 필요#########
        ######################################

        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\title_monster.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("title_monster", imgs_)

            time.sleep(0.5)

            for i in range(10):

                # 몬스터 도감 소제목 클릭
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 70, 600, 105, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    # 먼저 확인 한번 눌러주기
                    confirm_all(cla)

                    print("gyobum_point_1", imgs_)
                    # 클릭
                    click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                    time.sleep(0.3)

                    # 몬스터 도감 자세한 부분 클릭

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 130, 210, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        for a in range(10):
                            # 몬스터 도감 분석 클릭
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\title_monster.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("title_monster", imgs_)



                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\monster_boonsuk.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 500, 800, 900, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("monster_boonsuk", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                    result_inven = inven_check(cla)
                                    if result_inven == False:
                                        break
                                    else:
                                        for b in range(5):
                                            result = confirm_all(cla)
                                            if result == True:
                                                break
                                            time.sleep(0.1)

                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\monster_info_close_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 250, 800, 500, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("monster_info_close_btn", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break

                                else:

                                    for b in range(4):
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\monster_info_close_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 250, 800, 500, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("monster_info_close_btn", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                        else:
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\close_window.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 900, 600, 1000, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("close_window", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            else:
                                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\screen_click2.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(300, 900, 600, 1000, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("screen_click2", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)

                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_for(50, 130, 210, 700, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        # print("gyobum_point_2", imgs_)
                                        last = len(imgs_)
                                        # print("gyobum_point_2[last - 1]", imgs_[last - 1])
                                        click_pos_reg(imgs_[last - 1][0] - 10, imgs_[last - 1][1] + 10, cla)
                                        time.sleep(0.5)
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_for(50, 130, 210, 700, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        # print("gyobum_point_2", imgs_)
                                        last = len(imgs_)
                                        # print("gyobum_point_2[last - 1]", imgs_[last - 1])
                                        click_pos_reg(imgs_[last - 1][0] - 10, imgs_[last - 1][1] + 10, cla)
                                        time.sleep(0.3)

                                    # 몬스터 도감 마지막 포인트 클릭
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(220, 180, 930, 1040, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("gyobum_point_3", imgs_)
                                        click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                                        time.sleep(0.3)
                                    else:
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_33.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(220, 180, 930, 1040, cla, img, 0.75)
                                        if imgs_ is not None and imgs_ != False:
                                            print("gyobum_point_33", imgs_)
                                            click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                                            time.sleep(0.3)
                                        else:
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_333.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(220, 180, 930, 1040, cla, img, 0.75)
                                            if imgs_ is not None and imgs_ != False:
                                                print("gyobum_point_333", imgs_)
                                                click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                                                time.sleep(0.3)

                                            else:
                                                # 큰 포인트는 없는데 왼쪽에는 있을 경우 위에 보상을 받아야 하는 경우이다.
                                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(50, 130, 210, 700, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:

                                                    for c in range(3):
                                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(50, 130, 210, 700, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            # 600, 715, 830
                                                            x_reg = 640 + (c * 130)
                                                            end_ = False
                                                            for d in range(3):
                                                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\close_window.PNG"
                                                                img_array = np.fromfile(full_path, np.uint8)
                                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                                imgs_ = imgs_set_(400, 900, 600, 1000, cla, img, 0.8)
                                                                if imgs_ is not None and imgs_ != False:
                                                                    print("close_window", imgs_)
                                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                                    end_ = True
                                                                    break
                                                                else:
                                                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\skip\\screen_click2.PNG"
                                                                    img_array = np.fromfile(full_path, np.uint8)
                                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                                    imgs_ = imgs_set_(300, 900, 600, 1000, cla, img, 0.8)
                                                                    if imgs_ is not None and imgs_ != False:
                                                                        print("screen_click2", imgs_)
                                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                                        end_ = True
                                                                        break

                                                                    else:
                                                                        click_pos_2(x_reg, 135, cla)
                                                                        result_inven = inven_check(cla)
                                                                        if result_inven == False:
                                                                            break
                                                            if end_ == True:
                                                                break
                                                        else:
                                                            break
                                                        time.sleep(0.3)
                            else:
                                click_pos_2(100, 60, cla)

                            time.sleep(0.3)

                        for a in range(5):
                            result_confirm = confirm_all(cla)
                            if result_confirm == True:
                                break
                            time.sleep(0.1)

                else:
                    print("몬스터 도감 끝")



                    break
            if result_inven == True:
                # 특무대 교범으로 돌아가기
                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("gyobum_title", imgs_)
                        break
                    else:
                        click_pos_2(25, 60, cla)
                        for c in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)
                    time.sleep(0.3)
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\out_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(240, 30, 275, 55, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("out_point_1", imgs_)
                    click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)

        else:
            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\title_region.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title_region", imgs_)

                time.sleep(0.5)

                for i in range(10):

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 130, 210, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        # 지역 도감 자세한 부분 클릭
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_for(50, 130, 210, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            # print("gyobum_point_2", imgs_)
                            last = len(imgs_)
                            # print("gyobum_point_2[last - 1]", imgs_[last - 1])
                            click_pos_reg(imgs_[last - 1][0] - 10, imgs_[last - 1][1] + 10, cla)
                            time.sleep(0.5)

                            # 지역 도감 체크 부분 파악
                            # x + 90 클릭

                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\region_checked_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 940, 750, 1020, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:

                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\region_checked_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_for(300, 940, 750, 1020, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    # print("region_checked", imgs_)
                                    last = len(imgs_)
                                    # print("region_checked[last - 1]", imgs_[last - 1])
                                    click_pos_reg(imgs_[last - 1][0] + 90, imgs_[last - 1][1], cla)
                                    time.sleep(0.5)
                            else:
                                click_pos_2(355, 980, cla)
                                time.sleep(0.5)
                            time.sleep(0.5)
                            for c in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\title_region.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    click_pos_2(100, 60, cla)
                                time.sleep(0.5)
                    else:
                        # 끝
                        break
                    time.sleep(0.5)

                # 특무대 교범으로 돌아가기
                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("gyobum_title", imgs_)
                        break
                    else:
                        click_pos_2(25, 60, cla)
                        for c in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)
                    time.sleep(0.3)

            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\title_knowledge.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("title_knowledge", imgs_)

                    time.sleep(0.5)

                    for i in range(10):

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\title_knowledge.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("title_knowledge", imgs_)

                            # 몬스터 도감 소제목 클릭
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 130, 210, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:

                                confirm_all(cla)

                                print("gyobum_point_2", imgs_)
                                # 클릭
                                click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                                time.sleep(0.3)

                                # 지식 도감 자세한 부분 클릭

                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_for(50, 130, 210, 700, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    # print("gyobum_point_2", imgs_)
                                    last = len(imgs_)
                                    # print("gyobum_point_2[last - 1]", imgs_[last - 1])
                                    click_pos_reg(imgs_[last - 1][0] - 10, imgs_[last - 1][1] + 10, cla)
                                    time.sleep(0.3)

                                    for a in range(10):
                                        # 지식 도감 분석 클릭
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\knowledge_complete_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(500, 500, 800, 900, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("knowledge_complete_btn", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.3)

                                            result_inven = inven_check(cla)
                                            if result_inven == False:
                                                break
                                            else:
                                                for c in range(5):
                                                    result = confirm_all(cla)
                                                    if result == True:
                                                        break
                                                    time.sleep(0.1)

                                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\monster_info_close_btn.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(500, 250, 800, 500, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("monster_info_close_btn", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    break



                                            break
                                        else:
                                            # 지식 도감 마지막 포인트 클릭
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_4.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(220, 80, 900, 1000, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("gyobum_point_4", imgs_)
                                                click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                                                time.sleep(0.3)
                                        time.sleep(0.3)

                                    for a in range(5):
                                        result_confirm = confirm_all(cla)
                                        if result_confirm == True:
                                            break
                                        time.sleep(0.1)

                            else:
                                # 440 + 77
                                # 1005

                                for c in range(7):
                                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_point_5.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 90, 210, 120, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("gyobum_point_5", imgs_)
                                        x_reg = 440 + (c * 77)
                                        click_pos_2(x_reg, 1005, cla)

                                        for s in range(1):
                                            result_skip = skip_click(cla)
                                            if result_skip == True:
                                                break
                                            time.sleep(0.1)
                                    else:
                                        break
                                    time.sleep(0.2)


                                print("지식 도감 끝")
                                break
                        else:
                            click_pos_2(100, 60, cla)
                    # 지식 도감은 오류 있어서 아예 나가기

                    # 특무대 교범으로 돌아가기
                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("gyobum_title", imgs_)
                            break
                        else:
                            click_pos_2(25, 60, cla)
                            for c in range(10):
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\gyobum\\gyobum_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.2)
                        time.sleep(0.3)

    except Exception as e:
        print(e)
        return 0
