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
    
    time.sleep(3)
    
    # minescript.echo(utils.get_menu_info()[33])
    # pyperclip.copy(have_wait_time())
    minescript.echo(have_wait_time())
    minescript.echo("done")
    
test()