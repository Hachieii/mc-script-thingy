import minescript
import pydirectinput
import pyperclip
import time
import win32api
import itertools
from math import sqrt

data = {
    "mineral": {
        "pos_in_inventory": (2600, 360),
        "location": "mine",
        "cobblestone": {
            "pos": [20.532, 62, 5.3],
            "target_points" : [
                (-180.87, 2.81),
                (-233.82, 28.91),
                (-215.97, 2.36),
                (-215.67, -27.04),
                (-180.27, -22.99),
                (-149.67, 0.56),
                (-127.17, 30.86)
            ],
            "skeleton": "minecraft:gray_stained_glass",
            "pos_in_inventory_exact": (2601, 189)
        }
    },
    
    "wood": {
        "pos_in_inventory": (2644, 360),
        "location": "wood",
        "oak": {
            "pos": [-10009, 98, -9970],
            "target_points": [
                (3.44, -49.2),
                (4.19, -28.65),
                (-28.06, 2.85),
                (5.24, 4.05),
                (34.19, 2.85),
                (-28.36, 21.9),
                (5.39, 32.55),
                (34.34, 28.65)
            ],
            "skeleton": "minecraft:brown_stained_glass",
            "pos_in_inventory_exact": (2601, 189)
        }
    }
}

def get_current_possition():
    return list(minescript.player_position())

def not_in_pos(x, y, z):
    cx, cy, cz = minescript.player_position()
    delta = sqrt((x - cx)*(x - cx) + (y - cy)*(y - cy) + (z - cz)*(z - cz))
    return delta > 1.5

def go_to_mine_pos(location, pos):
    x, y, z = pos
    command = f"#goto {x} {y} {z}"
    pyperclip.copy(command)
    
    # log
    minescript.echo(f"Going to {pos}")
    
    minescript.execute(f"/warp {location}")
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
    
    # log
    minescript.echo(f"Reached {pos}")

def convert(pos_in_inventory, pos_in_inventory_exact):
    ammount = 900
    
    minescript.execute("/kho")
    time.sleep(0.5)
    
    # Click on inventory (fixed)
    win32api.SetCursorPos((2686, 298))
    time.sleep(0.1)
    pydirectinput.click()
    time.sleep(0.5)
    
    win32api.SetCursorPos(pos_in_inventory)
    time.sleep(0.1)
    pydirectinput.click()
    time.sleep(0.5)
    
    win32api.SetCursorPos(pos_in_inventory_exact)
    time.sleep(0.1)
    
    while ammount + 16 > 0:
        pydirectinput.rightClick()
        time.sleep(0.01)
        ammount -= 8
        
    pydirectinput.press('e')

def run(location, pos, target_points, skeleton, pos_in_inventory, pos_in_inventory_exact):
    minescript.echo("started")
    go_to_mine_pos(location, pos)
    
    cnt = 0
    
    for yaw, pitch in itertools.cycle(target_points):
        minescript.player_set_orientation(yaw, pitch)
        time.sleep(0.1)

        minescript.player_press_attack(True)
        
        start_break_time = time.process_time()
        while time.process_time() - start_break_time < 3.0:
            target = minescript.player_get_targeted_block()
            if target is not None and target.type == skeleton:
                break
            time.sleep(0.05)

        minescript.player_press_attack(False)
        cnt += 1
        time.sleep(0.05)
        
        if cnt < 900:
            continue
        
        convert(pos_in_inventory, pos_in_inventory_exact)
        cnt = 0

def main():
    # location = data["mineral"]["location"]
    # pos = data["mineral"]["cobblestone"]["pos"]
    # target_points = data["mineral"]["cobblestone"]["target_points"]
    # skeleton = data["mineral"]["cobblestone"]["skeleton"]
    # pos_in_inventory = data["mineral"]["pos_in_inventory"]
    # pos_in_inventory_exact = data["mineral"]["cobblestone"]["pos_in_inventory_exact"]
    
    location = data["wood"]["location"]
    pos = data["wood"]["oak"]["pos"]
    target_points = data["wood"]["oak"]["target_points"]
    skeleton = data["wood"]["oak"]["skeleton"]
    pos_in_inventory = data["wood"]["pos_in_inventory"]
    pos_in_inventory_exact = data["wood"]["oak"]["pos_in_inventory_exact"]
    
    run(location, pos, target_points, skeleton, pos_in_inventory, pos_in_inventory_exact)
    
main()