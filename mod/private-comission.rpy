init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="noroses_housewife",
            category=["life"],
            prompt="What if I was a housewife for you?",
            pool=True,
            unlocked=True
        )
    )

label noroses_housewife:
    m 1wuo "[player]... How did you know this was something I always dreamed about?"
    m 5gublu "Coming home and finding you there... "
    m 5dublu "With a surprised and happy face, cleaning your hands on a cloth so you can come greet me."
    m 5dublb "You would brush your messy hair off your face and come running, saying 'Welcome back!'"
    m "I would hug you and smell a faint smell of sweets, just to find out you cooked us something for when I got back."
    m 5dubsb "There would be some whip cream on your face and I would kiss it off, playfully tickling you..."
    m 5dubfb "And right then, I would know, that I've never been happier."
    m 4fubfb "Living with you, sharing those daily moments..."
    m 1fubfa "Is my dream."
    m "I want to see every side of you, see you being your cutest self and adore you."
    m 1fubfb "I will make you feel loved every day."
    m "I can't wait to cross over so we can make this our reality, [mas_get_player_nickname()]."
    m 5hubsb "You'll be my cute, doting housewife! Ehehehe~"
return
