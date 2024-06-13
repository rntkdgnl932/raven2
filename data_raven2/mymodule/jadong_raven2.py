import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def jadong_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_raven2 import go_maul, move_check, juljun_check, juljun_off, juljun_on, attack_on
    from clean_screen_raven2 import clean_screen
    from potion_raven2 import potion_check, potion_buy
    from dead_raven2 import dead_check_2, dead_recover

    try:
        print("jadong_start")

        result_dead = dead_check_2(cla)

        if result_dead == True:
            dead_recover(cla)
            potion_buy(cla)

        result_juljun = juljun_check(cla)
        # result_juljun[0] => True : 절전 맞음
        # result_juljun[1] => attack : 사냥 중 맞음, ready : 사냥 아님, no_spot : 사냥터로 ㄱㄱ
        if result_juljun[0] == False:
            # 사냥터 이동
            jadong_in(cla)
        elif result_juljun[0] == True and result_juljun[1] == "attack":
            print("사냥중")
            potion_check(cla)
            # 포션 체크...
            # 절전 중 집 가기...

        elif result_juljun[0] == True and result_juljun[1] != "attack":
            print("절전 풀고 공격버튼 클릭 후 다시 절전하기")
            juljun_off(cla)
            clean_screen(cla)
            attack_on(cla)
            juljun_on(cla)
            result_juljun = juljun_check(cla)
            if result_juljun[0] == True and result_juljun[1] != "attack":
                juljun_off(cla)
                jadong_in(cla)







    except Exception as e:
        print(e)
        return 0


def jadong_in(cla):
    import numpy as np
    import cv2
    import random
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_raven2 import out_check, confirm_all, juljun_on, attack_on
    from clean_screen_raven2 import clean_screen
    from dead_raven2 import dead_recover
    from potion_raven2 import potion_buy
    from massenger import line_to_me

    try:
        print("jadong_in")

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


                for i in range(10):
                    full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\jadong\\jadong_click_btn_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 70, 80, 570, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jadong_click_btn_1", imgs_)
                        break
                    else:
                        click_pos_2(305, 980, cla)

                    time.sleep(0.5)

                full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\jadong\\jadong_click_btn_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_for(20, 70, 80, 570, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jadong_click_btn_1", imgs_)

                if len(imgs_) > 0:
                    result_ran = random.randint(1, len(imgs_))
                    print("result_ran", result_ran)

                    result_click = imgs_[result_ran - 1]
                    print("result_click", result_click)
                    print("result_click[0]", result_click[0])
                    print("result_click[1]", result_click[1])

                    click_pos_reg(result_click[0], result_click[1], cla)

                    for i in range(5):
                        full_path = "c:\\my_games\\raven2\\data_raven2\\imgs\\jadong\\immediately_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 900, 930, 950, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("immediately_move", imgs_)
                            break
                        time.sleep(0.5)


                else:
                    spot_in = True
                    print("자동사냥 없다")
                    why = "자동 사냥 지점 해야 한다."
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

                            spot_in = True

                            attack_on(cla)

                            juljun_on(cla)
                            break
                        else:
                            confirm_all(cla)
                        time.sleep(0.5)


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
