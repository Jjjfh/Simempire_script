import os
import time
SCREEN = 'adb shell screencap /sdcard/screen'
file_name = 'D:/python.code/game_script/image'
pull_pc = 'adb pull /sdcard/screen'
TAP = "adb shell input tap "  # 点击屏幕 x y
SWIPE = "adb shell input swipe "  # 滑动屏幕


class adb:
    count = 0

    def screen_shot(self):
        self.count += 1
        cmd = SCREEN + str(self.count) + '.png'
        os.popen(cmd)
        time.sleep(3)
        return self.count

    def pull_screen(self):
        cmd = pull_pc + str(self.count) + '.png' + ' ' + file_name
        os.popen(cmd)
        time.sleep(3)
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
