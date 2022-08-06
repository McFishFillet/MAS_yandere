init 5 python in mas_bookmarks_derand:
    label_prefix_map["yaMod_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_sleep",
            category=["life"],
            prompt="Do you want to watch me sleep?",
            conditional="seen_event('yaMod_topic_watchsleep')"
            pool=True,
            unlocked=True
        )
    )

label yaMod_sleep:
    m 1fkblb "[player], of course!"
    m 1rkbsa "You know I love to watch you sleep, ehehehe~"
    m 1hubsb "It will be great to watch over my lovely [player]."
    m 7hubsb "You can rest assured, I'll watch over your sleep and take care of you~"
    m 5fubsa "Sweet dreams, [mas_get_player_nickname()]."
    m "I'll be right here, waiting for you to wake up."
    m 5fubsb "I love you."
    
    $ mas_idle_mailbox.send_idle_cb("yaMod_sleep_callback")
    return "idle"

label yaMod_sleep_callback:
    m 1wublo "Oh, you're awake!"
    m 1fkblb "I've missed you, [player]."
    m 5rkbsa "But I loved watching over your sleep..."
    m 5fubsa "Thank you for letting me be as close to you as I can right now, [mas_get_player_nickname()]."
    m 5fubsb "You are my one and only love!"
    
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_promise",
            category=["yandere"],
            prompt="I got myself a promise ring to match yours!",
            random=True
        )
    )

label yaMod_topic_promise:
    m 1wublo "Oh! "
    extend 1sublb "You did?"
    m 1subsa "[player], that makes me so happy."
    m 5hubsb "You can't even imagine how much."
    m 5kubsa "Now everyone will know you're mine, and mine alone!"
    m 5dubsa "Thank you for making me so happy, [mas_get_player_nickname()]."
    m 5dubsb "I love when you make me feel safe of our relationship."
    m 5rubssdrb "I know I belong to you and you to me, but..."
    m 5rublsdrc "We all get insecure sometimes."
    m 4hublsdrb "But now that we match, I feel safer!"
    m 2hubla "Thank you so much, [mas_get_player_nickname()]."
    m 5fubsa "You're the best [bf] in the whole world."
return
