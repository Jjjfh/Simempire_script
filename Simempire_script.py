import os
import time
import aircv as ac
from external_con import adb
import json


class script:
    a_adb = adb()

    def scan_district(self, orientation=None, step=100.0):
        start_coordinate = [0.0, 0.0]
        end_coordinate = [800, 600.0]
        if orientation == 'left':
            start_coordinate[0] = end_coordinate[0] - step
            start_coordinate[1] = end_coordinate[1]
            self.a_adb.swipe(start_coordinate, end_coordinate)
        elif orientation == 'right':
            start_coordinate[0] = end_coordinate[0] + step
            start_coordinate[1] = end_coordinate[1]
            self.a_adb.swipe(start_coordinate, end_coordinate)
        elif orientation == 'up':
            start_coordinate[0] = end_coordinate[0]
            start_coordinate[1] = end_coordinate[1] - step
            self.a_adb.swipe(start_coordinate, end_coordinate)
        elif orientation == 'down':
            start_coordinate[0] = end_coordinate[0]
            start_coordinate[1] = end_coordinate[1] + step
            self.a_adb.swipe(start_coordinate, end_coordinate)

    def first_auto_get(self):
        my_dict = {"brick": [], "copper": [], "copper_mine": [], "fishes": [], "fruits": [], "gold": [], "meat": [],
                   "niantu": [], "stone": [],
                   "vegetables": [], "wa": [], "weapon": [], "wood": [], "ciqi": [], "liangshi": []}
        self.a_adb.screen_shot()
        sourece_name = self.a_adb.pull_screen()
        im_source = ac.imread(sourece_name)
        elements = ["brick", "copper", "copper_mine", "fishes", "fruits", "gold", "meat", "niantu", "stone",
                    "vegetables", "wa", "weapon", "wood", "ciqi", "liangshi"]
        print('处理第' + str(self.a_adb.count) + '张图')
        for a in range(0, len(elements)):
            search_name = 'D:\python.code\game_script\image' + '\\' + elements[a] + '.png'
            im_search = ac.imread(search_name)
            result = ac.find_all_template(im_source, im_search, 0.90)
            ma_c = len(result)
            if ma_c == 0:
                print('没有' + elements[a])
            else:
                for a_cc in range(0, ma_c):
                    coordinate = result[a_cc]['result']
                    self.a_adb.tap(coordinate)  # 可以注释掉，该函数只完成截屏匹配存储文件，不完成点击
                    time.sleep(1)
                    my_dict[elements[a]].append(coordinate)
                print('收获了' + str(ma_c) + '个' + elements[a])
        file_n = "screen_t" + str(self.a_adb.count) + ".json"
        tf = open(file_n, "w")
        json.dump(my_dict, tf)
        tf.close()
        print('完成第' + str(self.a_adb.count) + '个文件保存')

    def finish_auto_get(self, num):
        file_name = "screen" + str(num) + ".json"
        tf = open(file_name, "r")
        my_dict = json.load(tf)
        for key, value in my_dict.items():
            if value:
                cou = len(value)
                for t in range(0, cou):
                    coordinate = value[t]
                    self.a_adb.tap(coordinate)
                    time.sleep(1)
                print('收集了' + str(cou) + '个' + key)

    def call_people(self):
        count = 0
        im_source = ac.imread("D:\python.code\game_script\image\\test.png")
        im_search = ac.imread("D:\python.code\game_script\image\people.png")
        result = ac.find_all_template(im_source, im_search, 0.80)
        coordinate = result[0]['result']
        self.a_adb.tap(coordinate)
        time.sleep(1)
        count += 1
        print('召集' + str(count) + '次移民')


# right600 left600 up400 down200
# te.scan_district(orientation='up', step=400)
# te.scan_district(orientation='right', step=600)
# te.scan_district(orientation='left', step=600)
# te.scan_district(orientation='down', step=200)
if __name__ == '__main__':
    adb_m = adb()
    te = script()
    count = 0
    coordinate_1 = (147, 147)
    coordinate_2 = (150, 170)
    coordinate_3 = (192, 147)
    coordinate_4 = (211, 173)
    coordinate_5 = (202, 106)
    coordinate_6 = (189, 83)
    coordinate_7 = (93, 64)
    sta_c = (701, 819)
    end_c = (707, 550)
    sta_c1 = (710, 634)
    end_c1 = (739, 339)
    sta_c2 = (832, 630)
    end_c2 = (998, 595)
    sta_c3 = (746, 765)
    end_c3 = (1078, 640)
    adb_m.tap(coordinate_2)
    time.sleep(1)
    adb_m.tap(coordinate_4)
    time.sleep(1)
    while 1:
        time.sleep(1800)
        count += 1
        adb_m.tap(coordinate_4)
        te.finish_auto_get(4)
        if count % 2 == 0:
            adb_m.tap(coordinate_2)
            te.finish_auto_get(2)
            print('60min')
        print('30min')

    # while 1:
    #     adb_m.tap(coordinate_1)
    #     te.finish_auto_get(1)
    #     adb_m.tap(coordinate_2)
    #     te.finish_auto_get(2)
    #     adb_m.tap(coordinate_3)
    #     te.finish_auto_get(3)
    #     adb_m.tap(coordinate_4)
    #     te.finish_auto_get(4)
    #     adb_m.tap(coordinate_5)
    #     te.finish_auto_get(5)
    #     adb_m.tap(coordinate_6)
    #     te.finish_auto_get(6)
    #     adb_m.tap(coordinate_7)
    #     te.finish_auto_get(7)
    #     adb_m.swipe(sta_c,end_c)
    #     adb_m.swipe(sta_c1, end_c1)
    #     adb_m.swipe(sta_c2, end_c2)
    #     te.finish_auto_get(8)
    #     adb_m.swipe(sta_c3, end_c3)
    #     te.finish_auto_get(9)
    #     print('完成1次收获')
    #     break
