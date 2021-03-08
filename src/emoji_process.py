import emot.core as emo

def emoji_process(data):
    output = [ ]
    for y,text in enumerate(data) :
        emoji_data = emo.emoji(text)
        i = 0

        for value in emoji_data["value"]:
            # Data_Train_lower[1][emoji_data["location"][i][0]] = ""
            text = text.replace(value, emoji_data["mean"][i].replace("_", " "))
            i += 1
        output.append(text)
    return output