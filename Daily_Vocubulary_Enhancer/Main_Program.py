import time
from plyer import notification
from wordnik import *
import json
import datetime
import requests
import random
WORDNIK_API_KEY= "d52b63b6880f17811310d0fbd3b0d3a8ef163a248f58dc831"  

WORDNIK_API_KEY= "d52b63b6880f17811310d0fbd3b0d3a8ef163a248f58dc831"  
def get_word_of_the_day(current_date):
    """
    Fetch word of the day from the Wordnik API
    """
    response_data = {"word": "Unavailable", "definition": "Unavailable"}
    if WORDNIK_API_KEY:
        url = f"https://api.wordnik.com/v4/words.json/wordOfTheDay?date={current_date}" \           
              f"&api_key={WORDNIK_API_KEY}"                 #fetching random word along with it's meaning on date basis
        response = requests.get(url)
        api_response = json.loads(response.text)
        if response.status_code == 200:
            response_data["word"] = api_response["word"].upper()
            for definition in api_response["definitions"]:
                response_data["definition"] = definition["text"].capitalize()
                break

    else:
        # use a mock word if there is no Wordnik API key
        response_data["word"] = "Sorry, No new word today"
        response_data["definition"] = "No definition available"
    return response_data

if __name__=="__main__":
        i=0
        while(i<5):
                start_dt = datetime.date(2015, 1, 1)
                end_dt = datetime.date.today()
                time_between_dates = end_dt - start_dt
                days_between_dates = time_between_dates.days
                random_number_of_days = random.randrange(days_between_dates)                    #generating a random date
                random_date = start_dt + datetime.timedelta(days=random_number_of_days)
                response_data=get_word_of_the_day(random_date)                  #generating random word and meaning
                print("Word:- "+ str(response_data["word"]).capitalize())
                print("Meaning:- "+str(response_data["definition"])
                notification.notify(                    #generating notification for user                                               
                title = "Word:- "+str(response_data["word"]).capitalize(),
                message = "Meaning:- "+str(response_data["definition"]) ,
                app_icon= "C:\\Users\\soubh\\OneDrive\\Desktop\\Projects\\Daily_Vocab_Enhancer\\word_icon.ico",
                timeout = 20
                )             
                time.sleep(30)
                i=i+1

