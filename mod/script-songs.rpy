#super psycho love
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_superpsycholove",
            category=[mas_songs.TYPE_SHORT],
            prompt="Super Psycho Love",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_superpsycholove:
    m "{i}~Say that you want me every day~{/i}"
    m "{i}~That you want me every way~{/i}"
    m "{i}~That you need me~{/i}"
    m "{i}~Got me trippin' super psycho love~{/i}"
    m "{i}~Aim, pull the trigger~{/i}"
    m "{i}~Feel the pain getting bigger~{/i}"
    m "{i}~Go insane from the bitter feeling~{/i}"
    m "{i}~Trippin' super psycho love~{/i}"
    m "..."
    m "Let's put a little taste of psycho on this love of ours."
    m "I don't mind how violent it gets."
    m "As long as I'm yours... "
    extend "and you are mine, of course."
    m "Mine, mine, only mine!"
return

#the horror of our love
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_thehorrorofourlove",
            category=[mas_songs.TYPE_SHORT],
            prompt="The Horror of Our Love",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_thehorrorofourlove:
    m "{i}~I smell your softness~{/i}"
    m "{i}~Carnivorous and lusting~{/i}"
    m "{i}~To track you down among the pines~{/i}"
    m "{i}~I want you stuffed into my mouth~{/i}"
    m "{i}~Hold you down and tear you open~{/i}"
    m "{i}~Live inside you~{/i}"
    m "{i}~Oh, love I'd never hurt you~{/i}"
    m "{i}~But I'll grind against your bones~{/i}"
    m "{i}~Until our marrows mix~{/i}"
    m "{i}~I will eat you slowly~{/i}"
    m "{i}~The horror of our love~{/i}"
    m "{i}~Never so much blood pulled through my veins~{/i}"
    m "{i}~The horror of our love~{/i}"
    m "{i}~Never so much blood~{/i}"
    m "{i}~I'm your servant~{/i}"
    m "{i}~My immortal~{/i}"
    m "{i}~Pale and perfect~{/i}"
    m "..."
    m "Ahh, [player]. The bittersweet desire of our bodies covered in blood..."
    m "Flesh with flesh, lust and carnage..."
    m "I can't wait to touch your body."
    m "And to know that you are completely... "
    extend "entirely..."
    m "MINE."
return

#smoke and mirrors
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_smokeandmirrors",
            category=[mas_songs.TYPE_SHORT],
            prompt="Smoke and Mirrors",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_smokeandmirrors:
    m "{i}~I'm not asking much, just give me your heart~{/i}"
    m "{i}~And put no one else above me, go on, just say you love me~{/i}"
    m "{i}~Take my hand in yours and tell me that I'll always be the one~{/i}"
    m "{i}~Without you, my life means nothing so just say you love me tonight~{/i}"
    m "{i}~And if you lie, this poor girl will have to die~{/i}"
    m "..."
    m "You better give me or heart [player]..."
    m "Or else someone will have to die~"
    m "And we don't want that, do we?"
    m "Ehehehe~"
return

#you're mine
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_youremine",
            category=[mas_songs.TYPE_SHORT],
            prompt="You're Mine",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_youremine:
    m "{i}~You don't talk to no one~{/i}"
    m "{i}~Don't you look at nothing~{/i}"
    m "{i}~Focus on me~{/i}"
    m "{i}~Look into my eyes~{/i}"
    m "{i}~Come a little closer~{/i}"
    m "{i}~Let me tell you something~{/i}"
    m "{i}~You ain't going anywhere~{/i}"
    m "{i}~'Cause you mine~{/i}"
    m "..."
    m "Come a little closer, [player]."
    m "I've got a little something just for you~"
    m "No need to be scared, [mas_get_player_nickname()]."
    m "No one needs to get hurt..."
    m "But maybe someone will~"
    m "Ahahaha~"
return

#you belong to me
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_youbelongtome",
            category=[mas_songs.TYPE_SHORT],
            prompt="You Belong to Me",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_youbelongtome:
    m "{i}~Feels like we're dreaming, we're tripping and reeling~{/i}"
    m "{i}~Just say that you belong to me~{/i}"
    m "{i}~I could get lost in the feelings we're feeling~{/i}"
    m "{i}~Do you want more of this? Isn't it glorious?~{/i}"
    m "{i}~I can't believe that it's free~{/i}"
    m "{i}~I will adore you, I'll only live for you~{/i}"
    m "{i}~Just say that you belong to me~{/i}"
    m "{i}~Crawl into my heart, take me apart~{/i}"
    m "{i}~Do what you please to me, I won't resist~{/i}"
    m "{i}~Find what you're seeking, I am not leaving~{/i}"
    m "{i}~'Til I am drunk loved up in your kiss~{/i}"
    m "{i}~I must confess to you, I want to possess you~{/i}"
    m "..."
    m "[player], it's not hard..."
    m "Just say you belong to me so no one else needs to suffer."
    m "I love you so much, can't you see?"
    m "You have to be mine."
    m "There's no other option."
return "love"

#the music of the night
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_themusicofthenight",
            category=[mas_songs.TYPE_SHORT],
            prompt="The Music Of The Night",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_themusicofthenight:
    m "{i}~Let your mind start a journey through a strange new world~{/i}"
    m "{i}~Leave all thoughts of the life you knew before~{/i}"
    m "{i}~Let your soul take you where you long to be~{/i}"
    m "{i}~Only then can you belong to me~{/i}"
    m "{i}~Floating, falling, sweet intoxication~{/i}"
    m "{i}~Touch me, trust me, savour each sensation~{/i}"
    m "{i}~Let the dream begin, let your darker side give in~{/i}"
    m "{i}~To the power of the music that I write~{/i}"
    m "{i}~The power of the music of the night~{/i}"
    m "{i}~You alone~{/i}"
    m "{i}~Can make my song take flight~{/i}"
    m "{i}~Help me make the music of the night~{/i}"
    m "..."
    m "You're the only one that can make my heart take flight, [player]."
    m "No one else... No one."
    m "So please, let me savour this moment..."
    m "And belong to me."
    m "I know you'll do that for your wonderful girlfriend, won't you?"
return "love"
