import minescript
import win32api
import time
import utils
import pyperclip
import re

def get_current_progess():
    content = str(utils.get_menu_info()[33])
    match = re.search(r'\((\d+)/(\d+)\)', content)
    
    a = int(match.group(1))
    b = int(match.group(2))
    
    return [a, b]

def have_wait_time():
    content = str(utils.get_menu_info()[33])
    match = re.search(r'literal\{(\d+:\d+:\d+)\}', content)
    return not match
    
def test():
    # while 1:
    #     minescript.echo(minescript.player_orientation())
    #     time.sleep(1)
    
    # while 1:
    #     minescript.echo(minescript.player_get_targeted_block().type)
    #     time.sleep(1)
    
    # while 1:
    #     minescript.echo(win32api.GetCursorPos())
    #     time.sleep(1)
    
    # time.sleep(3)
    
    # minescript.echo(utils.get_menu_info()[33])
    # pyperclip.copy(have_wait_time())
    # minescript.echo(have_wait_time())
    # minescript.echo("done")
    
    # minescript.execute("/login 00000000")
    # time.sleep(1)
    
    # minescript.player_inventory_select_slot(4)
    # minescript.player_press_use(True)
    # time.sleep(0.1)
    # minescript.player_press_use(False)
    
    # time.sleep(1)
    # utils.click_on_menu(22)
    # time.sleep(1)
    # utils.click_on_menu(22)
    # time.sleep(1)
    
    minescript.echo(minescript.world_info().spawn)
    # [0, 64, 0]
    
test()