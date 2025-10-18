import random
import webbrowser
from textblob import TextBlob

moods = {
    "positive": [
        "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "https://www.youtube.com/watch?v=UqyT8IEBkvY",
        "https://www.youtube.com/watch?v=09R8_2nJtjg"
    ],
    "negative": [
        "https://www.youtube.com/watch?v=RBumgq5yVrA",
        "https://www.youtube.com/watch?v=RgKAFK5djSk",
        "https://www.youtube.com/watch?v=hoNb6HuNmU0"
    ],
    "neutral": [
        "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
        "https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "https://www.youtube.com/watch?v=YykjpeuMNEk"
    ]
}

text = input("How are you feeling today? ")
polarity = TextBlob(text).sentiment.polarity

if polarity > 0.2:
    mood = "positive"
elif polarity < -0.2:
    mood = "negative"
else:
    mood = "neutral"

url = random.choice(moods[mood])
print(f"Detected mood: {mood.capitalize()}. Playing a matching song...")
webbrowser.open(url)