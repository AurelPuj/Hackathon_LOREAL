import emot
from emot.core import emoji
from emot.core import emoticons
from emot.emo_unicode import EMO_UNICODE
from emot.emo_unicode import UNICODE_EMO
from emot.emo_unicode import EMOTICONS
import emot.core as emo

def emoji(text):
    emoji_data = emo.emoji(text)
    i=0
    for value in emoji_data["value"] :
    
   # Data_Train_lower[1][emoji_data["location"][i][0]] = ""
        text = text.replace(value,emoji_data["mean"][i].replace("_"," "))
        i += 1
    return text
