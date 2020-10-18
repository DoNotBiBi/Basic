import pyautogui

import time
def test_gui():
    # print(pyautogui.size())  # 输出屏幕的宽和高 返回一个tuple
    for i in range(10):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

def test_gui2():
    for i in range(10):
        pyautogui.moveRel(100,0,duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)
def Get_Mouse_Position():
    try:
        while True:
            x,y=pyautogui.position()
            positionStr='x:'+str(x).rjust(4)+ ' y:'+str(y).rjust(4)
            print(positionStr,end='')
            print('\b'*len(positionStr),end='',flush=True)
    except KeyboardInterrupt:
        print('Done')

def test_MoustClick():
    # doubleClick
    # rightClick
    # middleClick
    # pyautogui.click(300,300,button='right')
    # time.sleep(5)
    # pyautogui.click()
    # distance=200
    # while distance > 0:
    #     pyautogui.dragRel(distance,0,duration=0.1)
    #     distance =distance-5
    #     pyautogui.dragRel(0, distance, duration=0.2)
    #     pyautogui.dragRel(-distance,0,duration=0.2)
    #     distance = distance - 5
    #     pyautogui.dragRel(0, -distance, duration=0.2)
    pyautogui.scroll(100)

