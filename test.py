from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver as appium_webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
import os
import math
import time
from appium import webdriver as app_web
from PIL import Image
from io import StringIO, BytesIO
import os
import time
import aircv as ac
from external_con import adb
import json

SCREEN = 'adb shell screencap /sdcard/screen'
file_name = 'D:/python.code/game_script/image'
pull_pc = 'adb pull /sdcard/screen'
TAP = "adb shell input tap "  # 点击屏幕 x y
SWIPE = "adb shell input swipe "  # 滑动屏幕


class Utils:
    count = 0

    def screen_shot(self):
        self.count += 1
        cmd = SCREEN + str(self.count) + '.png'
        os.popen(cmd)
        time.sleep(2)
        return self.count

    def pull_screen(self):
        cmd = pull_pc + str(self.count) + '.png' + ' ' + file_name
        # print(cmd)
        os.popen(cmd)
        time.sleep(2)
        return file_name + '/' + 'screen' + str(self.count) + '.png'

    def tap(self, position):
        cmd = TAP + str(position[0]) + " " + str(position[1])
        os.popen(cmd)
        time.sleep(3)

    def swipe(self, pos1, pos2):
        cmd = SWIPE + str(pos1[0]) + " " + str(pos1[1]) + " " + str(pos2[0]) \
              + " " + str(pos2[1])
        os.popen(cmd)
        time.sleep(3)


if __name__ == '__main__':
    a = 1 % 2
    print(a)
    # script_v0
    # use = Utils()
    # use.screen_shot()
    # file_name1 = use.pull_screen()
    # im_search1 = ac.imread("D:\python.code\game_script\image\start.png")
    # im_search2 = ac.imread("D:\python.code\game_script\image\end.png")
    # im_source = ac.imread(file_name1)
    # result = ac.find_all_template(im_source, im_search1)
    # start = result[0]['result']
    # result = ac.find_all_template(im_source, im_search2)
    # end = result[0]['result']
    # use.swipe(start, end)
    # # 到达目标区域后
    # use.screen_shot()
    # file_name1 = use.pull_screen()
    # im_source = ac.imread(file_name1)
    # im_search = ac.imread("D:\python.code\game_script\image\gold.png")
    # result = ac.find_all_template(im_source, im_search)
    # max_c = len(result)
    # print('共找到' + str(max_c) + '目标')
    # for n in range(0, max_c):
    #     coordinate = result[n]['result']
    #     use.tap(coordinate)
    # print('完成收获，结束')
    # im_search = ac.imread("D:\python.code\game_script\image\start.png")
    # im_source = ac.imread("D:\python.code\game_script\image\screen1.png")
    # result = ac.find_all_template(im_source, im_search)
    # print(result)

    '''script_v1.1'''
    # a_adb = adb()
    # elements = ["brick", "copper", "copper_mine", "fishes", "fruits", "gold", "meat", "niantu", "stone",
    #             "vegetables", "wa", "weapon", "wood", "ciqi", "liangshi"]
    # for a in range(1, 10):
    #     my_dict = {"brick": [], "copper": [], "copper_mine": [], "fishes": [], "fruits": [], "gold": [], "meat": [],
    #                "niantu": [], "stone": [],
    #                "vegetables": [], "wa": [], "weapon": [], "wood": [], "ciqi": [], "liangshi": []}
    #     print('处理第' + str(a) + '张图')
    #     source_name = 'D:/python.code/game_script/image/screen' + str(a) + '.png'
    #     im_source = ac.imread(source_name)
    #     for b in range(0, len(elements)):
    #         search_name = 'D:\python.code\game_script\image' + '\\' + elements[b] + '.png'
    #         im_search = ac.imread(search_name)
    #         result = ac.find_all_template(im_source, im_search, 0.8)
    #         ma_c = len(result)
    #         if ma_c == 0:
    #             pass
    #             # print('没有' + elements[b])
    #         else:
    #             for a_cc in range(0, ma_c):
    #                 coordinate = result[a_cc]['result']
    #                 my_dict[elements[b]].append(coordinate)
    #             print('收获了' + str(ma_c) + '个' + elements[b])
    #     # 保存文件
    #     file_n = "screen" + str(a) + ".json"
    #     tf = open(file_n, "w")
    #     json.dump(my_dict, tf)
    #     tf.close()
    #     print('wancheng' + str(a))
    # tf = open("screen1.json", "r")
    # my_dict = json.load(tf)
    # for key, value in my_dict.items():
    #     if value:
    #         cou = len(value)
    #         for t in range(0,cou):
    #             print(value)
    #         print('收集了' + str(cou) + '个' + key)

# Appium 测试
# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': '127.0.0.1:7555',
#     'platformVersion': '6.0.1',
#     'appPackage': 'com.trueknownewgame.ec2',
#     'appActivity': 'com.trueknownewgame.ec2.MainActivity',
#     'automationName': 'uiautomator2'  # toast
# }
# driver = appium_webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(50)
# actions = ActionChains(driver)
# el_authority = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
# el_authority.click()
#
# # 截图，app_screenshoot和当前程序文件夹同级
# driver.get_screenshot_as_file(f'{os.getcwd()}/app_screenshoot/1.png')
#
# # 校验弹窗
# toast_message = "请先登录"
# message = '//*[@text=\'{}\']'.format(toast_message)
# toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
# print(toast_element.text)
# assert toast_element.text == toast_message
#
# print("pass")
# time.sleep(13)
# TouchAction(driver).tap(x=390, y=700).perform()
# time.sleep(6)
# TouchAction(driver).tap(x=977, y=773).perform()
# time.sleep(5)
# TouchAction(driver).tap(x=390, y=700).perform()
# time.sleep(10)
# TouchAction(driver).tap(x=583, y=572).perform()
# time.sleep(2)
# TouchAction(driver).tap(x=753, y=805).perform()
# time.sleep(15)
# TouchAction(driver).tap(x=1229, y=150).perform()
#
# time.sleep(5)
# TouchAction(driver)   .press(x=694, y=858)   .move_to(x=704, y=621)   .release()   .perform()
# TouchAction(driver).tap(x=493, y=707).perform()
#
#
# TouchAction(driver).tap(x=753, y=837).perform()
# TouchAction(driver).tap(x=795, y=749).perform()
# TouchAction(driver).tap(x=1062, y=95).perform()
