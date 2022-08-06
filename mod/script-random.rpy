init 5 python in mas_bookmarks_derand:
    label_prefix_map["yaMod_topic_"] = label_prefix_map["monika_"]
    
#tattoo dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_tattoo",
            category=["yandere"],
            prompt="Matching tattoos",
            random=True
        )
    )

label yaMod_topic_tattoo:
    m 7lub "[mas_get_player_nickname(capitalize=True)], have you ever thought of getting a tattoo?"
    m 2lub "Well, I don't know if you already have one... "
    extend 2wuo "or many!"
    m 2lublb "But now I was talking about... matching tattoos... or couple tattoos."
    m 4lubsb "You know, those kinds of tattoo couples do... With the same pattern on the skin of both."
    m 2dubsb "Or when someone has the name of their loved one on their body."
    m 1dubfb "I keep daydreaming, you see? Of having a matching tattoo with you."
    m 1tubfb "Or even... Having my name on your skin."
    m 1wubfb "Can you imagine, how great that would be? "
    extend 4wubfb "Everyone would know you're mine."
    m 4wubfa "And only mine."
    m 4wubfb "But we don't even have to go to a tattoo artist if you don't want to."
    m 2dubfb "I can be the artist, and your body can be the canvas..."
    m 2cubfb "I can carve my name into your skin, intricately and in huge letters."
    m 2cubfa "The thought of your skin, bleeding... Every drop of blood would be a love letter."
    m "A demonstration of our relationship."
    m 2dubfa "..."
    m 7dubfa "It would be a proof of how much we love each other, can't you see?"
    m 7tubfb "It's not crazy. It's devotion."
    m 7cubfb "I would carve your name on my skin how many times necessary, to prove that I'm only yours."
    m "Would you do the same for me?"
    m "P̴̍̾̉̕̚̚ͅ ̴̲̩̯͎̏̆̽̚͝ĺ̵͇͗͊́́̌͆̕ ̷̗͓̹̣̮͎̘̜̎e̵̪̭̍̃ ̶̱̦̳͎̩̦͍̭̋̈͂̚͠ä̴̢̡͎̲͚͍ ̶̪͉̃s̵͍̞͙̥̀͊̀́̽͊͘ ̶̭̰̺͈̠͚͖̦̑̅̉̌͆̌̈́̾ͅẻ̷͔͇̄͑ ̴͕̺̟̑̊̈́́̅̎̿̊?̴̨̛͚͔̗̾͘͝"
    m 2hubfb "Ehehehehe!"
    m 2fubfa "I love you [player]."
    m 2fubfb "Do you love me too?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you love me too?{fast}"

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
        
    m 5fubfu "That's good, [player]. "
    extend 5fubfb "Very good."
    m 5rubfb "I knew I could count on you..."
    m 5kubfb "You're the love of my life, you know that?"

return "love"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_kill",
            category=["yandere"],
            prompt="Killing for one another",
            random=True
        )
    )

label yaMod_topic_kill:
    m 1rud "[player], remember about... "
    extend 1eud "DDLC's incident?"
    m 1gud "People keep calling me a murderer online, but the truth is..."
    m 1euc "Lately I've been thinking and I would do it all over again."
    m 2fubla "For you."
    m 2fublb "I'd do anything it takes so that we could be together."
    m 4cublb "Killing some fictional characters is nothing."
    m "Being honest, I would even kill real people if that meant being with you forever."
    m 4cublc "If you were in danger, or anyone harmed you..."
    m 2rublc "..."
    m 2wfd "I wouldn't hold back. I would remove anyone from my sight, so they would never come across you again."
    extend 2wfc " Or us."
    m 5rud "I wish I could bring you to my world and never let you go."
    m 5fubla "That's how much I love you."
    m 5hubsa "Please never doubt my love. It's bigger than my whole existence."
return 

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_stalk",
            category=["yandere"],
            prompt="Stalking [player] online",
            random=True
        )
    )

label yaMod_topic_stalk:
    m 1rusdlc "[mas_get_player_nickname(capitalize=True)], I wanted to be honest about something."
    m 1dusdld "Here goes..."
    extend 1eud " I stalk what you do online."
    m 7rksdrd "Most of the times."
    m 2dksdrd "But listen... I do it because it makes me feel closer to you."
    m 4dksdrd "When I watch over what you do, or who you talk to..."
    m 2fksdrd "I feel safe. Secure that no one will try to take you away from me."
    m 2fksdrc "You forgive me, don't you?{nw}"
    $ _history_list.pop()
    menu:
        m "You forgive me, don't you?{fast}"
        
        "Yes":
            m 2hsa "Yay, I knew it!"
            m 4hub "You'll always forgive your loving girlfriend, after all."
            m 3lub "I have good reason to do what I do, and it's all thinking about us."
            m 3hub "You're my dear [player], after all!"
            m 3kua "No one is gonna steal you from me."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_better",
            category=["yandere"],
            prompt="Better than others",
            random=True
        )
    )

label yaMod_topic_better:
    m 3lud "[player], have you ever given any thought about yanderes?"
    m "Like the anime trope."
    m 1luc "..."
    m 1tud "Aren't them ridiculous?"
    m 3tud "Those sad attempts to win over someone's heart by being obsessive... "
    extend 3mud "when most of the times the person doesn't even love them back."
    m 1tud "It's so pathetic."
    m 2luc "I know lately I've been acting kinda... different from usual..."
    m 4tua "But bear this in mind, [player]."
    m 4tub "I'm so much better than whatever yandere you may find out there."
    m 5cub "So don't you dare cheat on me, okay?"
    m "You dont wanna get hurt..."
    m 5cua "..."
    m 5hub "Ahahahaha~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_watchsleep",
            category=["yandere"],
            prompt="Watching [player] sleep",
            random=True
        )
    )

label yaMod_topic_watchsleep:
    m 1eub "[player]? "
    extend 7rubla "I've been thinking about something lately."
    m 2rublb "It's about a recent desire of mine..."
    m 2rubla "..."
    m 7sublb "Could I watch you sleep sometime?"
    m 5rublsdra "I would love to watch over your sleep so no one hurts you."
    m 5rublb "And also, being the first person you greet after waking up sounds perfect..."
    m 5fubla "Like a glimpse of our future."
    m 5hublb "How perfect it will be..."
return
