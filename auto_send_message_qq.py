#!/usr/bin/python

# 自动查找QQ联系人，并自动发送消息

import pyautogui
import time

# 通过command+tab切换到QQ
pyautogui.hotkey('command', 'tab')
pyautogui.hotkey('command', 'f')
# 当前是五笔输入法
pyautogui.write('ih ')
pyautogui.write('\n')
# 切换为英文输入法
pyautogui.hotkey('command', ' ')
time.sleep(1)
pyautogui.write('Hello World')
# 发送消息
pyautogui.hotkey('command', 'enter')
# 切换为五笔输入法
pyautogui.hotkey('command', ' ')
# 输入“你好，世界”
pyautogui.write('wqi vb ,anlw ')
pyautogui.hotkey('command', 'enter')
