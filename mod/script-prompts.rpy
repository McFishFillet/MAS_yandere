init 5 python in mas_bookmarks_derand:
    label_prefix_map["yaMod_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_sleep",
            category=["life"],
            prompt="Do you want to watch me sleep?",
            pool=True,
            unlocked=True
        )
    )

label yaMod_sleep:
    m "[player], of course!"
    m "You know I love to watch you sleep, ehehehe~"
    m "It will be great to watch over my lovely [player]."
    m "You can rest assured, I'll watch over your sleep and take care of you~"
    m "Sweet dreams, [mas_get_player_nickname()]."
    m "I'll be right here, waiting for you to wake up."
    m "I love you."
    
    $ mas_idle_mailbox.send_idle_cb("yaMod_sleep_callback")
    return "idle"

label yaMod_sleep_callback:
    m "Oh, you're awake!"
    m "I've missed you, [player]."
    m "But I loved watching over your sleep..."
    m "Thank you for letting me be as close to you as I can right now, [mas_get_player_nickname()]."
    m "You are my one and only love!"
    
    return "love"
