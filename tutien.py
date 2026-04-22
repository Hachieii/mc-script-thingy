import minescript
import time
import utils
from math import sqrt
import re

def join_map():
    joinables = utils.get_joinable_map()
    map_index = joinables[-1]
    
    while len(joinables) == 21: # full
        utils.click_on_menu(42) # next page
        time.sleep(0.2)
        joinables = utils.get_joinable_map()
        map_index = joinables[-1] if joinables else map_index
    
    utils.click_on_menu(map_index)

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
    join_map()
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

def go_to_bequan():
    minescript.execute("/warp bequan")
    time.sleep(2)
    minescript.chat("#goto 116 103 -99835")

def login():
    minescript.execute("/login 00000000")
    # yes hardcoded password, idc :p
    
    time.sleep(1)
    
    minescript.player_inventory_select_slot(4)
    minescript.player_press_use(True)
    time.sleep(0.1)
    minescript.player_press_use(False)
    
    time.sleep(1)
    utils.click_on_menu(22)
    time.sleep(1)
    utils.click_on_menu(22)
    time.sleep(2)

def relogin_if_disconnected():
    world = minescript.world_info()
    
    cnt = 0
    while not world:
        time.sleep(10)
        world = minescript.world_info()
        
        cnt += 1
        if cnt <= 10:
            continue
        exit(0)
    
    spawn_location = world.spawn
    if spawn_location == [0, 64, 0]:
        return
        
    login()
        
def crafting():
    minescript.execute("/warp chetao")
    time.sleep(2)
    minescript.chat("#goto 45 150 -99818")
    
    while have_enough_khoang_thach(10):
        while utils.get_syncId() <= 0:
            time.sleep(0.5)
            continue
        
        if utils.can_upgrade():
            utils.click_on_menu(33) # assuming have enough linh thach
            time.sleep(0.5)
            
        utils.click_on_menu(19)
        time.sleep(15)
        
    go_to_bequan()

def run(job):
    relogin_if_disconnected()
    
    try:
        job()
    except Exception as e:
        minescript.echo(e)

while 1:
    run(crafting)

# farming()
# go_to_bequan()