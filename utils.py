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
""")

get_syncId = pyjinn.get("get_syncId")
click_on_menu = pyjinn.get("click_on_menu")