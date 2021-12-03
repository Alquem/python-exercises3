def lyrics_generator(lyrics):
    lyric = ""
    count = 0
    for letter in lyrics:
                 
        if letter == 0:
            lyric += "Boom "
        elif letter == 1:
            lyric += "Drop the base "
            count += 1
        if count == 3:
            lyric += "!!!Break the base!!! "
            count = 0   
    return lyric

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))