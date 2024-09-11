import time
# import os
import sys
from PyQt5.QtTest import *


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dungeon_start(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import go_maul, move_check, juljun_check, juljun_off, juljun_on, attack_on, go_random, confirm_all
    from clean_screen_raven2 import clean_screen
    from potion_raven2 import potion_check, potion_buy
    from dead_raven2 import dead_check_2, dead_recover

    try:
        print("dungeon_start")

        # 특수_발바르_4
        # 특수_타파나_4
        # 일반_고대의신전, 일반_깊은늪, 일반_붉은바위협곡

        result_dead = dead_check_2(cla)

        if result_dead == True:
            dead_recover(cla)
            potion_buy(cla)

        result_dungeon_check = dungeon_check(cla, data)
        # result_dungeon_check[0] => True : 던전 진입 맞음
        # result_dungeon_check[1] => True : 사냥 중 맞음
        # result_dungeon_check[2] => True : 랜덤 이동해야함
        if result_dungeon_check[0] == False:
            # 사냥터 이동
            dungeon_in(cla, data)
        elif result_dungeon_check[0] == True:
            if result_dungeon_check[1] == True:
                if result_dungeon_check[2] == False:
                    print("사냥중")
                    potion_check(cla)
                    # 포션 체크...
                    # 절전 중 집 가기...
                else:
                    print("절전 풀고 공격버튼 클릭 후 다시 절전하기")
                    go_random(cla)
                    clean_screen(cla)
                    attack_on(cla)

                    # 혹시 진입할 수도 있음
                    confirm_all(cla)

                    juljun_on(cla)
            elif result_dungeon_check[1] == False:
                print("절전 풀고 공격버튼 클릭 후 다시 절전하기")
                go_random(cla)
                clean_screen(cla)
                attack_on(cla)

                # 혹시 진입할 수도 있음
                confirm_all(cla)

                juljun_on(cla)







    except Exception as e:
        print(e)
        return 0


def dungeon_in(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import go_maul, move_check, menu_open, out_check, juljun_on, attack_on, go_random, inven_check
    from clean_screen_raven2 import clean_screen
    from dead_raven2 import dead_recover
    from potion_raven2 import potion_buy

    from schedule import myQuest_play_add

    try:
        print("dungeon_in")

        clean_screen(cla)
        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dead\\boohwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(530, 30, 650, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_btn", imgs_)
            dead_recover(cla)
            potion_buy(cla)
        else:
            potion_buy(cla)

        complete = False

        # 특수_발바르_4, 특수_타파나_4
        # 일반_고대의신전_5, 일반_깊은늪_5, 일반_붉은바위협곡_2

        dun_y_click = 0

        dun = data.split("_")
        if dun[0] == "특수":
            y_check_1 = 90
            y_check_2 = 160
            y_click = 125

        elif dun[0] == "일반":
            y_check_1 = 150
            y_check_2 = 220
            y_click = 190

        elif dun[0] == "이벤트":
            y_check_1 = 220
            y_check_2 = 280
            y_click = 250

        if dun[1] == "발바르":
            dun_name = "balbar"
            dun_x_click = 280

            if int(dun[2]) > 4:
                dun_y_click = 4
            else:
                dun_y_click = int(dun[2])
        elif dun[1] == "타파나":
            dun_name = "tapana"
            dun_x_click = 460

            if int(dun[2]) > 4:
                dun_y_click = 4
            else:
                dun_y_click = int(dun[2])
        elif dun[1] == "고대의신전":
            dun_name = "temple"
            dun_x_click = 280

            if int(dun[2]) > 5:
                dun_y_click = 5
            else:
                dun_y_click = int(dun[2])
        elif dun[1] == "깊은늪":
            dun_name = "swamp"
            dun_x_click = 460

            if int(dun[2]) > 5:
                dun_y_click = 5
            else:
                dun_y_click = int(dun[2])
        elif dun[1] == "붉은바위협곡":
            dun_name = "redstone"
            dun_x_click = 635

            if int(dun[2]) > 2:
                dun_y_click = 2
            else:
                dun_y_click = int(dun[2])

        elif dun[0] == "이벤트":
            dun_name = "event"
            dun_x_click = 280

            # dun_y_click => 이벤트는 강제 클릭

        # 390, 440, 490...
        dun_y_step = 340 + (dun_y_click * 50)

        # balbar, tapana, temple, swamp, redstone

        dun_in = False
        dun_in_count = 0

        while dun_in is False:
            dun_in_count += 1
            if dun_in_count > 7:
                dun_in = True


            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\dungeon_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 150, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon_title", imgs_)


                # 특수 or 일반 클릭
                for i in range(5):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(5, y_check_1, 60, y_check_2, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("clicked", imgs_)
                        break
                    else:
                        click_pos_2(65, y_click, cla)

                # 해당 던전 클릭
                for i in range(5):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\dun_not_opened.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(dun_x_click - 40, 180, dun_x_click + 40, 280, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        dun_in = True
                        complete = True
                        print("dun_not_opened", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\ready_title\\" + str(dun_name) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(660, 600, 870, 680, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("dun_name is ", str(dun_name), imgs_)
                            break
                        else:
                            click_pos_2(dun_x_click, 200, cla)
                            time.sleep(0.3)
                    time.sleep(0.5)

                # 남은 시간 있는지 확인하기
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\anymore_time.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(520, 700, 610, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    dun_in = True
                    complete = True

                if complete != True:

                    if dun[0] == "이벤트":
                        # 해당 층수 클릭
                        for i in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\dungeon_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 150, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("dungeon_title", imgs_)
                                click_pos_2(770, 720, cla)

                                result_inven = inven_check(cla)

                                if result_inven == True:

                                    already = False
                                    for a in range(10):
                                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\already_dun_in.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(370, 110, 570, 150, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            already = True
                                            break
                                        time.sleep(0.2)
                                    if already == True:
                                        clean_screen(cla)
                                else:
                                    break
                            else:
                                result_out = out_check(cla)
                                if result_out == True:
                                    dun_in = True
                                    # 고대의 신전은 랜덤이동하기
                                    # if dun_name == "temple":
                                    go_random(cla)

                                    # 공격
                                    attack_on(cla)
                                    juljun_on(cla)

                                    break
                            time.sleep(0.5)
                    else:
                        # 해당 층수 클릭
                        for i in range(10):
                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\step_not_opened.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(240, dun_y_step - 30, 280, dun_y_step + 30, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                dun_in = True
                                complete = True
                                print("step_not_opened", imgs_)
                                break
                            else:
                                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\dungeon_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 150, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("dungeon_title", imgs_)
                                    click_pos_2(180, dun_y_step, cla)
                                    time.sleep(0.5)
                                    click_pos_2(770, 720, cla)

                                    result_inven = inven_check(cla)

                                    if result_inven == True:

                                        already = False
                                        for a in range(10):
                                            full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\already_dun_in.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(370, 110, 570, 150, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                already = True
                                                break
                                            time.sleep(0.2)
                                        if already == True:
                                            clean_screen(cla)
                                    else:
                                        break
                                else:
                                    result_out = out_check(cla)
                                    if result_out == True:
                                        dun_in = True
                                        # 고대의 신전은 랜덤이동하기
                                        # if dun_name == "temple":
                                        go_random(cla)

                                        # 공격
                                        attack_on(cla)
                                        juljun_on(cla)

                                        break
                            time.sleep(0.5)

            else:
                menu_open(cla)
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\menu_dungeon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 310, 960, 610, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu_dungeon", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\dungeon_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 150, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("dungeon_title_ing...", imgs_)
                            break
                        time.sleep(0.5)

            time.sleep(0.5)

        if complete == True:
            myQuest_play_add(cla, data)

    except Exception as e:
        print(e)
        return 0

def dungeon_check(cla, data):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import juljun_check, juljun_on
    from clean_screen_raven2 import clean_screen

    try:
        print("dungeon_check")

        is_dun = False
        attack = False
        random = False

        dun = data.split("_")

        # 특수_타파나_4

        if dun[1] == "발바르":
            dun_name = "balbar"
        elif dun[1] == "타파나":
            dun_name = "tapana"
        elif dun[1] == "고대의신전":
            dun_name = "temple"
        elif dun[1] == "깊은늪":
            dun_name = "swamp"
        elif dun[1] == "붉은바위협곡":
            dun_name = "redstone"
        elif dun[0] == "이벤트":
            dun_name = "event"

        if dun_name == "temple" or dun_name == "swamp":
            folder_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\" + str(dun_name) + "\\" + str(dun[2])
        else:
            folder_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\" + str(dun_name)
        file_list = os.listdir(folder_path)
        dun_len = len(file_list)
        # print(file_count)

        # balbar, tapana, temple, swamp, redstone


        # 애초에 절전 던전인지 먼저 확인하기
        for i in range(dun_len):
            if dun_name == "temple" or dun_name == "swamp":
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\" + str(dun_name) + "\\" + str(
                    dun[2]) + "\\" + str(i) + ".PNG"
            else:
                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\" + str(dun_name) + "\\" + str(
                    i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 120, 150, 160, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("던전 사냥 중", i, "번째 맵 확인")

                if dun_name == "temple" or dun_name == "swamp":
                    if i == 0 or i == 1:
                        print("랜덤 이동 해야함")
                        random = True
                is_dun = True
                break

        if is_dun == True:
            if random != True:
                result_juljun = juljun_check(cla)

                if result_juljun[1] == "attack":
                    attack = True
                else:
                    attack = False
        else:
            # 우선 던전에 들어왔는지 확인하기

            for i in range(5):

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\check\\map\\map_open.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 950, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("map_open", imgs_)

                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\map_title\\" + str(dun_name) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 30, 600, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\dungeon\\map_title\\step.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 70, 600, 110, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("던전 진입 완료")
                            is_dun = True
                            juljun_on(cla)

                            result_juljun_check = juljun_check(cla)
                            if result_juljun_check[1] == "attack":
                                attack = True
                        else:
                            print("처음부터 다시 진입")
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
                        imgs_ = imgs_set_(50, 100, 200, 260, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(250, 135, cla)
                        else:
                            clean_screen(cla)

                QTest.qWait(500)



        if is_dun == False:
            # 던전 아니라서 던전 들어가기 시도하기

            print("해당 던전 아니다.", data)

        return is_dun, attack, random
    except Exception as e:
        print(e)
        return 0