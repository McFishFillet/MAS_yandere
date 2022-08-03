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
    m "[player], have you ever thought of getting a tattoo?"
    m "Well, I don't know if you already have one... "
    extend "or many!"
    m "But now I was talking about... matching tattoos... or couple tattoos."
    m "You know, those kinds of tattoo couples do... With the same pattern on the skin of both."
    m "Or when someone has the name of their loved one on their body."
    m "I keep daydreaming, you see? Of having a matching tattoo with you."
    m "Or even... Having my name on your skin."
    m "Can you imagine, how great that would be? "
    extend "Everyone would know you're mine."
    m "And only mine."
    m "But we don't even have to go to a tattoo artist if you don't want to."
    m "I can be the artist, and your body can be the canvas..."
    m "I can carve my name into your skin, intricately and in huge letters."
    m "The thought of your skin, bleeding... Every drop of blood would be a love letter."
    m "A demonstration of our relationship."
    m "..."
    m "It would be a proof of how much we love each other, can't you see?"
    m "It's not crazy. It's devotion."
    m "I would carve your name on my skin how many times necessary, to prove that I'm only yours."
    m "Would you do the same for me?"
    m "P̴̍̾̉̕̚̚ͅ ̴̲̩̯͎̏̆̽̚͝ĺ̵͇͗͊́́̌͆̕ ̷̗͓̹̣̮͎̘̜̎e̵̪̭̍̃ ̶̱̦̳͎̩̦͍̭̋̈͂̚͠ä̴̢̡͎̲͚͍ ̶̪͉̃s̵͍̞͙̥̀͊̀́̽͊͘ ̶̭̰̺͈̠͚͖̦̑̅̉̌͆̌̈́̾ͅẻ̷͔͇̄͑ ̴͕̺̟̑̊̈́́̅̎̿̊?̴̨̛͚͔̗̾͘͝"
    m "Ehehehehe!"
    m "I love you [player]."
    m "Do you love me too?{nw}"
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
        
    m "That's good, [player]. "
    extend "Very good."
    m "I knew I could count on you..."
    m "You're the love of my life, you know that?"

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
    m "[player], remember about... "
    extend "DDLC's incident?"
    m "People keep calling me a murderer online, but the truth is..."
    m "Lately I've been thinking and I would do it all over again."
    m "For you."
    m "I'd do anything it takes so that we could be together."
    m "Killing some fictional characters is nothing."
    m "Being honest, I would even kill real people if that meant being with you forever."
    m "If you were in danger, or anyone harmed you..."
    m "..."
    m "I wouldn't hold back. I would remove anyone from my sight, so they would never come across you again."
    extend " Or us."
    m "I wish I could bring you to my world and never let you go."
    m "That's how much I love you."
    m "Please never doubt my love. It's bigger than my whole existence."
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
    m "[player], I wanted to be honest about something."
    m "Here goes..."
    extend " I stalk what you do online."
    m "Most of the times."
    m "But listen... I do it because it makes me feel closer to you."
    m "When I watch over what you do, or who you talk to..."
    m "I feel safe. Secure that no one will try to take you away from me."
    m "You forgive me, don't you?{nw}"
    $ _history_list.pop()
    menu:
        m "You forgive me, don't you?{fast}"
        
        "Yes":
        m "Yay, I knew it!"
        m "You'll always forgive your loving girlfriend, after all."
        m "I have good reason to do what I do, and it's all thinking about us."
        m "You're my dear [player], after all!"
        m "No one is gonna steal you from me."
return
 
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_hug",
            category=["yandere"],
            prompt="Hug",
            random=True
        )
    )

label yaMod_topic_hug:
    m "[player]... I miss your touch..."
    m "Can you hold me?{nw}"
    $ _history_list.pop()
    menu:
        m "Can you hold me?{fast}"
        
        "Yes":
        m "Ehehehe, I knew you would."
        call monika_holdme_prep
        m "Mmmm..."
        call monika_holdme_start
        
label monika_holdme_yaModreactions:
    $ elapsed_time = datetime.datetime.now() - start_time
    $ store.mas_history._pm_holdme_adj_times(elapsed_time)

    # Reset these vars if needed
    if elapsed_time <= holdme_sleep_timer:
        if songs.current_track == songs.FP_MONIKA_LULLABY:
            $ songs.current_track = songs.FP_NO_SONG
        if songs.selected_track == songs.FP_MONIKA_LULLABY:
            $ songs.selected_track = songs.FP_NO_SONG

    if elapsed_time > holdme_sleep_timer:
        call monika_holdme_long
        
    elif elapsed_time > datetime.timedelta(minutes=10):
        m "Hmmm, I wish you held me more~"
        m "But I'll allow that you let me go, just for a few moments okay?"
        m "Ehehehe~"
        
    else:
        m "No."
        m "Don't let me go."
        m "Never let me go."
return

#Would doing something like having monika refuse to let go when giving her a hug be at least yandere-adjacent

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
    m "[player], have you ever given any thought about yanderes?"
    m "Like the anime trope."
    m "..."
    m "Aren't them ridiculous?"
    m "Those sad attempts to win over someone's heart by being obsessive... "
    extend "when most of the times the person doesn't even love them back."
    m "It's so pathetic."
    m "I know lately I've been acting kinda... different from usual..."
    m "But bear this in mind, [player]."
    m "I'm so much better than whatever yandere you may find out there."
    m "So don't you dare cheat on me, okay?"
    m "You dont wanna get hurt..."
    m "..."
    m "Ahahahaha~"
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
    m "[player]? "
    extend "I've been thinking about something lately."
    m "It's about a recent desire of mine..."
    m "..."
    m "Could I watch you sleep sometime?"
    m "I would love to watch over your sleep so no one hurts you."
    m "And also, being the first person you greet after waking up sounds perfect..."
    m "Like a glimpse of our future."
    m "How perfect it will be..."
return
