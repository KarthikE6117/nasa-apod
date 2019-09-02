import requests
import json 
import urllib
from gtts import gTTS
import os
from playsound import playsound

#This is a program that uses NANA's API to fetch JSON data from NASA's live APOD services.
#This Program is developed by KARTHIK.
#contact info : karthikelango6117@gmail.com
#You can get your api keys for the NASA's domain.
#This program uses Text-to-speech method.

api_key = "xs7URtFIaGZjj5bocZZV4I5XaVgwd0mC2cyOMKML"
print("\t\t\t******* Welcome To NASA APOD Information Service !!! *******\n")
print("APOD stands for Astronomy Picture Of the Day.\n")
earth_date = input(str('Enter the Date (Syntax: "YYYY-MM-DD"): '))
print("\n")
#APOD data are fetched through this apod function.
def apod(api_key, earth_date):
    main_url = "https://api.nasa.gov/planetary/apod?date=" + str(earth_date) + "&api_key=" + str(api_key)
    json_response = urllib.request.urlopen(main_url)
    json_object = json.load(json_response)
    print('\t\t\t"' + str(json_object['title'])+ '"\n')
    print("DATE : " + str(json_object['date']) + "\n")
    
    information = str(json_object['explanation'])
    language = 'en'
    speech_info_object = gTTS(text = information, lang = language, slow = False)
    speech_info_object.save("info.mp3")
    print("INFORMATION :\n\t" + str(json_object['explanation']) + "\n")
    playsound("info.mp3")
    print("\nMEDIA PROOF : " + str(json_object['media_type'])+ "\n")
    print("REFERENCE URL : " + str(json_object['url'])+"\n")
    
    if 'hdurl' in json_object:
        print("HD url : " + str(json_object['hdurl']) + "\n")
    
    if 'copyright' in json_object:
        print("Copyright : " + str(json_object['copyright']))
    else: 
        print("Copyright : Not Available." )

apod(api_key, earth_date)

    
