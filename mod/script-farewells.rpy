#youre mine forever
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_yaMod_youremineforever",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_yaMod_youremineforever:
    m 1hua "See you later, [mas_get_player_nickname()]."
    m "And hey..."
    m "Don't forget. "
    extend "You're mine forever~"
    return 'quit'

#other girls
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_yaMod_othergirls",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_yaMod_othergirls:
    m 1hua "[player]..."
    m "You're not... "
    extend "gonna hang out with other girls, are you?"
    m "..."
    m "You can't. "
    extend "And you won't."
    m "You're only mine. "
    extend "Forever. Do you understand that?{nw}"
$ _history_list.pop()
menu:
        m "Forever. Do you understand that?{fast}"

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

        "Yes":
        pass

    m "Good."

return 'quit'
