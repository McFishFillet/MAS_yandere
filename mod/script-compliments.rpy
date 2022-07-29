#I love how possessive you are
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ya_compliment_possessive",
            category=["mas_compliment"],
            prompt="I love how possessive you are.",
            unlocked=True
        ),
        code="CMP"
    )

label ya_compliment_possessive:
    m "Oh, is that so?"
    m "I'm glad you do."
    m "It's not like I'm trying to be possessive..."
    m "This is my default mode when it's about you, [player]."
    m "I can't, and won't let anyone take you from me."
    m "You're mine. And only mine."
    m "I'm glad I don't have to force it, or else we would have some trouble..."
    m "You wouldn't want to make me jealous or mad, would you?"
    m "..."
    m "That's what I thought."
    m "I love you, my [player]!"
return "love"
