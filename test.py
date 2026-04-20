import minescript
import win32api
import time
import utils
import pyperclip
import re

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
    
    raw = utils.get_scoreboard_info()
    # pyperclip.copy(raw)
    minescript.echo(raw)
    
    minescript.echo('done')
    # res = re.search(r'(\d+)\s*\xca\x9f\xc9\xaa\xc9\xb4\xca\x9c', raw)
    
    # minescript.echo('\xca\x9f\xc9\xaa\xc9\xb4\xca\x9c' in raw)
    # for v in raw:
    #     minescript.echo(type(v))
    
    # minescript.echo(utils.dump())
    return

test()