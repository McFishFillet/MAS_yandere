init 5 python in mas_bookmarks_derand:
    label_prefix_map["yaMod_topic_"] = label_prefix_map["monika_"]
    
#tattoo dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_tattoo",
            category=["health"],
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
    
    
#Well I have some ideas but I dont know exactly what are the good ones haha, I think it’d be cool if monika talked about how she’d kill real people if the player were danger or harms way, maybe she says about her stalking what you do online
#Yeah, I’d like a compliment saying “I love how possessive you are” or something like that and maybe a conversation topic like “would you kill for me?”
#I was thinking maybe she could have a farewell message that’s like “remember, your mine forever!” Stuff like that
