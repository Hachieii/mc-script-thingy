import minescript
import time
import utils
from math import sqrt

def go_to_farm_land():
    minescript.player_press_sprint(True)
    minescript.player_press_forward(True)
    minescript.player_press_jump(True)
    
    while utils.get_syncId() <= 0:
        continue
    
    minescript.player_press_sprint(False)
    minescript.player_press_forward(False)
    minescript.player_press_jump(False)
    
    time.sleep(0.2)
    utils.click_on_menu(11)
    time.sleep(0.2)
    
def is_dead(x, y, z):
    cx, cy, cz = minescript.player_position()
    delta = sqrt((x - cx)*(x - cx) + (y - cy)*(y - cy) + (z - cz)*(z - cz))
    return delta > 1.5

def farming():
    while 1:
        go_to_farm_land()
        
        # should be tp to 1000.505 60 0.416
        x, y, z = minescript.player_position()
        
        while not is_dead(x, y, z):
            time.sleep(1)
            continue
        
def price_parser(x):
    base = {
        'K': 1000,
        'M': 1000000,
        'B': 1000000000
    }
    
    last = x[-1]
    if last not in base:
        return float(x)
    
    return float(x[:len(x) - 1]) * base[last]

def have_enough_khoang_thach(ammount):
    data = utils.get_scoreboard_info()
    cur = price_parser(data["khoang_thach"])
    return cur >= ammount
        
def crafting():
    while have_enough_khoang_thach(10):
        while utils.get_syncId() <= 0:
            time.sleep(1)
            continue
        utils.click_on_menu(19)
        time.sleep(15)

def main():
    # farming()
    crafting()

main()