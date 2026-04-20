import minescript
import win32api
import time

def test():
    # while 1:
    #     minescript.echo(minescript.player_orientation())
    #     time.sleep(1)
    
    # while 1:
    #     minescript.echo(minescript.player_get_targeted_block().type)
    #     time.sleep(1)
    
    while 1:
        minescript.echo(win32api.GetCursorPos())
        time.sleep(1)
    
    return

test()