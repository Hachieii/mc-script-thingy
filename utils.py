import java

pyjinn = java.eval_pyjinn_script("""
MinecraftClient = JavaClass("net.minecraft.class_310")
# net.minecraft.client.MinecraftClient

instance = MinecraftClient.method_1551()
# getInstance()

SlotActionType = JavaClass("net.minecraft.class_1713")
SlotActionType_map = {
    "CLONE": SlotActionType.field_7796,
    "PICKUP": SlotActionType.field_7790,
    "PICKUP_ALL": SlotActionType.field_7793,
    "QUICK_CRAFT": SlotActionType.field_7789,
    "QUICK_MOVE": SlotActionType.field_7794,
    "SWAP": SlotActionType.field_7791,
    "THROW": SlotActionType.field_7795
}

def get_syncId():
    player = instance.field_1724
    
    if player and player.field_7512:
        return player.field_7512.field_7763
        # currentScreenHandle.syncId

    return -1
    
def click_on_menu(slotId, button=0, actionType="PICKUP"):
    syncId = get_syncId() # window id
    # slotId = x # pos to click at
    # button = 0 # left click
    actionType = SlotActionType_map[actionType]
    player = instance.field_1724
    
    interactionManager = instance.field_1761
    interactionManager.method_2906 ( # clickSlot
        syncId,
        slotId,
        button,
        actionType,
        player
    )
    
def get_scoreboard_info():
    world = instance.field_1687
    scoreboard = world.method_8428() # getScoreboard()
    teams = scoreboard.method_1159() # getTeams()
    
    patterns = {
        "linh_thach": "\\u029f\\u026a\\u0274\\u029c \\u1d1b\\u029c\\u1ea1\\u1d04\\u029c",
        "khoang_thach": "\\u1d0b\\u029c\\u1d0f\\u00e1\\u0274\\u0262 \\u1d1b\\u029c\\u1ea1\\u1d04\\u029c",
        "thao_duoc": "\\u1d1b\\u029c\\u1ea3\\u1d0f \\u1d05\\u01b0\\u1ee3\\u1d04",
        "thien_xu": "\\u1d1b\\u029c\\u026a\\u00ea\\u0274 x\\u1d1c",
    }
    tu_vi_pattern = "\\u1d1b\\u1d1c \\u1d20\\u026a" # special case
    
    res = {
        "tu_vi": "",
        "linh_thach": "",
        "khoang_thach": "",
        "thao_duoc": "",
        "thien_xu": ""
    }
    
    for team in teams.toArray():
        # prefix = str(team.method_1144()) # getPrefix()
        # suffix = str(team.method_1136()) # getSuffix()
        # full_text = prefix + suffix
        
        # It is known that the information we are looking for only appear in prefix
        
        content = str(team.method_1144())
        
        for key, pattern in patterns.items():
            if len(res[key]):
                continue
            
            r = content.find(pattern)
            if r == -1:
                continue
            
            l = r - 2
            while content[l] != ' ':
                l -= 1
            
            res[key] = content[l + 1: r - 1]
       
        if len(res["tu_vi"]):
            continue
            
        idx = content.find(tu_vi_pattern)
        if idx == -1:
            continue
            
        idx = content.find("literal", idx)
        l = idx + len("literal{")
        r = content.find("}", l)
        
        v1 = content[l:r]
        
        tmp = content.find("literal{/}", idx) + len("literal{/}")
        idx = content.find("literal", tmp)
        
        l = idx + len("literal{")
        r = content.find(' ', l)
        
        v2 = content[l:r]
        
        res["tu_vi"] = f"{v1}/{v2}"
    
    return res
    
def get_menu_info():
    currentScreen = instance.field_1755
    screenHandler = currentScreen.method_17577() # getScreenHandler()
    slots = screenHandler.field_7761
    
    res = []
    
    for i in range(slots.size()):
        slot = slots.get(i)
        stack = slot.method_7677() # getStack()
        
        if stack.method_7960(): # isEmpty()
            res.append(["", ""])
            continue
            
        metadata = stack.method_57353() # getCompenents
        cnt = stack.method_7947() # getCount()
        
        res.append([str(metadata), cnt])
        
    return res

def get_joinable_map():
    res = []
    items = get_menu_info()
    
    for i in range(len(items)):
        metadata = items[i][0]
        
        if "tham gia" not in metadata:
            continue
            
        res.append(i)
        
    return res
""")

get_syncId = pyjinn.get("get_syncId")
click_on_menu = pyjinn.get("click_on_menu")
get_scoreboard_info = pyjinn.get("get_scoreboard_info")
get_menu_info = pyjinn.get("get_menu_info")
get_joinable_map = pyjinn.get("get_joinable_map")