init 5 python in mas_bookmarks_derand:
    label_prefix_map["yaMod_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_sleep",
            category=["life"],
            prompt="Do you want to watch me sleep?",
            conditional="seen_event('yaMod_topic_watchsleep')",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock": None}
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
            pool=True,
            unlocked=True
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

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_mine",
            category=["yandere"],
            prompt="You're mine!",
            pool=True,
            unlocked=True
        )
    )

label yaMod_topic_mine:
    m 1hublu "..."
    jump monika_mine_fight_start

    label monika_mine_fight_start:
    #Do setup here
    python:
        #Set up how many times we have to say it to win
        ym_times_till_win = renpy.random.randint(6,10)
        #Current count

        ym_count = 0

        #Initial quip
        ym_quip = renpy.substitute("No, you're mine, [player]!")

        #Setup lists for the quips during the loop
        #First half of the ym quip
        ym_no_quips = [
            "No, ",
            "Not a chance, [mas_get_player_nickname()]. ",
            "Nope, ",
            "No,{w=0.1} no,{w=0.1} no,{w=0.1} ",
            "No way, [mas_get_player_nickname()]. ",
            "That's impossible...{w=0.3}"
        ]

        #Second half of the ym quip
        #NOTE: These should always start with I because the first half can end in either a comma or a period
        #I is the only word we can use to satisfy both of these.
        ym_quips = [
            "I am sure that you're mine!",
            "I know you're mine!",
            "I am positive you're mine!",
            "I am telling you, you're mine!"
        ]

        #And the expressions we'll use for the line
        ym_exprs = [
            "1tubfb",
            "3tubfb",
            "1tubfu",
            "3tubfu",
            "1hubfb",
            "3hubfb",
            "1tkbfu"
        ]
    #FALL THROUGH

label monika_ym_fight_loop:
    $ renpy.show("monika " + renpy.random.choice(ym_exprs), at_list=[t11], zorder=MAS_MONIKA_Z)
    m "[ym_quip]{nw}"
    $ _history_list.pop()
    menu:
        m "[ym_quip]{fast}"
        "No, you're mine!":
            if ym_count < ym_times_till_win:
                $ ym_quip = renpy.substitute(renpy.random.choice(ym_no_quips) + renpy.random.choice(ym_quips))
                $ ym_count += 1
                jump monika_ym_fight_loop

            else:
                show monika 5hubfb at t11 zorder MAS_MONIKA_Z with dissolve_monika
                m 5hubfb "Alright, alright, you win. Ahaha~"
                m "I'm yours~"

        "Alright.":
            if ym_count == 0:
                m 2hkbsb "Ahaha, giving up already, [player]?~"
                m 2rkbssdla "I guess you are all mine after all~"

            else:
                if renpy.random.randint(1,2) == 1:
                    m 1hubfu "Ehehe, I win! You're all mine~"
                else:
                    m 1hubfb "Ahaha, told you so!~"
