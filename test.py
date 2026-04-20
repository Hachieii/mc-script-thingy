import minescript
import win32api
import time
import utils
import pyperclip
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
    # res = utils.get_menu_info()
    # res = utils.get_joinable_map()
    # minescript.echo(res)
    # pyperclip.copy(res)
    join_map()
   
    
    minescript.echo("done")
    
test()