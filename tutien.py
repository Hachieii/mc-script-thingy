import minescript
import time
import utils

def main():
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

main()