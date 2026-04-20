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
    
    time.sleep(3)
    
    utils.click_on_menu(33) # assuming have enough linh thach
    time.sleep(0.5)
    
    # reopen the menu
    minescript.player_press_backward(True)
    time.sleep(0.25)
    minescript.player_press_backward(False)
    
    minescript.player_press_forward(True)
    time.sleep(0.5)
    minescript.player_press_forward(False)
    
    minescript.echo("done")
    
test()