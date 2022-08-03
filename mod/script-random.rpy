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
    
#would you kill for me
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
    m ""
return 

#monika talked about how she’d kill real people if the player were danger or harms way 

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
    m ""
return

#maybe she says about her stalking what you do online
##Her talking about spying on you to because it makes her feel closer to you + she wants to make no one's trying to take you away from her.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_promise",
            category=["yandere"],
            prompt="Promise ring",
            random=True
        )
    )

label yaMod_topic_promise:
    m ""
return

#Also if you tell her you got a promise ring, she'll react excitedly that everyone will know you're hers and hers alone
 
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
    m ""
return

#topic where she's just bashing other fictional yanderes and being like I'm so much better

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
    m ""
return

#Some other ideas I had is that she could talk about enjoying watching the player sleep, she says she’d Lille everyone in the literature club all over again to be with the player, says she wants to bring you to her world and never let you go
