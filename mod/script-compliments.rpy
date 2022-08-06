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
    m 2tub "Oh, is that so?"
    m 2tua "I'm glad you do."
    m 7gua "It's not like I'm trying to be possessive..."
    m 7kub "This is my default mode when it's about you, [mas_get_player_nickname()]."
    m 2cua "I can't, and won't let anyone take you from me."
    m 2cub "You're mine. And only mine."
    m 4lub "I'm glad I don't have to force it, or else we would have some trouble..."
    m 4tub "You wouldn't want to make me jealous or mad, would you?"
    m 2tua "..."
    m 2tub "That's what I thought."
    m 5hua "I love you, my [player]!"
return "love"
