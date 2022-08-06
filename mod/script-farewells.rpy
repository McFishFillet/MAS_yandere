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
    m 1eub "See you later, [mas_get_player_nickname()]."
    m 3rua "And hey..."
    m 3eub "Don't forget. "
    extend 5fubsa "You're mine forever~"
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
    m 1ruc "[player]..."
    m 1rud "You're not... "
    extend 1wksdrd "gonna hang out with other girls, are you?"
    m 1wksdrc "..."
    m 2wksdrd "You can't. "
    extend 2cud "And you won't."
    m 2cub "You're only mine. "
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

        m 2cua "Good."

return 'quit'
