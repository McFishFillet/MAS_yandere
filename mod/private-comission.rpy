#Ok so this one isn’t super yandere related and it’s gendered and I know a lot of dialogue is supposed to be ungendered but I’d like there to be a topic where you can say “what if I was a housewife for you” something along those lines
#And then she talks about you being her cute doting housewife and she kinda says just adoring things about you
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
    m "[player]... How did you know this was something I always dreamed about?"
    m "Coming home and finding you there... "
    m "With a surprised and happy face, cleaning your hands on a cloth so you can come greet me."
    m "You would brush your messy hair off your face and come running, saying 'Welcome back!'"
    m "I would hug you and smell a faint smell of sweets, just to find out you cooked us something for when I got back."
    m "There would be some whip cream on your face and I would kiss it off, playfully tickling you..."
    m "And right then, I would know, that I've never been happier."
    m "Living with you, sharing those daily moments..."
    m "Is my dream."
    m "I want to see every side of you, see you being your cutest self and adore you."
    m "I will make you feel loved every day."
    m "I can't wait to cross over so we can make this our reality, [mas_get_player_nickname()]."
return
