import minescript
import pydirectinput
import pyperclip
import time
import win32api
import itertools
from math import sqrt

def get_angle():
    while True:
        yaw, pitch = minescript.player_orientation()
        
        text_hud = f"Yaw: {yaw:.2f} | Pitch: {pitch:.2f}"
        minescript.echo(text_hud)
        
        time.sleep(1) 
    
# yaw - pitch
# -180.87 2.81
# -233.82 28.91
# -215.97 2.36
# -215.67 -27.04
# -180.27 -22.99
# -149.67 0.56
# -127.17 30.86

# xyz
# 20.532 62 5.3

def get_current_possition():
    return list(minescript.player_position())

def not_in_pos(x, y, z):
    cx, cy, cz = minescript.player_position()
    delta = sqrt((x - cx)*(x - cx) + (y - cy)*(y - cy) + (z - cz)*(z - cz))
    return delta > 1.5

def go_to_mine_pos(mine_pos = [20.532, 62, 5.3]):
    x, y, z = mine_pos
    command = f"#goto {x} {y} {z}"
    pyperclip.copy(command)
    
    # log
    minescript.echo(f"Going to {mine_pos}")
    
    minescript.execute("/warp mine")
    time.sleep(1)
    
    pydirectinput.press('t')
    time.sleep(0.1)
    
    # pydirectinput.write(f"#goto {x} {y} {z}")
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('v')
    pydirectinput.keyUp('ctrl')
    time.sleep(0.05)
    pydirectinput.press('enter')
    
    while not_in_pos(x, y, z):
        time.sleep(0.1)
        continue
    
    # log
    minescript.echo(f"Reached {mine_pos}")

def convert_to_stone():
    ammount = 900
    
    minescript.execute("/kho")
    time.sleep(0.5)
    
    # 2688, 351
    # pydirectinput.moveTo(2690, 280)
    # pydirectinput.moveTo(2690, 280)
    win32api.SetCursorPos((2690, 280))
    time.sleep(0.1)
    pydirectinput.click()
    time.sleep(0.5)
    
    # while 1:
    #     minescript.echo(win32api.GetCursorPos())
    #     time.sleep(1)
    # 2570 132
    win32api.SetCursorPos((2570, 132))
    time.sleep(0.1)
    
    while ammount + 16 > 0:
        pydirectinput.rightClick()
        time.sleep(0.01)
        ammount -= 8
        
    pydirectinput.press('e')

def auto_mine(break_time=1.5):
    target_points = [
        (-180.87, 2.81),
        (-233.82, 28.91),
        (-215.97, 2.36),
        (-215.67, -27.04),
        (-180.27, -22.99),
        (-149.67, 0.56),
        (-127.17, 30.86)
    ]

    minescript.echo("started")
    go_to_mine_pos()
    
    cnt = 0
    
    for yaw, pitch in itertools.cycle(target_points):
        start_time = time.process_time()
        minescript.player_set_orientation(yaw, pitch)
        time.sleep(0.1)

        minescript.player_press_attack(True)
        
        while minescript.player_get_targeted_block().type != "minecraft:gray_stained_glass" and time.process_time() - start_time <= 5:
            continue

        minescript.player_press_attack(False)
        cnt += 1
        time.sleep(0.05)
        
        # minescript.echo(cnt)
        
        if cnt < 900:
            continue
        
        convert_to_stone()
        cnt = 0


def test():
    minescript.execute("/kho")
    time.sleep(0.5)
    
    # 2688, 351
    # pydirectinput.moveTo(2690, 280)
    # pydirectinput.moveTo(2690, 280)
    win32api.SetCursorPos((2690, 280))
    time.sleep(0.1)
    pydirectinput.click()
    time.sleep(0.5)
    
    # while 1:
    #     minescript.echo(win32api.GetCursorPos())
    #     time.sleep(1)
    # 2570 132
    win32api.SetCursorPos((2570, 132))
    time.sleep(0.1)
    
    while 1:
        pydirectinput.rightClick()
        time.sleep(0.1)


def main():
    auto_mine() 
    
main()