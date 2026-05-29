import pyautogui as robot

robot.sleep(3)
for i in range(1,21):
    robot.sleep(0.5)
    robot.write(f'{i}. I can do it', interval=0.1)
    robot.press('enter')