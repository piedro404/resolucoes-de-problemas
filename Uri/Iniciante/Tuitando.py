def twitter(txt):
    if len(txt)<=140:
        return "TWEET"
    
    return "MUTE"

txt = str(input())
print(twitter(txt))
