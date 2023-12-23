import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&apiKey=b5a0283addfe424db671e65f7f60a2f1",
            "entertainment" : "",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=b5a0283addfe424db671e65f7f60a2f1",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=b5a0283addfe424db671e65f7f60a2f1",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=b5a0283addfe424db671e65f7f60a2f1",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=b5a0283addfe424db671e65f7f60a2f1",
            "Apple" : "https://newsapi.org/v2/everything?q=apple&from=2023-12-21&to=2023-12-21&sortBy=popularity&apiKey=b5a0283addfe424db671e65f7f60a2f1",
            "Tesla" : "https://newsapi.org/v2/everything?q=tesla&from=2023-11-22&sortBy=publishedAt&apiKey=b5a0283addfe424db671e65f7f60a2f1",
            "tech crunch" : "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=b5a0283addfe424db671e65f7f60a2f1"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science],[Apple],[Tesla],[tech crunch]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to continu] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")


